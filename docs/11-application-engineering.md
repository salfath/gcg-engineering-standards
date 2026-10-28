# Application engineering

The product adapter translates these requirements into architecture decisions,
coding rules and checks appropriate to the runtime. Do not mandate microservices,
Kubernetes, a particular issue tracker or a universal file-size limit.

## Requirements and architecture

- Changes MUST link to acceptance criteria, affected users, failure behavior and
  applicable security/data-integrity invariants.
- Document module boundaries and data ownership. Keep domain rules in cohesive
  services; use ADRs for material tradeoffs, including alternatives and consequences.
- API changes MUST define versioning/compatibility, validation, authorization,
  error semantics and contract tests. Do not expose internal errors or secrets.
- Data-changing workflows MUST define transaction boundaries, concurrency control,
  idempotency/retry behavior and audit/side-effect ordering where applicable.
- Keep asynchronous side effects recoverable and deduplicated. Define timeouts,
  bounded retries and failure isolation for external dependencies.

## Maintainability and verification

Prefer small cohesive modules; numerical size/complexity budgets are product
rules, enforced by tooling where adopted. Do not split code merely to meet a
line count while obscuring transaction boundaries or domain behavior.

Adapters MUST select lint/format/static checks and a risk-based test strategy.
Use unit tests for domain rules, integration tests for database/transaction
behavior, contract tests for interfaces and browser/device tests for critical
user journeys. Include negative authorization, tenant separation, concurrency,
replay and dependency-failure scenarios where relevant.

Critical migrations, recovery and real-device compatibility require evidence
from representative environments. Unit mocks cannot certify those behaviors.
Apply targeted checks to low-impact changes and explain omitted test groups;
avoid tests that only mirror implementation structure.

## Usability and accessibility

Define supported screens, languages and accessibility acceptance criteria.
Web products SHOULD target WCAG 2.2 AA and document any exclusions. Test keyboard
navigation, visible focus, accessible control names, error feedback, contrast
and responsive layouts. Icon-only controls need an accessible name; a tooltip
alone must not be assumed sufficient.

Operational interfaces should prioritize rapid status scanning, consistent help,
clear pending/saved/error states and confirmation for consequential actions.
Product-specific calm UI rules supplement accessibility and task usability.

Reference: [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/).
