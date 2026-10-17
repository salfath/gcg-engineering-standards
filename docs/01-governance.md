# Governance and policy levels

- **MUST**: mandatory unless Engineering Lead approves a documented time-limited exception.
- **SHOULD**: default recommendation; deviations need rationale in README or ADR.
- **MAY**: team choice.

Each repo MUST name its technical owner, reviewer, runtime stack, environments, data classification, release procedure and incident contact. Standards changes MUST use reviewed PRs. Product ADRs cannot silently override global MUST rules.

## Minimum Definition of Done
Jira issue linked; acceptance criteria met; tests updated; security/privacy reviewed; documentation updated; CI green; independent review; release/rollback impact recorded where relevant.

Prioritize safety and correctness over tool uniformity. Avoid unnecessary infrastructure complexity.
