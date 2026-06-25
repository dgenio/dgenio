# Hi, I'm Diogo

I build open-source infrastructure for reliable AI agents. The focus is on
making agent behavior predictable: controlling context, running deterministic
work without an LLM in the loop, enforcing what tools are allowed to do, and
checking generated code before it ships. The repos below are independent but
designed to fit together.

> 📖 **New here? Read the overview** — [The Weaver Stack: One Contract Layer for Safe LLM Agents](https://pub.towardsai.net/the-weaver-stack-one-contract-layer-for-safe-llm-agents-7f733cad5eac) explains why these repos exist and how they compose.

## Start here

Pick the repo that matches the problem you have:

- **My agent has too many tools or oversized tool outputs** →
  [contextweaver](https://github.com/dgenio/contextweaver) compiles large tool
  catalogs into bounded choices and firewalls big tool results to keep prompts
  within budget.
- **My agent keeps repeating the same tool sequence** →
  [ChainWeaver](https://github.com/dgenio/ChainWeaver) compiles those repeated
  paths into typed, deterministic flows so the LLM is not re-invoked between
  steps that never change.
- **I want to control what an agent's tool calls are allowed to do** →
  [AgentFence](https://github.com/dgenio/AgentFence) (a local policy firewall
  you run in front of MCP tool calls) or
  [agent-kernel](https://github.com/dgenio/agent-kernel) (the same kind of
  enforcement as an embeddable capability/policy layer inside your own runtime).
- **I want to catch risky AI-generated code before merge** →
  [VibeGuard](https://github.com/dgenio/VibeGuard) is an offline pre-merge gate
  that flags common security risks and AI-generation artifacts in a diff.
- **I want to evaluate a decision policy on logged data before rolling it out** →
  [skdr-eval](https://github.com/dgenio/skdr-eval) estimates how a candidate
  recommender, routing, or targeting policy would perform offline, with
  diagnostics on whether the estimate can be trusted.

## The repos

- [VibeGuard](https://github.com/dgenio/VibeGuard) — fast, offline pre-merge
  check that flags common security risks and AI-generation artifacts in code
  diffs.
- [ChainWeaver](https://github.com/dgenio/ChainWeaver) — compiles repeated,
  deterministic tool sequences into auditable typed flows, removing unnecessary
  LLM calls between steps.
- [contextweaver](https://github.com/dgenio/contextweaver) — context gateway for
  tool-heavy agents that routes large tool catalogs to bounded choices and
  trims oversized tool results to control prompt tokens.
- [AgentFence](https://github.com/dgenio/AgentFence) — local MCP policy firewall
  that evaluates each tool call and allows, denies, or asks for approval, with
  no cloud dependency or telemetry.
- [agent-kernel](https://github.com/dgenio/agent-kernel) — embeddable
  capability-based authorization layer that issues revocable, principal-scoped
  tokens and keeps a tamper-evident audit of what ran.
- [weaver-spec](https://github.com/dgenio/weaver-spec) — language-agnostic
  contracts and shared vocabulary so these components can interoperate without
  adopting all of them.
- [skdr-eval](https://github.com/dgenio/skdr-eval) — offline policy evaluation
  library (applied ML side project) for estimating policy performance from
  logged decisions before an A/B test.

## How they relate

- **AgentFence and agent-kernel** apply the same idea — deciding whether a tool
  call is allowed — at different integration points. AgentFence is a standalone
  local proxy you put in front of MCP tool traffic; agent-kernel is the
  embeddable library you call from inside your own agent runtime.
- **contextweaver, ChainWeaver, agent-kernel, and weaver-spec** are meant to
  compose: ChainWeaver handles deterministic execution, contextweaver controls
  context and token budget, agent-kernel enforces authorization, and
  weaver-spec defines the shared contracts that let them work together. Each can
  also be used on its own.

Open to feedback, issues, design discussion, and collaboration.
