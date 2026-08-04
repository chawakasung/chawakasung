# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repo is

A working repository for the **TB & IGRA with Full Automation** topic — tuberculosis
infection (TBI/LTBI) screening by Interferon-Gamma Release Assay on fully automated
laboratory systems.

**There is no application code yet.** Right now the repo holds research notes and an
installed skill set. Do not invent build, test, or lint commands — none exist. Add them
to this file when real tooling arrives.

## Layout

```
CLAUDE.md                              this file
docs/roche-image-sources-tb-igra.md    catalogue of Roche image sources for the topic
skills-lock.json                       skill manifest (source + path + hash per skill)
.agents/skills/<name>/                 installed skills (real files)
.claude/skills/<name>                  symlinks into .agents/skills/
```

## Skills

Eight are installed. Seven trigger on their own; one needs to be asked for.

| Skill | Source | Invocation |
|---|---|---|
| `hall-of-fame-personas` | MrMaii/Hall-of-Fame-Studio | automatic |
| `karpathy-guidelines` | multica-ai/andrej-karpathy-skills | automatic |
| `scrutinize` | thananon/9arm-skills | automatic |
| `frontend-design` | anthropics/skills | automatic |
| `find-skills` | vercel-labs/skills | automatic |
| `grilling` | mattpocock/skills | automatic |
| `domain-modeling` | mattpocock/skills | automatic |
| `grill-with-docs` | mattpocock/skills | `/grill-with-docs` only — wraps the two above it |

### Installing more

Install **into the project and commit them** — do not use the `-g` / global flag, even
though `find-skills` suggests it. Skills belong to this repo so they travel with it.

```bash
npx skills add https://github.com/<owner>/<repo> --skill <name>
```

Then read the skill's `SKILL.md` before relying on it (installed skills run with full
agent permissions), and commit `.agents/`, `.claude/`, and `skills-lock.json` together.

### hall-of-fame-personas

The outlier of the set: ~650 files, ~4 MB, 41 personas (40 historical figures plus a
`project_owner` role archetype), and 24 Python scripts, with its `SKILL.md` and persona
data written mostly in Chinese. It ranks personas against a task, plans a roundtable, and
assembles role prompts.

The personas live in `source/personas/{slug}/`. To add or edit one, change its
`persona.json` (plus `prompt.md`/`examples.md`/`memory.md`/`regression.json`) and rebuild
with `python3 scripts/run_pipeline.py`, which validates, compiles the registries, and
regenerates the mindframe/dist/legacy artifacts. `project_owner` was authored this way.

Its documented commands assume the skill sits at `skills/hall-of-fame-personas/` in its own
repo. Here it lives at `.agents/skills/hall-of-fame-personas/`, so run the scripts with that
directory as the working directory:

```bash
cd .agents/skills/hall-of-fame-personas && python3 scripts/persona_runtime.py list
```

Its `## App Integration` section refers to a React app that does not exist here — ignore it.

### Overlap to be aware of

`frontend-design` covers similar ground to the built-in `artifact-design` skill. When
publishing an Artifact, load `artifact-design` as the tooling requires, and use
`frontend-design` for aesthetic direction on top of it.

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

- **Branch:** develop on `claude/tb-igra-full-automation-dmwlwv`. Never push elsewhere
  without explicit permission.
- **Push:** `git push -u origin <branch>`. A stop hook fails the turn on untracked
  files, so commit and push before finishing.
- **Pull requests:** only when explicitly asked.
- **Language:** the user writes in Thai — reply in Thai. Keep commit messages, code, and
  documentation in English.

## Domain notes

Terminology worth keeping straight when writing about the topic:

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
