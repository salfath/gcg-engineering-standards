# Product adoption and migration

**Phase 0:** inventory live server source, uncommitted changes, Git history, secrets, runtime, schema, integrations and backups. Reconcile live state with remote repo **before pulling or redeploying**.

**Phase 1:** reproducible local environment and smoke tests.
**Phase 2:** PR rules and CI.
**Phase 3:** immutable artifact build and staging promotion.
**Phase 4:** controlled production cutover and rollback drill.
**Phase 5:** disable direct source editing on servers; measure compliance.

Tentative pilot CBT, followed by Scola/Prima, then higher-risk Salus/Akor. Reassess order after repository audits. Track owners, blockers and evidence.
