"""
Procedural bronze portrait bust — Blender build script.

Builds, in one go:
  * a male head (cranium, brow, nose, cheeks, jaw, chin, lips, ears, eyes),
    swept-back hair, neck,
  * a jacketed torso truncated in the classic bust silhouette (flat bottom,
    slanted arm cuts), with notch lapels, shirt collar and a knotted tie,
  * a bronze base plate, a rough-hewn stone plinth and a plaster wall,
  * a patinated bronze material (warm bronze, verdigris in the recesses,
    polished highlights on the edges), stone and plaster materials,
  * a three-point studio light rig and a 3/4 portrait camera.

Run headless with the `bpy` pip module or inside Blender:

    python3 blender/bronze_bust.py --out blender/output --res 1024 --samples 128
    blender -b -P blender/bronze_bust.py -- --out blender/output

Outputs: bust.blend, bust.glb, bust.obj (+ .mtl) and preview.png.

Organic forms are built from metaballs (smooth unions) and converted to a
mesh, then refined with subdivision + displacement so the surface reads as
hand-modelled, hammered bronze rather than CSG primitives.
"""

import argparse
import math
import os
import sys

import bpy
import bmesh
from mathutils import Vector
from mathutils.bvhtree import BVHTree

# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def parse_args():
    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    elif argv and argv[0].endswith(".py"):
        argv = argv[1:]
    p = argparse.ArgumentParser(description="Build the bronze bust scene.")
    p.add_argument("--out", default="blender/output", help="output directory")
    p.add_argument("--res", type=int, default=1024, help="render size (px, square)")
    p.add_argument("--samples", type=int, default=128, help="Cycles samples")
    p.add_argument("--no-render", action="store_true", help="skip the preview render")
    p.add_argument("--no-export", action="store_true", help="skip glb/obj export")
    p.add_argument("--mb-res", type=float, default=0.018,
                   help="metaball resolution (smaller = finer, slower)")
    return p.parse_args(argv)


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

HEAD_Z = 1.47          # world height of the head's local origin (eye line ~ +0.02)
HEAD_TURN = -22.0      # degrees; face points -Y, negative turns toward -X
BUST_BOTTOM = 1.00     # flat truncation plane of the torso
PLATE_H = 0.045
PLINTH_TOP = BUST_BOTTOM - PLATE_H


def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 1.0
    return scene


def link(obj, coll=None):
    (coll or bpy.context.scene.collection).objects.link(obj)
    return obj


def new_collection(name):
    c = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(c)
    return c


# Measured (threshold 0.6): visible radius / element radius, per stiffness.
# A lone BALL of radius 0.05 shows as 0.0285 at stiffness 2, so every helper
# below takes the *visible* size and scales the field radius to match.
_VISIBLE_FRACTION = {1.0: 0.39, 2.0: 0.57, 3.0: 0.63, 4.0: 0.68, 5.0: 0.71, 6.0: 0.73}


def _fraction(stiffness):
    keys = sorted(_VISIBLE_FRACTION)
    s = min(max(stiffness, keys[0]), keys[-1])
    lo = max(k for k in keys if k <= s)
    hi = min(k for k in keys if k >= s)
    if lo == hi:
        return _VISIBLE_FRACTION[lo]
    t = (s - lo) / (hi - lo)
    return _VISIBLE_FRACTION[lo] * (1 - t) + _VISIBLE_FRACTION[hi] * t


def add_element(mb, kind, co, size=None, radius=1.0, stiffness=2.0, negative=False):
    e = mb.elements.new()
    e.type = kind
    e.co = Vector(co)
    e.radius = radius
    e.stiffness = stiffness
    e.use_negative = negative
    if size is not None:
        e.size_x, e.size_y, e.size_z = size
    return e


def ball(mb, co, r, stiffness=2.0, negative=False):
    """Ball whose visible radius (alone) is `r`."""
    return add_element(mb, "BALL", co, radius=r / _fraction(stiffness),
                       stiffness=stiffness, negative=negative)


def ellipsoid(mb, co, size, stiffness=2.0, negative=False):
    """Ellipsoid whose visible half-extents (alone) are `size`."""
    return add_element(mb, "ELLIPSOID", co, size=size, radius=1.0 / _fraction(stiffness),
                       stiffness=stiffness, negative=negative)


def metaball_object(name, resolution, threshold=0.6):
    mb = bpy.data.metaballs.new(name)
    mb.resolution = resolution
    mb.render_resolution = resolution
    mb.threshold = threshold
    obj = bpy.data.objects.new(name, mb)
    return obj, mb


def metaball_to_mesh(obj, name):
    """Evaluate a metaball object and replace it with a real mesh object."""
    dg = bpy.context.evaluated_depsgraph_get()
    ev = obj.evaluated_get(dg)
    me = bpy.data.meshes.new_from_object(ev)
    me.name = name
    mesh_obj = bpy.data.objects.new(name, me)
    mesh_obj.matrix_world = obj.matrix_world.copy()
    for c in obj.users_collection:
        c.objects.link(mesh_obj)
    bpy.data.objects.remove(obj)
    return mesh_obj


