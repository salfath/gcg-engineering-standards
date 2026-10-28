# Git, branches and pull requests

## One development trunk

Each repository MUST use `main` as its only long-lived development branch.
Use short-lived `feat/ISSUE-short-name`, `fix/ISSUE-short-name`,
`hotfix/ISSUE-short-name`, `docs/...` or `chore/...` branches for reviewed PRs to
`main`. Feature branches remain allowed: one trunk does not mean editing directly
on `main`. Prefer small changes integrated within a few days; numerical size/age
budgets belong in the adapter. Use feature flags or branch by abstraction for
unfinished work, with owners and removal plans.

Dev, staging and production are deployment environments, not source branches.
Build once from reviewed `main`; promote the same artifact digests. `main` may
advance while production remains on an earlier accepted release. Do not create
long-lived `develop`, `staging` or `production` development branches. Existing
repositories migrate through the [adoption process](09-adoption.md); an interim
deviation requires an approved expiring exception.

## Repository boundaries and traceability

A monorepo or separate component repositories are allowed. Document owners,
workspace setup, compatible component revisions and release boundaries in the
adapter. Repository shape does not weaken independent review or CI. Use a
tracker of record; PRs and branch naming must trace to the issue/accepted request.
Jira, GitHub Issues or another approved tracker may supply that reference.

## Review and merge

PRs MUST pass required CI and have at least one independent human approval.
Protect `main` against direct/force pushes and deletion; require owned-path review
through CODEOWNERS or an equivalent enforced reviewer mechanism. Dismiss stale
approvals after material updates and resolve blocking review threads before merge.
A sole author cannot provide their own independent approval. Sensitive changes
need domain-aware review. Prefer squash merge and branch deletion; Conventional
Commits are recommended. Protect release tags against replacement/deletion.

Check results and approval must apply to the candidate being merged. Use a merge
queue or update/revalidate when concurrent changes could invalidate the evidence.
Document narrowly scoped emergency bypass actors; their use requires incident
scope, evidence and retrospective, never routine `[skip ci]` or direct pushes.

## Verify enforcement

Check hosting-plan/visibility support before claiming protection. Record sanitized
configuration evidence and a disposable PR exercise showing that missing approval
or a failed required check prevents merge. Configuration text is not enforcement.

If enforcement is unavailable, record GCG-SCM-01 as GAP or an approved expiring
exception with compensating release controls. Resolve the capability before
claiming full compliance; do not publish private source merely to gain a feature.

Hotfixes use a PR to `main`, CI, a new immutable release, staging verification and
controlled promotion. Urgency does not implicitly bypass product integrity rules.

Reference: [Trunk-based development](https://trunkbaseddevelopment.com/).
