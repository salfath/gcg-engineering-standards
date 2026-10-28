# Release checklist

- [ ] Release owner and change window confirmed
- [ ] CI green, PR reviewed, changelog and artifact digest recorded
- [ ] Database compatibility/migration plan reviewed
- [ ] Backups verified and restore procedure known
- [ ] Production deployment lock held; migration step cannot be cancelled
- [ ] Target host only activates the artifact; no install or build on the target
- [ ] Exact digest deployed to staging and UAT approved
- [ ] Product-specific active session/transaction checks passed
- [ ] Production approval recorded
- [ ] Identical artifact promoted to production
- [ ] Smoke tests, logs and monitoring healthy
- [ ] Rollback target and incident contact ready
