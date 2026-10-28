# Repository adoption checklist

Map evidence to the [control register](../docs/12-control-register.md).
Record PASS/GAP/EXCEPTION/NOT_APPLICABLE/NOT_ASSESSED, owner and next review.
Checklists do not constitute approval.

- [ ] Canonical source/build/release repositories and actual live source identified
- [ ] Named technical/review/deployment/incident owners and deputies recorded
- [ ] Server-only changes reconciled; secret exposure triaged without publishing secrets
- [ ] Approved handbook ref pinned and product adapter reviewed
- [ ] Data classification, trust boundaries and safety invariants recorded
- [ ] Restorable off-host encrypted backups and RPO/RTO targets defined
- [ ] Clean-machine setup, runtime/dependency locks and synthetic seed verified
- [ ] setup/dev/test/lint/check commands fail honestly and match CI
- [ ] Hosting capability supports protection, or expiring exception is approved
- [ ] Main/tag protections verified; missing review/failed CI blocks test PR merge
- [ ] Required aggregate CI and applicable test/security checks have execution evidence
- [ ] Immutable CI build, manifest and artifact digests recorded
- [ ] Staging UAT verifies exact candidate and supported client combinations
- [ ] Product-specific preflight and compatible application rollback drill passed
- [ ] Isolated whole-application restore and alert-routing drills evidenced
- [ ] Shared-host/tier identities, permissions and resource boundaries assessed
- [ ] Deployment audit and monitoring/incident ownership verified
- [ ] Direct runtime-source editing disabled
- [ ] Gaps, remediation issues, exception expiries and evidence refresh scheduled
