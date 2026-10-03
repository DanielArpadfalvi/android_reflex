# Global AI Business Models for a 2-Founder Team (dev + sales), 2025-2026

Source-quality note for the report writer: VC reports (Menlo, Bessemer, McKinsey, Sequoia, Gartner, Eurostat) and investigative journalism (TechCrunch) are high-quality. Agency pricing figures come mostly from vendor/marketing blogs (agency-course sellers, SEO content), which are useful for price ranges but unreliable for "case study" revenue numbers. These are flagged inline as [low-quality]. Several primary pages (menlovc.com, fortune.com, ec.europa.eu) were blocked from direct fetch, so their figures come from search snippets and press releases.

## 1. Which categories of AI businesses are small teams running profitably now?

### Takeaway
Money is flowing into AI *applications* and *bought* (not built) solutions, and VCs have converged on "sell the work, not the tool" (services-as-software / vertical agents). For a bootstrapped 2-person team, the realistic profitable entry points are: (a) an AI implementation/automation service with setup fee + retainer, specialized into one vertical, then (b) productizing repeated deliverables into a vertical SaaS or managed "AI-enabled service". Horizontal tools and thin wrappers are the failure zone.

### Cited Findings
**Market demand (high quality)**
- Enterprise GenAI spend went from $11.5B (2024) to $37B (2025). Applications took more than half ($19B). — [Menlo Ventures press release, Dec 2025](https://www.globenewswire.com/news-release/2025/12/09/3202258/0/en/menlo-ventures-2025-state-of-generative-ai-report-enterprise-investment-hit-37b-in-2025-tripling-in-one-year.html)
- 76% of enterprise AI solutions were *purchased* rather than built in 2025, up from 53% the year before. — [Menlo Ventures](https://www.globenewswire.com/news-release/2025/12/09/3202258/0/en/menlo-ventures-2025-state-of-generative-ai-report-enterprise-investment-hit-37b-in-2025-tripling-in-one-year.html)
- About 47% of AI pilots reach production, against about 25% for conventional enterprise software. Coding is the largest departmental category at about $4B. Healthcare is the largest vertical at $1.5B. — [Menlo Ventures report page](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/) (via search summary; direct fetch blocked)

**VC theses (high quality)**
- Sequoia's Julien Bek published "Services: The New Software" on 5 March 2026. Its claim is that "the next $1T company will be a software company masquerading as a services firm." For every $1 spent on software, $6 go to services. Selling the tool exposes a company to commoditization by model vendors, while selling the outcome does not. — [Fortune, Apr 2026](https://fortune.com/2026/04/21/services-are-the-new-software-sequoia-venture-capital-julien-bek-ai-native-eye-on-ai/); [summary gist](https://gist.github.com/ravidsrk/41b0c53dadda095352396365c46184ed)
- AI-enabled roll-ups (General Catalyst "AI-enabled roll-up" model):
  - Titan (an IT MSP roll-up) says its pilots automate 38% of typical MSP tasks.
  - Crescendo (an AI-native call center) runs 60-65% gross margins, about 4x the industry norm.
  - Current (Thrive Holdings' accounting platform) has bought about 50 local accounting firms and reports revenue above $300M.
  - General Catalyst has taken service businesses from 5-10% to 35-40% EBITDA margins, mostly through revenue growth on a fixed cost base.
  - Source: [Caritas Ventures AI roll-up market map](https://caritas.ventures/ai-rollup-market-map/) (secondary aggregator; figures attributed to the companies)
- YC: 67 of 144 (46%) Spring 2025 companies were AI agent companies. Batches moved from generalist assistants to vertical agents (claims handling, contract audit, bookkeeping reconciliation, back-office, CRM and system implementations). 19% of agentic companies targeted healthcare and financial services. Outcome-based pricing is emerging. — [PitchBook](https://pitchbook.com/news/articles/y-combinator-is-going-all-in-on-ai-agents-making-up-nearly-50-of-latest-batch); [CB Insights](https://www.cbinsights.com/research/y-combinator-spring25-agentic-ai); [Catalaize S25 profile](https://catalaize.substack.com/p/y-combinator-s25-batch-profile-and)

**Outcome-priced AI support at scale**
- Intercom Fin charges $0.99 per resolved conversation (the $49 base plan includes 50 outcomes). It is reportedly nearing $100M ARR, about half of Intercom's revenue. — [Enterprise DNA, Aug 2026](https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-08-02-intercom-s-fin-ai-agent-is-nearing-100m-arr-roughly-half-of/); [Gleap pricing breakdown](https://www.gleap.ai/blog/intercom-fin-ai-pricing-2026)

**Bootstrapped and indie examples (Indie Hackers etc.)**
- WP Umbrella: $110k MRR in 2025, +67% YoY, bootstrapped, team of 7. It is not AI-centric, but it is a useful benchmark for a "boring niche" SaaS. — [Indie Hackers](https://www.indiehackers.com/post/what-2025-taught-me-about-growing-a-bootstrapped-saas-to-110k-mrr-wp-umbrella-8cd8c4bc1d)
- Pieter Levels' Photo AI is reported at about $132K MRR as a solo founder. It is a consumer AI product built on a large existing audience, so it is not replicable without that audience. — [Medium compilation](https://medium.com/startup-insider-edge/the-100k-mrr-illusion-5-micro-saas-founders-proving-its-possible-and-how-they-did-it-c3571dd336b3) [secondary]
- Reality check: about 70% of micro-SaaS earn under $1k MRR, about 5% exceed $100k MRR, and the median profitable micro-SaaS sits around $4.2k MRR. — [Superframeworks](https://superframeworks.com/articles/best-micro-saas-ideas-solopreneurs) [low-quality, unverified methodology]

### Inferences
- The VC thesis ("own the outcome") and the bootstrapped reality ("start as a service") point the same way. A dev + sales duo can start as an AI-enabled service provider in one vertical. Each delivered project then becomes a reusable template. Within 12-24 months the most-repeated workflow is packaged as a productized managed service or vertical SaaS.
- The "buy, not build" shift (76%) favors SMEs paying an outside party to implement off-the-shelf tools rather than funding custom R&D. This matches a local integrator/implementer role.

### Gaps
- No verified revenue figures were found for EU/CEE AI automation agencies of 2-5 people. Most "case studies" are from course-selling or marketing blogs.
- Menlo's departmental breakdown (support, sales, IT, legal) could not be fetched directly.

## 2. Unit economics per model (pricing, margins, API costs, sales cycle, churn, time to revenue, automatable share)

### Takeaway
Service-led models (automation agency, RAG/knowledge base, voice agents for SMEs) can reach first revenue within weeks at 50-75% gross margin. They are labor-bound, though, and retainers churn unless they are tied to measurable outcomes. Raw LLM/API costs are a small share of price in B2B workflows, with voice as the exception. The main costs are human implementation, data cleaning and maintenance.

### Cited Findings
**AI automation agency (AAA) / workflow automation** [mostly low-quality sources; use as ranges only]
- Typical pricing is a $3-10K setup fee plus a $500-3K/month retainer. The retainer is often 15-25% of the setup fee per month. — [IdeaProof playbook](https://ideaproof.io/guides/ai-automation-agency)
- Retainers average $1,500-4,000/month for SMBs. Local service businesses (HVAC, dental, real estate) pay $1,500-2,500/month. — [Layer3Labs](https://www.layer3labs.io/roi/ai-automation-agency-cost); [Ciela](https://ciela.ai/blogs/how-much-money-can-you-make-ai-automation-agency)
- Early-stage agencies typically run 4-8 clients at $800-1,500/month retainers, for $3-10K/month in total. — [Ciela](https://ciela.ai/blogs/how-to-create-recurring-revenue-ai-automation-agency)
- Claimed case: a legal-tech agency sold real-estate law firms contract-review AI at $75K setup + $4.5K/month. Eight firms produced $672K in year 1 at 73% gross margin. — [ALM Corp blog](https://almcorp.com/blog/make-money-ai-digital-agencies-2026/) [unverified, treat with caution]

**Custom RAG / internal knowledge base / AI implementation (EU pricing)**
- A custom RAG chatbot costs €5-15K to build plus €200-500/month to run. Small-to-medium RAG projects run €8-28K. A "real" RAG build (hybrid retrieval, reranking, eval suite) runs €18-45K. Delivery takes 5-8 weeks. — [Ailog RAG pricing guide](https://app.ailog.fr/en/blog/guides/rag-pricing-guide-2026); [Nexaton](https://nexaton-solutions.com/blog/ai-implementation-cost)
- n8n/workflow agencies charge €5-20K per project, while boutique AI consultancies charge €20-100K. Fixed-price "AI operations audit" offers exist, for example €2,500. — [Vectimo](https://www.vectimo.ai/en/ai-consulting/best-ai-consulting-europe-sme)

**AI voice agents / receptionists**
- Retell AI: the platform starts at $0.07/min, and the all-in cost (LLM + TTS + telephony) is typically $0.11-0.20/min. — [Retell pricing](https://www.retellai.com/pricing); [Beri.net analysis](https://www.beri.net/article/voice-ai-per-minute-pricing-vapi-retell-elevenlabs-bland-cost-per-resolved-call)
- Vapi: the headline $0.05/min fee becomes $0.25-0.33/min all-in. — [Beri.net](https://www.beri.net/article/voice-ai-per-minute-pricing-vapi-retell-elevenlabs-bland-cost-per-resolved-call); [Ainora](https://ainora.lt/blog/ai-voice-agent-cost-per-minute-2026)
- Managed SMB receptionist products sell at $99-500/month for under 500 calls/month. Raw developer-platform cost at that volume is $50-150/month, and about $85-130/month at 1,000 min/month on Retell. — [Jahanzaib](https://www.jahanzaib.ai/blog/ai-voice-agent-pricing-breakdown); [Octavius](https://octavius.ai/voice-ai/ai-virtual-receptionist-cost/)
- Inference: at a €300-500/month price, gross margin is roughly 60-80% before setup and support labor. Margins thin for high-volume clients unless pricing is per minute or per call.

**AI customer-service chatbots**
- The benchmark is Intercom Fin at $0.99 per resolution. SME clients will compare any local offer against this. — [Gleap](https://www.gleap.ai/blog/intercom-fin-ai-pricing-2026)

**AI SDR / sales and lead-gen automation: high churn warning**
- TechCrunch reported that 11x claimed about $14M ARR, which was closer to about $3M once lapsed trials were removed. Employees said 70-80% of customers used 3-month break clauses to exit (11x disputed this and claimed 79% retention). The CEO stepped down in May 2025. — [TechCrunch](https://techcrunch.com/2025/03/24/a16z-and-benchmark-backed-11x-has-been-claiming-customers-it-doesnt-have); [Explorium](https://www.explorium.ai/blog/data-for-gtm/11x-ai-sdr-customer-loss-what-comes-next/)

**AI gross margins at scale (benchmarks)**
- Bessemer's fast-growing "Supernovas" run at about 25% gross margin and about $1.13M ARR/FTE. Steadier "Shooting Stars" run at about 60% gross margin and about $164K ARR/FTE, reaching about $3M ARR in year 1 under a Q2T3 growth path. — [Bessemer State of AI 2025](https://www.bvp.com/atlas/the-state-of-ai-2025)
- a16z's Sarah Wang argues that unusually *high* gross margins in an AI app can be an "orange flag" because they suggest low usage. — [Mostly Metrics](https://www.mostlymetrics.com/p/can-bad-gross-margins-ever-be-a-good-sign)
- AI-native call center (Crescendo) gross margin is 60-65%, against roughly 15% for traditional BPO. — [Caritas Ventures](https://caritas.ventures/ai-rollup-market-map/)

**AI training/consulting + EU AI Act compliance**
- Article 4 of the EU AI Act (AI literacy) has applied since 2 February 2025. Providers *and deployers* must ensure staff have sufficient AI literacy, proportionate to role and risk. This applies to almost every organisation using AI in the EU. — [Noerr](https://www.noerr.com/en/insights/article-4-of-the-ai-act-obligations-and-opportunities-for-companies-when-dealing-with-ai-literacy); [VAIA Flanders AI Academy](https://www.vaia.be/en/blog/ai-literacy-eu-ai-act-art-4)

### Inferences (summary matrix; synthesized from the above, not a single source)
| Model | Typical price (EU SME) | Gross margin | Time to first € | Sales cycle | Churn risk | Automatable vs. labor |
|---|---|---|---|---|---|---|
| Workflow automation agency (n8n/Make + LLM) | €3-20K setup + €500-3K/mo | 50-75% (labor-driven) | 2-6 weeks | 2-8 weeks for SMEs | High if retainer = "maintenance" only | Mostly human (scoping, integration) |
| Internal RAG / knowledge base | €5-45K + €200-500/mo ops | 50-70% | 1-2 months | 1-3 months | Medium; sticky once embedded | Build is human; runtime automated |
| Voice receptionist (on Retell/Vapi) | €100-500/mo + setup | 60-80% at low volume | Weeks | Short (owner-operator) | Medium-high | Mostly automated after setup |
| AI support chatbot | Per-resolution or €100-1K/mo | 60-80% | Weeks | Short-medium | Competes with Intercom/Zendesk native AI | Mostly automated |
| AI SDR / outbound | €1-5K/mo | Variable | Fast | Short | Very high (11x case) | Automated, but quality issues |
| AI training / AI Act literacy | Per-day workshop / per-seat | 70-90% | Immediate | Short | One-off (needs upsell) | Human |
| Vertical SaaS / productized service | Subscription or per-outcome | 60-80% at scale | 6-18 months | Varies | Low if workflow-embedded | Automated + human QA |

- LLM token cost is rarely the binding constraint in B2B text workflows. Voice is the exception, at $0.11-0.33/min.
- The binding constraints are human hours for integration, data cleanup and ongoing tuning.

### Gaps
- No reliable churn statistics were found for small AI agency retainers. The sources quoted are marketing claims.
- No verified IDP/document-processing or AI bookkeeping pricing for EU SMEs was collected in this pass.
- Sales-cycle numbers come from inference and practitioner blogs, not surveys.

## 3. Case studies: successes and failures

### Takeaway
Successes share three traits: a narrow vertical, ownership of a measurable outcome, and embedding in the workflow (Intercom Fin, the AI roll-ups, vertical YC agents). Failures share the opposite traits: horizontal content generation resold on a commodity model (Jasper), or inflated outcome claims with high churn (11x).

### Cited Findings
- **Jasper (failure of a horizontal wrapper).**
  - Peak revenue is reported around $120M (2023) falling to an estimated $55M (2024). This is contested: other sources put 2022 ARR at about $75M, and its 2023 forecast was cut by at least 30%.
  - Jasper went through several layoff rounds and CEO changes and cut its internal valuation.
  - Its core value was access to a model that ChatGPT then offered for $20/month.
  - Sources: [Maginative](https://www.maginative.com/article/jasper-cuts-internal-valuation-as-ai-growth-slows/); [Latka](https://getlatka.com/companies/jasper.ai); [GrowthHunt postmortem](https://www.growthhunt.ai/growth-story/jasper). Revenue figures conflict across sources and are unaudited.
- **11x (failure, inflated metrics/churn).** See Section 2. — [TechCrunch](https://techcrunch.com/2025/03/24/a16z-and-benchmark-backed-11x-has-been-claiming-customers-it-doesnt-have)
- **Intercom Fin (success, outcome pricing on top of an existing distribution base).** — [Enterprise DNA](https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-08-02-intercom-s-fin-ai-agent-is-nearing-100m-arr-roughly-half-of/)
- **AI-enabled roll-ups (success, but capital-intensive).** Current (accounting), Titan (MSP) and Crescendo (call center). — [Caritas Ventures](https://caritas.ventures/ai-rollup-market-map/)
- **4-person content agency.** Claimed to reach $890K revenue after using AI across content production in 2025. — [ALM Corp](https://almcorp.com/blog/make-money-ai-digital-agencies-2026/) [unverified]
- **Wrapper mortality claims.** Some sources claim "80% of AI wrapper startups projected to fail by end-2026" and "65% 90-day churn". — [Navokit](https://www.navokit.com/en/blog/decline-of-wrapper-startups); [ValueAddVC](https://valueaddvc.com/blog/how-to-build-a-startup-in-a-market-where-ai-will-eventually-do-what-you-do). FLAG: these sources cite CB Insights/Gartner without links. One also states a "Feb 2025 GPT-4 Turbo 90% price cut" that I could not verify and that appears inaccurate. Do not use these numbers as facts. Only the directional claim (horizontal wrappers get absorbed) is supported by the Jasper case.

### Inferences
- A roll-up of acquired firms is out of reach for a bootstrapped duo. A light version is reachable: partnering with or white-labeling for local accountants, MSPs and law firms, then splitting the efficiency gain.
- The Hungarian Kft could reproduce the "Fin-style" outcome pricing locally (per resolved ticket, per processed invoice, per booked appointment). This reduces the ROI-proof friction in SME sales.

### Gaps
- No public, verified revenue numbers were found for small EU/CEE AI agencies. Stripe-verified dashboards (e.g., TrustMRR) were not reached in this pass.

## 4. Commoditization risk vs. durable moats (next ~2 years)

### Takeaway
The models most at risk are generic: chat-with-your-docs, content generation, meeting notes, email drafting and generic SMB copilots. Microsoft, OpenAI and Google bundle these cheaply (Copilot Business at $18-21/user/month). Durable positions combine local language, integration into local systems (Hungarian accounting/ERP, NAV invoicing, local CRMs), regulated or compliance workflows, outcome pricing and personal relationships/distribution.

### Cited Findings
- Microsoft 365 Copilot Business for SMBs (up to 300 users, no minimum) is $21/user/month list, with an $18 promo through 30 Sep 2026. Bundles run $23.50 (Business Standard + Copilot) and $32 (Business Premium + Copilot). — [Microsoft Tech Community](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/introducing-microsoft-365-copilot-business-empowering-small-and-medium-businesse/4469700); [Pax8](https://www.pax8.com/blog/microsoft-365-copilot-business-smb-offers/)
- Sequoia: selling a tool means "every model improvement from Anthropic, OpenAI, or Google threatens to commoditize your product into a feature." Selling outcomes avoids this. — [Fortune](https://fortune.com/2026/04/21/services-are-the-new-software-sequoia-venture-capital-julien-bek-ai-native-eye-on-ai/)
- Moats cited by survivors: data flywheel, workflow integration, distribution, brand and network effects. — [ValueAddVC](https://valueaddvc.com/blog/how-to-build-a-startup-in-a-market-where-ai-will-eventually-do-what-you-do) [opinion]
- Margin-compression risk even for AI-native services: if AI cuts delivery cost from $70 to $30, competition may push a 70% gross-margin AI accounting firm toward 45%. — [Caritas Ventures](https://caritas.ventures/ai-rollup-market-map/)
- The Jasper collapse illustrates the "model-access-as-product" risk. — [GrowthHunt](https://www.growthhunt.ai/growth-story/jasper)

### Inferences (risk ranking for a CEE SME-focused duo)
- **High risk (2 years):**
  - Generic internal chatbots/RAG over M365/Google data, since Copilot and Gemini can read SharePoint/Drive natively.
  - Generic AI content production.
  - Meeting summarization and email assistants.
  - Horizontal AI SDR tools.
- **Medium risk:**
  - Customer-service chatbots, as helpdesk vendors (Intercom, Zendesk, Freshdesk) ship native agents.
  - Voice receptionists, where Hungarian-language quality is currently a differentiator that shrinks as TTS/STT improve.
- **Lower risk / durable:**
  - Workflow automation bound to local systems and regulations (NAV online invoicing, Hungarian payroll and accounting packages, local ERPs).
  - Vertical managed services that own an outcome (e.g., document intake for accountants, claims or quote processing).
  - EU AI Act compliance and AI literacy training, which is a regulatory driver plus a trust relationship.
  - Change management and implementation for companies that already bought Copilot, which is complementary to the vendors rather than competing with them.
- The sales founder's network acts as a "distribution" moat, which matters most in CEE markets that buy on trust.

### Gaps
- No source quantifies Hungarian-language LLM/voice quality gaps or how fast they are closing.

## 5. Evidence on enterprise/SME AI adoption ROI: where value is delivered vs. where it fails

### Takeaway
Adoption is broad but P&L impact is narrow. The MIT NANDA report finds about 95% of GenAI pilots show no measurable P&L impact. McKinsey finds only about 6% are "high performers" and about 39% see any EBIT impact. Gartner expects over 40% of agentic AI projects to be cancelled by 2027. Value comes from workflow redesign, deep integration, systems with memory and learning loops, and buying from specialized vendors. In CEE, Hungary's AI adoption is about half the EU average, which means both a large greenfield market and slower buyers.

### Cited Findings
- **MIT NANDA, "The GenAI Divide: State of AI in Business 2025" (July/Aug 2025).**
  - Method: 52 executive interviews, 153 leader surveys and 300 public deployments.
  - About 95% of pilots delivered no measurable P&L impact, despite $30-40B of enterprise investment.
  - Over 80% of organisations piloted ChatGPT/Copilot-type tools, but these mainly boost individual productivity.
  - Successful cases embed AI into high-value workflows with memory and learning.
  - Sources: [Virtualization Review](https://virtualizationreview.com/articles/2025/08/19/mit-report-finds-most-ai-business-investments-fail-reveals-genai-divide.aspx); [Forbes](https://www.forbes.com/sites/jasonsnyder/2025/08/26/mit-finds-95-of-genai-pilots-fail-because-companies-avoid-friction/)
  - Note: the methodology has been criticised (small sample, narrow P&L definition). — [Medium critique](https://medium.com/@ai_93276/the-mit-95-of-genai-pilots-fail-report-what-it-gets-wrong-and-what-leaders-should-do-instead-3a6a1bd7a3d5)
  - Widely reported but not verified in this pass: externally purchased solutions succeed about twice as often as internal builds. This is consistent with Menlo's 76%-buy finding.
- **Contradicting signal.** Menlo reports about 47% of AI pilots reach production (vs. about 25% for traditional software). "Production" is not the same as "P&L impact," so this does not fully contradict MIT. — [Menlo](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)
- **McKinsey State of AI 2025.**
  - About 6% are "high performers" (≥5% of EBIT attributable to AI plus significant value).
  - About 39% report any enterprise-level EBIT impact, mostly under 5%.
  - High performers are about 3x more likely to fundamentally redesign workflows and spend more than 20% of digital budgets on AI.
  - 23% are scaling agents in at least one function, led by IT, knowledge management and engineering.
  - Source: [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- **Gartner (June 2025).** Over 40% of agentic AI projects will be cancelled by end-2027 due to escalating costs, unclear business value and inadequate risk controls. Based on a poll of 3,400+ organisations. — [MarTech](https://martech.org/gartner-40-of-agentic-ai-projects-will-fail-making-humans-indispensable/); [Forbes, Jul 2026](https://www.forbes.com/sites/robertszczerba/2026/07/07/why-40-of-agentic-ai-projects-may-be-canceled-by-2027/)
- **Eurostat 2025.**
  - 20.0% of EU enterprises (10+ employees) used AI in 2025, up from 13.5% in 2024.
  - Hungary is about 10.4% overall and about 8.7% for small firms, among the lowest in the EU.
  - Sources: [Eurostat news Dec 2025](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20251211-2); [Eurostat Statistics Explained](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Use_of_artificial_intelligence_in_enterprises)
  - The Hungary figure comes from a search summary. Direct fetch was blocked, so verify it on the Eurostat page.

### Inferences
- For an SME-focused service firm, the evidence favours:
  - selling scoped, measurable workflow outcomes (hours saved, tickets resolved, invoices processed) instead of "AI strategy" or generic pilots;
  - integrating into existing systems instead of building standalone chat;
  - offering an ongoing tuning/learning-loop retainer, which is exactly the "memory and learning" gap MIT identified.
- Hungary's low adoption (about 10%) means many SMEs are first-time buyers. Education (AI Act Article 4 literacy training) can work as a low-friction door-opener that converts into implementation projects.

### Gaps
- No Hungarian- or CEE-specific SME AI ROI studies were found in this pass.
- BCG's 2025 "AI at Work" / "Widening AI value gap" figures were not collected.
