# Product engineering adapter — REPLACE_PRODUCT

**Status:** UNCONFIGURED; not an adoption approval.
Owner/deputy/contact: REPLACE_WITH_MAINTAINED_REFERENCES.
Canonical source/build/release repositories: REPLACE.
Adopted approved handbook version/full commit: REPLACE.
Supported runtimes/platforms and data classification: REPLACE.
Risk profile, required test/drill intervals and rationale: REPLACE.
Repository/workspace owners, `main` protections and migration plan: REPLACE.

## Architecture and safety

Record module/data ownership, trust boundaries, critical invariants, API
compatibility and ADR links. Define product-specific size/complexity budgets.
For critical workflows, document transaction, retry/idempotency, audit ordering
and negative authorization/concurrency verification.

## Commands and test groups

| Interface | Exact command | Test groups / environment / limitations |
|---|---|---|
| setup | REPLACE | Locked dependencies, synthetic seeds, disposable local services |
| dev | REPLACE | App/dependency startup and endpoints |
| test | REPLACE | Enumerate unit/integration/contract/ops/browser/device groups |
| lint | REPLACE | Formatting/static/budget checks |
| check | REPLACE | Shared PR gate implementation; document CI-only checks |

Record destructive-test target guards. Distinguish mocks, real integration tests,
browser tests and real-device certification. Define accessibility acceptance.

## CI and repository enforcement

List exact required check names, event/path selection, aggregate semantics,
supported runtimes, scanner policies, action pinning and evidence retention.
Link merge-block exercises for failed checks and missing approvals.
Record hosting limitations as gaps/exceptions rather than claimed enforcement.

## Release, database and clients

Specify dev → staging/UAT → production promotion from reviewed `main`,
CI artifact generation/storage/digests and locked dependency/platform inputs,
per-component source/build identities, migration revision/compatibility window
and single-migrator lock. Link manifest
schema, product preflight, atomic activation, UAT/approval and smoke checks.
Record client/backend combinations and signed/download artifact identities.
Rollback selects validated artifacts compatible with the current schema;
data recovery is a separate approved incident action.

## Security and operations

Link data classification/flows, threat model, applicable versioned ASVS controls,
session/revocation/tenant policies, vulnerability severity and deadlines, privacy
inventory/purpose/vendor/retention/hold/deletion, secret rotation and restricted
evidence storage.
Record environment identities/permissions/resource limits and residual risks.

Specify backup schedule/retention/encryption/key recovery, isolated restore
procedure, RPO/RTO targets and measured drill evidence. Record liveness/readiness,
integrity alerts, alert injection, owners/deputies and incident escalation.

## Adoption and evidence

Map every control in the [register](../../docs/12-control-register.md) to
PASS/GAP/EXCEPTION/NOT_APPLICABLE/NOT_ASSESSED with owner, evidence, assessment
date, expiry/next review and remediation issue.
An unconfigured or unassessed row is not a pass.
