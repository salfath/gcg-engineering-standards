# Database migrations and recovery

Migrations MUST be version-controlled, repeatable and tested on representative non-production data. Prefer expand → migrate → contract; preserve compatibility with the previous app version during a defined rollback window. Destructive migrations need separate releases and explicit review.

## Migration preflight
Before a production migration, MUST verify a recent restorable backup, run a schema diff/status check, confirm the application compatibility window, and acquire a deployment lock. Never run migrations concurrently from multiple replicas or deploy jobs. A failed migration MUST stop the release and require inspected, reviewed repair or a forward migration; do not mark it rolled back automatically.

## Backup and recovery
**Backup is not rollback.** Restoring a snapshot may discard subsequent writes. Critical products MUST specify RPO/RTO, encrypted off-host backup schedules, retention, restore drills and migration preflight. Protect clinical, financial, exam and identity data.

A restore drill MUST recover the database, private file/object storage, and encryption keys together, then verify application reads. Run drills at least quarterly for critical products and monthly for high-risk data, and retain the measured RPO/RTO evidence. If off-host backup is not yet available, record a time-limited exception with a compensating control.
