# Testing and quality

Tests protect observable behavior and invariants. Select evidence by change risk,
not a universal coverage percentage. The adapter maps test groups to commands,
triggers and required statuses under [CI](04-ci.md).

## Behavior and integrity

- Behavior changes and bug fixes MUST add or update meaningful automated tests.
  Documentation-only work may use document validation with explicit rationale.
- Authorization, privacy, identity, money, critical sessions and migrations MUST
  include applicable negative/adversarial and failure-path scenarios.
- Critical writes MUST exercise constraints, transaction boundaries and concurrency
  against a real disposable database. Mocks alone do not prove those guarantees.
- Independently deployed interfaces SHOULD have contract/schema-drift checks.
- Prefer many fast unit tests, targeted integration tests and a bounded set of
  critical end-to-end journeys. Apply property/mutation testing where it adds value.

## Honest results

Adapters MUST state what is tested and what remains unverified. Publish test
reports and coverage where meaningful tool support exists, with scope/exclusions.
Coverage budgets are product decisions, not a replacement for behavioral review.
A passing average cannot excuse untested security or migration behavior.

Treat flaky tests as defects. Quarantine requires an owner, remediation issue,
expiry and compensating validation. Do not silently skip required tests or mask
failures with unlimited retries. Required gate semantics must reject missing,
failed or unexpectedly skipped evidence.

## Fixtures and non-functional checks

Use deterministic synthetic or verified anonymized fixtures. Destructive setup
MUST refuse targets without exact disposable-target validation and explicit opt-in;
operator confirmation alone does not make production a disposable test target.
Never include credentials, personal data or restricted production identifiers in
fixtures, screenshots or failure reports.

Web adapters SHOULD target WCAG 2.2 AA with automated checks and manual keyboard,
focus and assistive-technology evidence for critical journeys. Define performance
budgets and representative load tests for material scaling/release changes.
Device-specific guarantees require real-device evidence when applicable.

Retain sanitized results for the exact reviewed release, with access/retention
controls and links from PR/release records. A skipped group needs rationale;
a mock, source test or build cannot certify runtime/recovery/device behavior.
