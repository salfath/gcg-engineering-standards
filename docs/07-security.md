# Security and privacy

MUST: never commit credentials; placeholders only in `.env.example`; use restricted production secret stores; least privilege; MFA for maintainers; secret/dependency scanning; HTTPS; audit logging for sensitive operations; vulnerability triage.

## Secure development baseline
MUST run secret scanning with push protection where available, dependency vulnerability scanning, and static application security testing on every PR. MUST maintain a `SECURITY.md` with a private disclosure route and a triage SLA. MUST produce a software bill of materials (SBOM) for distributed artifacts where tooling supports it.

Authentication, authorization, payments, clinical/exam data, privacy, and migrations MUST receive a threat model and domain-aware review. Security requirements belong in acceptance criteria, not only in a post-merge review.

## Data and logs
MUST classify data and apply handling rules from the data governance standard. MUST NOT log secrets, tokens, credentials, or unmasked PII. Redaction MUST be tested, including messages formatted from multiple fields.

## Credentials and supply chain
Untrusted PR workflows MUST NOT access production secrets. Rotate exposed credentials; history cleanup alone is insufficient. Use least-privilege deployment identities and avoid shared administrator SSH accounts. Sign or checksum distributable binaries where feasible. Document third-party keys and data flows. Maintain a dependency update SLA for security patches.
