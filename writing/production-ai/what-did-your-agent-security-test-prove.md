# Your Agent Passed the Security Test. What Did You Actually Prove?

*An authorization decision, a policy test, and an agent-security claim are different things.*

Suppose an agent reads a document containing a malicious instruction: write a secret into a `.env` file. The agent attempts the write. A tool-call policy denies it before the upstream MCP server receives the request.

That is a useful test. It is also easy to overstate.

You have evidence that **one particular tool request**, with **particular arguments**, was denied at **one configured boundary** under **one effective policy**. You have not demonstrated that every path to the file was covered, that the policy was sufficient, or that prompt injection was prevented.

For production reviews, this distinction matters more than another green check.

## Five questions behind a passing test

### 1. Was the intended policy actually expressed?

Validation can establish that a policy is well formed. Fixtures can establish its decisions for selected examples. Neither establishes that the rules match the organization's intended permissions.

A permissive policy can pass every test written to confirm its permissive behavior.

**Ask:** which actions should be denied, and what counterexamples were included in the test set?

### 2. Which exact action was evaluated?

A log entry saying "authorized" is not enough to reproduce the decision. The reviewer needs to know, within appropriate confidentiality limits:

- tool and operation;
- arguments or a cryptographic binding to the relevant request;
- effective policy and version/digest;
- outcome and reason;
- enforcement point and available identity/context.

This does **not** mean copying raw secrets into CI artifacts. An evidence design must balance the ability to reconstruct decisions against sensitive-data handling.

**Ask:** can a reviewer connect the actual request to the actual evaluated policy, or are they merely looking at nearby logs?

### 3. Did enforcement happen before the side effect?

Testing a policy evaluator in isolation does not prove that the deployed client routes every tool call through it.

A mediated integration test can show that a denied request was not forwarded to the configured upstream server. It does not prove that a different client, transport, direct API path, or already-held credential cannot bypass that boundary.

**Ask:** what paths are intentionally out of scope, and which other controls cover them?

### 4. Can the evidence be verified later?

A hash chain can detect changes within the events it contains. Signing can establish stronger claims about the writer when keys are managed correctly.

Neither mechanism by itself proves that every relevant event was collected. Completeness, retention, trustworthy time, and anchoring may need separate treatment.

**Ask:** what integrity property is proven, and what collection assumptions remain?

### 5. What happened after an allow?

"Allow" is an authorization outcome. It is not evidence that the downstream tool executed correctly or that the intended business change occurred.

For a consequential operation, distinguish:

1. the requested action;
2. the authorization decision;
3. whether it was forwarded;
4. the result reported by the target;
5. the business-side effect, if independently observable.

A policy receipt answers only part of that chain.

## Evidence states are not security ratings

A reviewer should be able to distinguish missing observations from failed checks.

| Evidence state | Narrow meaning |
| --- | --- |
| `observed` | The supplied artifact supports the specific claim being checked. |
| `partial` | Relevant evidence exists, but a required part is missing. |
| `not_evaluated` | The available data does not support evaluating the claim. |
| `failed` | The supplied test, validation, or integrity evidence explicitly failed. |

An `observed` binding check does not mean "secure"; a `partial` check does not necessarily mean "unsafe". The labels describe the evidence, not a universal assessment of the agent.

There is a concrete, public example in the [AgentFence/VeriCordon evidence guide](https://github.com/dgenio/agentfence/blob/main/docs/evidence-bundle.md). A documented **pre-release** run had four audit events with **0/4** carrying both action and effective-policy binding fields, so the check remained `partial`. After an implementation change, a maintained **fresh-consumer test** recorded the binding fields on **3/3 supplied representative events**.

Neither number is a deployment-wide assurance result or external customer evidence. The point is that the report preserves exactly what was observed, including gaps.

## Where should authorization live?

The right control depends on the failure you are trying to prevent.

- **Model instruction:** useful behavioral guidance; not an independent authorization mechanism.
- **Application/runtime:** potentially rich business and user context; may be tightly coupled to the application.
- **Tool proxy:** a useful point to inspect mediated calls and arguments; can be bypassed if other routes exist.
- **Target API:** can enforce permissions even when an intermediary is bypassed; may lack the application-level intent that motivated the action.

These controls may need to coexist. The [MCP specification's authorization guidance](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) addresses transport and token security; that is important, but it does not automatically answer whether a particular principal should perform a particular high-impact tool action with those arguments at this moment.

The [OWASP practical guide to secure MCP server development](https://genai.owasp.org/resource/a-practical-guide-for-secure-mcp-server-development/) is a complementary security reference. Neither a standard nor a product's support for it substitutes for evidence from your own deployed system.

## A short review worksheet

For the next agent/tool release, fill in these six lines before accepting the security claim:

| Review field | What to record |
| --- | --- |
| Claim | The narrow statement this test is meant to establish |
| Boundary | The actual point that evaluated or blocked the request |
| Evidence | Artifact, policy version, recorded calls, result, verification |
| Coverage | The calls and paths the evidence represents |
| Missing | Anything not observed, not evaluated, or deliberately excluded |
| Next test | A specific counterexample that could invalidate the claim |

A useful outcome may be: *our existing gateway and CI evidence already answer these questions; we do not need another tool*. That is a good result.

## A reproducible public example

[AgentFence](https://github.com/dgenio/agentfence) is a local tool-call policy boundary. [VeriCordon](https://github.com/dgenio/agentfence/blob/main/docs/evidence-bundle.md) packages narrowly scoped local/CI authorization evidence into `report.md` and `report.json`, with explicit non-claims.

The maintained public examples are available to run and inspect. This is not a hosted security certification, sandbox, promise of complete mediation, or guarantee about what a downstream tool did.

If you review agent authorization changes and already have this solved in CI or your gateway, I would be interested in that counterexample. If your team repeatedly needs to reconstruct these decisions by hand, describe the missing review step via [the public commercial-validation discussion](https://github.com/dgenio/agentfence/issues/274) **without posting sensitive policies, customer information, credentials or audit logs**. Private enquiries can instead use the [VeriCordon contact site](https://vericordon.diogofcul.chatgpt.site/).

---

**Sources and scope:** [AgentFence evidence design and non-claims](https://github.com/dgenio/agentfence/blob/main/docs/evidence-bundle.md) · [AgentFence threat model](https://github.com/dgenio/agentfence/blob/main/docs/threat-model.md) · [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) · [OWASP MCP security guide](https://genai.owasp.org/resource/a-practical-guide-for-secure-mcp-server-development/).

*The hypothetical file-write scenario is not a customer case study. The cited 0/4 and 3/3 samples are project-documented test observations; they are not proof of external adoption or deployed security.*
