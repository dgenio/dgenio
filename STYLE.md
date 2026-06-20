# Profile README style guide

This repository is a GitHub **profile / portfolio README**. Its main asset is a
disciplined, neutral, scannable voice. This document records the de facto style
so future edits (human or AI) preserve it instead of relying on memory.

`AGENTS.md` is the canonical entry point for automated editors; this file is the
detailed style reference it links to.

## Writing-style invariant

- **Neutral, honest tone.** Describe what each repo does and the problem it
  solves. Do not market.
- **No overclaiming.** The following terms are banned in the README and
  portfolio copy unless they are literally, verifiably true and necessary:
  - `best`
  - `leading`
  - `production-ready`
  - `enterprise-grade`
  - `trending`
- **Honest maturity language.** Use the maturity values already used in
  `portfolio.yml` (`draft`, `experimental`, `beta`, …). Do not inflate them.
- **Problem-first chooser.** The `## Start here` section is organized as
  "problem the reader has -> repo that solves it". Keep new entries in that
  shape: a bold/arrow problem statement, the repo link, one neutral sentence.
- **~80-column wrapping.** Prose is hard-wrapped to roughly 80 columns
  (see commit history: "Re-wrap ... to ~80 columns"). Keep it. Long URLs and
  table rows are the only allowed exceptions.
- **Verify before describing.** Read a linked repo's own README/description
  before writing or editing its one-line summary in this profile. Keep the
  profile line consistent with the repo's actual scope.

## Image and accessibility policy

The README currently has zero images, which keeps first paint fast and avoids
third-party data calls. Any future image (badge, diagram, metrics panel) must
follow these rules:

- **Alt text is mandatory.** Every image must have concise, descriptive alt
  text. Treat it like a one-line description of what the image communicates, not
  a filename.
  - Markdown: `![meaningful description](path)` — never `![](path)`.
  - HTML: `<img src="..." alt="meaningful description">`.
- **Long descriptions** for complex visuals go in an adjacent text block or a
  `<details>` block, not crammed into the alt text.
- **Mermaid / diagram blocks** render without alt text, so a diagram must be
  accompanied by an adjacent textual description of the same information.

## Simplicity guardrail

The profile is fast and clutter-free today; that is worth protecting.

- **Prefer text and native Markdown** over badge walls, GIFs, or live
  third-party image services.
- **Self-host over live-embed.** If an image is justified, prefer an asset
  committed to the repo over a live external image URL (which adds latency and a
  third-party data call).
- **No telemetry / no opaque third parties.** The portfolio's ethos is "no cloud
  dependency or telemetry". Do not add widgets that send profile or visitor data
  to unverified third parties.
- **Justify each visual.** A badge or image should earn its place; default to
  leaving it out. These are sensible defaults, not absolute bans — document the
  reason when you add a visual.

## Links

- External repos are linked with absolute `https://github.com/...` URLs.
- See `AGENTS.md` for the in-repo documentation link strategy (absolute vs
  relative) and why the README is kept free of non-repo `github.com/dgenio/...`
  links.
