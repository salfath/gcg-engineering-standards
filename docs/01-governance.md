# Governance and policy levels

- **MUST**: mandatory unless Engineering Lead approves a documented time-limited exception.
- **SHOULD**: default recommendation; deviations need rationale in README or ADR.
- **MAY**: team choice.

Each repo MUST name its technical owner, at least one independent reviewer, a backup incident contact, runtime stack, environments, data classification, release procedure and incident contact. A single maintainer cannot satisfy the independent-review requirement on their own. Standards changes MUST use reviewed PRs. Product ADRs cannot silently override global MUST rules.

## Minimum Definition of Done
Issue linked in the tracker of record; acceptance criteria met; tests updated; security/privacy reviewed; documentation updated; CI green; independent review; release/rollback impact recorded where relevant. For production changes, retain the artifact digest and approval evidence.

## Ownership and exceptions
Any deviation from a MUST rule MUST be recorded in the exception register with an accountable owner, rationale, compensating control, approval, expiry date, and review date. Expired exceptions are violations, not defaults. Risk acceptance belongs to a named owner, not to an implicit team habit.

Prioritize safety and correctness over tool uniformity. Avoid unnecessary infrastructure complexity.
