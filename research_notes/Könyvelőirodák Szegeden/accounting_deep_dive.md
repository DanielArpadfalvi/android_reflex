# AI automation for Hungarian accounting firms (könyvelőirodák): deep dive, October 2026

Research date: 2026-10-03. Scope: goes deeper than `reports/AI üzleti lehetőségek Szegeden.md` and `research_notes/AI üzleti lehetőségek Szegeden/hungary_verticals.md`, and does not repeat them.

**Method and source-quality warning.** The egress proxy blocked direct page fetches for almost every Hungarian domain: 5percado.hu, vamprogram.hu, ks.hu, zeuss.hu, and in curl tests also ado.hu, adozona.hu, mkoe.hu, nav.gov.hu, penzugyiszakkepzes.kormany.hu, profession.hu and rsm.hu. Non-HU benchmark sites such as getuku.com were blocked too. The session's web-search budget also ran out partway through.

As a result, **almost every Hungarian finding below comes from search-engine result summaries (snippets), not from reading the full page.** The URL given is the page the snippet came from. Numbers should be spot-checked before they go into a sales deck. Where the snippet did not make clear which page a number came from, this is marked "attribution uncertain".

---

## 1. How a typical small Hungarian accounting firm works: fees, staff, aging, consolidation

### Takeaway
A typical small firm charges about 25-50k HUF/month for a Kft and 12-18k HUF for a KATA or sole-trader client. Payroll is billed extra. A median mérlegképes (chartered) accountant costs about 550k HUF gross per month, or roughly 620k HUF with employer contributions. The profession is old (average age about 51-52) and shrinking: fewer people are training, and roughly a third of accountants plan to leave. Firm sales happen, with earn-out structures, but no Hungarian roll-up player or deal statistics were found. No source quantified the monthly time split between tasks.

### Cited Findings

