# Implementation playbooks

## Headless commerce
Treat the commerce backend as the authoritative catalog and operational source. Keep stable product/category routes, canonical URLs, crawlable navigation, accurate product/offer data, identifiers, images, availability, shipping and return policies. Reconcile price and inventory across storefront, backend and enabled channels. Verify feed acceptance separately from storefront SEO. Test server rendering or prerendering, dynamic data freshness, redirect migrations and checkout handoff. Do not assume headless is automatically better for SEO.

For B2B, distinguish distributor, supplier, manufacturer and reseller accurately. Map procurement questions to product specs, pack sizes, MOQ/minimum order, quote paths, service areas, delivery terms and certifications where verified. A minimum checkout may be intentional: preserve it and optimize clarity and suitable basket building rather than removing it to improve raw conversion. Avoid unsupported delivery or availability promises; offer a quote/contact path where appropriate.

## Service business
Map buyer problem, industry, location and service to real capabilities, evidence and a clear inquiry path. Publish distinct regional pages only when the service and content genuinely differ or meet specific local needs. Track qualified inquiries and downstream acceptance rather than form submissions alone.

## Portfolio and expertise
Map nonbrand role/skill/problem queries to case studies with context, contribution, technical architecture, tradeoffs and evidence-backed impact. Protect employer/client confidentiality. Keep public project/article routes independently indexable with dynamic sitemap updates when needed; an index.txt or llms.txt file is optional supplementary material, not a substitute for HTML, links or sitemap.

## Answerability
For each target query enumerate necessary facts, authoritative source, public URL, freshness requirement and unsupported claims. Example: 'Can a supplier deliver 500 certified items to my facility tomorrow?' requires quantity, specification, current availability, destination, delivery cutoff and certification evidence. If unavailable, explicitly say confirmation is required and route to a quote. Never invent an answer to satisfy a query.

## Platform guidance
Use official crawler, indexing, structured-data and merchant documentation current at execution time. Search-enabled assistants vary by mode and query. Do not treat platform-specific preferences or keyword-density scores as established ranking factors. FAQ/HowTo markup does not guarantee rich results; schema must match visible content and current eligibility. Do not confuse geographic SEO with generative engine optimization.