# Database migrations and recovery

Migrations MUST be version-controlled, repeatable and tested on representative non-production data. Prefer expand → migrate → contract; preserve compatibility with the previous app version during a defined rollback window. Destructive migrations need separate releases and explicit review.

**Backup is not rollback.** Restoring a snapshot may discard subsequent writes. Critical products MUST specify RPO/RTO, encrypted off-host backup schedules, retention, restore drills and migration preflight. Protect clinical, financial, exam and identity data. Never run migrations concurrently from multiple replicas.
