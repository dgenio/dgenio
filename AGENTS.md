# AGENTS.md

Guidance for AI coding agents (and humans) editing this repository. This is the
canonical agent guide; the documents it references hold the detail.

## What this repo is

This is a **GitHub profile / portfolio repository** (`dgenio/dgenio`). It ships
no application code. Its job is to present a neutral, scannable map of the
owner's open-source repos and how they relate.

Tracked content:

- `README.md` — the rendered profile (the public artifact).
- `portfolio.yml` — the single source of truth for the repo list and metadata.
- `check_portfolio.py` — consistency checker between `README.md` and
  `portfolio.yml`.
- `.github/workflows/check.yml` — CI that runs the checker on push/PR to `main`.

## Hard rules

1. **Keep `README.md` and `portfolio.yml` consistent.** Every
   `https://github.com/dgenio/<repo>` link in the README must correspond to an
   entry in `portfolio.yml`, and every portfolio name/link must appear in the
   README. `check_portfolio.py` enforces this and runs in CI.
2. **Do not add non-repo `github.com/dgenio/...` links to `README.md`.** The
   consistency check treats every `github.com/dgenio/<x>` link in the README
   as a portfolio repo. Linking, for example, to a file path under
   `dgenio/dgenio` would be read as a bogus repo and fail CI. Link in-repo
   docs from
   `CONTRIBUTING.md`, `AGENTS.md`, or the issue-template config instead.
3. **Follow the style guide.** Neutral tone, no overclaim terms, honest
   maturity, problem-first chooser, ~80-column wrapping. See `STYLE.md`.
4. **Verify linked-repo descriptions.** Read a repo's own README/description
   before writing or editing its one-line summary here.
5. **Images require alt text** and must follow the simplicity guardrail in
   `STYLE.md`. The README is image-free today; keep it that way unless a visual
   clearly earns its place.

## In-repo documentation link strategy

A profile README renders in two places: the public profile page and the repo
view. **Relative links resolve in the repo view but break on the profile page.**
To avoid broken links and to keep the consistency check meaningful:

- The README **does not** link to in-repo docs. Cross-linking between in-repo
  docs (this file, `STYLE.md`, `CONTRIBUTING.md`, `SECURITY.md`) uses **relative
  links**, which render correctly when those docs are viewed in the repo.
- If a README link to an in-repo doc ever becomes necessary, use the full
  repo-absolute URL form (`https://github.com/dgenio/dgenio/blob/main/<file>`),
  and update `check_portfolio.py` so the link is not mistaken for a portfolio
  repo.

## Validation steps

Before committing, run the consistency check:

```sh
python check_portfolio.py
```

Exit code `0` means `README.md` and `portfolio.yml` are consistent. Fix any
reported mismatch before pushing; CI runs the same check.

## Where things live (avoid duplication)

- **Style / tone / accessibility / simplicity rules:** `STYLE.md`.
- **How to contribute / propose changes:** `CONTRIBUTING.md`.
- **Security reporting:** `SECURITY.md`.
- **Recommended topics & description:** `docs/discoverability.md`.
- **Notable changes:** `CHANGELOG.md`.

Pick the one canonical home above and cross-link to it; do not restate the same
rule in multiple files.