def bisect_mesh(obj, planes):
    """Cut a mesh by planes (world-space point, normal); remove the side the
    normal points to and cap the holes."""
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    inv = obj.matrix_world.inverted()
    for co, no in planes:
        lco = inv @ Vector(co)
        lno = (inv.to_3x3() @ Vector(no)).normalized()
        geom = bm.verts[:] + bm.edges[:] + bm.faces[:]
        bmesh.ops.bisect_plane(bm, geom=geom, dist=1e-5, plane_co=lco,
                               plane_no=lno, clear_outer=True, clear_inner=False)
        edges = [e for e in bm.edges if e.is_boundary]
        if edges:
            bmesh.ops.holes_fill(bm, edges=edges, sides=0)
    bm.to_mesh(obj.data)
    bm.free()
    obj.data.update()


def shade_smooth(obj, angle=math.radians(45)):
    me = obj.data
    for p in me.polygons:
        p.use_smooth = True
    try:
        me.shade_smooth()
    except Exception:
        pass
    mod = obj.modifiers.new("SmoothByAngle", "SMOOTH_BY_ANGLE") if hasattr(bpy.types, "SmoothByAngleModifier") else None
    if mod is not None:
        mod.angle = angle


def add_subsurf(obj, levels=2, render=None):
    m = obj.modifiers.new("Subdivision", "SUBSURF")
    m.levels = levels
    m.render_levels = render if render is not None else levels
    return m


def add_displace(obj, texture, strength, mid=0.5, coords_obj=None):
    m = obj.modifiers.new("Displace", "DISPLACE")
    m.texture = texture
    m.strength = strength
    m.mid_level = mid
    if coords_obj is not None:
        m.texture_coords = "OBJECT"
        m.texture_coords_object = coords_obj
    return m


def add_solidify(obj, thickness, offset=1.0):
    m = obj.modifiers.new("Solidify", "SOLIDIFY")
    m.thickness = thickness
    m.offset = offset
    m.use_even_offset = True
    return m


_BVH_CACHE = {}


def surface_bvh(target):
    """BVH of `target`'s evaluated mesh (modifiers applied), world space."""
    key = target.name
    if key not in _BVH_CACHE:
        bpy.context.view_layer.update()
        dg = bpy.context.evaluated_depsgraph_get()
        _BVH_CACHE[key] = BVHTree.FromObject(target, dg)
    return _BVH_CACHE[key]


def surface_point(target, x, z, offset=0.0, from_y=-0.8):
    """Point on the front of `target` at (x, z), pushed out by `offset`.
    Rays go along +Y; where the panel overhangs the silhouette the ray is
    aimed at the body axis so the panel wraps round the side."""
    bvh = surface_bvh(target)
    origin = Vector((x, from_y, z))
    hit = bvh.ray_cast(origin, Vector((0, 1, 0)), 3.0)
    if hit[0] is None:
        d = (Vector((0.0, 0.0, z)) - origin).normalized()
        hit = bvh.ray_cast(origin, d, 3.0)
    if hit[0] is None:
        return None, None
    return hit[0] + hit[1] * offset, hit[1]


def drape(obj, target, offset):
    """Bake a flat XZ panel onto the surface of `target` (world = local here)."""
    me = obj.data
    inv = obj.matrix_world.inverted()
    for v in me.vertices:
        w = obj.matrix_world @ v.co
        p, _ = surface_point(target, w.x, w.z, offset)
        if p is not None:
            v.co = inv @ p
    me.update()


def mesh_from_polys(name, verts, faces, coll=None):
    me = bpy.data.meshes.new(name)
    me.from_pydata([Vector(v) for v in verts], [], faces)
    me.update()
    obj = bpy.data.objects.new(name, me)
    link(obj, coll)
    return obj


def grid_strip(name, left, right, rows=12, coll=None):
    """Quad strip between two polylines (same length) — used for the tie."""
    assert len(left) == len(right)
    verts, faces = [], []
    n = len(left)
    for i in range(n):
        verts.append(left[i])
        verts.append(right[i])
    for i in range(n - 1):
        a, b, c, d = 2 * i, 2 * i + 1, 2 * i + 3, 2 * i + 2
        faces.append((a, b, c, d))
    return mesh_from_polys(name, verts, faces, coll)


def subdivide_ngon(obj, cuts=3):
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    bmesh.ops.subdivide_edges(bm, edges=bm.edges[:], cuts=cuts, use_grid_fill=True)
    bmesh.ops.triangulate(bm, faces=bm.faces[:])
    bmesh.ops.join_triangles(bm, faces=bm.faces[:], angle_face_threshold=3.0,
                             angle_shape_threshold=3.0)
    bm.to_mesh(obj.data)
    bm.free()


