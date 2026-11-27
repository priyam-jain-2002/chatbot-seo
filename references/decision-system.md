# Decision system and durable project files

Keep project-specific records in the target project (not this public skill repository). Reuse existing conventions if present; otherwise use docs/discovery/.

- DECISIONS.md: index of decisions and supersession links.
- decisions/ADR-NNN.md: one meaningful tradeoff per record.
- BUSINESS.md: audiences, regions, offer, operating constraints, conversion goals and baseline.
- QUERY-MAP.md: query ID, audience, intent, locale, canonical URL, evidence fields, missing facts, next action.
- GATE-REPORT.md: gate, scope, status, severity, evidence, date, owner, remediation.
- EVALS.md: fixed query suite, search surface, model/version if available, locale, repeated runs and scoring rubric.
- CHANGELOG.md: deployed changes, evidence, experiment results and rollback.
- BACKLOG.md: ranked fixes, dependencies, effort, impact hypothesis and acceptance criteria.

## ADR template

ID / title:
Status: proposed | accepted | superseded | rejected
Date / owner:
Context and evidence:
Options (including do nothing):
Decision and rationale:
Business invariants and risks:
Affected routes / systems:
Acceptance tests and success metrics:
Rollback / review date:
Supersedes / links:

Never silently overwrite an accepted business rule. Raise a new ADR if evidence supports changing it. Separate observed facts, hypotheses, decisions and outcomes. Redact private customer data, credentials, commercially sensitive metrics and unpublished evidence before sharing.