# Product adoption and migration

**Phase 0:** inventory live server source, uncommitted changes, Git history, secrets, runtime, schema, integrations and backups. Reconcile live state with remote repo **before pulling or redeploying**.

**Phase 1:** reproducible local environment and smoke tests.
**Phase 2:** PR rules and CI.
**Phase 3:** immutable artifact build and staging promotion.
**Phase 4:** controlled production cutover and rollback drill.
**Phase 5:** disable direct source editing on servers; measure compliance.

Tentative pilot CBT, followed by Scola/Prima, then higher-risk Salus/Akor. Reassess order after repository audits. Track owners, blockers and evidence.

## Phase gates
Do not advance to the next phase while a gate is open. Each gate needs an accountable owner, evidence, and a date. Deviations require an exception register entry. Phase 5 is not complete until direct production source editing is technically blocked, not merely prohibited by policy.

## Compliance measures
Track at least: protected default branch, required CI checks, independent review, immutable artifact digest, restore-drill date, secret-scanning status, dependency-update SLA, and production approval evidence. Review these measures quarterly and publish the trend to engineering leadership.
