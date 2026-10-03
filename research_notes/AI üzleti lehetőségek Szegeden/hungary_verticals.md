# AI automation verticals in Hungary: opportunity assessment for a small Hungarian (Szeged-based) company, 2025-2026

Research date: 2026-10-03. About 20 search/fetch calls. Several primary sources (fairconto.hu) were blocked by the egress proxy, so some numbers come from search-engine snippets and are marked as such. Where no source supports a number it is listed under Gaps rather than guessed.

## Q1. Baseline: how ready are Hungarian firms for AI, and what does AI automation cost in Hungary?

### Takeaway
Hungarian SMEs adopt AI late (KSH/Eurostat put corporate AI use well below the EU average). So the gap is large, but customers need education and a lot of hand-holding. A local market for AI automation agencies already exists, with public price points: pilots cost about HUF 0.4-1.5M, and retainers about HUF 150-600k a month.

### Cited Findings
- KSH: only 7.4% of Hungarian enterprises use AI, against an EU average of 19.95%. Eurostat gives Hungary 3.7%. The two sources disagree, probably because of different definitions or years (search snippet summary) — [ResearchGate: MI vállalati használata Magyarországon](https://www.researchgate.net/publication/400080296_A_mesterseges_intelligencia_vallalati_hasznalata_Magyarorszagon_agazati_es_regionalis_bontasban); [MTAK paper](https://real.mtak.hu/217335/1/2025_03_203.pdf)
- KSH-NMHH (2024): only 5% of firms with 5-249 employees used AI in business decisions. Hungary's Digital Decade 2030 target is 24% AI use — [ictglobal.hu](https://ictglobal.hu/technologia/a-magyarok-tobbsege-mar-hasznal-ai-t-de-a-kkv-k-le-vannak-maradva/)
- A K&H survey (2026) reports a "record": 58% of the companies surveyed use some AI solution. This is a bank survey with a different sample and a broad definition, so it contradicts the KSH figure — [digitalhungary.hu](https://www.digitalhungary.hu/gazdasag/Rekordot-dontott-a-mesterseges-intelligencia-hasznalata-a-magyar-cegeknel-a-vallalatok-58-szazaleka-mar-alkalmaz-valamilyen-AI-megoldast-K-amp-H/32196); [prim.hu 2026-07](https://hirek.prim.hu/cikk/2026/07/13/egyre_tobb_ceg_epiti_be_mukodesebe_az_ai-t_rekordot_mutat_a_k_h_felmerese)
- KSH digital economy research (June 2026): the Hungarian economy is "split", with a large gap in digital maturity between firms — [hvg.hu](https://hvg.hu/tudomany/20260622_ksh-digitalis-gazdasag-kutatas-magyar-cegek-digitalizacio-fejlettseg)
- Agency price benchmarks (2026, agency blog): pilot chatbot HUF 400k-1.5M; RAG knowledge-base agent HUF 1.5-8M; ERP-integrated multi-agent system from HUF 5M; a focused AI pilot HUF 500k-1.2M; an MVP covering 1-2 use cases HUF 1.2-2.8M — [appforge.hu](https://appforge.hu/blog/ai-ugynok-chatbot-arak-2026/)
- A simple n8n workflow starts at HUF 50k, complex systems run HUF 200-500k. n8n Cloud Starter costs about HUF 9,500 a month. Self-hosted n8n is free plus about HUF 3k a month for a VPS — [socialpro.hu n8n guide](https://www.socialpro.hu/blog/n8n-magyar-utmutato-2026/); [susanatoth.com](https://susanatoth.com/workflow-automatizalas-kisvallalkozas-n8n-make-zapier/)
- Typical SME retainer is HUF 150-600k + VAT a month. A one-off audit or setup costs HUF 200-800k + VAT. Claimed payback is 3-9 months — [amarketingesed.hu](https://amarketingesed.hu/tudasbazis/ai-marketing-automatizacio-magyar-kkv-2026-teljes-utmutato/) (vendor content; payback claim not independently verified)
- A trained Hungarian website chatbot for a small business costs about HUF 24,900-80,000 a month. Self-service widgets start at HUF 1,900 a month — [apexweb.hu chatbot price comparison](https://apexweb.hu/tudasbazis/ai-chatbot-arak-osszehasonlitas-2026)

### Inferences
- With low adoption and high skepticism, a done-for-you or hybrid model (setup fee plus monthly retainer) fits better than pure self-serve SaaS for SMEs. The exception is narrow vertical tools that plug into software customers already use.
- The generic "AI automation agency" positioning is already crowded with many small players (socialpro, appforge, ai-smart, apexweb, northflow, and others). Differentiation has to come from a vertical focus.

### Gaps
- No official count of Hungarian AI automation agencies, and no data on their revenue.
- No KSH regional (Dél-Alföld) breakdown of AI adoption was retrieved. The ResearchGate paper reportedly has a regional breakdown, but it was not fetched.

## Q2. For each vertical: automatable workflows, market size, current tools and competitors, willingness to pay, barriers

### Takeaway
The strongest combination of countable customers, repetitive document work and reachable decision-makers is in accounting firms, private dental and medical clinics (phone and booking), társasház managers, and AI-literacy training. Legal is attractive but well defended by Wolters Kluwer (Jogtár Expert AI plus its Libra acquisition) and Clausis. Public tenders already have several AI monitoring startups. The local BYD supply chain creates a Szeged-specific opening in documentation and quality paperwork for manufacturing SMEs.

### Cited Findings

#### A. Accounting firms (könyvelőirodák)
- **Market size:** more than 55,000 registered accountants can be looked up in the registry. About 50,000 hold a valid registration and count as active because of mandatory CPD (continuing professional development). The registry was last updated 10 Sep 2026 — [PM register (penzugyiszakkepzes.kormany.hu)](https://penzugyiszakkepzes.kormany.hu/nevjegyzek-konyvviteli-szolgaltatast-vegzok); [Kredit.Futár](https://kreditpontoskepzeskonyveloknek.hu/toroltek-merlegkepes-konyvelok-nyilvantartasabol/)
- **Market segments (FairConto analysis, from search snippet only; page blocked; date unknown):** about two dozen large multinational-linked firms (about 3,000 staff, 4.8%), medium-sized offices (about 7,000, 11.1%), mini offices (about 10,000, 15.9%) and solo practitioners (about 20,000, 31.7%). The percentages do not add to 100%, so the remaining segments, probably in-house accountants, are missing from the snippet — [fairconto.hu](https://fairconto.hu/a-konyvelesi-piac-elemzese/)
- **Incumbent AI features:**
  - Kulcs Connect (Kulcs-Soft) does automatic invoice matching with AI and OCR. Every package includes 1,000 AI document-processing runs a year — [ks.hu](https://ks.hu/kulcs-connect/)
  - Billingo has a NAV incoming-invoice sync (Standard package and up), an accountant login, and an announced generative AI assistant for data queries — [billingo.hu/funkciok](https://www.billingo.hu/funkciok)
  - Szamlify has a built-in assistant in all packages — [quilly comparison](https://quilly.campmoney.hu/blog/szamlazoprogram-osszehasonlitas.html)
- **Specialist competitors:**
  - Zeuss is an accounting-office ERP with a smart document manager, payroll and bookkeeping — [zeuss.hu](https://zeuss.hu/funkciok/)
  - Adriana (via Mynds.ai at Boolanga) is an AI invoice-processing pipeline that exports to 35 Hungarian bookkeeping programs (RLB, Novitax, Kulcs-Soft) — [mynds.ai](https://mynds.ai/2025/10/15/konyvelesi-feladatok-automatizalasa-a-mesterseges-intelligencia-segitsegevel/)
- **Accuracy claim:** AI-assisted invoice OCR reaches about 95-98% extraction accuracy on good-quality documents. This is a vendor claim — [virtualworkforce.ai](https://virtualworkforce.ai/hu/szamla-ocr-pontos/)
- **Automatable workflows:**
  - receipt and invoice capture, with NAV Online Számla reconciliation of incoming invoices against bank statements
  - client document chasing by email and WhatsApp
  - a FAQ bot for clients
  - month-end checklists
  - payroll data intake

  Incumbent features plus independent tools already cover invoice capture — [szamlazoprogramom.hu](https://www.szamlazoprogramom.hu/blog/adatexport-konyvelo-programba-igy-automatizald-a-penzugyi-adminisztraciot-2026-ban)

#### B. Law firms and notaries
- **Market size:** about 12,500 practicing lawyers, about 6,000 trainee lawyers, about 500 employed lawyers, plus 2,500-3,000 former in-house counsel who joined the bar (search snippet summarizing Bar sources) — [bpugyvedikamara.hu](https://bpugyvedikamara.hu/kamarank/bemutatkozas/); [szakmaikamarak.hu](https://szakmaikamarak.hu/tagjaink/magyar-ugyvedi-kamara/)
- **Bar regulation:** the Hungarian Bar (MÜK) has published positions on AI use, including one on Hungarian AI speech-to-text transcription services for lawyers. Its focus is competence and controlled use — [MÜK szakmai álláspontok](https://www.xn--mk-xka.hu/szakmai-iranymutatasok); [jogaszvilag.hu](https://jogaszvilag.hu/napi/a-mesterseges-intelligencia-alkalmazasa-az-ugyvedi-tevekenysegben-muk-tajekoztatas/)
- **Law change:** the Üttv. (Act on Attorneys) amendment widens the supplementary activities lawyers may carry out and explicitly opens room for legaltech — [jogaszvilag.hu](https://jogaszvilag.hu/a-jovo-jogasza/valtozik-az-uttv-marciustol-bovulnek-az-ugyvedi-tevekenyseg-gyakorlasa-kereteben-kiegeszito-jelleggel-folytathato-tevekenysegi-korok-jon-a-legaltech/)
- **Competitors:**
  - Wolters Kluwer sells Jogtár Expert AI as an add-on to Jogtár subscriptions. The AI price is not public; the Adó Jogtár base package is HUF 145,990 + VAT — [wolterskluwer.com Jogtár Expert AI](https://www.wolterskluwer.com/hu-hu/news/jogtar-expert-ai-mesterseges-intelligencia-jog); [shop](https://shop.wolterskluwer.hu/termek-reszletek/ado/ado-1/ado-jogtarr.p280/YSO0956.v6866)
  - Wolters Kluwer acquired the legal AI assistant Libra and offers it in Hungary as an agentic legal work environment — [jogaszvilag.hu](https://jogaszvilag.hu/a-jovo-jogasza/a-wolters-kluwer-felvasarolja-a-jogi-ai-asszisztens-szoftver-szolgaltatot-a-libra-t/)
  - Praetor AI adds contract analysis and anonymisation to the Praetor case-management system — [wolterskluwer.com](https://www.wolterskluwer.com/hu-hu/expert-insights/ugyvedi-munka-mesterseges-intelligenciaval-praetor-ai)
  - Clausis is a Hungarian AI-native legal OS covering Hungarian-law research, drafting and firm knowledge base — [clausis.ai](https://clausis.ai/)
  - Legito supports the Hungarian language for contract work — [aiinfok.hu](https://aiinfok.hu/ai-a-jogi-szektorban-a-legjobb-eszkozok-szerzodesek-elemzesere/)
- **Adoption lag:** an expert interview says Hungary is about 1-2 years behind early Western European adopters in law-firm AI — [jogaszvilag.hu legaltech 2026](https://jogaszvilag.hu/a-jovo-jogasza/mit-hoz-a-legaltech-2026-ban-interju-megyeri-andreaval-eder-roberttel-es-kramli-gergellyel/)

#### C. Private healthcare and dental clinics
- **Market size proxy:** FoglaljOrvost.hu lists more than 2,400 private doctors in more than 130 specialties. A town like Baja has 19 private dentists on Medgo — [foglaljorvost.hu](https://foglaljorvost.hu/); [medgo.hu](https://medgo.hu/list/maganfogorvos/baja)
- **Vendor claims (treat as unreliable):** VoiceFleet's blog cites the "Magyar Fogorvosok Egyesülete" as saying more than 50% of clinics lose patients daily to missed calls, plus a testimonial claiming +38% bookings. Both are marketing content, and the statistic could not be verified at the cited association — [voicefleet.ai](https://voicefleet.ai/blog/ai-recepcios-fogorvosi-rendelo-magyarorszag-2026)
- **Hungarian voice receptionist competitors:** AI Squad, SmartHívás, Apex Web (from HUF 39,900 a month, live in 5-10 days), AI-Smart, NorthFlow, Botcenter, and Comnica AI:gent (a call-center voicebot) — [aisquad.hu](https://aisquad.hu/); [smarthivas.hu](https://www.smarthivas.hu/); [apexweb.hu/ai-recepcios](https://apexweb.hu/ai-recepcios); [comnica.hu](https://comnica.hu/comnica-aigent/); [northflowpartner.com](https://www.northflowpartner.com/ai-telefonos-asszisztens)

#### D. Real estate and társasház management
- **Agencies:** more than 3,000 real-estate agencies and more than 8,000 agents. About 1,500 small agencies (6 agents or fewer) in Budapest and about 800 elsewhere. The VG source is older and its date was not checked, so verify it — [vg.hu](https://vg.hu/vallalatok/negy-lakast-ad-el-egy-atlagos-magyar-ingatlankozvetito-572301); [ingatlanangyal.hu](https://ingatlanangyal.hu/ingatlanos/)
- **Platform overlap:** ingatlan.com already offers AI ad translation and is rolling out AI listing-text generation. This commoditizes the "AI ad copy" use case — [tudastar.ingatlan.com](https://tudastar.ingatlan.com/hirek/igy-fejleszt-ai-megoldasokat-az-ingatlan-com-szabo-petert-kerdeztuk/)
- **Társasház software:** an established market already adding AI.
  - eHÁZ says almost 13,000 condominiums use its software — [ehaz.hu](https://www.ehaz.hu/)
  - Thaz-SofT covers more than 100,000 units and includes an AI assistant — [tarsashazaink.hu](https://tarsashazaink.hu/)
  - TSH Manager offers AI-generated reports for more than 20,000 units — [kkmegoldasok.hu](https://kkmegoldasok.hu/)

#### E. Manufacturing and automotive supply chain (Szeged specific)
- **BYD Szeged:** BYD has business relationships with 192 Hungary-based companies, 24 of them official suppliers (Sept 2026). The plant start slipped from end-2025 to mid or late 2026 — [telex.hu](https://telex.hu/gazdasag/2026/09/10/byd-beszallito-lanc-hozzaadott-ertek-magyar-vallalkozas); [vg.hu](https://www.vg.hu/vilaggazdasag-magyar-gazdasag/2026/09/byd-szegedi-gyar-csuszas-kovetkezmeny-elektromos-auto)
- **First supplier:** QP Zrt. (Győr) was the first announced Hungarian supplier. BYD inspected its production over video cameras — [szegedma.hu](https://szegedma.hu/szeged/2026/01/szegedi-byd-gyar-magyar-beszallito-kivalasztas); [vg.hu](https://www.vg.hu/vilaggazdasag-magyar-gazdasag/2026/01/byd-qp-gyor-autoipar)

#### F. Logistics and transport
- No current count of licensed Hungarian road-haulage firms was found. MKFE (the Hungarian road hauliers' association) and the authority describe the licensing process — [mkfe.hu](https://www.mkfe.hu/hu/mkfe-tudasbazis/letolto-dokumentumok/eu-licenc.html); [itrack.hu](https://www.itrack.hu/fuvarozoi-engedely/)

#### G. Agriculture (KAP / egységes kérelem)
- **2025 applications:** about 155,000 single (unified) applications. As of 2 June 2026, 133,275 had been submitted for 2026, 71% of them (94,366) through chamber (NAK) village advisers (falugazdász). This figure comes from a search snippet — [NAK](https://www.nak.hu/sajto/sajtokozlemenyek/108722-mar-csak-negy-hetig-nyujthatok-be-az-egyseges-kerelmek); [Államkincstár](https://www.allamkincstar.gov.hu/hirek/az-agrartamogatasokra-junius-10-ig-nyujthato-be-a-2025.-evi-egyseges-kerelem)
- **Filing window:** applications run through a state system, with a 7 April-10 June 2025 window — [kap.gov.hu](https://kap.gov.hu/news/2025-04-07/095303/indul-2025.-evi-egyseges-kerelmek-benyujtasa)

#### H. Tourism and hospitality
- **2025 volume:** a record year, with 46.8M guest nights (+4.3%) and 19.5M guests — [kormany.hu](https://kormany.hu/kormanyzat/nemzetgazdasagi-miniszterium/hirek-nemzetgazdasagi-miniszterium/2025-ben-ujabb-rekordevet-zart-a-hazai-turizmus-kozel-20-millio-vendeg-mintegy-47-millio-vendegejszakat-toltott-a-magyarorszagi-szallashelyeken)
- **Private accommodation:** "private and other" accommodation has 266,870 bed spaces — [index.hu](https://index.hu/gazdasag/2025/02/21/ngm-turizmus-szallashelyek-magan--es-egyeb-szallashely-szallashely-minosites-make-fmke-bkik-mtu-vendeglatas/)

#### I. Public tenders (közbeszerzés)
- **Existing AI tools:**
  - Tender Értesítő: monitoring plus a "Tender AI" chat with tender documents — [tender-ertesito.hu](https://www.tender-ertesito.hu/)
  - TenderMonitor — [kozbeszerzesmonitor.hu](https://kozbeszerzesmonitor.hu/)
  - TenderAI: monitoring combined with OPTEN data — [tenderai.hu](https://tenderai.hu/)
  - KözbeszGuru GPT: bid prep, deficiency remedy (hiánypótlás) and legal remedy advice — [kozbeszguru.hu](https://www.kozbeszguru.hu/kozbeszguru-gpt)
  - Napitender — [napitender.hu](https://napitender.hu/magyar-kozbeszerzes-figyelo/)
- **Practitioner warning:** a practitioner blog argues that AI misses the essential judgment in procurement — [kozbeszguru.hu blog](https://www.kozbeszguru.hu/blog/kozbeszguru-2/az-ai-majd-tudja-a-kozbeszerzesben-epp-a-lenyeg-hianyzik-belole-722)

#### J. HR and guest workers (vendégmunkás)
- **Quota:** capped at 35,000 permits in 2025, and again 35,000 for 2026 — [kormany.hu](https://kormany.hu/hirek/a-magyar-munkahelyek-a-magyaroke-a-nemzetgazdasagi-miniszter-2026-ra-is-35-ezer-foben-hatarozza-meg-a-vendegmunkas-kvotat); [index.hu](https://index.hu/gazdasag/2025/12/03/nemzetgazdasagi-miniszterium-vendegmunkas/)
- **Headcount:** about 106,000 foreign workers in 2025 (up from 67,000 in 2020). Rules tightened from 1 Jan 2025 — [economx.hu](https://www.economx.hu/magyar-gazdasag/2026/06/05/vendegmunkasok-kulfoldi-munkavallalok-magyarorszag-adatok/); [tozsdeforum.hu](https://tozsdeforum.hu/gazdasag/drasztikus-szigoritas-vendegmunkas-kvota-magyarorszagon/)

#### K. Call centers and voice agents
- See section C for competitors. Comnica has 20 years of call-center experience and sells the AI:gent voicebot — [comnica.hu](https://comnica.hu/comnica-aigent/)

#### L. E-commerce
- **Market:** 2,100bn HUF gross e-commerce market in 2025. PwC tracks about 38,000 webshops; another figure says about 45,500 webshops (+19% year on year). More than 120M orders and 4.3M online shoppers. Temu is the largest online seller — [PwC Digitális Kereskedelmi Körkép 2025](https://www.pwc.com/hu/hu/sajtoszoba/2025/digitalis_kereskedelmi_korkep_2025.html); [PwC e-toplista 2025](https://www.pwc.com/hu/hu/kiadvanyok/assets/pdf/e-toplista_2025.pdf)

#### M. AI literacy training (EU AI Act Article 4)
- **Requirement:** Article 4 has applied since 2 Feb 2025. It has no direct fines, but companies must be able to document their efforts — [madarassy-legal.com](https://www.madarassy-legal.com/eu-ai-act-szabalyozas-2026-amit-most-kell-tudnia-cegeknek-es-maganszemelyeknek/); [MKIK](https://vallalkozzdigitalisan.mkik.hu/hirek/hir?id=1027)
- **PwC HU e-learning prices:** €120/person for 15 employees or fewer; €2,500 up to 50; €4,500 up to 200; €5,000 up to 500; €7,500 up to 1,000; €10,000 above 1,000 — [pwc.com/hu](https://www.pwc.com/hu/hu/szolgaltatasok/technologiai_tanacsadas/mi_jartassag_elearning.html)
- **Other prices:** live workshops by an independent trainer start at HUF 175,000 — [rolandgyarmathy.hu](https://rolandgyarmathy.hu/ai-kepzes/). t-method also sells MI-jártasság (AI literacy) training — [t-method.hu](https://t-method.hu/mi-jartassag/)

### Inferences
- **Accounting**
  - About 50k registered accountants and roughly 20k solo or micro-office practitioners make this the largest countable professional vertical.
  - Invoice OCR alone is commoditizing because Kulcs-Soft, Billingo and Zeuss bundle it.
  - The open space is the "glue" around the bookkeeping program: client document chasing, NAV-versus-bank reconciliation exceptions, client Q&A, and onboarding. It should be sold to mini offices (3-15 staff) as a hybrid of setup plus monthly fee.
- **Dental/private clinics**
  - Strong pain point (phone handling, multilingual dental tourists).
  - The low-end Hungarian voice receptionist market is crowded (at least 6 players, entry price about HUF 40k a month).
  - To win, a small firm needs deep integration with the booking or practice-management systems clinics actually use, or local presence (Szeged has a university dental faculty and private clinics).
  - EESZT (national e-health records system) integration is a regulatory barrier; not researched here.
- **Legal**
  - The buyer is about 12.5k lawyers, but the research and drafting layer is held by Wolters Kluwer (Jogtár data moat plus Libra) and Clausis.
  - A small firm should avoid competing on legal research and instead offer done-for-you implementation (document templates, intake, transcription, privacy-safe deployment) for small offices.
- **Real estate agencies**
  - ingatlan.com's built-in AI copy weakens the listing-text use case.
  - Lead response and qualification (call/chat) is the residual opportunity.
  - The társasház segment already has software incumbents adding AI, so selling as an integration partner to them may beat competing.
- **Szeged/BYD**
  - 192 Hungarian firms in BYD's orbit, plus local suppliers that must meet Chinese OEM documentation and quality demands (PPAP, 8D reports, bilingual HU/EN/CN documents).
  - This makes for a local niche in AI-assisted quality and tender documentation and translation.
  - This is an inference: no source quantified demand for it.
- **Agriculture**
  - About 155k applicants a year, but 71% file through NAK village advisers.
  - The real customer is therefore advisers, consultancies and larger farms, not individual farmers.
  - Seasonal, state-controlled systems make SaaS hard; a service model fits better.
- **Public tenders**
  - Monitoring is already covered by at least 5 Hungarian tools, some with AI chat.
  - Bid preparation with AI remains thin and liability-heavy.
  - It is a moderate opportunity only as a done-for-you bid-writing service bundled with an existing consultant.
- **AI literacy training**
  - Price anchors are clear (PwC €2.5-10k per company; independent trainers from HUF 175k per workshop) and so is the legal hook.
  - It works best as a lead-generation front-end for selling automation projects, the "train, then automate" funnel.

### Gaps
- The number of private dental and medical clinics in Hungary (KSH/NNGYK figures) was not retrieved.
- No current count of licensed haulage firms.
- No count of Hungarian condominiums (társasházak), and no count of licensed közös képviselők (condominium managers).
- Csongrád-Csanád county breakdowns for KAP applicants, clinics and accountants were not found.
- Pricing for Jogtár Expert AI and Clausis is not public.
- The FairConto accounting segmentation could not be verified because the page was blocked.
- Willingness-to-pay surveys per vertical were not found. Budgets above come from vendor price lists only.
- Hungarian startup-database coverage (Hiventures portfolio, Startup Hungary) was not checked due to the call budget.

## Q3. Ranking: attractiveness for a small Szeged-based AI company, and the best delivery model

### Takeaway
On available evidence, the ranking is below. Pure horizontal "AI agency" and pure voice-receptionist SaaS are the most crowded. Vertical depth plus integrations, sold as hybrid (setup plus monthly fee), is the defensible path.

| Rank | Vertical | Evidence on market size | Competition | Suggested model |
|---|---|---|---|---|
| 1 | Accounting firms (client document chasing, NAV/bank reconciliation exceptions, client Q&A) | about 50k registered accountants; about 20k solo practitioners (snippet) | Incumbents bundle OCR; few cover workflow glue | Hybrid: setup HUF 200-800k plus monthly fee |
| 2 | AI literacy training plus follow-on automation | Every AI-using company under Article 4 | PwC, independent trainers | Service (workshops) used as a funnel |
| 3 | Szeged manufacturing/BYD supplier documentation (quality docs, bilingual documents, RFQ/quotes) | 192 firms linked to BYD; 24 suppliers | Few specialized players found | Done-for-you projects (pilot HUF 0.5-1.2M) |
| 4 | Private dental/medical clinics (phone, booking, multilingual) | more than 2,400 private doctors on one platform | Crowded: 6+ Hungarian voice vendors from about HUF 40k a month | Hybrid with practice-system integration |
| 5 | Law firms (intake, templates, transcription, implementation) | about 12.5k lawyers | Wolters Kluwer Jogtár AI/Libra, Clausis, Praetor, Legito | Done-for-you implementation, not research SaaS |
| 6 | Real estate/társasház (lead response, owner communication) | more than 3,000 agencies; eHÁZ at about 13k condominiums | ingatlan.com native AI; társasház software adding AI | Partner or integration |
| 7 | Public tenders (bid prep) | Not quantified | 5+ monitoring tools with AI | Service with a procurement consultant |
| 8 | E-commerce (product text, support) | about 38-45k webshops; HUF 2,100bn market | Many generic tools; Temu pressure on margins | Low-ticket SaaS; weak fit |
| 9 | Agriculture/KAP | about 155k applicants (71% via NAK advisers) | State and NAK advisers dominate | Sell to advisers; seasonal |
| 10 | Tourism (guest messaging) | 46.8M guest nights; 266,870 private bed spaces | Channel managers and global tools (not researched) | Low priority |
| — | HR/guest workers, logistics | Guest-worker quota 35k; no haulage count | Not researched in depth | Insufficient evidence |

### Cited Findings
- Price anchors for the models above: [appforge.hu](https://appforge.hu/blog/ai-ugynok-chatbot-arak-2026/); [amarketingesed.hu](https://amarketingesed.hu/tudasbazis/ai-marketing-automatizacio-magyar-kkv-2026-teljes-utmutato/); [apexweb.hu](https://apexweb.hu/ai-recepcios); [PwC MI-jártasság](https://www.pwc.com/hu/hu/szolgaltatasok/technologiai_tanacsadas/mi_jartassag_elearning.html)
- Market-size numbers: see the per-vertical citations in Q2.

### Inferences
- The ranking is a judgment call based on countable customers, documented competition and repetitiveness of the work. It is not based on measured willingness to pay.
- **SaaS versus service:** Hungarian SMEs have low AI maturity (KSH 5-7%), so done-for-you or hybrid wins early revenue. Productize repeatable pieces into a vertical SaaS after 10-20 customers in one vertical (for example, an accounting-office client-portal agent integrated with RLB/Novitax/Kulcs).
- **Barriers:**
  - GDPR and professional secrecy (lawyers, health data).
  - EESZT and health-data rules.
  - Dependence on incumbent software APIs (bookkeeping programs, NAV Online Számla API).
  - Hungarian voice quality and latency.
  - Incumbents bundling AI for free.

### Gaps
- No customer interviews or survey data validating willingness to pay per vertical.
- No data on churn or ARPU (average revenue per user) for Hungarian AI receptionist vendors.
