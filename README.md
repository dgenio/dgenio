# Hi, I'm Diogo

**Open-source building blocks for reliable, predictable AI agents — context
control, deterministic execution, tool-call policy, and pre-merge code checks.**

I build open-source infrastructure for reliable AI agents. The focus is on
making agent behavior predictable: controlling context, running deterministic
work without an LLM in the loop, enforcing what tools are allowed to do, and
checking generated code before it ships. The repos below are independent but
designed to fit together.

> 📖 **New here? Read the overview** —
> [The Weaver Stack: One Contract Layer for Safe LLM Agents](https://pub.towardsai.net/the-weaver-stack-one-contract-layer-for-safe-llm-agents-7f733cad5eac)
> explains why these repos exist and how they compose.

## Start here

Pick the repo that matches the problem you have. I label labs, experiments,
and active incubations explicitly so you can distinguish reusable tools from
research hypotheses and reference material.

### Libraries and tools

- **My agent has too many tools or oversized tool outputs** →
  [contextweaver](https://github.com/dgenio/contextweaver) compiles large tool
  catalogs into bounded choices and firewalls big tool results to keep prompts
  within budget.
- **My agent keeps repeating the same tool sequence** →
  [ChainWeaver](https://github.com/dgenio/ChainWeaver) compiles those repeated
  paths into typed, deterministic flows so the LLM is not re-invoked between
  steps that never change.
- **I want to control what an agent's tool calls are allowed to do** →
  [AgentFence](https://github.com/dgenio/AgentFence) is a standalone local MCP
  policy firewall; [agent-kernel](https://github.com/dgenio/agent-kernel) is an
  embeddable capability/policy layer for your own runtime.
- **I want to catch risky AI-generated code before merge** →
  [VibeGuard](https://github.com/dgenio/VibeGuard) is an offline pre-merge gate
  for security risks and AI-generation artifacts in a diff.
- **My coding agent keeps repeating a failure already corrected in review** →
  [lessonweaver](https://github.com/dgenio/lessonweaver) is an **incubating
  product hypothesis**: it is testing whether evidence-backed change selection
  adds value beyond an equally capable human choosing the smallest intervention
  (nothing, an instruction, a Skill, or deterministic enforcement). Its public
  experiment/kill criteria are versioned in the repo; it should not yet be read
  as proven “self-improving agents.”
- **I want portable assurance for a high-risk agent action** →
  [intentflow](https://github.com/dgenio/intentflow) is an **incubating research
  hypothesis**. v0 is a legacy/experimental reference runtime; v1 first tests
  whether a minimal action-assurance contract adds material value beyond a
  strong policy + exact request/approval/receipt + signed-attestation baseline.
  If that comparison fails, the protocol/language direction is explicitly meant
  to shrink or stop.
- **I want these components to interoperate without adopting all of them** →
  [weaver-spec](https://github.com/dgenio/weaver-spec) defines the
  language-agnostic contracts and shared vocabulary that contextweaver,
  ChainWeaver, and agent-kernel build on, so each stays independently usable.
- **I want to evaluate a decision policy on logged data before rolling it out** →
  [skdr-eval](https://github.com/dgenio/skdr-eval) estimates how a candidate
  recommender, routing, or targeting policy would perform offline, with
  diagnostics on whether the estimate can be trusted. It is an experimental
  applied-ML project, separate from the agent-runtime libraries above.

### Labs and reference architectures

Use these to learn, compare, or adapt patterns rather than as drop-in runtime
dependencies:

- **I want a reproducible lab for comparing agent-routing policies** →
  [agent-routing-eval-lab](https://github.com/dgenio/agent-routing-eval-lab)
  is a reference evaluation harness for routing experiments and rollout
  evidence.
- **I want hands-on examples of agent-security failures and controls** →
  [mcp-agent-security-dojo](https://github.com/dgenio/mcp-agent-security-dojo)
  is an educational security lab with vulnerable and governed scenarios.
- **I want to see the governance pieces assembled into one reference system** →
  [enterprise-agent-control-plane](https://github.com/dgenio/enterprise-agent-control-plane)
  is a reference architecture for an auditable agent control plane.

## Portfolio map

| Project | Type | Best fit |
| --- | --- | --- |
| [contextweaver](https://github.com/dgenio/contextweaver) | Library | Context and tool-budget control |
| [ChainWeaver](https://github.com/dgenio/ChainWeaver) | Library | Deterministic repeated workflows |
| [AgentFence](https://github.com/dgenio/AgentFence) | CLI / proxy | MCP tool-call policy enforcement |
| [agent-kernel](https://github.com/dgenio/agent-kernel) | Library | Embedded capabilities and authorization |
| [VibeGuard](https://github.com/dgenio/VibeGuard) | CLI / CI gate | Pre-merge AI-code checks |
| [lessonweaver](https://github.com/dgenio/lessonweaver) | **Incubating product** | Evidence-backed intervention selection for recurring coding-agent failures |
| [intentflow](https://github.com/dgenio/intentflow) | **Incubating research / legacy v0** | Test portable action-assurance contracts against strong baselines |
| [weaver-spec](https://github.com/dgenio/weaver-spec) | Contract spec | Shared interoperability contracts |
| [skdr-eval](https://github.com/dgenio/skdr-eval) | Experimental library | Offline policy evaluation |
| [agent-routing-eval-lab](https://github.com/dgenio/agent-routing-eval-lab) | Reference lab | Routing evaluation |
| [mcp-agent-security-dojo](https://github.com/dgenio/mcp-agent-security-dojo) | Educational lab | Agent-security exercises |
| [enterprise-agent-control-plane](https://github.com/dgenio/enterprise-agent-control-plane) | Reference architecture | End-to-end governance patterns |

## Incubation discipline

Two repos currently have explicit falsification gates rather than ordinary
feature roadmaps:

- **LessonWeaver:** pilot → preregistered confirmatory experiment → ablation →
  external replication. It graduates only if behavior, safety, product-value,
  complexity, and replication gates all pass against a fair human baseline.
- **IntentFlow v1:** strong existing-policy/attestation baseline → adversarial
  corpus → category kill gate. Second verifier, substantial formal-method work,
  and a new `.iflow` frontend remain blocked until a material assurance gap is
  demonstrated.

A smaller product, an existing-standards profile, or an archived hypothesis is
a successful incubation outcome when that is what the evidence supports.
Implementation throughput and GitHub stars are not substitutes for those gates.

## How they relate

At a glance, the request path composes as: context control (contextweaver) →
deterministic execution (ChainWeaver) → authorization (agent-kernel), on shared
contracts (weaver-spec). AgentFence can enforce at the external MCP boundary.
VibeGuard, LessonWeaver, skdr-eval, and the labs sit around that core path.
IntentFlow's future role is deliberately unresolved until its action-assurance
category experiment passes.

- **AgentFence and agent-kernel** apply the same idea — deciding whether a tool
  call is allowed — at different integration points. AgentFence is a standalone
  local proxy you put in front of MCP tool traffic; agent-kernel is the
  embeddable library you call from inside your own agent runtime.
- **contextweaver, ChainWeaver, agent-kernel, and weaver-spec** are meant to
  compose: ChainWeaver handles deterministic execution, contextweaver controls
  context and token budget, agent-kernel enforces authorization, and
  weaver-spec defines shared contracts. Each can also be used on its own.

## Contact

Open to feedback, design discussion, and collaboration. Concrete ways to start:

- **Found a bug or have a feature request for a specific project?** Open an
  issue on that repo (linked above).
- **Have a question, idea, or want to discuss the ecosystem as a whole?** Open
  an issue on this profile repo.