# --------------------------------------------------------------------------
# Textures (for Displace modifiers)
# --------------------------------------------------------------------------


def make_textures():
    hammer = bpy.data.textures.new("HammeredBronze", "CLOUDS")
    hammer.noise_scale = 0.07
    hammer.noise_depth = 2
    hammer.noise_basis = "VORONOI_F2_F1"
    hammer.intensity = 1.0

    skin = bpy.data.textures.new("SkinTool", "CLOUDS")
    skin.noise_scale = 0.012
    skin.noise_depth = 2
    skin.noise_basis = "BLENDER_ORIGINAL"

    strands = bpy.data.textures.new("HairStrands", "CLOUDS")
    strands.noise_scale = 0.35
    strands.noise_depth = 1
    strands.noise_basis = "VORONOI_F1"

    stone = bpy.data.textures.new("RoughStone", "CLOUDS")
    stone.noise_scale = 0.09
    stone.noise_depth = 4
    stone.noise_basis = "VORONOI_CRACKLE"

    chisel = bpy.data.textures.new("Chisel", "CLOUDS")
    chisel.noise_scale = 0.02
    chisel.noise_depth = 1
    chisel.noise_basis = "VORONOI_F2"
    return hammer, skin, strands, stone, chisel


# --------------------------------------------------------------------------
# Geometry
# --------------------------------------------------------------------------


def build_head(coll, mb_res):
    """Head + neck as one smooth metaball union (local: face points -Y)."""
    obj, mb = metaball_object("HeadMeta", mb_res)
    link(obj, coll)

    # cranium & skull
    ellipsoid(mb, (0, 0.012, 0.030), (0.078, 0.093, 0.088))
    ball(mb, (0, 0.055, 0.005), 0.070)                    # occiput
    ellipsoid(mb, (0, -0.040, 0.058), (0.066, 0.040, 0.044))   # forehead
    ellipsoid(mb, (0, -0.060, 0.082), (0.050, 0.030, 0.025))   # upper forehead
    ellipsoid(mb, (0.000, 0.000, 0.088), (0.060, 0.070, 0.028))  # crown
    # temples
    for s in (-1, 1):
        ellipsoid(mb, (s * 0.062, -0.025, 0.035), (0.020, 0.045, 0.045))

    # mid-face mass, cheeks, jaw, chin
    ellipsoid(mb, (0, -0.030, -0.020), (0.060, 0.060, 0.060))
    for s in (-1, 1):
        ball(mb, (s * 0.050, -0.052, -0.020), 0.030)      # cheekbones
        ball(mb, (s * 0.038, -0.045, -0.055), 0.028)      # lower cheeks
        ellipsoid(mb, (s * 0.046, -0.010, -0.075), (0.032, 0.052, 0.028))  # jaw
        ellipsoid(mb, (s * 0.062, 0.015, -0.040), (0.022, 0.040, 0.045))   # jaw hinge
    ball(mb, (0, -0.058, -0.098), 0.031)                  # chin
    ellipsoid(mb, (0, -0.040, -0.088), (0.040, 0.030, 0.022))  # chin base

    # brow ridge — heavy, overhanging the eyes
    for s in (-1, 1):
        ellipsoid(mb, (s * 0.032, -0.088, 0.040), (0.034, 0.016, 0.012), stiffness=3)
    ellipsoid(mb, (0, -0.084, 0.034), (0.016, 0.016, 0.014), stiffness=3)  # glabella

    # eyes: recessed sockets with eyeballs and lids
    for s in (-1, 1):
        ball(mb, (s * 0.031, -0.070, 0.017), 0.020, stiffness=3, negative=True)
        ball(mb, (s * 0.031, -0.066, 0.017), 0.015, stiffness=4)
        ellipsoid(mb, (s * 0.031, -0.074, 0.030), (0.024, 0.009, 0.006), stiffness=4)  # upper lid
        ellipsoid(mb, (s * 0.031, -0.073, 0.003), (0.022, 0.008, 0.005), stiffness=4)  # lower lid

    # nose — long, straight, prominent
    ellipsoid(mb, (0, -0.092, 0.006), (0.012, 0.024, 0.036), stiffness=3)   # bridge
    ellipsoid(mb, (0, -0.104, -0.020), (0.015, 0.022, 0.022), stiffness=3)  # dorsum
    ball(mb, (0, -0.114, -0.033), 0.021, stiffness=3)                        # tip
    for s in (-1, 1):
        ball(mb, (s * 0.019, -0.099, -0.037), 0.014, stiffness=3)            # alae
        ball(mb, (s * 0.034, -0.080, -0.050), 0.008, stiffness=3, negative=True)  # nasolabial fold

    # mouth — firm, closed
    ellipsoid(mb, (0, -0.095, -0.058), (0.029, 0.011, 0.007), stiffness=4)   # upper lip
    ellipsoid(mb, (0, -0.094, -0.071), (0.025, 0.012, 0.007), stiffness=4)   # lower lip
    ellipsoid(mb, (0, -0.100, -0.064), (0.027, 0.006, 0.003), stiffness=6, negative=True)  # lip line
    ellipsoid(mb, (0, -0.090, -0.047), (0.006, 0.010, 0.006), stiffness=5, negative=True)  # philtrum

    # ears
    for s in (-1, 1):
        ellipsoid(mb, (s * 0.083, 0.012, -0.008), (0.010, 0.020, 0.034), stiffness=3)
        ellipsoid(mb, (s * 0.086, 0.010, -0.004), (0.004, 0.011, 0.020), stiffness=5, negative=True)
        ball(mb, (s * 0.084, 0.020, 0.010), 0.011, stiffness=4)   # helix
        ball(mb, (s * 0.082, 0.004, -0.032), 0.009, stiffness=4)  # lobe

    # neck
    ellipsoid(mb, (0, 0.012, -0.160), (0.050, 0.055, 0.100))
    ellipsoid(mb, (0, 0.030, -0.200), (0.060, 0.060, 0.060))
    ball(mb, (0, -0.030, -0.135), 0.030)  # larynx / throat

    obj.location = (0, 0, HEAD_Z)
    obj.rotation_euler = (0, 0, math.radians(HEAD_TURN))
    return obj


