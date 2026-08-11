# dgenio portfolio incubation discipline

AI-assisted implementation makes code cheaper to produce. It does not make maintainer attention, external adoption, experimental design, review, credibility, or distribution cheap.

This portfolio therefore treats **overproduction before validation** as a first-class risk.

## WIP limit

Only **one speculative product incubation** receives primary implementation bandwidth at a time.

Current sequence:

1. **LessonWeaver** — active product incubation: complete the minimum semantic vertical slice, run the pilot, freeze the confirmatory experiment, run ablations, and require external replication before broad promotion.
2. **IntentFlow v0** — maintenance/credibility containment only while LessonWeaver is the active product experiment; bounded correctness/security/honesty fixes remain allowed.
3. **Core proven/stronger repos** — continue normal support, adoption, reliability, contributor, and interoperability work where external usefulness already exists.
4. **LessonWeaver decision gate** — continue standalone, narrow, move selected capability elsewhere, or archive based on evidence.
5. **IntentFlow v1** — only after that portfolio decision should the protocol experiment receive material implementation bandwidth beyond the strong-baseline/adversarial-corpus research needed to cheaply test whether the category exists.

This WIP limit is about **primary speculative expansion**, not a ban on maintenance, security fixes, contributor support, or low-cost falsification research.

## Why

Running several speculative projects at full implementation speed creates predictable failure modes:

- feature count grows faster than independent adoption;
- the maintainer becomes the designer, evaluator, gold-label author, and primary user;
- sunk-cost pressure makes narrowing/archiving harder;
- distribution and external validation receive less attention than implementation;
- AI agents can keep a large backlog moving even when the product thesis is still unproven.

## Graduation is evidence, not throughput

A project does not graduate because it has:

- many issues closed;
- a polished README;
- a large test suite;
- multiple same-maintainer implementations;
- sophisticated formalism;
- more integrations;
- more GitHub stars.

Graduation criteria belong to each project's own incubation contract.

For the current incubations:

- **LessonWeaver:** behavior + safety + product-value + complexity + external-replication gates against an equally capable human baseline.
- **IntentFlow v1:** a material assurance gap beyond a strong policy/request/approval/receipt/signed-attestation baseline, followed by minimal portable semantics, independent verification/enforcement evidence, and external interoperability before standards-like claims.

## Negative results are successful incubation outcomes

The portfolio explicitly accepts these as good outcomes when supported by evidence:

- shrink a product to the one subsystem that creates measurable value;
- move a reusable contract into `weaver-spec`;
- express an agent-specific assurance profile over an existing standard rather than inventing a new protocol;
- archive a standalone direction;
- keep a research corpus/reference implementation without productizing it.

The objective is not to preserve every repo as a growing product. The objective is to discover which ideas deserve continued investment and which should become smaller, simpler, or stop.