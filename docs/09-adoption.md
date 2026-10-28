# Product adoption and migration

Adoption is evidence-based. Record the exact handbook version/commit, product
adapter, owners, control applicability, gaps and approved exception expiry in an
[adoption record](../templates/project/standards-adoption.example.yml).

| Phase | Exit evidence |
|---|---|
| 0 — Inventory | Canonical/live source reconciled; runtime, secrets exposure, schema, integrations and backup state understood |
| 1 — Local | Clean-machine setup, locked dependencies, synthetic seed and documented checks pass |
| 2 — PR and CI | Protection configuration plus failing/passing PR exercise and independent review evidence |
| 3 — Immutable release | CI-built manifest, integrity verification and staging UAT for exact digests |
| 4 — Operations | Recovery/rollback/alert drills, measured outcomes, approved cutover and support roster |
| 5 — Sustain | Direct source editing disabled; evidence refresh, exception expiry and control review scheduled |

Before phase 0 reconciliation, do not pull/redeploy over unidentified server-only
changes. Inspect approved product scope only; co-hosted systems are not implicitly
authorized. Inventory evidence must be sanitized.

Track each applicable control as PASS, GAP, EXCEPTION or NOT_ASSESSED; use reviewed
NOT_APPLICABLE rationale. Proposed policies and desired infrastructure are not
evidence of implementation. Do not advance a dependent gate with unresolved gaps
unless a scoped, expiring exception is approved.

CBT is a proposed pilot, not assumed compliant; see the
[dated pilot assessment and acceptance plan](adoption/cbt-pilot.md).
Reassess the order of Scola/Prima and higher-risk Salus/Akor after their audits.
No handbook change grants permission to deploy, restart or inspect unrelated
services.
