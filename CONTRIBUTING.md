# Contributing

Thanks for your interest in improving this profile. This repository holds only
the profile README and the small tooling that keeps it consistent — it ships no
library code. Contributions here are about keeping the portfolio map accurate,
clear, and well-organized.

For code issues in the actual libraries (contextweaver, ChainWeaver, AgentFence,
agent-kernel, VibeGuard, weaver-spec, skdr-eval), open an issue or PR on that
library's own repository instead.

## Scope

In scope for this repo:

- Fixing or improving a repo's one-line description in the profile map.
- Adding a repo that is missing from the map (and to `portfolio.yml`).
- Improving structure, wording, or accessibility of the README.
- Improving the consistency tooling (`check_portfolio.py`).

Out of scope: changes to the libraries themselves, and marketing copy.

## How to propose a change

1. **Read the conventions first.** `STYLE.md` documents the writing style
   (neutral tone, banned overclaim terms, ~80-column wrapping, problem-first
   chooser, image/accessibility rules). `AGENTS.md` is the canonical guide for
   automated edits and explains the README ↔ `portfolio.yml` contract.
2. **Edit the source of truth.** `portfolio.yml` is the single source of truth
   for the repo list and metadata. If you change a repo entry, update both
   `portfolio.yml` and `README.md` so they stay consistent.
3. **Verify a linked repo before describing it.** Read the repo's own
   README/description so the one-line summary here matches its actual scope.
4. **Run the consistency check** before opening a PR:

   ```sh
   python check_portfolio.py
   ```

   It must exit `0`. CI runs the same check on every push and pull request.
5. **Open a PR.** Use one of the issue forms under "New issue" if you want to
   propose a change without writing it yourself.

## Contributing a quick fix (good first contributions)

Small, self-contained changes are very welcome and are a good first step:

- Spotted an outdated or inaccurate repo description? Open a one-line fix.
- Found a repo that is in `## The repos` but missing from `## Start here`
  (or vice versa)? Add the missing entry.
- Noticed a wrong-case repo link, a typo, or a wrapping slip? Fix it.
- Saw an image without alt text? Add concise descriptive alt text.

Issues suitable for a first contribution are labeled
[`good first issue`](https://github.com/dgenio/dgenio/labels/good%20first%20issue).
Keep the change minimal and matched to the existing style; that is the fastest
path to merge.

## Commit and PR conventions

- Use [Conventional Commits](https://www.conventionalcommits.org/) prefixes
  (`feat:`, `fix:`, `docs:`, `chore:`), matching recent history.
- Keep PRs focused: one logical change per PR where practical.
- Record notable user-visible changes in `CHANGELOG.md`.