def build_hair(coll, mb_res):
    """Swept-back hair cap with a receded hairline (local frame = head frame)."""
    obj, mb = metaball_object("HairMeta", mb_res, threshold=0.7)
    link(obj, coll)
    ellipsoid(mb, (0, 0.018, 0.092), (0.090, 0.108, 0.048))       # top
    ellipsoid(mb, (0, 0.072, 0.030), (0.082, 0.045, 0.080))       # back
    ellipsoid(mb, (0, 0.005, 0.112), (0.066, 0.080, 0.028))       # crown lift
    for s in (-1, 1):
        ellipsoid(mb, (s * 0.080, 0.030, 0.035), (0.022, 0.078, 0.055))   # sides
        ellipsoid(mb, (s * 0.060, -0.050, 0.100), (0.028, 0.032, 0.024))  # front sweeps
        ball(mb, (s * 0.050, -0.070, 0.104), 0.017, negative=True)        # receding temples
    ellipsoid(mb, (0, -0.066, 0.108), (0.032, 0.024, 0.020))              # front wave
    # combed-back ridges running front to back
    for k in (-1.5, -0.5, 0.5, 1.5):
        ellipsoid(mb, (k * 0.032, 0.010, 0.112), (0.013, 0.090, 0.011), stiffness=4)
    obj.location = (0, 0, HEAD_Z)
    obj.rotation_euler = (0, 0, math.radians(HEAD_TURN))
    return obj


def build_torso(coll, mb_res):
    """Jacketed shoulders/chest, later truncated to the bust silhouette."""
    obj, mb = metaball_object("TorsoMeta", mb_res * 1.3)
    link(obj, coll)
    # boxy, tailored silhouette: a wide shoulder bar over a deep chest slab
    ellipsoid(mb, (0, 0.000, 1.220), (0.215, 0.080, 0.045), stiffness=3)  # shoulder line
    ellipsoid(mb, (0, -0.010, 1.100), (0.185, 0.100, 0.175), stiffness=3)  # chest slab
    ellipsoid(mb, (0, 0.045, 1.110), (0.175, 0.070, 0.160), stiffness=3)   # back
    ellipsoid(mb, (0, -0.045, 1.190), (0.120, 0.060, 0.050), stiffness=3)  # upper chest fullness
    for s in (-1, 1):
        ellipsoid(mb, (s * 0.195, -0.005, 1.215), (0.055, 0.075, 0.042), stiffness=3)  # shoulder caps
        ellipsoid(mb, (s * 0.200, 0.000, 1.110), (0.042, 0.072, 0.110), stiffness=3)   # upper arms
        ball(mb, (s * 0.090, 0.015, 1.245), 0.045, stiffness=3)                    # trapezius slope
    ellipsoid(mb, (0, 0.015, 1.265), (0.065, 0.060, 0.035), stiffness=3)   # collar mass
    ellipsoid(mb, (0, 0.040, 1.290), (0.085, 0.045, 0.025), stiffness=3)   # jacket collar (back of neck)
    return obj


def truncate_torso(obj):
    planes = [
        ((0, 0, BUST_BOTTOM), (0, 0, -1)),                       # flat bottom
        ((0.205, 0, 1.030), Vector((0.78, 0.0, -0.63))),         # slanted arm cut, +X
        ((-0.205, 0, 1.030), Vector((-0.78, 0.0, -0.63))),       # slanted arm cut, -X
        ((0, 0.120, 1.03), Vector((0.0, 0.70, -0.71))),          # slight back cut
    ]
    bisect_mesh(obj, planes)


