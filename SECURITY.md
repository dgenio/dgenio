# Security policy

This repository (`dgenio/dgenio`) is a **GitHub profile / portfolio repo**. It
contains only the profile README and a small consistency checker — no shipped
library code and no runtime that processes untrusted input.

## Reporting an issue in one of the libraries

Security reports for the actual projects should go to that project's own
repository, where the maintainers and security tooling for that code live:

- contextweaver — https://github.com/dgenio/contextweaver
- ChainWeaver — https://github.com/dgenio/ChainWeaver
- AgentFence — https://github.com/dgenio/AgentFence
- agent-kernel — https://github.com/dgenio/agent-kernel
- VibeGuard — https://github.com/dgenio/VibeGuard
- weaver-spec — https://github.com/dgenio/weaver-spec
- skdr-eval — https://github.com/dgenio/skdr-eval

Prefer each repository's private vulnerability reporting (GitHub Security
Advisories) where enabled, rather than a public issue, for anything sensitive.

## Reporting an issue with this profile repo

For problems limited to this repo itself — for example a broken or misdirected
link, or an issue in `check_portfolio.py` — open a regular issue. There is no
sensitive attack surface here, so public reporting is appropriate.

Please do not include exploit details or secrets in any report filed here.
