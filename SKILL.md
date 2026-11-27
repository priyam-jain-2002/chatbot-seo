---
name: chatbot-seo
description: Audit, design, implement and evaluate SEO, GEO (generative engine optimization), AEO, AI discoverability, geographic search and conversion-aware website architecture. Use for indexing, headless migrations, ecommerce feeds, service pages, portfolios, answerability, search visibility and AI citation audits.
---

# SEO / GEO engineering

Optimize for qualified discovery, reliable retrieval, accurate answers, trust, useful action and measured outcomes. Do not promise ranking, citation or revenue. Geographic SEO and generative engine optimization are distinct but can overlap.

## Operating workflow

1. Inspect existing project instructions, decisions, deployment, analytics and business constraints. Identify audience, geography, offer, conversion action and success metric. Record missing evidence rather than guessing.
2. Establish baseline and map representative branded and nonbranded queries to actual public URLs, required facts and authoritative sources. Identify gaps in discovery versus answerability.
3. Apply [release gates](references/gates.md). Classify PASS/FAIL/UNKNOWN/N/A; prioritize critical blockers and commercial impact, not arbitrary aggregate scores.
4. Record consequential choices using [decision system](references/decision-system.md). Preserve accepted constraints. Compare alternatives and do nothing; state assumptions, rollback and acceptance tests.
5. Implement smallest useful changes using [playbooks](references/playbooks.md). Read only applicable sections. Respect authorization; do not publish private information, fabricate claims, or silently change pricing or checkout rules.
6. Verify in deployed environment with [evaluation protocol](references/evaluation.md). Distinguish implementation, deployment, crawling, indexing, citation and conversion as separate evidence states.
7. Report baseline, changes, gate results, unresolved blockers, evidence, next actions and review date. Maintain project files for later agents and regression checks.

## Core rules

- Start with business intent, not keyword volume. Prioritize qualified buyers and meaningful conversion.
- Canonical HTML pages, crawlable links, correct HTTP responses, metadata, sitemap and robots are foundational. Compare raw HTML with rendered output; do not mistake a text index for actual indexed pages.
- Make each priority question answerable with explicit verified facts, source, scope, date and uncertainty. A discoverable page can still be unanswerable.
- Build trustworthy entity and product/service signals. Use schema matching visible truth, not schema for its own sake. Avoid unsupported certifications, reviews and statistics.
- Create genuinely useful pages for distinct intent; no doorway pages or mass-generated filler.
- Make the next action work and measure it. Respect business constraints and unit economics.
- Treat platform-specific ranking preferences as hypotheses unless supported by current official evidence. Verify current platform guidance before changing crawler policies or schema.
- Never expose private data to improve AI retrieval. Respect crawler access policy and confidentiality.

## Progressive disclosure

- [Gates](references/gates.md): mandatory audit and release criteria.
- [Decision system](references/decision-system.md): durable project files and ADR template.
- [Evaluation](references/evaluation.md): reproducible search, AI and conversion tests.
- [Playbooks](references/playbooks.md): commerce, services, portfolios and answerability.

## Legacy tools

Existing scripts and references are retained for compatibility, not mandatory execution. Inspect code and dependencies before running, especially automatic installations or network calls. Content scores, keyword density and citation-trigger suggestions are diagnostics, not verified ranking signals or release gates. Schema generator output requires validation against visible content and current eligibility.

- scripts/audit_content.py
- scripts/extract_queries.py
- scripts/schema_generator.py
- references/query_patterns.md
- references/citation_triggers.md
- references/platform_preferences.md

Legacy platform guidance is non-normative; the gates, verified current documentation and accepted project decisions take precedence.
