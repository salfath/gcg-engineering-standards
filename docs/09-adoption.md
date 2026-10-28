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

## Common adoption contract

All existing and future applications adopt the same approved control baseline.
Stack adapters implement controls; they do not replace them with weaker policy.
New repositories implement the applicable baseline before their first production
release. Existing repositories inventory gaps, assign owners and agree a dated
migration plan; unresolved mandatory controls require approved expiring exceptions.

For migration to `main`, reconcile server-only changes and divergent branches,
identify the accepted source, update PR targets/checks and deployment inputs,
validate in dev/staging, then retire old development/environment branches through
reviewed product changes. Do not rename/delete branches or redeploy applications
as a side effect of adopting this handbook. No automatic migration is authorized.

Product assessments, owners, exceptions, schedules and evidence stay in product
repositories or restricted stores. Select adoption order by risk/readiness rather
than product name. Review compliance on an approved cadence and after material
changes. No handbook change grants permission to deploy, restart or inspect
unrelated services. A policy merge does not establish product compliance.
