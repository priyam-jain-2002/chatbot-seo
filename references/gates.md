# SEO / GEO release gates

Apply per representative URL/template and priority query cohort. Record PASS, FAIL, UNKNOWN or N/A with reason, evidence URL/artifact, timestamp, owner and next action. UNKNOWN is not PASS. Block affected releases on critical failures; do not average away blockers.

| Gate | Pass criteria | Evidence |
|---|---|---|
| G0 Business alignment | Audience, geography, intent, conversion, serviceability and unit economics defined; constraints protected | Approved decision file; funnel baseline |
| G1 Discovery | Canonical public URL is linked via crawlable navigation, valid sitemap where eligible, correct robots and indexing directives; no unintended soft 404 or duplicate | HTTP checks, raw HTML, sitemap fetch, webmaster inspection |
| G2 Retrieval | Intended public content is available to relevant crawlers in initial HTML or reliably rendered output; no login, WAF, JS or routing obstruction | Raw vs rendered comparison, crawler logs where available; status and content type |
| G3 Answerability | Priority questions map to canonical URLs and explicit, accurate facts with source, scope, freshness and missing-data handling | Query-to-evidence matrix; extract answers without inventing facts |
| G4 Trust | Entity identity, contacts, authorship where appropriate, evidence, policies and product/service claims are verifiable; structured data agrees with visible content | Source checks, schema validation, human review |
| G5 Intent and quality | Each page serves distinct demand and offers substantive value; no doorway pages, keyword stuffing, fabricated reviews or mass-generated near duplicates | Query/page mapping, duplicate review, competitor and first-party demand evidence |
| G6 Actionability | Relevant next step works end-to-end on mobile and desktop; price, minimums, service area, eligibility and delivery conditions clear; analytics capture outcome | Test checkout/quote/contact, error states, event receipts; preserve approved restrictions |
| G7 Distribution | Applicable feeds and listings use consistent identifiers, URLs, pricing, inventory and policies; diagnostics checked at destination | Feed validation plus merchant/platform acceptance and actual listing status |
| G8 Measurement | Baseline, target, window, cohort, instrumentation and attribution limitations recorded; repeatable search/AI evaluation exists | Search console, analytics, CRM/order data, prompt suite |
| G9 Release integrity | Representative routes and dynamic publishing verified in production; migration redirects, canonical host, cache invalidation and rollback tested | Before/after crawl, deployment checks, new-content publish test |

Critical blockers: unintended noindex/robots denial, broken canonical routes, false claims, exposure of private data, broken conversion path, violation of business constraints. Scope noncritical failures explicitly with owners and deadlines. Do not claim live indexing, citation or sales without corresponding evidence.