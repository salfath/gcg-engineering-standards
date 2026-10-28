# Contributing

Propose changes through a tracked issue and PR. Explain the problem, affected
controls/products, compatibility and rollout. An originating request may be linked
in the PR until a tracked issue is assigned. Require independent human review by
an engineering owner. English identifiers; documentation may use Bahasa Indonesia
or English.

For policy changes, identify new/changed MUST rules, migration window, owners and
exception handling. Update CHANGELOG under Unreleased. Keep draft status until
Engineering Lead explicitly approves an exact version/commit and effective date.

Validate local links with `python3 scripts/check_handbook.py`. Parse changed YAML
and check placeholder commands fail when unconfigured. Do not run product deploys
or recovery drills merely to validate this handbook.

Separate observations, proposed actions and verified outcomes. Product evidence
must name its source/candidate, assessment date and limitations. Keep credentials,
personal data, sensitive topology and restricted evidence out of this public repo.
