# Changelog

Notable changes to the profile and portfolio map. This is a lightweight log of
user-visible changes (repos added/removed, descriptions revised, structure or
tooling changes), not a commit-by-commit history.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/),
and dates use commit dates (YYYY-MM-DD).

## [Unreleased]

### Added

- Repository governance and contributor documentation: `CONTRIBUTING.md`,
  `AGENTS.md`, `STYLE.md`, `SECURITY.md`, `.github/CODEOWNERS`,
  GitHub issue templates, `docs/discoverability.md`, and this changelog.
- Complete portfolio routing for `lessonweaver`, `intentflow`,
  `agent-routing-eval-lab`, `mcp-agent-security-dojo`, and
  `enterprise-agent-control-plane`, with experiments/labs separated from
  reusable libraries and tools.

### Changed

- Landing-experience pass on the README: added a one-line portfolio tagline,
  a problem-first chooser, an at-a-glance portfolio table, a clearer maturity
  boundary between reusable tools and reference material, a request-path
  composition summary, and an explicit Contact block.
- `portfolio.yml` now lists all maintained projects represented by the profile
  README rather than only the original Weaver Stack subset.

## 2026-06-17

### Added

- `portfolio.yml` as the single source of truth for the repo list and metadata.
- `check_portfolio.py` and a CI workflow that verify `README.md` and
  `portfolio.yml` stay consistent.

### Fixed

- Markdown link regex now handles a trailing `)` correctly.

## 2026-06-06

### Changed

- Rewrote the profile README as a neutral, problem-first project router.
- Softened and aligned VibeGuard wording.
- Re-wrapped README prose to ~80 columns.

## 2026-03-11

### Added

- Initial profile README with project details.

[Unreleased]: https://github.com/dgenio/dgenio/commits/main
