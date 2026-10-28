# Testing and quality

Tests exist to protect behavior and invariants, not to maximize a coverage number. Riskier changes need stronger evidence.

## Required test layers

- **MUST** add or update automated tests for every behavior change and bug fix.
- **MUST** cover authorization, privacy, money, identity, exam, and migration paths with negative and adversarial tests, not only happy paths.
- **MUST** exercise database constraints and concurrency against a real disposable database for critical writes; mocks alone do not prove schema or transaction behavior.
- **SHOULD** keep a test pyramid: many fast unit tests, fewer integration tests, and a small set of critical end-to-end journeys.
- **SHOULD** use contract tests between independently deployed components and validate generated API specifications for drift.

## Coverage and quality signals

- **MUST** measure coverage in CI and publish the report.
- **SHOULD** enforce a changed-code coverage target (for example 70% line and branch) rather than a single repository-wide number. Do not merge untested security or migration code to satisfy an average.
- **MUST** treat a flaky test as a defect. Quarantine it with an owner and expiry date; do not hide it with unlimited retries.

## Test data

- **MUST** use synthetic or anonymized data. Never copy production dumps to laptops or CI without approved controls.
- **MUST** make fixtures deterministic and disposable. Seed scripts must refuse non-disposable targets unless an operator explicitly confirms intent.
- **MUST NOT** place real PII, credentials, tokens, or production identifiers in fixtures, screenshots, or test reports.

## Non-functional tests

- **SHOULD** run accessibility checks for public-facing interfaces against WCAG 2.1 AA and record manual keyboard and screen-reader evidence.
- **SHOULD** define performance budgets for critical journeys and run load tests before major releases or scale changes.
- **MAY** use mutation testing or property-based testing for high-risk pure logic.

## Evidence

- **MUST** retain test reports, coverage, and failure artifacts for the release under review.
- **SHOULD** link the relevant test evidence in the pull request and release manifest.
