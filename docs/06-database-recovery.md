# Database migrations and recovery

Migrations MUST be version-controlled, repeatable and tested on representative
non-production data. Schema changes MUST run through the adapter-defined
controlled migration or module-upgrade procedure. Routine application imports, requests and replica
startup MUST NOT perform uncontrolled schema mutation. A framework-managed upgrade
may initialize its registry inside the single locked migration process.

Prefer expand → migrate → contract; define the rollback window and preserve
previous-app compatibility through it. Destructive changes need separate releases,
review and data preflight. Test clean installation and supported upgrade paths;
listing migration heads does not exercise migrations. Where downgrade is supported,
test upgrade → downgrade → upgrade only on disposable data, including collisions,
length limits and deterministic data folding.

Before production migration, verify a recent restorable backup, inspect migration
status/schema impact and confirm compatibility and the repair plan. A failed
migration stops the release for inspected, reviewed repair or a forward fix; it
is not automatically treated as rolled back. Destructive or incompatible changes
need an explicit maintenance/recovery plan and independent approval.

A single controlled migrator MUST hold a deployment/database lock. Do not run
concurrent migrations from application replicas.

## Recovery

**Backup is not rollback.** Snapshot restore may discard subsequent writes.
Critical products MUST define RPO/RTO, encrypted off-host schedules, retention,
key recovery, backup-failure alerting and restore-drill cadence with named owners.
The risk profile MUST set a maximum drill interval, rationale and review trigger;
material storage, key or migration changes require affected recovery revalidation.

Drills MUST use isolated targets and restore database plus required objects/media,
verify content integrity, reconcile outbox side effects and deletion/hold policy,
then verify authenticated application readiness. Measure RPO from the restored
recovery point and RTO through safe application availability. Logical dump timing
alone does not establish PITR or whole-application recovery.

Record backup identity/chain, exact candidate, sanitized target, timestamps,
checks, measured outcomes, reviewer and residual risks. Targets remain targets
until evidence demonstrates them. Product runbooks define approved recovery
actions and preserve clinical, financial, exam and identity invariants.