**Fees (könyvelési díjak), 2026**
- Kft fees are typically 30,000-70,000+ HUF/month. Budapest averages 35-55k for a Kft, the countryside 28-45k, so Budapest runs 15-20% higher. The cheapest offers (simple KATA) start at about 11,500 HUF/month. A complex international Kft can exceed 150k HUF/month — [qjob.hu 2026](https://qjob.hu/blog/articles/konyveles-arak); [dulubi.hu 2026](https://dulubi.hu/blog/konyvelo-arak-2026/) (snippets, attribution between the two uncertain).
- The net base fee for a Bt./Kft. is 25-50k HUF/month, depending on revenue and number of items (tételszám) — [joszaki.hu Kft könyvelés árak 2026](https://joszaki.hu/arak/kft-konyveles) (snippet).
- Bookkeepie has about 400 firms' current prices in its database. Minimum base fees: about 18k HUF/month for a sole trader, about 12k for KATA, about 35k for a Bt., about 40k for a Kft, all before surcharges — [bookkeepie.com könyvelési árak 2026](https://www.bookkeepie.com/hu/blog/konyveles-arak) (snippet).
- **Acounto** is a digital, automation-heavy accounting provider. Its prices: Egyéni 9,990 + VAT, Start 34,990 + VAT, Extra 84,990 + VAT (for more than 1,000 invoices a year). It claims more than 1,500 clients nationwide — [acounto.com/arak-csomagok](https://acounto.com/arak-csomagok/) (snippet). This is the low-price anchor that traditional firms compete against.
- No 2026 source on per-employee payroll (bérszámfejtés) fees was retrieved before the search budget ran out; see Gaps.

**Staff costs and shortage**
- Profession.hu Bériránytű (salary guide) for mérlegképes könyvelő: the average expected salary is 570,471 HUF gross, the median 550,000 HUF, and 80% fall in a 350-720k band. Pest county is about 585k and Budapest about 542k — [profession.hu/fizetesek/merlegkepes-konyvelo](https://www.profession.hu/fizetesek/merlegkepes-konyvelo) (snippet).
- A "good" accountant costs 600-800k HUF gross even outside Budapest, and an experienced mérlegképes in Budapest about 1M HUF — [felnottkepzes.hu / zeuss.hu 2026](https://zeuss.hu/2026/02/17/mennyibe-kerul-egy-jo-konyvelo-2026-ben/) (snippet, attribution uncertain between these two).
- In 2022 Pénzcentrum described accounting as a "hiányszakma" (shortage occupation) — [penzcentrum.hu 2022](https://www.penzcentrum.hu/karrier/20221013/hianyszakmava-valt-a-korabbi-sztarmunka-igy-kereshetsz-joval-az-atlag-folott-1129881) (older).
- HR Portál (June 2025): it is hard for SMEs to find a good accountant — [hrportal.hu 2025-06-13](https://www.hrportal.hu/hr/ezert-nehez-a-kkv-nak-jo-konyvelot-talalni-20250613.html) (headline only).

**Aging of the profession**
- The average accountant in Hungary is 51 years old, and more than half are 50 or older. Fewer new accountants are qualifying than are retiring. Enrolment in accountant training fell from 2,654 to 1,492 over five years. Nearly a third of accountants plan to leave the profession in the short term, and a quarter of those give age as the reason — search summary drawn from [haszon.hu](https://haszon.hu/megkeresni/konyveles/konyvelok-munkaerohiany), [trendfm.hu](https://trendfm.hu/cimlap/egyre-tobb-a-munka-de-utanpotlas-nincs-mi-lesz-igy-a-konyvelokkel-15615), [pallas70.hu](https://pallas70.hu/karrier-hir/2163) (attribution uncertain, dates not visible).
- PENTA UNIÓ surveyed nearly 8,000 registered accountants between 2013 and 2018 (**old data**):
  - Over the period, the 41-50 age group grew by 6 points to 36%, and the 51-60 and 61-65 groups each grew by 2 points to 27%.
  - The 31-40 group fell by 14 points to 19%. The 20-30 group stayed flat at 3%.
  - At retirement age, nearly half of accountants stop working.
  - About 14% (about 7,000 accountants) were expected to leave through retirement.

  Source: [5percado.hu](https://5percado.hu/nyugdijba-mennek-a-konyvelok-de-hol-az-utanpotlas/) (snippet).
- "MKOE 2025 research" (as relayed by the KAVOSZ article):
  - more than 1,700 businesses employing more than 7,000 accountants, "many over 70";
  - average age 52;
  - only 30% of accounting businesses are digitalised;
  - some clients still bring invoices in person.

  Source: [kavosz.hu MI a könyvelésben](https://www.kavosz.hu/az-en-vallalkozasom/mi-a-konyvelesben/) (snippet). **Caution:** 7,000 accountants in 1,700 businesses is far below the ~50k registered accountants, so this is probably a sample or member base, not the market. Verify with MKOE.
- In January 2024 the accountant training requirements were tightened — [piacesprofit.hu](https://piacesprofit.hu/cikkek/gazdasag/szigorodik-a-konyvelo-kepzes.html); [eduline.hu 2024-01-02](https://eduline.hu/felnottkepzes/20240102_Januartol_szigorodnak_a_konyvelo_kepzes_feltetelei).

**Consolidation**
- Zeuss's guide to selling a firm (Nov 2025):
  - Due diligence covers 3 years of financials, client contracts, authority cases, GDPR, an anonymised client matrix and liability insurance.
  - Payment is typically 60-80% at closing and 20-40% as earn-out or escrow over 12-24 months.
  - Handover runs 1-2 cycles in parallel, with a transition services agreement (TSA) and a scheduled transfer of NAV authorisations (meghatalmazások).

  Source: [zeuss.hu/2025/11/03/konyveloirodat-eladni-es-venni](https://zeuss.hu/2025/11/03/konyveloirodat-eladni-es-venni-igy-erdemes-csinalni/) (snippet). This shows a practice market exists, but no deal volumes were found.
- An old (2010) GVH/HÉTFA study of the accountant–client relationship reported, per the search summary:
  - 78% of accountants had trouble when a new client brought records late or incomplete;
  - on average 18.5% of clients owe fees.

  Source: [GVH/HÉTFA 2010 PDF](https://www.gvh.hu/pfile/file?path=%2Fgvh%2Fversenykultura_fejlesztes%2Ftamogatott_programok%2Ftamogatott_programok%2F70_2010_HETFA_Tanulmany_konyvelo_fin.pdf&inline=true) (**2010, old; snippet attribution uncertain**). Still one of the few structured Hungarian studies.

### Inferences
- **Loaded staff cost:**
  - A 550k gross salary plus 13% social contribution tax (szocho) is about 620k HUF/month.
  - At roughly 140 productive hours a month, that is about **4,400 HUF per productive hour** (own calculation).
  - So every 10 hours/month saved is worth about 44k HUF/month of capacity.
  - The more relevant value is "one more client per accountant" (about 30-45k HUF/month revenue each), because the binding constraint is the shortage of accountants, not the wage bill.
- **Fee anchors:**
  - A 200-client mini-office with an average fee of about 30-35k HUF has gross revenue of about 6-7M HUF/month.
  - A tool or service at 50-150k HUF/month is about 1-2.5% of revenue. That is plausible if it frees capacity for 2-5 extra clients.
- **Succession pressure:** with an average age of about 51-52 and owners near retirement, firms will be selling. A "digitised, transferable practice" (clean client files, PMT/AML documentation, documented processes) has sale-value appeal. This is a second pitch angle beyond time saving.
- **Monthly cycle**, from general knowledge of Hungarian deadlines (verify in interviews):
  - The 12th of the following month: payroll returns (08-as bevallás), tax and contribution payments.
  - The 20th: VAT for monthly filers.
  - In between: collecting documents, matching bank statements, posting.
  - So the crunch runs from about the 5th to the 20th.
  - The cited sources did not confirm this calendar, so treat it as an interview hypothesis.

### Gaps
- No Hungarian time-use study showing how a small firm's hours split between document collection, bank matching, VAT, payroll, NAV correspondence and client questions. **This is the top interview question.**
- No count of accounting firms (as opposed to registered persons) by size band. FairConto's segmentation remains unverified (see earlier notes).
- No 2025-2026 figure on clients per accountant, and no payroll fee per head.
- No Csongrád-Csanád-specific salary or fee data.

---

## 2. Accounting software landscape, interfaces and AI features (2025-2026)

### Takeaway
No public market-share data exists, and searches confirmed this. The installed-base "big names" are RLB-60, Novitax (NTAX/TAXA/WINTAX), Kulcs-Könyvelés, Tensoft, Infotéka and Forint-Soft. Integration with them is mostly **file-based** (DBF, CSV and XML imports), not REST APIs. Cloud "office platforms" are moving into exactly the "glue" space: Zeuss/iBookr.ai, Számlázz.hu's Számlaverzum/SMARTBooks, and Billingo. The most important finding is that **cheap SaaS tools for document chasing and NAV-based missing-document detection already exist**: ÜgyfélSegéd costs from about 100 HUF per client per month, and Zeuss's office ERP from 35k HUF/month. The NAV Online Számla API and the new eÁFA M2M 2.0 API are public and free.

### Cited Findings

**Market share**
- No statistically based market-share survey was found online. The landscape: Kulcs-Soft is a long-established, widely used player; Novitax is one of the best-known families; RLB is a "well-proven name" with a classic logic used for years. Installed systems (RLB-60, Tensoft, older Kulcs-Soft versions) long dominated the market — search summary of [pannako.blog.hu 2026-04-16](https://pannako.blog.hu/2026/04/16/top_10_program_konyveloknek_2026-ban_magyarorszagon), [autofoliabudapest.blog.hu 2025](https://autofoliabudapest.blog.hu/2025/02/06/konyvelo_programok_osszehasonlitasa_melyiket_erdemes_valasztani), [hup.hu](https://hup.hu/node/177365).
- A Pannako "Top 10 programs for accountants 2026" puts **Zeuss first** as a "complete modern accounting-office platform". The criteria were automation, document management and digital data collection, client communication, NAV fit and scalability — [pannako.blog.hu](https://pannako.blog.hu/2026/04/16/top_10_program_konyveloknek_2026-ban_magyarorszagon). This may be SEO or vendor-adjacent content; treat it as weak.

**RLB-60**
- Imports invoice data from Számlázz.hu only from a file named `KSZLAKET.DBF`. The file must sit in a directory with no spaces in its name and must not have been opened in Excel — [tudastar.szamlazz.hu](https://tudastar.szamlazz.hu/gyik/rlb60-adatimport-nem-mukodik).
- Downloads supplier invoices from NAV Online Számla using the client's NAV technical-user credentials (menu: Könyvelés → Online számla fogadás) — [docs.rlb.hu online számla fogadás](https://docs.rlb.hu/dokumentacio/2/online-szamla-fogadas).
- Has a module for receiving online cash-register (pénztárgép) data — [docs.rlb.hu](https://docs.rlb.hu/dokumentacio/1/online-penztargep-adatok-fogadasa-es-konyvelese).
- Integrations exist from Billingo and Számlázz.hu — [billingo.hu/integraciok/rlb60](https://www.billingo.hu/integraciok/rlb60); [integracio.szamlazz.hu/rlb-60](https://integracio.szamlazz.hu/rlb-60).
- A third-party bank-statement converter for RLB exists: [bankkontir.hu](https://bankkontir.hu/).
- The search summary concluded that RLB mainly uses offline DBF file imports rather than APIs.

**Novitax**
- Products: NTAX (double-entry), TAXA (single-entry), WINTAX (integrated ERP).
- Automation is rule-based: user-built posting rules and settlement rules "can almost fully replace manual kontírozás (account coding)", which Novitax describes as the "seeds of AI".
- The 2026 versions add a "Bevallás XML Adattár" (tax-return XML repository).
- Sources: [novitax.hu NTAX](https://novitax.hu/szoftvereink/kettos-konyvviteli-program-ntax/); [novitax.hu 2026-02](https://novitax.hu/2026/02/eles-menupontok-2026-os-ntax-programban/); [tudastar.novitax.hu](https://tudastar.novitax.hu/ntax-2026-27-02-verzio/).
- No generative-AI feature was announced in the snippets.

**Kulcs-Soft**
- Kulcs-Könyvelés has a bank-statement importer for HUF and FX statement files from banks. From 2026-01-01, MBH corporate clients use MBH Vállalati Netbank exports — [fokonyv.kulcs-soft.hu](https://fokonyv.kulcs-soft.hu/support/solutions/articles/80001058047-banksz%C3%A1mlakivonat-importer).
- Kulcs Connect offers AI + OCR invoice matching and NAV/bank data import — [ks.hu/kulcs-connect](https://ks.hu/kulcs-connect/).
- Kulcs-Soft has published an eÁFA/M2M/ÁNYK/ONYA 2027 readiness article — [ks.hu](https://ks.hu/m2m-eafa-anyk-onya-igy-keszulunk-a-2027-es-valtozasokra/) (fetch blocked).
- Its support FAQ on eÁFA is at [fokonyv.kulcs-soft.hu](https://fokonyv.kulcs-soft.hu/support/solutions/articles/80001137019-gyakran-ism%C3%A9telt-k%C3%A9rd%C3%A9sek-eafa).

**Infotéka (Napló.NET)**
- Publishes newsletters on eÁFA/M2M updates — [tudasbazis.infoteka.hu](https://tudasbazis.infoteka.hu/hirlevel2.htm). No AI or API detail was retrieved.

**Zeuss / iBookr.ai** (most relevant competitor)
- Zeuss is an accounting-office ERP. Its features include quoting, **data requests (adatbekérés)**, **client status management**, task assignment, a time tracker, invoicing, a smart document manager, payroll and a bookkeeping program.
- Its AI matches invoice images, does kontírozás and processes bank CSVs.
- It claims **40 work-hours saved per month**.
- Pricing is tiered by client count. The starter office (1-50 clients) costs **35,000 HUF/month + VAT**, including the ERP, time tracker, invoicing, document manager, an AI assistant, "online fogadóóra" (online office hours) and 2 GB storage. Annual payment gets a 15% discount.
- Sources: [zeuss.hu/funkciok](https://zeuss.hu/funkciok/); [zeuss.hu/dijak](https://zeuss.hu/dijak/) (snippets).
- iBookr.ai Kft:
  - founded 2020, based in Győr;
  - owns the Énkönyvelőm and Zeuss brands;
  - its "Auróra" AI books bank and invoice items for the accountant to verify;
  - claims nearly 99% accuracy on 21,000 single-entry invoice items;
  - organised KATTexpo (see Q4).

  Sources: [ibookr.com](https://ibookr.com/); [crunchbase](https://www.crunchbase.com/organization/ibookr-ai-kft); [storeinsider.hu](https://storeinsider.hu/cikk/a-mesterseges-intelligencia-konyvelesben-is-legyozte-az-embert).

**Számlázz.hu**
- "Számlaverzum": NAV data sync makes all of a user's invoices, including those issued in other invoicing systems, available in Számlázz.hu, so accountants no longer need to collect them — [szamlazz.hu/szamlaverzum](https://www.szamlazz.hu/szamlaverzum).
- An "online financial data connection" pushes incoming and outgoing invoice data to accounting software — [szamlazz.hu](https://www.szamlazz.hu/egyedi-megoldasok/online-penzugyi-adatkapcsolat/).
- SMARTBooks is an online bookkeeping program for accountants — [szamlazz.hu/smartbooks-konyveles](https://www.szamlazz.hu/smartbooks-konyveles/); [smartbooks.hu](https://smartbooks.hu/portal/public/accountantProduct).
- It offers accountant user roles — [tudastar.szamlazz.hu](https://tudastar.szamlazz.hu/gyik/konyvelo-szamlazhat-felhasznalo-jogosultsagai).

**Other office and ERP tools**
- **ÜgyfélSegéd**:
  - NAV-data-based; it automatically flags **missing invoice images and bank statements**;
  - gives the accountant and the client a shared surface with a NAV-based invoice list;
  - matches invoice images with AI;
  - converts **PDF bank statements into an import for the bookkeeping program**.

  Pricing: Alap 1,490 HUF/month + 100 HUF per active business; Prémium 2,490 + 200 HUF per business (+27% VAT). No lock-in, 14-day trial — [ugyfelseged.hu](https://ugyfelseged.hu/) (snippet).
- Octopus 8 ERP (Vision-Software, developed since 1998) is a general ERP that also suits accounting firms — [visionsoft.hu](https://www.visionsoft.hu/octopus-8-erp-hO8.html). A separate "Octolibra könyvelés" exists ([octolibra.hu](https://octolibra.hu/)), but no details were retrieved.

**Public NAV interfaces**
- NAV Online Számla has a public M2M API: specification v3.0, test endpoint `api-test.onlineszamla.nav.gov.hu`, production `api.onlineszamla.nav.gov.hu`, and XSDs on GitHub — [github.com/nav-gov-hu/Online-Invoice](https://github.com/nav-gov-hu/Online-Invoice) (fetched directly).
- eÁFA M2M: since **3 Aug 2026** the live environment only accepts the **2.0 XSD**. NAV published a 2.0 interface specification with fuller tax-technical explanations, and an XML converter tool for eÁFA analytics on the new XSD — [nav.gov.hu](https://nav.gov.hu/sajtoszoba/hirek/2026.-augusztus-3-tol-a-nav-bevezeti-az-eafa-m2m-2.0-xsd-t); [nav.gov.hu spec 2.0](https://nav.gov.hu/ado/eafa/informaciok/megjelent-az-eafa-m2m-interfeszspecifikacio-2.0); [eafa-test.nav.gov.hu](https://eafa-test.nav.gov.hu/).

### Inferences
- **The "glue" space is no longer empty.**
  - ÜgyfélSegéd covers NAV-based missing-document detection plus a portal at about 21-42k HUF/month for 200 clients (own calculation from its price list).
  - Zeuss's ERP bundles data requests and client status from 35k HUF/month.
  - Optimato (Q5) sells document-chasing automation as a service.
  - A custom-built portal or reminder tool at 50-200k HUF/month will be compared against these.
  - The Kft's differentiation must be: (1) done-for-you setup and change management in firms that will not adopt software themselves (only about 30% are digitalised, per the KAVOSZ/MKOE snippet); (2) channels the SaaS tools do not cover (Viber/WhatsApp/email inbox triage, phone); (3) integration with the firm's specific legacy program (RLB DBF, Novitax, Kulcs exports); (4) eÁFA-transition and PMT/AML work. Alternatively it could be a reseller or implementation partner for ÜgyfélSegéd or Zeuss.
- **Integration reality:** legacy desktop programs mean the realistic integration surface is the NAV Online Számla API (free, standardised), bank statement files (PDF, CSV, MT940) and the programs' file exports and imports. It is not vendor APIs.

### Gaps
- No market-share numbers, not even rough ones. Ask in interviews and ask MKOE.
- API and export documentation for Tensoft, Forint-Soft and Infotéka was not retrieved (search budget exhausted).
- 2025-2026 AI announcements from Billingo, Tensoft, Forint-Soft and Infotéka were not verified.
- "Konyvelo.ai"-type startups: no product with that name was found.
- Open banking (PSD2 AIS) access for Hungarian SME accounts as an alternative to statement files was not researched.

---

## 3. Regulatory changes 2025-2027 that create work for accountants

### Takeaway
Q4 2026 to Q1 2027 is a pile-up of deadlines:
1. **ÁNYK retires on 31 Dec 2026.** The December 2026 VAT return is due through eÁFA by 20 Jan 2027, yet **98.9% of monthly VAT returns still went through ÁNYK** at end-September 2026.
2. **Receipt data reporting** has been mandatory since 1 Sep 2026, with sanctions from 1 Jan 2027.
3. **KATA's broad restoration from 2027** is planned by the new government; about 300-350k businesses may be affected and the law is due around the year-turn.
4. **Payroll complexity** has grown with the expanded SZJA (personal income tax) exemptions for mothers and the doubled family allowance.
5. **The Pmt. (AML law) amendment of 9 Jan 2026** extends sanctions screening and widens the beneficial-owner definition, with fines up to 400M HUF.

### Cited Findings

**eÁFA and ÁNYK**
- ÁNYK is withdrawn on 31 Dec 2026, and from 1 Jan 2027 returns can only be filed online. For VAT, eÁFA (web UI) and M2M replace ÁNYK. Monthly filers must submit the December 2026 return **through eÁFA by 20 Jan 2027** — [PwC HU 2026](https://www.pwc.com/hu/hu/sajtoszoba/2026/adodigitalizacios_valtozasok.html); [Andersen](https://hu.andersen.com/hu/hirek/afabevallas-kotelezove-valik-eafa/); [RSM](https://www.rsm.hu/blog/digitalis/eafa-atallas-2027-tol-milyen-lepesekre-kell-felkeszulniuk-a-vallalatoknak).
- "Three months before the ÁNYK withdrawal, **98.9% of monthly VAT returns** still arrive through ÁNYK." A company that cannot file on time because it has not prepared risks a default fine of **up to 1M HUF** — [adozona.hu "Áfariasztás: 99 százalék még nem váltott"](https://adozona.hu/afa/eAFA_bevallas_ANYK_M2M_riasztas_2EJ749); [profitline.hu](https://profitline.hu/afa-riasztas-a-vallalkozok-99-a-meg-nem-valtott-491076); [penzcentrum.hu 2026-09-27](https://www.penzcentrum.hu/vallalkozas/20260927/robban-a-birsagbomba-az-adobevallasoknal-vegleg-kivezetik-a-megszokott-rendszert-egymillios-buntetest-kockaztat-aki-nem-lep-idoben-1206233).
- A possible postponement of the ÁNYK withdrawal has come up in professional circles, but **there is no official decision** — search summary of [minositettkonyvelok.hu](https://www.minositettkonyvelok.hu/anyk-kivezetese-itt-a-pontos-datum/) and related pages (attribution uncertain). Check before selling on this deadline.
- How eÁFA works:
  - NAV assembles a VAT-return draft from available data (Online Számla and so on). The company or accountant reviews, modifies and approves it.
  - The accountant's role shifts from data entry to data verification and advisory.
  - The VAT analytics can be prepared in the bookkeeping program and uploaded directly.
  - NAV published the draft of the **2665** VAT return form.

  Sources: [ado.hu NAV-figyelő](https://ado.hu/ado/kozeleg-az-anyk-kivezetese-megjelent-a-2665-os-afabevallas-tervezete-nav-figyelo-49-het/); [onadozo.hu](https://www.onadozo.hu/hirek/a-nav-uj-eafa-koncepcioja-bizzuk-a-bevallast-a-gepekre-11753); [smart-konyvelo.hu](https://smart-konyvelo.hu/blog/eafa-2027-kotelezo-anyk-kivezetes-harom-csatorna).
- eÁFA assigns tax codes to **invoice line items**, not whole invoices. The basis becomes document-level, line-by-line VAT analytics. Common discrepancies include invoices missing from the VAT analytics or from NAV Online Számla, and these discrepancies feed NAV's risk analysis. eÁFA's warning messages help users fix basic mismatches — [szamlazz.hu blog 2024-12](https://www.szamlazz.hu/blog/2024/12/eafa-webfeluleti-mukodesenek-tapasztalatai/); [adozona.hu 2027-től kötelező az eÁfa](https://adozona.hu/2027_es_adovaltozasok/2027tol_kotelezo_az_eafa_felkeszult_mar_a_m_A22UE8); [EY HU](https://www.ey.com/hu_hu/insights/tax/mit-nez-eloszor-a-nav-egy-afa-fokuszu-adoellenorzes-soran) (snippets).
- The 2.0 XSD drops the structure that mirrored ÁNYK's form layout, a "paradigm shift" — [adovilag.hu 2026-07-03](https://adovilag.hu/2026/07/03/celegyenesben-az-eafa-m2m/); [simplyx.eu](https://simplyx.eu/hu/blog/eafa-m2m-2-0-felkeszules/).
- The Csongrád-Csanád chamber (CSKIK) itself published "Fontos változás az eÁfa-val kapcsolatban" — [cskik.hu](https://cskik.hu/fontos-valtozas-az-eafa-val-kapcsolatban/). This is a local channel signal.

**Receipt data reporting (nyugtaadat-szolgáltatás)**
- Mandatory from 1 Sep 2026 for manual and computer-generated receipts. Data must be sent within 3 calendar days of issue, as a daily summary broken down by VAT rate. E-cash registers are not mandatory for everyone, and manual receipts remain allowed. NAV grants a sanction-free period from 1 Sep to 31 Dec 2026; **sanctions may apply from 1 Jan 2027** — [nav.gov.hu](https://nav.gov.hu/ado/enyugta/nyugtaadat-szolgaltatas); [billingo.hu](https://www.billingo.hu/tudastar/olvas/e-nyugta-bevezetese); [adopraxis.hu](https://adopraxis.hu/cikk/nyugtaadat-szolgaltatas-2026-szeptemberetol); [acounto.com](https://acounto.com/nyugtaadat-szolgaltatas-2026-teendok/).

**KATA, KIVA and átalányadó (flat-rate tax)**
- The new government (Prime Minister Magyar Péter, Finance Minister Kármán András) plans to **restore broad KATA access from 2027**. KATA users would again be able to invoice companies, and the scheme would open beyond full-time sole traders, with a probably higher monthly tax. GKI estimates 300-350k businesses affected; there were about 444k KATA users before 2022. The final law is expected around the 2026/27 year-turn — [hovege.hu 2026-10-02](https://hovege.hu/ugyes-bajos/2026/10/02/kata-valtozas/); [telex.hu 2026-05-12](https://telex.hu/g7/penz/2026/05/12/kata-vissza-karman-andras-vallalkozok-adozas); [adozona.hu GKI](https://adozona.hu/kata_kiva/kata_visszater_2027_vallalkozas_adozas_8W800T).
- 2026 thresholds and rates:
  - The subjective VAT-exemption threshold (alanyi áfamentesség) rises from 18M to 20M HUF.
  - The átalányadó cost ratio is 45% in 2026 and 50% in 2027. The átalányadó eligibility limit for 2026 is 38,736,000 HUF.
  - KIVA is open to firms with up to 100 employees and 6bn HUF revenue, and they can stay in it up to 200 employees and 12bn; the rate is 10%.

  Source: [online-adotanacsadas.hu](https://www.online-adotanacsadas.hu/2026-evi-adovaltozasok-egyeni-vallalkozokkal-osszefuggesben-kata-afa-es-atalanyadozas-szamokban/); [rsm.hu KIVA](https://www.rsm.hu/blog/adotanacsadas/kiva-vagy-nem-kiva-ez-itt-a-kerdes-kinek-eri-meg-a-kiva-szerinti-adozas-2026-tol).

**Payroll (bérszámfejtés)**
- From 1 Jan 2026:
  - mothers under 30 are fully exempt from SZJA;
  - mothers of two who turn 40 after 31 Dec 2025 are exempt;
  - the family allowance has doubled (133,340 HUF of tax-base reduction per child per month for one dependant; 266,660 per child for two).

  Employees must give their employer an adóelőleg-nyilatkozat (tax-advance declaration) for the exemptions to apply during the year, and declarations do not carry over to a new employer — [adozona.hu 2026](https://adozona.hu/2026_os_adovaltozasok/Fontosabb_adovaltozasok_2026ra_5HLSGN); [BDO](https://www.bdo.hu/hu-hu/aktualitasok-blog/blog/csaladi-kedvezmenyek-2026); [rsm.hu bérszámfejtés 2026](https://www.rsm.hu/blog/berszamfejtes/berszamfejtes-2026-berszamfejtes-tb-valtozasok).
- Minimum wage:
  - 2026: 322,800 HUF (+11%, not the 13% originally agreed).
  - 2027: the 3-year agreement originally pencilled in 374,600 HUF (+14%), but it must be renegotiated. The garantált bérminimum (guaranteed minimum wage for skilled jobs) for 2027 is undecided; speculation puts it above 400k.

  Sources: [rsshirek.hu](https://rsshirek.hu/minimalber/); [tudasfaja.com](https://www.tudasfaja.com/minimalber-2027-elmaradhat-a-14-szazalekos-emeles-uj-rendszeren-dolgoznak/); [hvg.hu 2024](https://hvg.hu/gazdasag/20240919_Brutto-375-ezer-forint-lehet-a-minimalber-2027-ben) (older). **The 2027 figure is unresolved as of Oct 2026.**

**Pmt. (Act LIII of 2017, AML) and client due diligence**
- Accounting service providers with a seat, branch or site in Hungary must keep an internal AML policy (belső szabályzat) and keep it current. The policy must cover client due diligence, risk assessment (low, medium or high client categories), training and data retention. Suspicious transactions must be reported electronically to NAV's Pénzmosás Elleni Információs Iroda (AML financial intelligence unit) — [net.jogtar.hu Pmt.](https://net.jogtar.hu/jogszabaly?docid=a1700053.tv); [konyvelohirlap.hu](https://konyvelohirlap.hu/penzmosas-elleni-torveny-penzmosas-elleni-szabalyzat-konyveloknek/); [officina.hu](https://officina.hu/gazdasag/180-kinek-kotelezo-2018-penzmosas-elleni-szabalyzatot-kesziteni).
- Due diligence is required **for every client**, with documented identification of the beneficial owner, backed by ID copies and company documents — [minositettkonyvelok.hu PMT 2026 január](https://www.minositettkonyvelok.hu/pmt_2026_01_uj/).
- The **9 Jan 2026 amendment** is the first practically noticeable step of a series of changes expected through 2028:
  - Ongoing sanctions screening now covers the EU and UN lists **and the Hungarian national counter-terrorism list**, and requires **regular re-screening of the whole client base**.
  - A person exercising actual direction or control also counts as a beneficial owner.
  - PMT documentation is inseparable from the mandate (engagement) relationship and must be kept for **8 years**.
  - Per MKK, the amendment clarifies rather than creates obligations.

  Source: [minositettkonyvelok.hu PMT_2026_01 PDF](https://www.minositettkonyvelok.hu/wp-content/uploads/PMT_2026_01_u%CC%81j.pdf); [officina.hu 7+1 változás](https://officina.hu/gazdasag/242-penzmosas-elleni-torveny) (snippets).
- Enforcement:
  - For accounting and tax-advisory services, fines range from **100,000 HUF to 400M HUF**.
  - By end-2024 NAV's FIU had applied nearly 4,000 sanctions in the AML area (scope unclear: probably all obliged entities).
  - Fines were imposed even where a single document was missing or there was no real laundering risk.
  - Typical failures were basic identification steps and legal-entity documentation, not the risk logic.
  - On-site inspections are rare and are almost always preceded by electronic ones.

  Sources: [identigo.hu bírság esetpéldák](https://identigo.hu/blog/penzmosas-elleni-birsag-7-anonim-esetpelda-konkretumokkal/); [forum.identigo.hu ellenőrzési tapasztalatok 2026](https://forum.identigo.hu/t/ugyfelatvilagitas-jogi-szemelyek-ellenorzesi-tapasztalatok-2026/461); [vezinfoblog.hu](https://www.vezinfoblog.hu/pennzmosas-elleni-torveny-ellenorzesi-tipusok-leggyakrabban-elofordulo-hibak/); [vezinfo.hu "NAV ellenőrzések új módszerekkel" 2025-04](https://www.vezinfo.hu/rendezveny/penzmosas-ellenorzesek-20250416-konferencia-budapest/) (vendor and training-provider content).
- Supervision is split by service-provider category. The sources point to **NAV** running the Pmt. checks of accountants, but the exact supervisor under Pmt. §5 was not verified — [vezinfo.hu](https://www.vezinfo.hu/rendezveny/penzmosas-ellenorzesek-20250416-konferencia-budapest/).

**Other**
- Retirement of Ügyfélkapu / move to Ügyfélkapu+ and DÁP, and a new authorisation (meghatalmazás) system for accounting firms. Accountants described being "locked out" (2025) — [platform.dap.gov.hu tájékoztató](https://platform.dap.gov.hu/tajekoztatok/tajekoztato-konyveloknek-es-adoszakertoknek-az-ugyfelkapu-kivezeteserol.pdf); [pallas70.hu](https://pallas70.hu/tudashalo/hirek/ugyfelkapu-2025); [minositettkonyvelok.hu](https://www.minositettkonyvelok.hu/uj-meghatalmazasi-rendszer-a-konyveloirodak-szamara/).

### Inferences
- **Timing:** the sharpest pain falls in November 2026 to February 2027. That period combines the first eÁFA filing (20 Jan), the start of receipt-reporting sanctions, possible client churn and tax-regime choices driven by KATA (2027 law expected around the year-turn), payroll setup for the new year, and year-end closing. Firms will be **too busy to adopt anything new in Dec-Jan**. The selling window is Oct-Nov 2026 for "eÁFA readiness / exception check" offers, or Feb-Apr 2027 after the first painful cycles.
- **AML/KYC** is a credible automation target: a per-client obligation, an 8-year archive, a new whole-portfolio re-screening requirement and documented fines of 100k-400M HUF. A one-off "PMT backfile clean-up" project, plus continuous sanctions re-screening, is a clear, deadline-free and fear-driven offer. identiGO already sells a "Pmt. nyilvántartó" (AML register), so it is a competitor or partner.
- **KATA** reinstatement could bring a wave of onboarding of small, low-fee clients. That increases the value of automated onboarding (KYC plus document intake) for firms that take them on.

### Gaps
- Final 2027 KATA rules, the 2027 minimum wage and guaranteed minimum wage, and any ÁNYK postponement decision were all unresolved as of the snippets. Re-check in November 2026.
- No official NAV statistics on eÁFA adoption by accountants as opposed to companies.
- No GDPR guidance from NAIH specific to accountants using LLMs was found.

---

## 4. Professional bodies and channels to reach interviewees

### Takeaway
The highest-yield channels are:
- the official **PM register XLS**, which includes addresses and can therefore be filtered to Szeged and Csongrád-Csanád postcodes;
- MKOE (about 18.7k Facebook followers);
- the **Minősített Könyvelők Egyesülete** (MKK), which publishes the PMT and Közlönyfigyelő newsletters;
- Facebook groups and pages (Könyvelők klubja 5,000+ members, "Könyvelők" with about 17k followers, Egy könyvelő élete, **Könyvelő kAPPtár**);
- events (Könyvelő Fesztivál in March, Könyvelők éjszakája in April, KATTexpo, Cashbook Konferencia, PENTA KönyvelőKoktél);
- local directories (Könyvelő Tudakozó Csongrád-Csanád, JóSzaki Szeged).

No MKOE Csongrád-Csanád group page was found.

### Cited Findings
- **Register:** the register of accounting service providers is public, in alphabetical order, and **downloadable as XLS**. Fields: registration number, certificate number, name, birth name, mother's name, permanent address, mailing address and phone. Last updated 10 Sep 2026 — [penzugyiszakkepzes.kormany.hu](https://penzugyiszakkepzes.kormany.hu/nevjegyzek-konyvviteli-szolgaltatast-vegzok) (snippet). It is governed by Korm. rendelet 93/2002 — [net.jogtar.hu](https://net.jogtar.hu/jogszabaly?docid=a0200093.kor).
- **NAIH** issued an opinion on what is public in the register, including that data is not retroactively public — [naih.hu](https://naih.hu/dontesek-infoszab-allasfoglalasok?download=601%3Akonyvviteli-szolgaltatast-vegzok-nyilvantartasaban-visszamenolegesen-nem-nyilvanosak-az-erintettek-adatai).
- **MKOE:** a nonprofit professional association. Phone 06 1 336 7000, titkarsag@mkoe.hu. Its Facebook page has 18,694 followers — [mkoe.hu](https://mkoe.hu/); [facebook.com/mkoe.hirek](https://www.facebook.com/mkoe.hirek/). **No Szeged or Csongrád-Csanád group page surfaced in search.**
- **Minősített Könyvelők Egyesülete (MKK):** publishes "PMT a könyvelői gyakorlatban" (Jan 2026), a monthly "Könyvelői Közlönyfigyelő" and a "Segédlet a könyvelői feladatokhoz" — [minositettkonyvelok.hu](https://www.minositettkonyvelok.hu/pmt_2026_01_uj/); [KK_2026_06](https://www.minositettkonyvelok.hu/wp-content/uploads/KK_2026_06.pdf); [MKK-Segedlet](https://www.minositettkonyvelok.hu/wp-content/uploads/MKK-Segedlet.pdf).
- The Magyar Adótanácsadók és Könyvviteli Szolgáltatók Országos Egyesülete (an association of tax advisers and accounting service providers) issued an open letter to legislators — [onadozo.hu](https://www.onadozo.hu/hirek/a-magyar-adotanacsadok-es-konyvviteli-szolgaltatok-orszagos-egyesuletenek-nyilt-levele-a-jogalkotok-reszere-9605).
- The Számviteli Egyesület (MSZSZE) covers the "NGM regisztráció" (register-related training) — [mszsze.hu](https://www.mszsze.hu/oktatas/ngm-regisztracio).
- MKVK (the chamber of auditors) publishes AML (pénzmosás) communications and model policies — [mkvk.hu](https://mkvk.hu/szabalyozas/szabalyzatok/PMT-szabalyozas/penzmosas_kozlemenyek). Its regional organisation for the south of the Great Plain (Dél-Alföld) was not retrieved.
- **Facebook:**
  - "Könyvelők" page: 16,932 followers.
  - "Könyvelők klubja": closed group with 5,000+ members; people ask on gyakorikerdesek.hu why they are not admitted, which suggests it vets members.
  - "Egy könyvelő élete": 15,515 likes.
  - Also "Könyvelő kAPPtár" (an app directory for accountants), "Könyvelőfesztivál" and "Könyvelő leszek".

  Sources: [facebook.com/konyvelok](https://www.facebook.com/konyvelok/); [gyakorikerdesek.hu](https://www.gyakorikerdesek.hu/uzlet-es-penzugyek__adozas-konyveles__7989270-miert-nem-vesznek-be-a-facebookon-a-konyvelok-klubja-csoportba-ha-valaki-tagja); [facebook.com/egykonyveloelete](https://www.facebook.com/egykonyveloelete/); [facebook.com/konyvelokapptar](https://www.facebook.com/konyvelokapptar/) (snippet counts, dates unknown).
- **Events:**
  - **Könyvelő Fesztivál 2026**: 25-26 March 2026, Sugár mozi, Budapest, themed "accountants as entrepreneurs" — [programturizmus.hu](https://www.programturizmus.hu/ajanlat-konyvelo-fesztival.html); [gotravel.hu](https://gotravel.hu/program-konyvelo-fesztival).
  - **Könyvelők éjszakája**: 30 April 2026 — [konyvelokejszakaja.hu](https://konyvelokejszakaja.hu/).
  - **KATTexpo** (Könyvelés Automatizációs és Technológiai Expo): held in Győr at the university's management campus, organised by iBookr. Its tracks are data collection and processing, and bookkeeping automation — [kattexpo.hu](https://kattexpo.hu/); [ibookr.com](https://ibookr.com/2024/01/10/kattexpo-hu-hamarosan/) (date of the next edition unknown).
  - **2. Cashbook Konferencia**: on paperless accounting and digital collaboration — [cashbookkonferencia.hu](https://cashbookkonferencia.hu/).
  - **PENTA KönyvelőKoktél**: e-learning viewable 4-31 Dec 2026 — [penta.hu](https://penta.hu/konferenciak/konyvelokoktel).
- **Local directories:** [Könyvelő Tudakozó, Csongrád-Csanád](https://konyvelotudakozo.hu/csongrad-csanad-megye.html?oldal=1); [JóSzaki, Szeged](https://joszaki.hu/szakemberek/konyveles/szeged). Szeged firms surfaced in search include könyVELÜNK, Vizsu-Tax and Jakus Könyvelőiroda (from the search summary).
- **Newsletters and press:** adozona.hu, ado.hu, 5percado.hu, adopraxis.hu, onadozo.hu, adovilag.hu, konyvelohirlap.hu and pallas70.hu all actively cover eÁFA, PMT and AI topics (see citations throughout). Bookkeepie (a directory of about 400 firms) sells accountant marketing packages at 6,900-26,500 HUF/month — [bookkeepie.com/hu/konyveloknek](https://www.bookkeepie.com/hu/konyveloknek).

### Inferences
- **Practical interview pipeline:**
  1. Download the register XLS and filter by mailing-address postcode. Szeged is 67xx; Csongrád-Csanád is mostly 66xx-68xx. This gives a list of registered individuals, not firms.
  2. Cross-reference with Könyvelő Tudakozó and JóSzaki to find the firms.
  3. Prioritise warm introductions from the salesperson's network.
  4. Use MKK and MKOE content (PMT, eÁFA) as the hook for a free local "eÁFA + PMT readiness" breakfast via CSKIK.
- **GDPR caution:** the register holds personal data (addresses, phone numbers). Using it for direct marketing raises a legitimate-interest question; NAIH has opined on the register's publicity. Prefer firm-level public contacts.
- KATTexpo is run by iBookr/Zeuss, a competitor. Könyvelő kAPPtár looks like a listing channel for accountant tools.

### Gaps
- MKOE's regional or county groups and their Szeged meeting schedule were not found; contact MKOE directly.
- The MKVK Dél-Alföld regional organisation, Számviteli Levelek (Wolters Kluwer?) and Piac & Profit readership numbers were not retrieved.
- The number of registered accountants in Csongrád-Csanád is unknown until the XLS is downloaded and filtered (not possible here because of the proxy).

---

## 5. Existing AI and automation offerings (Hungary and international) and what accountants value

### Takeaway
In Hungary, document chasing and NAV-based gap detection are already productised:
- **ÜgyfélSegéd**: about 100-200 HUF per client per month;
- **Zeuss/iBookr**: office ERP from 35k HUF/month, Auróra AI posting, a claimed 40 h/month saved;
- **Optimato Consulting**: a done-for-you document-chasing automation agency on Google Workspace or M365;
- **Acounto**: an AI-heavy digital accounting provider with 1,500+ clients, which plans to license its software to partner accountants;
- **identiGO**: a Pmt. compliance tool.

Internationally, surveys consistently rank **getting documents from clients** as the #1 firm pain. Capital is flowing into AI-native firms and roll-ups (Current/Crete, Basis, Pennylane).

### Cited Findings

**Hungary**
- **Optimato Consulting** turns monthly document requests, reminders and gap lists into automatic processes on the firm's existing Google Workspace or Microsoft 365, so there is no new platform to learn. Features:
  - personalised monthly emails and deadlines for each client;
  - a central view of who has submitted documents and what is missing;
  - smart reminders that go only to clients with open items;
  - automatic filing into the right folders;
  - internal exception lists, so the accountant does not review every client.

  It sells nationwide and online, and also targets real estate and law firms — [optimatoconsulting.com/konyveloirodaknak](https://optimatoconsulting.com/konyveloirodaknak/) (snippet; prices not seen). **This is essentially offer (a); it is a direct competitor.**
- **ÜgyfélSegéd**: see Q2 (NAV-based missing invoice images and bank statements, AI matching, PDF bank statement to import; 1,490 + 100 HUF/client or 2,490 + 200 HUF/client per month) — [ugyfelseged.hu](https://ugyfelseged.hu/).
- **Zeuss / iBookr.ai / Énkönyvelőm**: see Q2 — [zeuss.hu](https://zeuss.hu/); [ibookr.com](https://ibookr.com/).
- **Acounto** wants to automate the accounting-service process. Its AI systems book VAT and bank items automatically, and it plans to roll out its software to selected partner accountants — search summary citing [konyvelok.hu interjú](https://konyvelok.hu/interju/a-mesterseges-intelligencia-segit-mi-pedig-iranyitjuk) (attribution uncertain); prices in Q1.
- **Bookkeepie "Zsebkönyvelő"**: an AI knowledge-base assistant running on a closed, curated knowledge base maintained by the Bookkeepie team, with no live internet — [ado.hu](https://ado.hu/szamvitel/ai-a-konyvelesben-az-automatizalt-megoldasok-az-emberi-tudassal-ellenorizve-jelentik-a-szakma-jovojet/) (snippet). This is a precedent for an "accountant FAQ bot".
- **Mynds.ai / Adriana**: invoice pipeline exporting to 35 programs (see earlier notes).
- **DigitBooks.hu**: exists — [digitbooks.hu](https://digitbooks.hu/) (no details).
- **virtualworkforce.ai** markets an "AI assistant for accounting firms" in Hungarian — [virtualworkforce.ai/hu](https://virtualworkforce.ai/hu/ai-asszisztens-konyveloirodaknak/) (no details).
- **identiGO**: AML (Pmt.) register, templates, a forum, and case studies on fines — [identigo.hu](https://identigo.hu/blog/penzmosasi-torveny-minden-teendo-es-nyomtatvany-egy-helyen/) (prices not retrieved).
- Vendor claims on AI matching (unverified): an "intelligent matching" algorithm that handles partial payments, FX differences and several invoices per transfer; machine learning "cuts corrections by 70%"; a mid-sized firm automating half its invoices "saves 80-120 h/month" — [zeuss.hu 2026-01-19](https://zeuss.hu/2026/01/19/ciposdoboztol-a-mesterseges-intelligenciaig-igy-alakul-at-a-magyar-konyveles-2026-ra/) (snippet, attribution uncertain; vendor marketing).
- Adoption signals (relayed by KAVOSZ):
  - Wolters Kluwer: AI use among accountants more than quadrupled in one year;
  - Thomson Reuters: 21% of tax and accounting firms already used generative AI;
  - AI users close the month on average 7.5 days faster.

  Source: [kavosz.hu](https://www.kavosz.hu/az-en-vallalkozasom/mi-a-konyvelesben/) (secondary; international data).

**International benchmarks**
- **Dext:** Practice plans cost $17.70 (Essentials) or $19.20 (Advanced) per client per month, with a 10-client minimum. Volume pricing: about £391/month for 50 clients, £894 for 150, £1,541 for 300. **AutoEntry** sells credit bundles: £15.45 (50 credits) to £119.35 (500 credits) a month, with unlimited client companies — [costbench.com](https://costbench.com/software/accounting/dext/); [receiptflow.co](https://receiptflow.co/blog/dext-vs-autoentry-uk-bookkeepers) (aggregator snippets).
- **Karbon** (practice management): users save **3.2 h per employee per week** by automatically chasing clients. Some firms save 3.5 h/week on chasing and 3.3 h/week on managing work. Total savings average 19.9 h per employee per week (Karbon's 2026 Firm Usage Survey, 14% of its customer base; self-reported vendor data) — [karbonhq.com](https://karbonhq.com/resources/accounting-firm-productivity/).
- **Survey data:**
  - In a 2024 survey of 367 accounting and bookkeeping firm owners, "getting information and documents from clients" was the #1 challenge at 65.2%, up from 53.8%. A 2025 follow-up confirmed it as the top issue.
  - In a 2026 survey of firms across 8 countries, about 7 in 10 named chasing missing documents as the #1 task to hand to an AI agent.
  - Firms spend about 5 h/week detecting and fixing client data errors.

  These appeared in a search summary across [taxdome.com statistics](https://taxdome.com/blog/accounting-statistics), [liscio.me](https://www.liscio.me/resources/how-accounting-firms-can-automate-client-document-collection), [enterprisedna.co](https://enterprisedna.co/resources/guides/accounting-stop-chasing-client-documents/) and [gridex.dev](https://gridex.dev/blog/why-cpa-firms-lose-time-chasing-client-documents/). **Attribution uncertain** (the 367-firm survey is probably Karbon's or TaxDome's). Verify before quoting.
- **Roll-ups and AI-native firms:**
  - **Current (formerly Crete)**, backed by Thrive Capital, ZBS and Bessemer, with an OpenAI partnership: a plan to spend $500M+ over two years buying US accounting firms; more than $300M annual revenue, about 900 staff and 20+ firms; rebranded June 2026 — [themiddlemarket.com](https://www.themiddlemarket.com/latest-news/crete-plans-500m-ai-driven-roll-up-of-accounting-firms).
  - **Basis:** $100M Series B at $1.15B valuation (Accel, Feb 2026), AI agents for accounting firms.
  - **Multiplier:** raised $62.5M and bought 8 firms ([TechCrunch 2025-06](https://techcrunch.com/2025/06/18/multiplier-founded-by-ex-stripe-exec-nabs-27-5m-to-fuel-ai-powered-accounting-roll-up)).
  - **Modus:** $85M (audit).
  - **Pennylane** (Paris, SME financial OS used by accountants): €175M led by TCV with Blackstone Growth, Jan 2026, "anticipating market consolidation" — [eu-startups.com](https://www.eu-startups.com/2026/01/sequoia-backed-french-accounting-unicorn-pennylane-secures-e175-million-as-it-approaches-profitability/).
  - Tracker: [debitai.co/rollup](https://debitai.co/rollup/).
- **Tabby** (an AI bookkeeper for small businesses) reports 5,500 SMB users — [aiforradalom.hu](https://aiforradalom.hu/uzlet/ai-konyvelo-valtja-le-az-emberi-konyveloket-tabby-automatizalja-a-kisvallalatok-).

### Inferences
- **Price anchors for Hungarian buyers:**
  - SaaS: ÜgyfélSegéd at about 0.1-0.2k HUF per client per month, Zeuss from 35k per office per month.
  - International: Dext at about 6-7k HUF per client per month (own conversion; not a Hungarian price reality).
  - A retainer of 50-200k HUF/month must therefore be justified by service (setup, migration, change management, ongoing tuning, channels and integration), **not** by features.
- **What accountants value most** (international, consistent with the Hungarian pain points): fewer chasing touches, a single "who is missing what" view, and exception lists instead of full review. Optimato and ÜgyfélSegéd already message exactly this in Hungarian.
- **Partner option:** the Kft could be the Szeged/Dél-Alföld implementation partner for ÜgyfélSegéd or Zeuss (onboarding firms, migrating client lists, wiring NAV technical users, training staff) and add custom pieces on top (Viber/WhatsApp intake, inbox triage, AML). This avoids head-on competition with sub-1k HUF/client SaaS.
- **Roll-up angle:** with an aging profession and earn-out-based sales, an "acquire an old practice and run it AI-first" model exists in the US (Current) and is backed in Europe (Pennylane's consolidation remark). For a 2-founder Kft this is a later option (year 2-3), not an entry point.

### Gaps
- Prices and traction for Optimato, identiGO, DigitBooks and virtualworkforce.ai were not retrieved.
- Customer counts for Zeuss and ÜgyfélSegéd are unknown.
- Uku, Karbon and TaxDome pricing was not retrieved (getuku.com blocked); Juno and Digits were not researched.

---

## 6. Documented pain points voiced by Hungarian accountants

### Takeaway
Hungarian evidence is mostly secondary: articles, vendor blogs and an old study. Recurring themes:
- clients bring documents late or incomplete, and some still in person;
- overload from too many clients at low fees;
- succession and aging;
- forced digital transitions (Ügyfélkapu+/DÁP, eÁFA, receipt data);
- AML paperwork.

Quantified Hungarian survey data on time loss is missing. Interviews must create it.

### Cited Findings
- Only about 30% of accounting businesses are digitalised, and some clients still bring invoices in person (MKOE 2025, as relayed) — [kavosz.hu](https://www.kavosz.hu/az-en-vallalkozasom/mi-a-konyvelesben/) (snippet; verify).
- 78% had problems with late or incomplete records from a new client, and 18.5% of clients are in arrears on fees — [GVH/HÉTFA 2010](https://www.gvh.hu/pfile/file?path=%2Fgvh%2Fversenykultura_fejlesztes%2Ftamogatott_programok%2Ftamogatott_programok%2F70_2010_HETFA_Tanulmany_konyvelo_fin.pdf&inline=true) (**2010; attribution uncertain**).
- Accountants can only work well if they receive documents on time. Late documents lead to late returns and fines. Overloaded low-fee accountants juggle too many clients and miss deadlines — [dulubi.hu](https://dulubi.hu/blog/konyvelo-arak-2026/); [webkonyvelo.hu](https://www.webkonyvelo.hu/egy-elerheto-konyvelot-szeretnek/); [vrg.co.hu](https://vrg.co.hu/2024/06/03/7-into-jel-hogy-a-konyvelod-nem-megfeleloen-vegzi-a-munkajat/) (client-side and vendor viewpoints).
- "More work, but no successors" — [trendfm.hu](https://trendfm.hu/cimlap/egyre-tobb-a-munka-de-utanpotlas-nincs-mi-lesz-igy-a-konyvelokkel-15615). "Value your good accountant" (shortage) — [haszon.hu](https://haszon.hu/megkeresni/konyveles/konyvelok-munkaerohiany).
- "Locked gates and accountants left outside" (Ügyfélkapu 2025 changes) — [pallas70.hu](https://pallas70.hu/tudashalo/hirek/ugyfelkapu-2025); "Ügyfélkapu+ szolgáltatásról könyvelői szemmel" — [egykonyveloelete.hu](https://egykonyveloelete.hu/ugyfelkapu-szolgaltatasrol-konyveloi-szemmel/).
- eÁFA readiness gap: 98.9% of monthly VAT returns still via ÁNYK at end-September 2026 — [adozona.hu](https://adozona.hu/afa/eAFA_bevallas_ANYK_M2M_riasztas_2EJ749).
- Számlázz.hu frames its products around the pain that "accountants spend valuable work time collecting client invoices and re-entering them" ("Az adatrögzítés nem könyvelés", 2020) — [szamlazz.hu blog 2020](https://www.szamlazz.hu/blog/2020/11/az-adatrogzites-nem-konyveles-a-szamlazz-hu-elhozta-a-valtozast/) (older); [szamlazz.hu Q&A 2021](https://www.szamlazz.hu/blog/2021/10/konyvelok-kerdeztek-mi-valaszolunk-digitalizacios-qa/).
- AML: fines for single missing documents; legal-entity identification is the most frequent failure — [forum.identigo.hu 2026](https://forum.identigo.hu/t/ugyfelatvilagitas-jogi-szemelyek-ellenorzesi-tapasztalatok-2026/461).
- Payroll: the 2026 exemptions depend on employee declarations that do not transfer between employers, which creates collection work — [money.hu 2026-01-08](https://tudastar.money.hu/hir/20260108/szja-kedvezmeny-adoeloleg-nyilatkozat/); [csaladinet.hu](https://www.csaladinet.hu/hirek/tb_ellatasok-penzugyek/csaladi_penzugyek/36472/2026-os_szja-kedvezmenyek_ennyi_penzt_hagysz_az_asztalon_ha_nem_nyilatkozol_idoben).

### Inferences
- **Pain ranking hypothesis for interviews:** (1) document chasing; (2) eÁFA tax-code and analytics mismatches during the first cycles; (3) capacity and hiring; (4) client questions about regime changes (KATA 2027, payroll exemptions); (5) PMT/AML documentation. Test whether (2) and (5) carry a fear premium that (1) lacks: (1) is chronic, while (2) and (5) bring fines.

### Gaps
- No forum threads or Facebook posts could be read directly; closed groups are not indexable and fetches were blocked.
- No recent (2024-2026) Hungarian survey quantifying hours lost to chasing.

---

## 7. Candidate offer shapes, with estimated value, integration difficulty and risks

### Takeaway
All value figures below are **own estimates** built on the cited anchors: the loaded accountant cost of about 4,400 HUF per productive hour (from the [profession.hu](https://www.profession.hu/fizetesek/merlegkepes-konyvelo) median plus 13% szocho), Karbon's 3.2 h per employee per week on chasing ([karbonhq.com](https://karbonhq.com/resources/accounting-firm-productivity/)), Zeuss's claimed 40 h/month ([zeuss.hu](https://zeuss.hu/)), and SaaS price anchors (ÜgyfélSegéd, Zeuss, Dext). The reference firm has **5 staff and about 200 clients**.

The most defensible offers are:
- **(b) eÁFA/NAV-bank-ledger exception check**, timed to the Jan 2027 cut-over;
- **(d) AML/KYC backfile and re-screening**, driven by fear of fines, with little SaaS saturation found apart from identiGO.

**(a) Document chasing** is real but already productised cheaply, so it should be sold as setup and integration or as a partner resale, not as a standalone product.

### Comparison table (own estimates; validate in interviews)

| Offer | Time saved (5-staff, 200-client firm) | Indicative value per month | Integration difficulty | Main competitors / anchors | Key risks |
|---|---|---|---|---|---|
| (a) Document-chasing assistant (email/Viber/WhatsApp reminders, missing-items list from NAV Online Számla data, auto-filing) | If Karbon's 3.2 h/employee/week holds: about 14 h/employee/month, about 70 h/month in total | about 300k HUF of capacity (70 h × 4.4k) | Low-medium. NAV Online Számla API (free, per-client technical user); email/M365/Google; Viber/WhatsApp Business APIs; no ledger write-back needed | ÜgyfélSegéd (about 21-42k HUF/month for 200 clients), Zeuss ERP (from 35k), Optimato (service) | Price anchoring by cheap SaaS; client-side adoption (clients ignore portals); managing NAV technical-user credentials; GDPR (accountant is controller for client data, Kft processor) |
| (b) NAV Online Számla vs bank vs ledger/VAT-analytics exception report before eÁFA filing | Unknown; hypothesis 0.5-1.5 h per VAT-paying client per month at first, falling as data is cleaned | High in Jan-Mar 2027 (risk of 1M HUF fine, NAV risk analysis) | Medium-high. Needs ledger and VAT-analytics export from RLB (DBF), Novitax, Kulcs etc.; bank statements (PDF/CSV); NAV API; tax-code logic per eÁFA line | Accounting programs (they generate analytics and upload); eÁFA's own warnings; Kulcs Connect, Zeuss bank matching | Vendors close the gap themselves; tax-logic errors lead to liability, so position as "flags for human review"; narrow window if eÁFA stabilises |
| (c) Client FAQ bot / inbox triage (routing, drafts, KATA 2027 / payroll-exemption / eÁFA explainers) | Not measured; likely smaller than (a) | Moderate | Low-medium (M365/Gmail, knowledge base) | Bookkeepie Zsebkönyvelő (curated KB), generic chatbots (HUF 1.9-80k/month, see earlier report) | Advice liability; hallucination on fast-changing rules (KATA law not final); clients prefer "their" accountant |
| (d) AML/KYC (Pmt.) onboarding and backfile: beneficial-owner capture, ID/document collection, risk scoring, scheduled sanctions re-screening incl. the national list, 8-year archive | One-off backfile of 200 clients (hours per client unknown) plus ongoing re-screening | High fear premium (fines 100k-400M HUF) | Medium (company register / e-cégjegyzék data, sanctions lists, document store, policy templates) | identiGO (Pmt. register), MKVK/MKK templates, officina templates | Regulatory accuracy; Pmt. changes through 2028; the supervisor's acceptance of automated records; data-protection risk of the ID copies the Kft would process |
| (e) Payroll data intake (attendance, leave, new hires, adóelőleg-nyilatkozat for the 2026 mothers' and family exemptions) | Not quantified | Moderate; peaks in January and on hires | Low-medium (forms, e-signature, export to the payroll program) | Zeuss payroll module; payroll programs | Special-category or sensitive data (health/sick leave, children); errors directly affect net pay |

### Cited Findings (anchors used above)
- Karbon automated chasing saves 3.2 h per employee per week — [karbonhq.com](https://karbonhq.com/resources/accounting-firm-productivity/).
- Zeuss claims 40 h/month saved; its starter plan is 35k HUF/month for 1-50 clients — [zeuss.hu](https://zeuss.hu/); [zeuss.hu/dijak](https://zeuss.hu/dijak/).
- ÜgyfélSegéd costs 1,490 + 100 HUF per client per month (Alap) or 2,490 + 200 HUF (Prémium) — [ugyfelseged.hu](https://ugyfelseged.hu/).
- Dext costs $17.70-19.20 per client per month — [costbench.com](https://costbench.com/software/accounting/dext/).
- An eÁFA default fine of up to 1M HUF; 98.9% of returns still via ÁNYK — [adozona.hu](https://adozona.hu/afa/eAFA_bevallas_ANYK_M2M_riasztas_2EJ749).
- Pmt. fines of 100k-400M HUF; re-screening required since Jan 2026 — [identigo.hu](https://identigo.hu/blog/penzmosas-elleni-birsag-7-anonim-esetpelda-konkretumokkal/); [minositettkonyvelok.hu](https://www.minositettkonyvelok.hu/wp-content/uploads/PMT_2026_01_u%CC%81j.pdf).
- RLB imports via DBF; RLB's NAV inbound invoice download needs the client's technical user — [tudastar.szamlazz.hu](https://tudastar.szamlazz.hu/gyik/rlb60-adatimport-nem-mukodik); [docs.rlb.hu](https://docs.rlb.hu/dokumentacio/2/online-szamla-fogadas).
- Median mérlegképes salary is 550k HUF gross — [profession.hu](https://www.profession.hu/fizetesek/merlegkepes-konyvelo).

### Inferences
- **Suggested pricing shape** (hypothesis to test):
  - (b) as an "eÁFA readiness check plus first three cycles": a fixed setup of 300-600k HUF, then about 300-800 HUF per VAT-paying client per month.
  - (d) as a one-off backfile project priced per client (e.g. 2-5k HUF per client), plus a monthly re-screening retainer.
  - (a) only as a setup or implementation fee on top of ÜgyfélSegéd or Zeuss, or a light custom build on M365/Google in the style of Optimato.

  All figures are own estimates. No Hungarian willingness-to-pay data exists.
- **Interview questions this implies:**
  1. Which program and version do you use, and how do you export the general ledger and VAT analytics?
  2. How many clients do you have, how many are VAT payers, and how many monthly filers?
  3. Hours per month spent on chasing; how many clients are late by the 10th?
  4. Have you filed through eÁFA yet? What mismatches did you see?
  5. What is the state of your PMT files, and when did you last re-screen?
  6. Do you already use ÜgyfélSegéd, Zeuss or Kulcs Connect?
  7. What would you pay to take on 5 more clients without hiring?
- **The biggest strategic risk** is that the "glue" niche identified in the earlier report is being filled by Hungarian SaaS priced at roughly 1/10 of a service retainer. The Kft's edge is human implementation and local trust, which argues for a service and partner model plus compliance-driven offers (eÁFA, PMT) with deadlines and fines attached.

### Gaps
- No Hungarian time-and-motion data for any of (a)-(e); all savings above are extrapolated from vendor and international data.
- Whether NAV Online Számla API queries of a client's **inbound** invoices work with the accountant's own technical-user setup per client: by developer knowledge, the API supports buyer-side digest queries with the taxpayer's technical user, but this was not verified here. Check spec v3.0 on [GitHub](https://github.com/nav-gov-hu/Online-Invoice).
- Bank-statement access routes (PSD2 AIS providers serving Hungarian banks) and their cost were not researched.
- No prices for Optimato or identiGO, so competitive positioning for (a) and (d) is incomplete.