def build_lapels(coll, torso, side):
    """One notch lapel (side = +1 viewer-right / -1) as a shrinkwrapped strip."""
    s = side
    y = -0.30  # in front of the torso; shrinkwrap pulls it onto the jacket
    pts = [
        (s * 0.030, y, 1.300),  # top at the collar
        (s * 0.095, y, 1.292),  # collar notch outer
        (s * 0.128, y, 1.262),  # notch point
        (s * 0.112, y, 1.236),  # notch bottom
        (s * 0.152, y, 1.212),  # lapel point
        (s * 0.118, y, 1.120),
        (s * 0.072, y, 1.035),  # button point
        (s * 0.008, y, 1.004),
        (s * 0.006, y, 1.100),  # roll line
        (s * 0.014, y, 1.200),
    ]
    faces = [tuple(range(len(pts)))]
    obj = mesh_from_polys(f"Lapel{'R' if s > 0 else 'L'}", pts, faces, coll)
    subdivide_ngon(obj, cuts=6)
    drape(obj, torso, offset=0.006)
    add_solidify(obj, 0.008, offset=0.0)
    m = obj.modifiers.new("Bevel", "BEVEL")
    m.width = 0.003
    m.segments = 2
    add_subsurf(obj, 1)
    return obj


def build_collar(coll, head_obj):
    """Shirt collar: a band around the neck plus two collar points."""
    # band
    bm = bmesh.new()
    n = 28
    lower, upper = [], []
    for i in range(n + 1):
        a = math.radians(35 + (290 * i / n))  # open in front (-Y)
        r = 0.078
        x, y = r * math.sin(a), r * math.cos(a) + 0.010
        lower.append(bm.verts.new((x, y, -0.205)))
        upper.append(bm.verts.new((x, y, -0.160)))
    for i in range(n):
        bm.faces.new((lower[i], lower[i + 1], upper[i + 1], upper[i]))
    me = bpy.data.meshes.new("CollarBand")
    bm.to_mesh(me)
    bm.free()
    band = bpy.data.objects.new("CollarBand", me)
    link(band, coll)
    band.parent = head_obj
    add_solidify(band, 0.010, offset=1.0)
    shade_smooth(band)

    # collar points (local to the head frame, so they follow the head turn)
    pts_objs = []
    for s in (-1, 1):
        pts = [
            (s * 0.015, -0.055, -0.185),
            (s * 0.070, -0.045, -0.192),
            (s * 0.078, -0.060, -0.225),
            (s * 0.028, -0.078, -0.262),
            (s * 0.010, -0.070, -0.230),
        ]
        o = mesh_from_polys(f"CollarPoint{'R' if s > 0 else 'L'}", pts,
                            [tuple(range(len(pts)))], coll)
        subdivide_ngon(o, cuts=3)
        o.parent = head_obj
        add_solidify(o, 0.009, offset=0.0)
        pts_objs.append(o)
    return [band] + pts_objs


def build_tie(coll, torso):
    """Windsor knot + tapered blade with a central dimple."""
    # knot
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=24, v_segments=16, radius=1.0)
    me = bpy.data.meshes.new("TieKnot")
    bm.to_mesh(me)
    bm.free()
    knot = bpy.data.objects.new("TieKnot", me)
    link(knot, coll)
    p, _ = surface_point(torso, 0.0, 1.268, offset=0.010)
    knot.location = p if p is not None else Vector((0.0, -0.10, 1.268))
    knot.scale = (0.025, 0.020, 0.030)
    knot.rotation_euler = (math.radians(-12), 0, 0)
    shade_smooth(knot)
    add_subsurf(knot, 1)

    # blade
    y = -0.30
    left, right = [], []
    zs = [1.250, 1.225, 1.185, 1.135, 1.085, 1.050, 1.030]
    ws = [0.015, 0.019, 0.023, 0.027, 0.031, 0.034, 0.028]
    for z, w in zip(zs, ws):
        left.append((-w, y, z))
        right.append((w, y, z))
    left.append((0.0, y, 1.012))
    right.append((0.0, y, 1.012))
    blade = grid_strip("TieBlade", left, right, coll=coll)
    drape(blade, torso, offset=0.020)
    add_solidify(blade, 0.010, offset=0.0)
    add_subsurf(blade, 1)
    return [knot, blade]


def build_base_plate(coll):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co.x *= 0.40
        v.co.y *= 0.245
        v.co.z *= PLATE_H
    me = bpy.data.meshes.new("BasePlate")
    bm.to_mesh(me)
    bm.free()
    obj = bpy.data.objects.new("BasePlate", me)
    link(obj, coll)
    obj.location = (0.0, 0.02, PLINTH_TOP + PLATE_H / 2)
    obj.rotation_euler = (0, 0, math.radians(-6))
    m = obj.modifiers.new("Bevel", "BEVEL")
    m.width = 0.006
    m.segments = 3
    return obj


