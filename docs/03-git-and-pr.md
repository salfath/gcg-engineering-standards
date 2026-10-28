# Git, branches and pull requests

Use trunk-based development: `main` is the only long-lived development branch.
Use short-lived `feat/ISSUE-short-name`, `fix/ISSUE-short-name`,
`hotfix/ISSUE-short-name`, `docs/...`, `chore/...`. Prefer branches under
three days. Split large work; use feature flags where necessary. No environment
branches.

PRs MUST pass required CI and have at least one independent human approval.
Protect main against direct/force pushes and deletion; protect release tags
against replacement/deletion. Document narrowly scoped emergency bypass actors
and require incident evidence for their use. Prefer squash merge and branch
deletion. Conventional Commits recommended.

## Verify enforcement

Check plan/visibility support for private repositories before claiming protection.
Record sanitized configuration evidence and a disposable PR exercise showing
that missing approval or a failed required check prevents merge. Configuration
text in a runbook is not evidence of enforcement.

If enforcement is unavailable, record GCG-SCM-01 as GAP or an approved expiring
exception, identify the compensating release control, and resolve the hosting
capability before claiming compliance. Do not publish private source merely to
obtain a hosting feature.

Hotfixes follow PR, CI, new release, staging verification and controlled
production deployment. Emergency exceptions require an incident record,
authorized scope and retrospective; product integrity constraints still apply.
