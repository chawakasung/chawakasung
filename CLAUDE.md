# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repo is

A personal working repository holding **two unrelated topics** plus the skill set used
across both. Check which one you are in before assuming context.

1. **TB & IGRA with Full Automation** — tuberculosis infection (TBI/LTBI) screening by
   Interferon-Gamma Release Assay on fully automated laboratory systems. Research notes,
   `docs/`, and the domain notes near the end of this file.
2. **Hall of Frame** — a framed-art-print business (also referred to as "Only Frame")
   selling on FB Marketplace. Its assets live outside this repo on the owner's machine;
   what is here is the `hof-story-teller` skill and the batch builder it pairs with.

**There is no application code yet.** Apart from one standalone script inside a skill,
the repo holds notes and skills. Do not invent build, test, or lint commands — none
exist. Add them to this file when real tooling arrives.

Note the collision: **HOF here means Hall of Frame, not Hall of Fame.** A
`hall-of-fame-personas` skill was briefly installed and then reverted (commits `e239200`
and `08fa3cf`), so git history contains a genuine Hall of *Fame* skill that is unrelated
to the Hall of *Frame* business. The brand name is a pun on the other one, which makes
the two easy to conflate.

## Layout

```
CLAUDE.md                              this file
docs/roche-image-sources-tb-igra.md    catalogue of Roche image sources for the TB topic
skills-lock.json                       skill manifest (source + path + hash per skill)
.agents/skills/<name>/                 installed skills (real files)
.claude/skills/<name>                  symlinks into .agents/skills/
```

## Skills

Eight are present. Seven trigger on their own; one needs to be asked for.

| Skill | Source | Invocation |
|---|---|---|
| `karpathy-guidelines` | multica-ai/andrej-karpathy-skills | automatic |
| `scrutinize` | thananon/9arm-skills | automatic |
| `frontend-design` | anthropics/skills | automatic |
| `find-skills` | vercel-labs/skills | automatic |
| `grilling` | mattpocock/skills | automatic |
| `domain-modeling` | mattpocock/skills | automatic |
| `hof-story-teller` | written here — not installed | automatic |
| `grill-with-docs` | mattpocock/skills | `/grill-with-docs` only — wraps the two above it |

### `hof-story-teller`

Copy for the Hall of Frame business: FB Marketplace `LISTING.txt`, social captions,
gallery blurbs, and the brand story. Hand-written in this repo, so it has **no entry in
`skills-lock.json`** — that file tracks skills fetched by `npx skills add`, and a local
skill has no upstream source or hash to record. Edit it directly; nothing regenerates it.

It carries `scripts/rebuild.py`, the batch builder that crops four 1080×1350 Marketplace
images per SKU and flags a missing `LISTING.txt`. The script is the reason the skill
exists — it prepares the images and leaves the copy to be written. It reads paths from
`$HOF_PROJ` / `$HOF_DB`, needs Pillow, and touches only the owner's local asset folders,
none of which are in this repo. It cannot run in a Claude Code web session.

Two working assumptions are recorded inside the skill and are cheap to correct: customer
copy is written in **Thai**, and the pieces are **reproductions, not originals**. The
second one drives a set of fidelity rules — no wording implying an original or a limited
edition, no invented sizes, materials, or prices.

### Installing more

Install **into the project and commit them** — do not use the `-g` / global flag, even
though `find-skills` suggests it. Skills belong to this repo so they travel with it.

```bash
npx skills add https://github.com/<owner>/<repo> --skill <name>
```

Then read the skill's `SKILL.md` before relying on it (installed skills run with full
agent permissions), and commit `.agents/`, `.claude/`, and `skills-lock.json` together.

### Overlap to be aware of

`frontend-design` covers similar ground to the built-in `artifact-design` skill. When
publishing an Artifact, load `artifact-design` as the tooling requires, and use
`frontend-design` for aesthetic direction on top of it.

For the Hall of Frame gallery pages, `hof-story-teller` decides what gets said and in what
order; `frontend-design` decides how it looks. Write the copy first, then design around it.

## Environment constraints

**General web access is blocked.** The network policy rejects outbound CONNECT for
`roche.com`, `diagnostics.roche.com`, news mirrors, and even Wikipedia (gateway returns
403). This means:

- `WebSearch` **works** — it goes through a separate channel.
- `WebFetch` and `curl` to arbitrary hosts **fail**. Do not promise to download a file,
  scrape a page, or verify a link's contents.
- npm registry and GitHub (via the git proxy) are reachable, so `npx skills add` works.

Check `curl -sS "$HTTPS_PROXY/__agentproxy/status"` to see current policy denials before
concluding something is broken. Never disable TLS verification or unset `HTTPS_PROXY`.

When a source cannot be fetched, say so plainly and hand over the URL rather than
describing page contents you have not seen.

## Conventions

- **Branch:** one per topic, assigned at session start — `claude/tb-igra-full-automation-dmwlwv`
  for the TB work, `claude/hof-story-teller-ruu08t` for Hall of Frame. Use the branch the
  session names; never push elsewhere without explicit permission.
- **Push:** `git push -u origin <branch>`. A stop hook fails the turn on untracked
  files, so commit and push before finishing.
- **Pull requests:** only when explicitly asked.
- **Language:** the user writes in Thai — reply in Thai. Keep commit messages, code, and
  documentation in English. **Customer-facing Hall of Frame copy is the exception: it is
  written in Thai**, since it is the product rather than documentation.

## Domain notes — TB & IGRA

Applies to topic 1 only; nothing below concerns Hall of Frame. Terminology worth keeping
straight when writing about the topic:

| Term | Meaning |
|---|---|
| TBI / LTBI | Tuberculosis infection / latent TB infection — infected, not diseased |
| IGRA | Interferon-Gamma Release Assay — blood test measuring IFN-γ released by T cells |
| ESAT-6, CFP-10 | *M. tuberculosis*-specific antigens, absent from BCG and most NTM |
| TST | Tuberculin Skin Test (Mantoux) — the older method IGRA is compared against |
| Indeterminate | Result where controls fail, common in immunosuppressed patients |
| TLA | Total Lab Automation |
| TAT | Turnaround time |

Two facts that are easy to get wrong: **IGRA cannot distinguish latent infection from
active disease** — a positive result always needs clinical and radiographic correlation.
And IGRA's advantage over TST is specificity from BCG vaccination, not sensitivity.

If the domain model grows, `domain-modeling` maintains `CONTEXT.md` as a glossary and
`docs/adr/` for decisions. Neither exists yet; create them lazily when there is something
real to record.