def build_plinth(coll, stone_tex):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.subdivide_edges(bm, edges=bm.edges[:], cuts=48, use_grid_fill=True)
    for v in bm.verts:
        v.co.x *= 0.56
        v.co.y *= 0.46
        v.co.z *= 0.62
    me = bpy.data.meshes.new("Plinth")
    bm.to_mesh(me)
    bm.free()
    obj = bpy.data.objects.new("Plinth", me)
    link(obj, coll)
    obj.location = (0.0, 0.02, PLINTH_TOP - 0.31)
    add_displace(obj, stone_tex, strength=0.014, mid=0.5)
    return obj


def build_wall(coll):
    me = bpy.data.meshes.new("Wall")
    s = 3.0
    me.from_pydata([(-s, 0, 0), (s, 0, 0), (s, 0, 2 * s), (-s, 0, 2 * s)], [], [(0, 1, 2, 3)])
    me.update()
    obj = bpy.data.objects.new("Wall", me)
    link(obj, coll)
    obj.location = (0, 0.75, 0)
    return obj


# --------------------------------------------------------------------------
# Materials
# --------------------------------------------------------------------------


def _nodes(mat):
    mat.use_nodes = True
    nt = mat.node_tree
    nt.nodes.clear()
    return nt, nt.nodes, nt.links


def bronze_material():
    mat = bpy.data.materials.new("PatinatedBronze")
    nt, nodes, links = _nodes(mat)

    out = nodes.new("ShaderNodeOutputMaterial")
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Metallic"].default_value = 1.0
    links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])

    texco = nodes.new("ShaderNodeTexCoord")
    geo = nodes.new("ShaderNodeNewGeometry")
    ao = nodes.new("ShaderNodeAmbientOcclusion")
    ao.inputs["Distance"].default_value = 0.05
    ao.samples = 8

    # colours
    bronze = nodes.new("ShaderNodeRGB"); bronze.outputs[0].default_value = (0.42, 0.26, 0.12, 1)
    dark = nodes.new("ShaderNodeRGB"); dark.outputs[0].default_value = (0.12, 0.075, 0.045, 1)
    verdigris = nodes.new("ShaderNodeRGB"); verdigris.outputs[0].default_value = (0.14, 0.40, 0.34, 1)
    polished = nodes.new("ShaderNodeRGB"); polished.outputs[0].default_value = (0.78, 0.66, 0.48, 1)

    # large-scale mottling between bronze and dark bronze
    n1 = nodes.new("ShaderNodeTexNoise")
    n1.inputs["Scale"].default_value = 9.0
    n1.inputs["Detail"].default_value = 6.0
    n1.inputs["Roughness"].default_value = 0.6
    links.new(texco.outputs["Object"], n1.inputs["Vector"])
    r1 = nodes.new("ShaderNodeMapRange")
    r1.inputs["From Min"].default_value = 0.35
    r1.inputs["From Max"].default_value = 0.65
    links.new(n1.outputs["Fac"], r1.inputs["Value"])
    mix1 = nodes.new("ShaderNodeMix"); mix1.data_type = "RGBA"
    links.new(r1.outputs["Result"], mix1.inputs["Factor"])
    links.new(dark.outputs[0], mix1.inputs[6])
    links.new(bronze.outputs[0], mix1.inputs[7])

    # verdigris where AO is high (recesses) modulated by fine noise
    n2 = nodes.new("ShaderNodeTexNoise")
    n2.inputs["Scale"].default_value = 40.0
    n2.inputs["Detail"].default_value = 8.0
    links.new(texco.outputs["Object"], n2.inputs["Vector"])
    inv_ao = nodes.new("ShaderNodeMath"); inv_ao.operation = "SUBTRACT"
    inv_ao.inputs[0].default_value = 1.0
    links.new(ao.outputs["AO"], inv_ao.inputs[1])
    mul = nodes.new("ShaderNodeMath"); mul.operation = "MULTIPLY"
    links.new(inv_ao.outputs[0], mul.inputs[0])
    links.new(n2.outputs["Fac"], mul.inputs[1])
    r2 = nodes.new("ShaderNodeMapRange")
    r2.inputs["From Min"].default_value = 0.10
    r2.inputs["From Max"].default_value = 0.45
    links.new(mul.outputs[0], r2.inputs["Value"])
    mix2 = nodes.new("ShaderNodeMix"); mix2.data_type = "RGBA"
    links.new(r2.outputs["Result"], mix2.inputs["Factor"])
    links.new(mix1.outputs[2], mix2.inputs[6])
    links.new(verdigris.outputs[0], mix2.inputs[7])

    # polished highlights on convex edges (pointiness)
    r3 = nodes.new("ShaderNodeMapRange")
    r3.inputs["From Min"].default_value = 0.56
    r3.inputs["From Max"].default_value = 0.70
    links.new(geo.outputs["Pointiness"], r3.inputs["Value"])
    mix3 = nodes.new("ShaderNodeMix"); mix3.data_type = "RGBA"
    links.new(r3.outputs["Result"], mix3.inputs["Factor"])
    links.new(mix2.outputs[2], mix3.inputs[6])
    links.new(polished.outputs[0], mix3.inputs[7])
    links.new(mix3.outputs[2], bsdf.inputs["Base Color"])

    # roughness: matte in the patina, glossier on polished metal
    rough = nodes.new("ShaderNodeMapRange")
    rough.inputs["From Min"].default_value = 0.0
    rough.inputs["From Max"].default_value = 1.0
    rough.inputs["To Min"].default_value = 0.30
    rough.inputs["To Max"].default_value = 0.62
    links.new(r2.outputs["Result"], rough.inputs["Value"])
    n3 = nodes.new("ShaderNodeTexNoise")
    n3.inputs["Scale"].default_value = 120.0
    links.new(texco.outputs["Object"], n3.inputs["Vector"])
    radd = nodes.new("ShaderNodeMath"); radd.operation = "MULTIPLY_ADD"
    links.new(n3.outputs["Fac"], radd.inputs[0])
    radd.inputs[1].default_value = 0.15
    links.new(rough.outputs[0], radd.inputs[2])
    links.new(radd.outputs[0], bsdf.inputs["Roughness"])

    # micro bump (tooling marks)
    n4 = nodes.new("ShaderNodeTexNoise")
    n4.inputs["Scale"].default_value = 220.0
    n4.inputs["Detail"].default_value = 4.0
    links.new(texco.outputs["Object"], n4.inputs["Vector"])
    bump = nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.18
    bump.inputs["Distance"].default_value = 0.002
    links.new(n4.outputs["Fac"], bump.inputs["Height"])
    links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    return mat


