# Release and deployment

**Build once; promote the identical immutable artifact.** Default release tag: `vYYYY.MM.DD-N` (CalVer). Record full commit SHA, artifact digest, schema compatibility and notes. Protect tags. Docker-capable apps SHOULD publish digest-addressed images to GHCR; legacy apps MAY publish checksum-verified release bundles.

## Immutable build and deployment
MUST build the artifact in CI, not on staging or production. Deployment MUST only download, verify, extract, and activate an artifact; it MUST NOT run package installation, compilation, or asset builds on the target host. Use an atomic release directory plus a `current` symlink, or an equivalent digest-addressed container rollout. Retain at least the previous known-good release for rollback.

MUST validate a release manifest in CI. The manifest records the tag, commit, artifact digest, schema revision, prior-version compatibility, approvals, and rollback target.

## Environments and approval
Environments: local; optional integration/dev; staging/UAT; production. Use least-privilege deployment automation and environment-scoped secrets. Production MUST require a recorded approval, smoke tests, and monitoring. Do not build or install dependencies on staging/prod during deploy.

## Database changes
Apply migrations as a separate, non-cancellable step with a verified backup and preflight. Deploy the application only after the schema is compatible with both the previous and new application versions. See [database migrations and recovery](06-database-recovery.md).

## Rollback
Rollback MUST redeploy an earlier validated artifact, never automatically restore the database. Recheck health and critical journeys, monitor, and record the deployment result. APK/desktop installers need separately versioned manifests and backend compatibility.

## Evidence
Retain the release manifest, artifact digest, approval, smoke-test result, deployment result, and rollback target. Measure lead time, deployment frequency, change failure rate, and recovery time.
