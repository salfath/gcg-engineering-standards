# Security and privacy

MUST: never commit credentials; placeholders only in `.env.example`; restricted
production secret stores; least privilege; maintainer MFA; dependency/secret
scanning; HTTPS; sensitive-operation audit logging and vulnerability triage.

## Product security profile

Each adapter MUST classify data and document trust boundaries, external data
flows, threat model, authorization/tenant boundaries, session and credential
revocation, encryption/key ownership, audit redaction and retention/deletion.
Critical workflow changes require domain-aware threat assessment and independent
review, including negative tests proving unauthorized operations leave no effects.

Select applicable [OWASP ASVS](https://asvs.owasp.org/) controls with versioned IDs
and documented exclusions; evaluate mobile-specific verification for mobile
clients. Map process requirements to [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final)
where useful. A mapping is not a certification.

## Vulnerability and data lifecycle

Maintain a `SECURITY.md` or clearly linked private disclosure route with a severity
model, accountable owner and triage/remediation deadlines. Define exception expiry
and verification of fixes. Escalate active exploitation and
exposed credentials immediately under the incident process. Scanning is not a
substitute for authentication/authorization design review.

Untrusted PR workflows MUST NOT access production secrets. Rotate exposed
credentials; history cleanup alone is insufficient. Production data in development
requires explicit approval, minimization and verified anonymization.

Document retention, holds and deletion propagation through objects, exports and
backups. Restrict diagnostic evidence access. Record third-party keys/data flows
and vendor access. Sign/checksum distributed binaries where supported and verify
integrity before use.

Run static application security testing for supported languages and generate an
SBOM for distributed artifacts where tooling supports it. Unsupported coverage
requires reviewed rationale and compensating validation in the adapter; it is
not an implicit pass. Automate dependency update proposals with risk-based patch
deadlines. Enable secret push protection where supported and repository scanning
on PRs and pushes; an exposed credential must be rotated even after removal.
Generated dependency updates still require review and CI.

Data inventory, purpose, retention, vendor and privacy-review requirements are
specified in [data governance](14-data-governance.md).