def stone_material():
    mat = bpy.data.materials.new("RoughStone")
    nt, nodes, links = _nodes(mat)
    out = nodes.new("ShaderNodeOutputMaterial")
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Roughness"].default_value = 0.95
    links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    texco = nodes.new("ShaderNodeTexCoord")
    n = nodes.new("ShaderNodeTexNoise")
    n.inputs["Scale"].default_value = 25.0
    n.inputs["Detail"].default_value = 10.0
    links.new(texco.outputs["Object"], n.inputs["Vector"])
    ramp = nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].color = (0.22, 0.21, 0.19, 1)
    ramp.color_ramp.elements[1].color = (0.46, 0.44, 0.40, 1)
    links.new(n.outputs["Fac"], ramp.inputs["Fac"])
    links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    bump = nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.6
    bump.inputs["Distance"].default_value = 0.01
    links.new(n.outputs["Fac"], bump.inputs["Height"])
    links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    return mat


def plaster_material():
    mat = bpy.data.materials.new("Plaster")
    nt, nodes, links = _nodes(mat)
    out = nodes.new("ShaderNodeOutputMaterial")
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Roughness"].default_value = 1.0
    links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    texco = nodes.new("ShaderNodeTexCoord")
    n = nodes.new("ShaderNodeTexNoise")
    n.inputs["Scale"].default_value = 6.0
    n.inputs["Detail"].default_value = 12.0
    n.inputs["Roughness"].default_value = 0.7
    links.new(texco.outputs["Object"], n.inputs["Vector"])
    ramp = nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].color = (0.62, 0.60, 0.57, 1)
    ramp.color_ramp.elements[1].color = (0.80, 0.78, 0.75, 1)
    links.new(n.outputs["Fac"], ramp.inputs["Fac"])
    links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    bump = nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.35
    bump.inputs["Distance"].default_value = 0.02
    links.new(n.outputs["Fac"], bump.inputs["Height"])
    links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    return mat


def assign(obj, mat):
    obj.data.materials.clear()
    obj.data.materials.append(mat)


# --------------------------------------------------------------------------
# Camera, lights, render
# --------------------------------------------------------------------------


def build_camera_and_lights(scene, coll):
    target = bpy.data.objects.new("CamTarget", None)
    link(target, coll)
    target.location = (0.0, -0.02, 1.26)

    cam_data = bpy.data.cameras.new("Camera")
    cam_data.lens = 85
    cam_data.sensor_width = 36
    cam_data.dof.use_dof = True
    cam_data.dof.focus_object = target
    cam_data.dof.aperture_fstop = 5.6
    cam = bpy.data.objects.new("Camera", cam_data)
    link(cam, coll)
    cam.location = (-0.85, -1.75, 1.40)
    c = cam.constraints.new("TRACK_TO")
    c.target = target
    c.track_axis = "TRACK_NEGATIVE_Z"
    c.up_axis = "UP_Y"
    scene.camera = cam

    def light(name, kind, loc, energy, size=1.0, color=(1, 1, 1)):
        ld = bpy.data.lights.new(name, kind)
        ld.energy = energy
        ld.color = color
        if kind == "AREA":
            ld.size = size
        o = bpy.data.objects.new(name, ld)
        link(o, coll)
        o.location = loc
        t = o.constraints.new("TRACK_TO")
        t.target = target
        t.track_axis = "TRACK_NEGATIVE_Z"
        t.up_axis = "UP_Y"
        return o

    light("Key", "AREA", (-2.0, -1.4, 2.7), 260, size=1.6, color=(1.0, 0.96, 0.90))
    light("Fill", "AREA", (1.9, -1.9, 1.5), 70, size=2.5, color=(0.92, 0.95, 1.0))
    light("Rim", "AREA", (0.9, 0.35, 2.4), 120, size=0.6, color=(1.0, 0.98, 0.95))

    world = bpy.data.worlds.new("World")
    scene.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value = (0.55, 0.54, 0.52, 1)
    bg.inputs["Strength"].default_value = 0.25


