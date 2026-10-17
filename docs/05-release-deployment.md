# Release and deployment

**Build once; promote the identical immutable artifact.** Default release tag: `vYYYY.MM.DD-N` (CalVer). Record full commit SHA, artifact digest, schema compatibility and notes. Protect tags. Docker-capable apps SHOULD publish digest-addressed images to GHCR; legacy apps MAY publish checksum-verified release bundles.

Environments: local; optional integration/dev; staging/UAT; production. Do not build or install dependencies on staging/prod during deploy. Use least-privilege deployment automation and environment-scoped secrets. Production needs approval, smoke tests and monitoring. CBT MUST avoid active exam windows; Salus/Akor require transaction/data-integrity checks.

Rollback MUST redeploy an earlier validated artifact, never automatically restore database. Recheck health and monitor. APK/desktop installers need separately versioned manifests and backend compatibility.
