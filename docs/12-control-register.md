# Verifiable control register

**Status:** Proposed controls; approval/adoption follows
[governance](01-governance.md). This register summarizes the normative chapters;
it does not replace their detail. Product owners map each control to applicable
commands, configuration and evidence in their adapter.

PASS requires current evidence for the assessed scope and exact candidate where
relevant. GAP means an unmet requirement. NOT_ASSESSED means evidence is missing.
EXCEPTION needs Engineering Lead approval and expiry. NOT_APPLICABLE requires
reviewed rationale. Neither a target nor a template is evidence of a PASS.

| Control | Minimum requirement | Verification / evidence | Accountable role |
|---|---|---|---|
| GCG-GOV-01 | Canonical repo, named owners, pinned approved policy and adapter | Reviewed ownership/adoption record and source identity | Product technical owner |
| GCG-GOV-02 | Governed deviations and exceptions | Risk, compensating control, approver, expiry, remediation issue | Engineering Lead |
| GCG-DEV-01 | Reproducible development | Clean-machine setup, runtime/dependency locks, synthetic seeds | Product technical owner |
| GCG-DEV-02 | Honest command interface | setup/dev/test/lint/check mapping, nonzero failures, local/CI parity | Product technical owner |
| GCG-SCM-01 | Protected integration branches/tags and independent review | Configuration evidence plus missing-review/failed-check merge-block exercise | Repository administrator |
| GCG-CI-01 | Mandatory PR quality gate | Required aggregate check; passing/failing runs on reviewed SHA | CI owner |
| GCG-CI-02 | Safe workflow execution | Audited SHA-pinned actions, least privilege, no production secrets in PR jobs | CI/security owner |
| GCG-ENG-01 | Requirements and domain integrity | Acceptance criteria, ADRs, API compatibility and transaction/retry tests as applicable | Product technical owner |
| GCG-ENG-02 | Maintainability and usable interfaces | Static/budget checks and critical journey/accessibility evidence as applicable | Product technical owner |
| GCG-SEC-01 | Security/privacy profile | Data/trust boundaries, threat assessment, authorization/tenant negative tests | Security/product owner |
| GCG-SEC-02 | Dependency/secret and vulnerability lifecycle | Scanner runs, severity/response policy, remediation or expiring exceptions | Security owner |
| GCG-REL-01 | Build once, identify immutable output | CI source SHA, locked inputs, manifest/artifact digests and build evidence | Release owner |
| GCG-REL-02 | Controlled identical-artifact promotion | Digest verification, exact-candidate UAT, approvals, product preflight, deploy history | Deployment owner |
| GCG-DB-01 | Safe versioned migrations | Disposable install/upgrade evidence, rollback compatibility window, migrator lock | Database/product owner |
| GCG-DR-01 | Recoverable data and application | Off-host encrypted backup, isolated restore/rollback drill, integrity checks, measured RPO/RTO | Operations owner |
| GCG-OPS-01 | Actionable observable operations | Readiness/integrity checks, injected alert routing, incident roster/runbook | Operations owner |
| GCG-OPS-02 | Shared-host isolation | Identity/permissions, network/storage/resource boundaries and residual assessment | Platform owner |
| GCG-AI-01 | Accountable AI-assisted work | Declared assistance, scoped access, meaningful validation, independent human review | PR owner/reviewer |

## Evidence lifecycle

Record assessment date, policy ref, product/source ref, environment or scope,
verifier, evidence reference, result and next review/expiry. Store sensitive
evidence behind access controls; a public adoption record can contain a sanitized
summary and opaque reference.

Refresh affected evidence after material changes to workflow configuration,
hosting capability, dependencies, topology or critical behavior. Engineering Lead
and product owners define review cadence and migration deadlines; no indefinite
unreviewed exceptions. Compliance claims must identify scope and unresolved gaps.

## External references

These inform control design; this handbook is not an external certification.

- [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final): secure development process.
- [OWASP ASVS](https://asvs.owasp.org/): versioned application verification requirements.
- [SLSA](https://slsa.dev/spec/v1.2/): build integrity and provenance.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): web accessibility.