def setup_render(scene, res, samples):
    scene.render.engine = "CYCLES"
    scene.cycles.device = "CPU"
    scene.cycles.samples = samples
    scene.cycles.use_adaptive_sampling = True
    scene.cycles.use_denoising = True
    try:
        scene.cycles.denoiser = "OPENIMAGEDENOISE"
    except TypeError:
        pass
    scene.cycles.max_bounces = 8
    scene.render.resolution_x = res
    scene.render.resolution_y = res
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    scene.view_settings.view_transform = "AgX"
    scene.view_settings.look = "AgX - Medium High Contrast"
    scene.view_settings.exposure = -1.2


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------


def build(args):
    scene = reset_scene()
    hammer, skin, strands, stone, chisel = make_textures()

    bust_coll = new_collection("Bust")
    env_coll = new_collection("Environment")
    rig_coll = new_collection("CameraAndLights")

    head_mb = build_head(bust_coll, args.mb_res)
    hair_mb = build_hair(bust_coll, args.mb_res)
    torso_mb = build_torso(bust_coll, args.mb_res)

    # metaballs → meshes
    bpy.context.view_layer.update()
    head = metaball_to_mesh(head_mb, "Head")
    hair = metaball_to_mesh(hair_mb, "Hair")
    torso = metaball_to_mesh(torso_mb, "Torso")
    truncate_torso(torso)

    # stretched coordinates so the hair noise reads as combed strands
    strand_empty = bpy.data.objects.new("StrandCoords", None)
    link(strand_empty, rig_coll)
    strand_empty.location = (0, 0, HEAD_Z)
    strand_empty.rotation_euler = (0, 0, math.radians(HEAD_TURN))
    strand_empty.scale = (0.02, 0.35, 0.05)
    strand_empty.hide_render = True

    for o in (head, hair, torso):
        shade_smooth(o)
    # surface refinement
    add_subsurf(head, 1)
    add_displace(head, skin, strength=0.0025)
    add_subsurf(hair, 1)
    add_displace(hair, strands, strength=0.006, coords_obj=strand_empty)
    add_subsurf(torso, 1)
    add_displace(torso, hammer, strength=0.005)
    add_displace(torso, chisel, strength=0.002)

    # tailoring
    lapels = [build_lapels(bust_coll, torso, s) for s in (-1, 1)]
    collar = build_collar(bust_coll, head)
    tie = build_tie(bust_coll, torso)
    plate = build_base_plate(bust_coll)

    # environment
    plinth = build_plinth(env_coll, stone)
    wall = build_wall(env_coll)

    # materials
    bronze = bronze_material()
    for o in [head, hair, torso, plate] + lapels + collar + tie:
        assign(o, bronze)
    for o in lapels + tie[1:]:
        shade_smooth(o)
    assign(plinth, stone_material())
    shade_smooth(plinth)
    assign(wall, plaster_material())

    build_camera_and_lights(scene, rig_coll)
    setup_render(scene, args.res, args.samples)
    return scene


def export(args, scene):
    out = os.path.abspath(args.out)
    os.makedirs(out, exist_ok=True)
    blend = os.path.join(out, "bust.blend")
    bpy.ops.wm.save_as_mainfile(filepath=blend, compress=True)
    print("saved", blend)
    if not args.no_export:
        # only the bust itself (no wall / camera / lights) goes to the exchange formats
        for o in bpy.data.objects:
            o.select_set(o.type == "MESH" and o.name not in ("Wall",))
        glb = os.path.join(out, "bust.glb")
        bpy.ops.export_scene.gltf(filepath=glb, export_format="GLB",
                                  use_selection=True, export_apply=True,
                                  export_materials="EXPORT")
        print("saved", glb)
        obj = os.path.join(out, "bust.obj")
        bpy.ops.wm.obj_export(filepath=obj, export_selected_objects=True,
                              apply_modifiers=True, export_materials=True)
        print("saved", obj)
    if not args.no_render:
        scene.render.filepath = os.path.join(out, "preview.png")
        bpy.ops.render.render(write_still=True)
        print("saved", scene.render.filepath)


if __name__ == "__main__":
    a = parse_args()
    s = build(a)
    export(a, s)
