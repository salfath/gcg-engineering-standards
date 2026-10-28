# Database migrations and recovery

Migrations MUST be version-controlled, repeatable and tested on representative
non-production data. The migration tool owns schema changes; importing or
starting the app must not create/mutate schema.

Prefer expand → migrate → contract; define the rollback window and preserve
previous-app compatibility through it. Destructive changes need separate releases,
review and data preflight. Test clean installation and supported upgrade paths;
listing migration heads does not exercise migrations. Where downgrade is supported,
test upgrade → downgrade → upgrade only on disposable data, including collisions,
length limits and deterministic data folding.

A single controlled migrator MUST hold a deployment/database lock. Do not run
concurrent migrations from application replicas.

## Recovery

**Backup is not rollback.** Snapshot restore may discard subsequent writes.
Critical products MUST define RPO/RTO, encrypted off-host schedules, retention,
key recovery, backup-failure alerting and restore-drill cadence with named owners.

Drills MUST use isolated targets and restore database plus required objects/media,
verify content integrity, reconcile outbox side effects and deletion/hold policy,
then verify authenticated application readiness. Measure RPO from the restored
recovery point and RTO through safe application availability. Logical dump timing
alone does not establish PITR or whole-application recovery.

Record backup identity/chain, exact candidate, sanitized target, timestamps,
checks, measured outcomes, reviewer and residual risks. Targets remain targets
until evidence demonstrates them. Product runbooks define approved recovery
actions and preserve clinical, financial, exam and identity invariants.
