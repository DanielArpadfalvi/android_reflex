# Interjúterv könyvelőirodáknak: ügyfélfeltáró interjúk Szegeden és Csongrád-Csanádban

*Állapot: 2026. október 3. Gyakorlati munkaanyag a Kft. két alapítójának (fejlesztő/IT-projektvezető és értékesítő). Senkit nem kerestünk még meg.*

**Háttéranyagok:**
- `research_notes/Könyvelőirodák Szegeden/accounting_deep_dive.md`: piac, szoftverek, jogszabályok, versenytársak
- `reports/AI üzleti lehetőségek Szegeden.md`: stratégia, 90 napos validáció
- `research_notes/Könyvelőirodák Szegeden/prospects_szeged_city.md` és `prospects_county.md`: 31 szegedi és 24 vármegyei iroda
- `reports/Könyvelőirodák top 20 lista.md`: rangsorolt első megkeresési lista két hullámban

> **Figyelem:** a háttéranyagok számadatainak nagy része keresőtalálat-kivonatból (snippetből) származik, és ellenőrizetlen. Ilyen például a „98,9% még ÁNYK-n” adat, a bírságplafonok és a versenytársak árai. Ezeket a megkeresésekben csak forrásmegjelöléssel vagy óvatos megfogalmazással használjuk. **Az ÁNYK esetleges halasztását** a szakma felvetette, hivatalos döntés nem volt róla. Az első üzenetek kiküldése előtt (és novemberben újra) ellenőrizni kell a nav.gov.hu-n.

## Röviden: mit akarunk megtudni hat-nyolc hét alatt

Október elejétől november végéig **15–20 interjút** készítünk szegedi és vármegyei könyvelőirodák tulajdonosaival és vezető könyvelőivel, mielőtt a december–januári zárás és az első eÁFA-bevallás (2027. január 20.) elviszi az idejüket. Három kérdésre keresünk választ.

1. **Fáj-e eléggé** (b) a NAV Online Számla, a bankkivonat és a főkönyv/ÁFA-analitika közötti eltérések kézi keresése az eÁFA előtt, illetve (d) a Pmt. (pénzmosás elleni törvény) szerinti ügyfélátvilágítási aktak rendbetétele és a teljes ügyfélkör ismételt szankciólistás szűrése? Annyira kell fájnia, hogy **fizessenek érte**.
2. **Mit csinálnak most helyette**, mennyi idővel, milyen szoftverrel? Kell-e nekik egy szolgáltatás, vagy elég a programjuk vagy egy olcsó SaaS (ÜgyfélSegéd, Zeuss, Kulcs Connect, identiGO)?
3. **Ki dönt, mennyiből és mikor?** Van-e legalább 3 iroda, amely konkrét lépést tesz: adatmintát ad, szándéknyilatkozatot ír alá vagy fizetett pilotot vállal?

A **dokumentumbekérést (a)** kontrollként vizsgáljuk. Ez a legismertebb fájdalom, de olcsón termékesítették már. Csak integrációs vagy bevezetési szolgáltatásként érdekes (`accounting_deep_dive.md`, 5. és 7. fejezet).

---

## 1. Célok és hipotézisek

### 1.1 Célok

- **Elsődleges:** eldönteni, hogy (b) vagy (d) (vagy egyik sem) legyen-e a Kft. első fizetős könyvelőirodai ajánlata, és milyen árszerkezettel.
- **Másodlagos:**
  - feltérképezni a helyi irodák szoftverkörnyezetét, mert ettől függ az integráció;
  - kideríteni, ki dönt és mennyit költenek eszközökre;
  - legalább 3 pilotpartnert és 2–3 ajánlót vagy multiplikátort szerezni (MinKE, MKOE, kamara).
- **Mellékes:** referencia- és bizalomépítés az értékesítő hálózatában, a „szegedi irodák mit látnak az eÁFA előtt” összefoglaló mint tartalom.

### 1.2 Cáfolható hipotézisek

Minden hipotézishez megadtuk, mi számít megerősítésnek és mi cáfolatnak. A küszöbök **saját, induló becslések**. Az első 5 interjú után (8. fejezet) finomíthatók, de nem lazíthatók utólag csak azért, hogy átmenjen a hipotézis.

| # | Terület | Hipotézis | Megerősíti, ha… | Cáfolja, ha… |
|---|---|---|---|---|
| H1 | Fájdalom (b) | A 3–25 fős irodák a NAV–bank–főkönyv eltérések kézi keresését az ÁFA-bevallás előtt a havi ciklus 3 legidőigényesebb vagy legkockázatosabb feladata közé sorolják. | Az interjúk legalább 40%-ában spontán (nem rávezetve) előkerül, és konkrét múltbeli esetet mesélnek el: eltérés, önellenőrzés, NAV-levél. | Az alanyok többsége szerint „a program megcsinálja”, vagy nem tudnak az elmúlt 3 hónapból konkrét esetet mondani. |
| H2 | Fájdalom (d) | A Pmt. 2026. januári módosítása (teljes ügyfélkör ismételt szankciólistás szűrése, bővebb tényleges tulajdonosi kör) óta az irodák többségének hiányos az ügyfélátvilágítási aktája, és ez aggasztja őket. | Legalább 40% bevallja, hogy az akták egy része hiányos, vagy az újraszűrést még nem végezték el, **és** az elmúlt 12 hónapban költött rá időt vagy pénzt (sablon, képzés, identiGO, ügyvéd). | A többség szerint rendben van (például identiGO-t vagy belső szabályzatot használnak), vagy a téma nem érdekli őket, mert „ritka az ellenőrzés”. |
| H3 | Gyakoriság | (b) havonta ismétlődik a havi ÁFA-bevallók miatt, a 2027-es első eÁFA-ciklusokban pedig megugrik. (d) egyszeri nagy munka (visszamenőleges rendbetétel), utána rendszeres újraszűrés. | (b): havi bevallós ÁFA-alany ügyfelek aránya ≥ 30%. (d): az alany meg tudja becsülni, hány akta hiányos. | (b): az ügyfelek többsége negyedéves/éves bevalló vagy alanyi mentes (ritka feladat). (d): kevés jogi személy ügyfél, egyszerű tulajdonosi szerkezetek. |
| H4 | Jelenlegi megoldás | Ma Excelben, a könyvelőprogram listáiban és szemmel egyeztetnek. A megoldás személyhez kötött és nem dokumentált. | Leírnak egy kézi lépéssort (letöltés, Excel, összefésülés, jegyzet), amely ügyfelenként 20+ percet visz el. | Már van automatizált megoldásuk, amellyel elégedettek (Kulcs Connect, Zeuss bankpárosítás, saját makró), vagy a programjuk beépített egyeztetője elég. |
| H5 | Időráfordítás | Egy 5 fős, kb. 200 ügyfeles irodában (b) havi 20–60 munkaórát visz el (saját becslés: 0,5–1,5 óra × ÁFA-s ügyfél). | Az alany becslése és egy konkrét elmúlt hónap rekonstrukciója egyaránt havi ≥ 15 órát ad. | Havi < 5 óra az egész irodára, vagy nem tudják megbecsülni, mert nem tűnik fel. |
| H6 | Fizetési hajlandóság | (b) esetén fix 300–600 ezer Ft bevezetés + 300–800 Ft/ÁFA-s ügyfél/hó, (d) esetén 2–5 ezer Ft/ügyfél egyszeri rendbetétel + havi újraszűrési díj elfogadható ár egy 3–25 fős irodának. **(Saját árhipotézis, nincs mögötte magyar adat.)** | Legalább 3 iroda vállal 4–5. szintű elköteleződést (szándéknyilatkozat árral vagy fizetett pilot) ebben az ársávban. | Az árhorgonyra mindenhol az ÜgyfélSegéd/Zeuss árszintjére (havi néhány tízezer Ft) hivatkoznak, vagy csak ingyenes pilotra nyitottak. |
| H7 | Döntéshozó | A 3–25 fős irodákban a tulajdonos-ügyvezető egyedül, 2–4 héten belül dönt egy havi 100 ezer Ft alatti eszközről. | Az alany elmond egy konkrét múltbeli vásárlást (szoftver, képzés), amelyről ő döntött, és amelynek az átfutása rövid volt. | Társtulajdonosi vagy könyvvizsgálói jóváhagyás kell, illetve a beszerzés 2–3 hónap, vagy „év elején szoktunk dönteni”. |
| H8 | Szoftverkörnyezet | A helyi irodák többsége asztali könyvelőprogramot használ (RLB-60, Novitax, Kulcs-Soft, Infotéka, Forint-Soft, Tensoft). Ezekből a főkönyv és az ÁFA-analitika fájlba (DBF/CSV/XML/XLSX) exportálható, így API nélkül is lehet integrálni. | A mintában ≥ 2 program a teljes minta ≥ 60%-át fedi le, és az exportot az alany meg tudja mutatni. | Szétszórt szoftverpark (5+ program, mind kis részaránnyal), vagy az export nem elérhető vagy nem használható. |
| H9 | Időzítés | Október–novemberben még hajlandók eszközt bevezetni az eÁFA előtt. Decembertől februárig nem. | Konkrét novemberi időpontot adnak egy próbafuttatásra (például a novemberi bevallásra, decemberi határidővel). | „Majd az első eÁFA-hónapok után”, „januárban már nem fogok új dolgot tanulni”: ekkor az ajánlatot 2027 február–áprilisra kell időzíteni (lásd 8.4). |
| H10 | Alternatíva és versenytárs | A helyi irodák többsége nem használ ÜgyfélSegédet, Zeusst, Optimatót vagy identiGO-t. A szolgáltatásalapú („megcsináljuk helyetted”) modellre van igény a SaaS-szal szemben. | A minta < 30%-a használ ilyen eszközt, és a nem használók indoka „nincs időm bevezetni” vagy „nem ismerem”, nem az, hogy „nincs rá szükség”. | A minta többsége már használ ilyet és elégedett, vagy kifejezetten önkiszolgáló, olcsó eszközt keres. |
| H11 | Csatorna és bizalom | A meleg bemutatás legalább háromszor akkora arányban hoz interjút, mint a hideg megkeresés, és a helyi jelenlét előny. | Meleg megkeresésből ≥ 50%, hidegből ≤ 15% interjúarány; az alanyok említik, hogy számít a helyi jelenlét. | Nincs különbség, vagy a helyi jelenlét senkinek nem szempont. Ekkor az országos, online értékesítés is opció. |
| H12 | (a) kontroll | A dokumentumbekérés fáj, de önálló termékként nem fizetnének érte többet egy SaaS árszintjénél. | Ha (a) a legnagyobb fájdalom, de az árhorgonyra a SaaS-szintet mondják, akkor (a) csak integrációként vagy viszonteladásként jöhet szóba. | Ha (a)-ért kifejezetten szolgáltatásként (bevezetéssel, Viber/WhatsApp-csatornával) magas árat is vállalnának, akkor (a) visszakerül a lehetséges első ajánlatok közé. |

**Bizonyíték-hierarchia (a Mom Test szerint):** a múltbeli viselkedés (mit csináltak, mennyi ideig tartott, mire költöttek) erősebb a véleménynél („jó ötlet”). Az elköteleződés (idő, adat, pénz) pedig erősebb mindkettőnél. Bók, „érdekes” vagy „szóljanak, ha kész” **nem bizonyíték**.

---

## 2. Mintavétel

### 2.1 Létszám

- **Cél: 18 interjú** könyvelőirodákkal (minimum 15, maximum 20). Ennél több interjú ritkán ad új mintázatot; ha 12–15 után már nem hallunk újat, megállhatunk.
- **Plusz 2–3 szakértői vagy multiplikátor-beszélgetés**, ezeket külön értékeljük, nem számítanak a kvótába:
  - a RÓ Könyvelőiroda tulajdonosa (MinKE digitalizációs munkacsoport, `prospects_county.md`);
  - egy könyvelőprogram helyi viszonteladója vagy oktatója (integráció, export);
  - CSMKIK vagy MKOE-kapcsolat (rendezvény, csatorna).
- Ahol lehet, az irodán belül két szerepet is meghallgatunk: **a tulajdonost** (döntés, költségkeret) és **a vezető könyvelőt** (aki a munkát ténylegesen végzi). Ez lehet egy közös 45 perc vagy egy 15 perces második beszélgetés.

### 2.2 Szegmenskvóták

A kvóták átfedhetnek: egy iroda lehet egyszerre „3–9 fős, vármegyei, agrár, hagyományos”. A besorolás a prospect-jegyzetek alapján **előzetes**, és snippetadatokra épül. Az interjú után a valós adatok alapján újra kell sorolni.

| Dimenzió | Szegmens | Kvóta (18-ból) | Miért |
|---|---|---|---|
| Méret | Egyéni / 1–2 fő | 3–4 | Kontrollcsoport: ők a legkevésbé valószínű vevők, de a megye nagy része ilyen. |
| | 3–9 fő | 9–10 | Fő célszegmens, gyors tulajdonosi döntés. |
| | 10–25 fő | 4–5 | A legnagyobb fájdalom és költségkeret, de lassabb döntés. |
| Földrajz | Szeged (beleértve a szegedi irodából dolgozó bordányi/szatymazi székhelyűeket) | 11–12 | Pilothoz személyes jelenlét kell. |
| | Vármegye (Hódmezővásárhely, Makó, Szentes, Csongrád, Algyő, Felgyő stb.) | 6–7 | Más ügyfélkör, gyakran agrár, kevésbé digitális. |
| Ügyfélkör | Agrár / őstermelő fókuszú | legalább 3 | Más ÁFA-helyzet (kompenzációs felár, őstermelők), más dokumentumfolyam. |
| | Jogi személy ügyfelek túlsúlya (Kft./Bt.) | legalább 8 | (d) szempontjából: tényleges tulajdonos, céges iratok. |
| Digitalizáltság | Digitálisan fejlett (portál, papírmentes, távkönyvelés) | 5–6 | Gyorsabb bevezetés. Kérdés, hogy már megoldották-e. |
| | Hagyományos (papíralapú, személyes átadás) | 5–6 | A legtöbb kézi munka, de lassú bevezetés. |
| Különleges | Idegen nyelvű ügyfélkör (kínai, szerb, német, angol/román) | 1–2 | Résajánlat-vizsgálat (többnyelvű ügyfélkommunikáció). |

### 2.3 A top 20 lista használata

Forrás: `reports/Könyvelőirodák top 20 lista.md`, két hullámra bontva (1. hullám: 8 iroda, 2. hullám: 12 iroda), plusz a „Kimaradtak, de figyelendők” szakasz.

**Lépések:**

1. **Ellenőrzés (1. hét):** a lista „Ellenőrzési teendők” pontjai szerint e-cegjegyzek.hu, opten/nemzeticegtar, saját honlap, aktív-e az álláshirdetés. A névrokon-gyanús irodákat (Stabil Kontír, Prémium Audit, Tabula Rasa, Kalkulus, JOY'S UNITED, SZETAX) megkeresés előtt tisztázni kell.
2. **Meleg kapcsolat feltérképezése:** az értékesítő a 20 iroda mellé beírja, kit ismer, aki ismeri az iroda vezetőjét, vagy ügyfele az irodának. Ez lesz a „Meleg út” oszlop a toborzási táblában (lásd 3.1).
3. **Kvótához rendelés** (előzetes besorolás a prospect-jegyzetek alapján):

| Szegmens | Jelöltek a top 20-ból | Tartalék a jegyzetekből |
|---|---|---|
| 3–9 fő, Szeged | KADMIN PLUS, Dr. Szetei, TOP CONTROLL, EU-TAX, Tabula Rasa, Prémium Audit, JOY'S UNITED, SZETAX, FRAME | ENTER 92., V-2, Vizsu-Tax, ANGEL Consulting |
| 10–25 fő | GoldenEggs, ADÓKONTÓ 2000, Stabil Kontír (ellenőrizendő), Kalkulus (honlap szerint 15 fő) | – |
| 3–9 fő, vármegye | RÓ Könyvelőiroda, Professional Analysis, Ancsi (Algyő) | AB-LF Controlling, KWOTAX, Quaestura, Kyra-Tax |
| Egyéni / 1–2 fő | StaBILL, City Tax (registry: 1 fő), Papír mentes könyvelő | CONTADOR PLUSZ, Kutás Vanda, E-Adat, Meridián '97 |
| Agrár | Professional Analysis, StaBILL | AB-LF, Kutás Vanda, BA Kontír |
| Digitálisan fejlett | EU-TAX, TOP CONTROLL, KADMIN PLUS, RÓ, Papír mentes könyvelő | V-2, FRAME |
| Hagyományos | FRAME (elavult honlap), City Tax | ANGEL Consulting, LIBRA Account-Team, Meridián '97 |
| Jogász a csapatban (d) | Law & Balance, Kalkulus | – |
| Idegen nyelvű ügyfélkör | JOY'S UNITED (kínai), StaBILL (szerb) | E-Adat (angol/román), Vizsu-Tax, ANGEL (német) |

4. **Hullámok:** először az 1. hullám 8 irodája (a meleg utak elsőbbséget kapnak), majd a 2. hullám. A kvótahiányokat (jellemzően: egyéni, hagyományos, agrár) a tartaléklistából töltjük fel.
5. **Tölcsér-matek (feltételezés, az első két hét után korrigálandó):** meleg megkeresésnél kb. 50–60%, hidegnél kb. 10–15% interjúarány. 18 interjúhoz kb. **20 meleg + 40 hideg** megkeresés kell. Ha a top 20 + tartalék nem elég, a CSMKIK könyvelői adatbázisa és a Könyvelő Tudakozó vármegyei listája a bővítés forrása, de csak az irodák üzleti elérhetőségeivel (lásd 3.4).

---

## 3. Toborzás

### 3.1 Sorrend és csatornák

1. **Meleg bemutatás az értékesítő hálózatán keresztül (elsődleges).** Két típusa van:
   - közös ismerős, aki személyesen ismeri az iroda vezetőjét;
   - ismerős vállalkozó, aki **ügyfele** az irodának. Ez a legerősebb út, de vigyázni kell, hogy az ügyfél ne érezze kínosnak.

   Az értékesítő megkéri az ismerőst, hogy továbbítsa a lenti rövid szöveget, vagy kérdezze meg, adhatja-e a számát.
2. **Szakmai szervezetek és közösségek:**
   - **Minősített Könyvelők Egyesülete (MinKE/MKK):** a RÓ Könyvelőiroda tulajdonosán keresztül, aki a jegyzetek szerint az egyesület digitalizációs munkacsoportjában dolgozik. Kérés: interjú, és ha hasznosnak tartja, ajánlás 2–3 kollégának.
   - **MKOE (Magyar Könyvelők Országos Egyesülete):** titkarsag@mkoe.hu, 06 1 336 7000. Kérdés: van-e Csongrád-Csanád vármegyei csoport vagy helyi összejövetel. A jegyzetekben nem találtunk ilyet.
   - **CSMKIK (Csongrád-Csanád Megyei Kereskedelmi és Iparkamara):** a kamara „Digitális ébresztő” rendezvényeket tart, és van könyvelői adatbázisa (csmkik.hu). A jegyzetekben cskik.hu és csmkik.hu is szerepel; a hivatalos elérhetőséget ellenőrizni kell. Kérés: egy rövid, **gyakorlati, nem értékesítő** „eÁFA + Pmt. felkészülés” reggeli vagy előadás november első felében, ahol interjúalanyokat is toborozhatunk.
3. **Facebook-csoportok:**
   - **Könyvelők klubja** (zárt, 5000+ tag), Könyvelő kAPPtár, Egy könyvelő élete.
   - A szakmai csoportok szabályai gyakran tiltják a szolgáltatói posztokat. **Posztolás előtt** az adminisztrátortól engedélyt kell kérni, és csak kutatási felhívást teszünk ki, értékesítést nem (lásd 3.3 E sablon).
   - Az országos csoportokból jellemzően nem szegedi alanyok jönnek. Belőlük legfeljebb 2–3-at vonjunk be kontrollként, a kvótán felül.
4. **Hideg megkeresés** az iroda honlapján közzétett általános üzleti e-mail-címre vagy kapcsolati űrlapra, illetve LinkedIn-üzenetben a cég vezetőjének. Rövid, személyre szabott üzenet, kétszeri utánkövetéssel.
5. **Telefon:** csak a cég által közzétett irodai számon, hétfőtől csütörtökig 9 és 11 között, a havi határidőkön kívül (lásd 9. fejezet).

**Kerülendő:** a KATTexpo és az iBookr/Zeuss csatornái, mert versenytárs szervezi őket. Megfigyelőként mehetünk, toborozni ott ne toborozzunk.

### 3.2 A köszönet (amit cserébe adunk)

Kicsi, hasznos, nem pénzbeli ajándék. Készítsük el az első héten:

- **„eÁFA-felkészültségi ellenőrzőlista” (1–2 oldal, PDF).**
  - **Tartalom:** a NAV nyilvános tájékoztatói alapján lépések, határidők és gyakori eltéréstípusok. Ilyenek a NAV Online Számla és az ÁFA-analitika közötti eltérések, a soronkénti adókód, az M2M 2.0 XSD 2026. augusztus 3-tól, a decemberi bevallás 2027. január 20-ig eÁFA-ban, és a nyugtaadat-szolgáltatás szankciói 2027. január 1-jétől.
  - **Kötelező lábjegyzet:** „Tájékoztató jellegű, nem adótanácsadás; forrás: NAV, dátum.”
  - Kiküldés előtt nézesse át egy, a hálózatból ismert mérlegképes könyvelő vagy adószakértő.
- **„Mit láttunk N szegedi irodánál” anonimizált összefoglaló** (2–3 oldal) a kutatás végén, december elején. Benne: időráfordítások, eszközök, gyakori problémák. Irodát, személyt vagy ügyfelet nem azonosítunk benne.
- Opcionálisan: a CSMKIK-előadásra szóló meghívó.

Ne adjunk pénzt, vásárlási utalványt vagy „ingyenes pilotot” az interjúért cserébe. Ez torzítja a választ, és az ingyenes pilot a fizetési hajlandóság mérését is tönkreteszi.

### 3.3 Üzenetsablonok

A könyvelők átlagéletkora kb. 51–52 év (`accounting_deep_dive.md`), ezért hidegben **magázunk**. Melegben az ismerős stílusát követjük. A [szögletes zárójeles] részeket személyre kell szabni. Minden üzenetben benne van, hogy **interjú, nem értékesítés**, és hogy mennyi időről van szó.

#### A) Meleg bemutatás: az értékesítő üzenete a közös ismerősnek

> Szia [Név]!
>
> Kérnék tőled egy kis szívességet. [Fejlesztő neve] kollégámmal szegedi könyvelőirodákat kérdezünk meg arról, hogyan készülnek az eÁFA-ra (januártól megszűnik az ÁNYK) és a pénzmosási szabályok idei változására. Most még nem árulunk semmit, egyszerűen meg akarjuk érteni, mi viszi el a legtöbb időt egy irodában.
>
> Úgy tudom, jól ismered [Iroda vezetőjének neve]-t a [Iroda neve]-ből. Továbbítanád neki az alábbi pár sort, vagy megkérdeznéd, felhívhatom-e? Kb. 45 perc lenne, nálunk egy kávé mellett vagy online, ahogy neki kényelmes.
>
> Köszönöm előre is!
> [Értékesítő neve]

**Továbbítható rövid szöveg (a közös ismerős küldi tovább):**

> Kedves [Név]!
>
> [Értékesítő neve] és [Fejlesztő neve] szegedi cégük nevében könyvelőirodákat kérdeznek arról, hogyan zajlik náluk a havi ciklus, az eÁFA-felkészülés és az ügyfélátvilágítás. **Nem értékesítenek, interjút kérnek**, kb. 45 percben, egy Önnek alkalmas időpontban, október–november folyamán. Cserébe egy eÁFA-felkészültségi ellenőrzőlistát és a kutatás anonim összefoglalóját küldik el. Ha belefér, szívesen megadom az elérhetőségüket: [telefon / e-mail].

#### B) Hideg e-mail (az iroda általános címére)

**Tárgy:** 45 perc az eÁFA-átállásról, interjú, nem értékesítés

> Tisztelt [Név / Iroda neve]!
>
> [Értékesítő neve] vagyok, egy szegedi cég egyik alapítója. Társammal, [Fejlesztő neve] informatikussal azt vizsgáljuk, hogyan dolgoznak a szegedi és Csongrád-Csanád vármegyei könyvelőirodák az ÁNYK megszűnése (2026. december 31.) és a 2027-es eÁFA-bevezetés előtt, és mennyi munkát ad a pénzmosás elleni törvény idei módosítása.
>
> **Nem értékesíteni szeretnénk**, hanem tanulni. Egy kb. 45 perces beszélgetést kérnénk az irodában vagy online, az Önnek megfelelő időpontban, lehetőleg a havi határidőkön kívül. Arról kérdeznénk, hogyan zajlik a havi munka, és mi viszi el a legtöbb időt.
>
> Köszönetképpen elküldjük az eÁFA-felkészültségi ellenőrzőlistánkat, és ha kéri, a kutatás végén (december elején) a szegedi irodák tapasztalatainak névtelen összefoglalóját is.
>
> Ha nyitott rá, kérem, jelezzen vissza egy-két alkalmas időpontot, vagy hívjon a [telefonszám] számon.
>
> Tisztelettel:
> [Értékesítő neve]
> [Kft. neve] · [telefon] · [web, ha van]
>
> *Az Ön elérhetőségét az iroda honlapjáról vettük. Ha nem szeretne további üzenetet kapni tőlünk, elég egy rövid válasz, és töröljük.*

#### C) LinkedIn- vagy Facebook-üzenet (rövid, egy vezetőnek)

> Jó napot, [Név]!
>
> Szegedi cégünkkel azt kutatjuk, hogyan készülnek a helyi könyvelőirodák az eÁFA-ra és a Pmt. idei változásaira. Nem értékesítünk: egy 45 perces interjút kérnénk, október–novemberben, Önnek alkalmas időpontban. Cserébe eÁFA-felkészültségi ellenőrzőlistát és a kutatás anonim összefoglalóját adjuk. Belefér egy beszélgetés?
>
> [Név], [Kft.]

#### D) Utánkövetés (5–7 munkanap múlva, legfeljebb kétszer)

> Tisztelt [Név]!
>
> Csak röviden visszajeleznék a [dátum]-i levelemre a 45 perces eÁFA- és Pmt.-interjúval kapcsolatban. Tudom, hogy a hónap közepe a bevallások miatt zsúfolt, ezért a hónap utolsó hetében vagy a következő hónap elején is szívesen jövünk, akár 30 percre rövidítve.
>
> Ha most nem aktuális, azt is megköszönöm, ha jelzi. Akkor nem zavarjuk tovább.
>
> Üdvözlettel:
> [Név]

#### E) Facebook-csoportba (csak adminisztrátori engedéllyel)

> Sziasztok! Szegedi kis cégünkkel kutatást végzünk könyvelőirodák körében: hogyan zajlik a havi ciklus, mennyi idő megy el a NAV–bank–főkönyv egyeztetésre, és hogyan készültök az eÁFA-ra és a Pmt. idei változásaira. **Nem értékesítünk**, 45 perces (online is lehet) beszélgetésre keresünk irodavezetőket, elsősorban Csongrád-Csanádból. Köszönetképpen eÁFA-felkészültségi ellenőrzőlistát és a kutatás anonim összefoglalóját küldjük. Ha érdekel, írj privátban! (A posztot [admin neve] engedélyével tettem ki.)

#### F) Köszönőlevél az interjú után (24 órán belül)

> Kedves [Név]!
>
> Köszönjük a mai beszélgetést, nagyon sokat tanultunk belőle, különösen [egy konkrét dolog, amit mondott]. Mellékelten küldöm az ígért eÁFA-felkészültségi ellenőrzőlistát. A kutatás anonim összefoglalóját december elején küldjük.
>
> [Ha megállapodtunk következő lépésben:] Ahogy megbeszéltük, [dátum]-án jelentkezünk a [következő lépés] ügyében.
>
> Üdvözlettel:
> [Név]

### 3.4 Adatvédelmi óvatosság a toborzásnál

- **A könyvviteli szolgáltatók nyilvántartásából (PM-névjegyzék, XLS) ne küldjünk tömeges e-mailt, és ne telefonáljunk végig a listán.** A névjegyzék természetes személyek adatait tartalmazza (cím, telefon). A NAIH állást foglalt a nyilvánosság korlátairól, és a közvetlen megkeresés jogalapja (jogos érdek) kétséges. A névjegyzék legfeljebb arra használható, hogy megbecsüljük a vármegyei könyvelők számát, vagy ellenőrizzük, regisztrált-e valaki.
- **Csak üzleti elérhetőséget használjunk:** az iroda honlapján, cégjegyzékben vagy kamarai adatbázisban közzétett általános e-mail-címet, kapcsolati űrlapot, irodai telefonszámot, LinkedIn-profilt.
- **Gazdasági reklám:** természetes személynek küldött közvetlen üzleti ajánlathoz előzetes hozzájárulás kellhet (Grt.). A kutatási felkérés nem reklám, de **ne csempésszünk bele ajánlatot**, és minden hideg üzenetben legyen leiratkozási lehetőség.
- A meleg bemutatásnál az ismerős adja meg a kapcsolatot, vagy kérdezi meg előbb az érintettet. Adatot ne kérjünk ki a háta mögött.
- A toborzási táblát (név, iroda, elérhetőség, státusz) korlátozott hozzáférésű helyen tároljuk, és a kutatás végén töröljük azok adatait, akik nem kértek további kapcsolatot.

**Toborzási tábla (oszlopok):** iroda · top 20 #/hullám · szegmens(ek) · kapcsolattartó (szerep) · meleg út (ki ismeri) · csatorna · 1. megkeresés dátuma · 1. utánkövetés · 2. utánkövetés · státusz (nincs válasz / elutasította / időpont / kész) · interjú dátuma · interjúkód (I-01…).

---

## 4. Az interjú lebonyolítása

### 4.1 Előkészítés (alanyonként kb. 20 perc)

- Az iroda ellenőrzött adatai: létszám, árbevétel, ügyfélkör, honlap, álláshirdetés, fizetett-e már valamilyen eszközért, ha ez látszik.
- Két előzetes kérdés az alanynak (opcionális, e-mailben): kb. hány ügyfél, és milyen könyvelőprogram. Ez spórol 5 percet.
- Kinyomtatott kérdéssor (5. fejezet), jegyzetsablon (7. fejezet), a (b) és (d) egyoldalas makettje egy mappában (6. fejezet). **A makettet csak a végén vesszük elő.**
- Adatkezelési tájékoztató egy rövid bekezdésben (lásd 10.3), és a hozzájárulás a hangfelvételhez.

### 4.2 Szerepek

| Szerep | Ki | Feladat |
|---|---|---|
| **Kérdező (moderátor)** | Az **értékesítő** az első 5 interjúban (ő hozza a kapcsolatot és a bizalmat) | Vezeti a beszélgetést, tartja az időt, mélyít („mesélje el a legutóbbit”), és nem árul. |
| **Jegyzetelő + technikai mélyítő** | A **fejlesztő** | Szó szerinti idézeteket ír, számokat rögzít (óra, darab, Ft). A **szoftver- és integrációs blokkot ő kérdezi** (export, formátum, NAV technikai felhasználó). A végén összefoglalja, mit hallott. |
| Szerepcsere | A 6. interjútól | A szerepek felváltva mennek, hogy mindketten megtanulják a másik részét. Az értékesítő akkor se kezdjen bele ajánlatba, ha ő jegyzetel. |

Szabály: **egyszerre egy ember kérdez.** A jegyzetelő csak a blokkok végén szól közbe, egy-egy pontosító kérdéssel.

### 4.3 Hozzájárulás a felvételhez

A beszélgetés elején, a felvétel elindítása előtt:

> „Ha nem bánja, felvennénk a beszélgetést, hogy ne kelljen mindent jegyzetelnünk. A felvételt csak mi ketten hallgatjuk meg, legfeljebb 30 napig tároljuk, utána töröljük, és amit idézünk, név nélkül idézzük. Ügyféladatot, nevet, adószámot kérem, ne mondjon. Ha bármikor kikapcsolnánk, csak szóljon. Rendben van így?”

- A hozzájárulás tényét a felvétel elején még egyszer mondjuk ki („Ön hozzájárult a felvételhez, ugye?”), és írjuk be a jegyzetbe is.
- Ha nemet mond, csak jegyzetelünk. Ez is teljesen rendben van.
- Ha AI-alapú leiratkészítőt használunk, ezt mondjuk meg, és olyan szolgáltatást válasszunk, amely nem tanít a felvételen, és EU-ban tárol (lásd 10.3).

### 4.4 Mom Test-alapelvek a gyakorlatban

1. **Az ő életükről beszélünk, nem az ötletünkről.** Az első 35 percben nem mondjuk ki, hogy mit szeretnénk építeni.
2. **Múlt, nem jövő:** konkrét eseteket kérdezünk („a legutóbbi alkalommal…”), nem véleményt vagy feltételezést („használná-e…?”).
3. **Számokat kérünk:** óra, ügyfélszám, alkalom, forint. Ha nem tudja, rekonstruáljuk vele együtt („az októberi ÁFA-zárásnál ki mit csinált, hány órát?”).
4. **Bókot nem gyűjtünk.** Ha azt mondja, „ez nagyon jó ötlet lenne”, visszakérdezünk: „Mit próbált eddig ennek a megoldására?”
5. **Keressük a pénzt és az időt, amit már elköltött a problémára.** Ha semmit nem költött rá és nem keresett megoldást, valószínűleg nem fáj eléggé.
6. **Csendet hagyunk.** A legjobb válaszok a második szünet után jönnek.
7. **Nem adunk tanácsot és nem vitatkozunk.** Különösen adókérdésben nem (lásd 10. fejezet).

**Rossz kérdés helyett jó kérdés:**

| Kerülendő | Helyette |
|---|---|
| „Használna egy eszközt, ami eÁFA előtt kilistázza az eltéréseket?” | „Az utolsó ÁFA-bevallás előtt hogyan derült ki, hogy valami nem stimmel a NAV-adatokkal? Mesélje el lépésről lépésre!” |
| „Fontos Önnek az ügyfélátvilágítás?” | „Mikor nézték át utoljára az összes ügyfél Pmt.-aktáját? Ki csinálta, mennyi ideig tartott?” |
| „Mennyit fizetne érte?” | „Mire költött az elmúlt egy évben szoftverre, képzésre, külső segítségre? Kb. mennyit?” |
| „Problémát jelent a dokumentumbekérés?” | „Az elmúlt hónapban hány ügyfélnél kellett háromszor vagy többször szólni a hiányzó számlákért?” |
| „Gondolja, hogy az AI segíthetne?” | „Ha holnaptól lenne egy plusz embere heti 10 órára, mit adna neki először?” |

### 4.5 45 perces menetrend

| Idő | Blokk | Ki kérdez | Cél |
|---|---|---|---|
| 0:00–0:03 | Bemutatkozás, cél („tanulni jöttünk, nem árulni”), felvétel engedélyezése | Moderátor | Bizalom, keretek |
| 0:03–0:07 | **A** Iroda profilja | Moderátor | Szegmentálás: létszám, ügyfélszám, ügyfélkör |
| 0:07–0:15 | **B** Havi ciklus és időráfordítás + **C** Dokumentumbekérés | Moderátor | Hol megy el az idő? (a) kontroll |
| 0:15–0:23 | **D** NAV–bank–főkönyv egyeztetés + **E** eÁFA-felkészülés | Moderátor | (b) fájdalom, gyakoriság, megoldás |
| 0:23–0:29 | **F** Pmt./AML ügyfélátvilágítás | Moderátor | (d) fájdalom |
| 0:29–0:31 | **G** Ügyfélkommunikáció (röviden) | Moderátor | Csatornák, kérdések |
| 0:31–0:35 | **H** Szoftverek és integrációk + **I** Korábbi próbálkozások | **Fejlesztő** | Integrációs valóság, versenytársak |
| 0:35–0:38 | **J** Döntéshozatal és költségkeret | Moderátor | Ki, mennyiből, mikor |
| 0:38–0:43 | **Opcionális megoldás-próba és elköteleződés-kérés** (6. fejezet), *vagy* mélyítés a legnagyobb fájdalomnál | Moderátor | Reakció, következő lépés |
| 0:43–0:45 | **K** Zárás | Moderátor | Ajánlás, köszönet, következő lépés |

**Gyakorlati tippek:**
- Ha az alany 30 percet ad, a G és az I blokk kimarad, a megoldás-próba pedig egy külön, második találkozóra kerül.
- Ha 60 percet ad, a megoldás-próba 10 percre bővülhet. Ezt a változatot érdemes kérni, ha az első 35 percben magas fájdalom jött elő.
- **Közvetlenül az interjú után** a két alapító 15 percben átbeszéli és kitölti a jegyzetsablont és a pontozást (7. fejezet). A memória 24 óra alatt sokat veszít.

---

## 5. Kérdéssor

Jelölések: **Fő kérdés** (mindig feltesszük), *mélyítő kérdés* (ha van idő vagy érdekes a válasz), **Piros zászló** (a hipotézis ellen szóló vagy figyelmeztető válasz). A számokat mindig kérjük.

### A) Az iroda profilja (3–4 perc)

1. **Hány fővel dolgoznak, és ki mit csinál?** (tulajdonos, könyvelők, bérszámfejtő, adminisztrátor)
2. **Kb. hány ügyfelük van? Ebből hány Kft./Bt., egyéni vállalkozó, KATA-s, őstermelő, egyéb?**
3. **Hány ügyfél ÁFA-alany, és ebből hány havi bevalló?**
   - *Mélyítés:* „Van-e sok külföldi vagy idegen nyelvű ügyfél? Agrárügyfelek?”
   - *Mélyítés:* „Hogyan változott az ügyfélszám az elmúlt 2 évben? Vállalnának több ügyfelet, ha bírnák?”
4. *Mélyítés:* „Keresnek most munkatársat? Mióta? Mennyire nehéz könyvelőt találni Szegeden?”

**Piros zászló:** kevesebb mint 20 ÁFA-s ügyfél, szinte csak alanyi mentes vagy KATA-s ügyfélkör. Ekkor (b) gyenge, (d) is kicsi.

### B) A havi ciklus és az időráfordítás (4 perc)

5. **Vegyük végig a múlt hónapot! Mi történt az 1-jétől a hónap végéig? Mikor van a legnagyobb nyomás?**
   - *Mélyítés:* „Mi történik a 12-éig (bérek, járulékok) és a 20-áig (ÁFA)? Hol szokott csúszni?”
6. **Ha a havi munkaidőt 100%-nak vesszük, nagyjából mennyi megy el a dokumentumok begyűjtésére, a rögzítésre és kontírozásra, az egyeztetésre (bank, NAV), a bevallásokra, a bérszámfejtésre és az ügyfélkérdésekre?**
   - *Mélyítés:* „Melyik az, amit a legszívesebben kiadna a kezéből? Miért?”
   - *Mélyítés:* „Ha holnaptól lenne egy plusz embere heti 10 órára, mit adna neki először?”
7. *Mélyítés:* „Mennyi túlórával jár egy átlagos hónap? És a január?”

**Piros zászló:** „nálunk minden rendben van, nincs csúszás”, és nem tud konkrét szűk keresztmetszetet mondani. Ilyenkor vagy tényleg rendben van, vagy nem a döntéshozóval beszélünk.

### C) Dokumentumbekérés (a kontroll) (3–4 perc)

8. **Hogyan kapják meg a számlákat és a bankkivonatokat az ügyfelektől? Milyen csatornán?** (e-mail, portál, Viber/WhatsApp, személyesen, papíron)
9. **Az elmúlt hónapban az ügyfelek kb. hány százaléka küldött hiánytalanul a határidőig? Hányszor kellett szólni a többieknek?**
   - *Mélyítés:* „Ki szól nekik, és hogyan? Mennyi idő ez havonta?”
   - *Mélyítés:* „Honnan tudják, hogy valami hiányzik? Megnézik a NAV Online Számlát?”
10. *Mélyítés:* „Próbáltak már portált vagy automatikus emlékeztetőt? (ÜgyfélSegéd, Zeuss, saját űrlap) Mi lett vele?”

**Piros zászló (a)-ra nézve:** „már ÜgyfélSegédet vagy Zeusst használunk, és működik”. Ez nem rossz hír: a (a) helyett (b)-t vagy (d)-t érdemes vizsgálni náluk, illetve azt, hogy partnerként együttműködhetünk-e az eszközzel.

### D) NAV–bank–főkönyv egyeztetés (4 perc) – a (b) hipotézis magja

11. **Mesélje el, hogyan zajlott az utolsó ÁFA-bevallás előtti ellenőrzés egy tipikus ügyfélnél! Milyen listákat néz meg, és milyen sorrendben?**
    - *Mélyítés:* „Honnan tölti le a NAV Online Számla adatokat? A könyvelőprogramba közvetlenül, vagy kézzel?”
    - *Mélyítés:* „Hogyan veti össze a bankkivonattal? Excelben? Szemmel?”
12. **Milyen eltérések szoktak előjönni?** (NAV-ban van, de nincs a főkönyvben; kifizették, de nincs számla; eltérő ÁFA-kulcs vagy összeg; duplikáció; sztornó; devizás)
    - *Mélyítés:* „Az elmúlt 3 hónapban volt-e olyan, hogy egy eltérés csak a bevallás után derült ki? Mi lett a vége? (önellenőrzés, NAV-levél, bírság)”
13. **Ügyfelenként kb. mennyi időt visz el ez az ellenőrzés egy átlagos hónapban? És a legrosszabb ügyfélnél?**
    - *Mélyítés:* „Ki csinálja? A tapasztalt könyvelő vagy az asszisztens? Le van-e írva valahol, hogyan kell?”
14. *Mélyítés:* „Kaptak-e az elmúlt egy évben NAV-tól eltérésre vagy adatminőségre vonatkozó megkeresést vagy levelet?”

**Piros zászló (b)-re nézve:**
- „A program automatikusan párosít, csak a kivételeket nézem, az pár perc.”
- „Évente egyszer nézzük meg rendesen.”
- Nem tud konkrét eltérést vagy esetet mondani az elmúlt 3 hónapból.

**Zöld jel:** saját Excel-sablon vagy makró, külön ember erre a feladatra, önellenőrzések miatti bosszúság, „mindig a 18–19-én derül ki”.

### E) eÁFA-felkészülés (4 perc)

15. **Hol tartanak az eÁFA-val? Adtak már be eÁFA-n keresztül bevallást, vagy próbálták az eÁFA tervezetet?**
    - *Mélyítés:* „Mit látott, amikor összevetette a NAV-tervezetet a saját analitikájával? Milyen eltérések jöttek ki?”
16. **Mit csinál a könyvelőprogramjuk az eÁFA-hoz?** (ÁFA-analitika előállítása, M2M-feltöltés, frissítés)
    - *Mélyítés:* „Mit mondott a szoftverszállító, mikor lesz kész? Bízik benne?”
17. **Mi a terv a decemberi bevallásra (2027. január 20.)? Mi aggasztja a legjobban?**
    - *Mélyítés:* „Mennyi plusz időre számít a januári első ciklusban? Hogyan fogják megoldani?”
    - *Mélyítés:* „Hogyan készülnek a nyugtaadat-szolgáltatás miatt a kiskereskedő ügyfeleknél?”
18. *Mélyítés:* „Ha az ÁNYK kivezetését elhalasztanák, mit változtatna ez Önöknél?”

**Piros zászló:**
- „A szoftver mindent megold, nem foglalkozunk vele.”
- „Már két hónapja eÁFA-n adunk be, semmi gond.”
- Teljes nyugalom, határidő-érzet nélkül.

Ezek a válaszok (b) sürgősségét gyengítik. Jegyezzük fel azt is, ha az alany a halasztásra vár, mert ez az időzítést befolyásolja.

### F) Pmt./AML ügyfélátvilágítás (5–6 perc) – a (d) hipotézis magja

19. **Hogyan zajlik egy új ügyfél felvételekor az átvilágítás? Mit kérnek be, hol tárolják?** (személyazonosító okmány, tényleges tulajdonosi nyilatkozat, cégkivonat, kockázati besorolás)
20. **Mikor nézték át utoljára a meglévő ügyfelek aktáit? Mi derült ki?**
    - *Mélyítés:* „Az ügyfelek kb. hány százalékánál hiányos valami? (lejárt okmány, hiányzó nyilatkozat, változott tulajdonos)”
    - *Mélyítés:* „Az idei módosítás után (2026. január) végeztek-e szankciólistás újraszűrést a teljes ügyfélkörön? Hogyan?”
21. **Volt-e Pmt.-ellenőrzésük, vagy hallottak kollégától ellenőrzésről, bírságról? Mi volt a tapasztalat?**
22. **Ki felel az irodában a Pmt.-ért? Mennyi idő megy el erre havonta, illetve egy alkalommal?**
    - *Mélyítés:* „Használnak sablont vagy eszközt? (MinKE-segédlet, identiGO, saját Excel, ügyvéd)”
    - *Mélyítés:* „Mennyit költöttek rá az elmúlt egy évben? (szabályzat, képzés, szoftver)”
23. *Mélyítés:* „Ha holnap jönne egy ellenőrzés, mennyire nyugodtan nyitná ki az aktákat?” (1–5)

**Piros zászló (d)-re nézve:**
- „identiGO-t használunk, minden rendben”.
- Kevés jogi személy ügyfél.
- „Ez csak papírmunka, senki nem ellenőrzi.” Közöny: nem tart a bírságtól, és nem költött rá semmit.

**Zöld jel:** ellenőrzési tapasztalat vagy kolléga bírsága, hiányzó újraszűrés, „ezt tavasszal rendbe akartuk tenni, de nem jutott rá idő”.

### G) Ügyfélkommunikáció (2 perc)

24. **Milyen csatornákon keresik Önöket az ügyfelek? (telefon, e-mail, Viber, WhatsApp, Messenger) Hány megkeresés jön egy átlagos héten?**
    - *Mélyítés:* „Milyen kérdések ismétlődnek? (KATA 2027, bérkedvezmények, eÁFA, nyugta)”
    - *Mélyítés:* „Ki válaszol? Mennyi idő ez hetente?”

**Piros zászló:** „ritkán keresnek, és a telefon a megszokott”. Ez a (c) ügyfélkérdés-bot ötletet gyengíti (a fő ajánlatot nem).

### H) Használt szoftverek és integrációk (3 perc, a fejlesztő kérdez)

25. **Milyen könyvelőprogramot használnak, melyik verziót, helyben vagy felhőben?** (RLB-60, Novitax NTAX/TAXA, Kulcs-Könyvelés, Infotéka, Forint-Soft, Tensoft, SMARTBooks, egyéb)
26. **Hogyan jön be a NAV Online Számla adat és a bankkivonat a programba?** (közvetlen NAV-letöltés technikai felhasználóval, fájlimport, PDF-konverter, kézi rögzítés)
    - *Mélyítés:* „Az ügyfelek NAV technikai felhasználóját kezelik-e Önök? Hány ügyfélnél?”
27. **Ki tudják-e exportálni a főkönyvet vagy az ÁFA-analitikát fájlba? Milyen formátumban? Meg tudná mutatni, hol van a menüben?** (ha lehet, képernyőn, ügyféladat nélkül)
28. *Mélyítés:* „Milyen egyéb eszközöket használnak? (Microsoft 365 vagy Google, tárhely, Excel-makrók, Billingo, Számlázz.hu, bankportál, aláírás)”
29. *Mélyítés:* „Ki az irodában az informatikai ügyek felelőse? Van külső informatikus?”

**Piros zászló:**
- Nincs exportlehetőség, vagy az export csak nyomtatható (PDF).
- A tulajdonos szerint „a programhoz senki ne nyúljon”.
- Felhős rendszer, amely zárt, és a szállító nem engedi az adatkiadást.

Ezek az integrációt teszik kockázatossá; a válaszokat szoftverenként összesítjük.

### I) Korábbi próbálkozások eszközökkel (2 perc)

30. **Az elmúlt 2 évben milyen új eszközt vagy szolgáltatást próbáltak ki a munka könnyítésére? Mi lett belőle?**
    - *Mélyítés:* „Mi alapján döntötték el, hogy marad vagy megy? Mennyi ideig tartott a bevezetés?”
    - *Mélyítés:* „Hallottak-e ezekről: ÜgyfélSegéd, Zeuss, Kulcs Connect, Optimato, Acounto, identiGO? Néztek-e valamelyiket?”
31. *Mélyítés:* „Használnak-e ChatGPT-t vagy más AI-eszközt az irodában? Mire? Van-e erre szabály?”

**Piros zászló:** két-három bevezetési kudarc után „soha többé új rendszert” hozzáállás. Ez nem kizáró ok, de ilyenkor csak „megcsináljuk helyetted” modell működhet.

### J) Döntéshozatal és költségkeret (3 perc)

32. **Az utolsó olyan szoftvert vagy szolgáltatást, amiért havidíjat fizetnek, ki választotta ki, és hogyan zajlott a döntés?**
    - *Mélyítés:* „Mennyi ideig tartott az első megkereséstől a szerződésig? Kellett-e társtulajdonos vagy könyvvizsgáló jóváhagyása?”
33. **Kb. mennyit költenek havonta vagy évente szoftverre, képzésre és külső szolgáltatásra összesen?**
    - *Mélyítés:* „Ebből mennyi az, amit az utóbbi egy évben vezettek be?”
34. *Mélyítés:* „Az év melyik szakaszában szoktak ilyenről dönteni? Mikor nem lehet ilyennel megkeresni Önöket?”

**Piros zászló:** „minden ilyet a [külső személy] dönt el”, „év elején, költségvetésből”, „csak ingyenes lehet”.

### K) Zárás (2 perc)

35. **„Mit nem kérdeztünk, amit kellett volna?”** (Gyakran ez hozza a legjobb információt.)
36. **„Kit javasolna még, akivel érdemes beszélnünk? Bemutatna neki?”**
37. **„Visszajöhetünk 2–3 hét múlva, ha lesz mit mutatnunk, és megkérdezhetjük a véleményét?”**
38. Köszönet, az ellenőrzőlista ígérete, a következő lépés dátummal.

### Gyors értelmezési segédlet: piros zászlók összesítve

| Jel | Mit jelent | Teendő |
|---|---|---|
| Csak dicsér, nincs múltbeli példa | Udvariasság, nem fájdalom | Kérjünk konkrét esetet; ha nincs, alacsony fájdalompontszám |
| „Ha kész lesz, szóljanak” | Nincs elköteleződés | 0. szintű elköteleződés, ne számoljuk pozitívnak |
| A szoftver vagy SaaS már megoldja, és elégedett | A probléma megoldott | Partneri lehetőség? Egyébként alacsony illeszkedés |
| „Majd ha az eÁFA lement” | Rossz időzítés, nem hiányzó fájdalom | Időpont 2027 február–áprilisra |
| Nem tud számot mondani (óra, darab) | Nem érzékeli a költséget | Rekonstrukció az elmúlt hónapból; ha így sem, alacsony fájdalom |
| A döntéshozó nincs jelen | A válaszok nem kötelező érvényűek | Kérjünk 15 percet a tulajdonossal |

---

## 6. Opcionális megoldás-próba és elköteleződés-kérés (az utolsó kb. 5–10 perc)

**Csak akkor** vegyük elő, ha az alany az első 35 percben **saját szavaival** magasnak írta le a fájdalmat (b)-nél vagy (d)-nél. Ha nem, a mélyítés folytatódik, és a makettet nem mutatjuk meg. A gyenge fájdalomra mutatott makett csak udvarias dicséretet hoz.

### 6.1 A két egyoldalas makett (az 1–2. héten elkészítendő)

Papíron vagy laptopon, **mintaadatokkal**. Valódi ügyféladatot nem használunk, és nem kérünk.

**(b) „eÁFA előtti kivétellista” (egy oldal)**
- **Mit kap az iroda:** minden havi ÁFA-zárás előtt ügyfelenként egy rövid listát az eltérésekről a NAV Online Számla, a bankkivonat és a főkönyv/ÁFA-analitika között. Csak a kivételek szerepelnek benne, emberi ellenőrzésre jelölve.
- **Példa-táblázat** (fiktív adatokkal), oszlopok: ügyfél · tétel · eltérés típusa (NAV-ban van, főkönyvben nincs / bankban kifizetve, számla nincs / ÁFA-kulcs eltér / duplikáció) · összeg · javasolt teendő · státusz.
- **Hogyan:** a meglévő könyvelőprogram exportjából és a NAV Online Számla adataiból dolgozik, nem kell programot váltani. A bevezetést mi csináljuk.
- **Első futás:** a novemberi bevallásra (decemberi határidő) mint főpróba, élesben a decemberire (2027. január 20., eÁFA).

**(d) „Pmt.-akta rendbetétel és újraszűrés” (egy oldal)**
- **Mit kap az iroda:** egyszeri átvilágítást az ügyfélkör Pmt.-aktáiról (mi hiányzik: tényleges tulajdonosi nyilatkozat, lejárt okmány, kockázati besorolás, utolsó szankciólistás szűrés dátuma), majd rendszeres újraszűrést és hiánylistát, valamint automatikus bekérést az ügyfelektől.
- **Példa-áttekintő** (fiktív): ügyfél · típus · tényleges tulajdonos rögzítve? · okmány érvényes? · kockázati kategória · utolsó szűrés · hiányzó dokumentum.
- **Fontos kitétel a lapon:** az eszköz támogatja, de nem helyettesíti az iroda Pmt.-felelősségét és belső szabályzatát.

### 6.2 A megoldás-próba menete (3–4 perc)

1. „Az elmondottak alapján ezt a két dolgot rajzoltuk fel. Melyik áll közelebb ahhoz, ami Önnél fáj, ha egyik is?”
2. Hagyjuk, hogy ő beszéljen. A kérdések: „Mi hiányzik róla?”, „Mit venne le róla?”, „Mit tenne vele az első héten?”
3. **Ne védjük a makettet.** Ha azt mondja, hogy a programja ezt tudja, kérjük meg, hogy mutassa meg.

### 6.3 Árhorgonyok tesztelése (hipotézisek!)

Az árakat **nem kérdezzük** („mennyit fizetne?”), hanem **kimondjuk, és figyeljük a reakciót**: arckifejezés, „ennyi?”, „ez sok”, csend, vagy összehasonlítás valamivel. Interjúnként **egy** ajánlatot és **egy** árpontot teszteljünk, és az árpontokat forgassuk az interjúk között, hogy összehasonlítható legyen.

| Ajánlat | Árpont A (alacsony) | Árpont B (közép) | Árpont C (magas) | Összevetési horgony, amit ők ismerhetnek |
|---|---|---|---|---|
| (b) Pilot: első 3 ciklus (nov.–jan.), legfeljebb 30 ÁFA-s ügyfél | 150 ezer Ft egyszeri | 250 ezer Ft | 400 ezer Ft | Kb. 4 400 Ft egy könyvelői munkaóra teljes költsége (saját számítás); 1 millió Ft-ig terjedő mulasztási bírság eÁFA-nál (snippet) |
| (b) Folyamatos díj | Bevezetés 300 ezer + 300 Ft/ÁFA-s ügyfél/hó | 450 ezer + 500 Ft | 600 ezer + 800 Ft | ÜgyfélSegéd kb. 100–200 Ft/ügyfél/hó; Zeuss 35 ezer Ft/hó-tól |
| (d) Akta-rendbetétel (egyszeri) | 2 000 Ft/ügyfél | 3 500 Ft/ügyfél | 5 000 Ft/ügyfél | Pmt.-bírság 100 ezer–400 millió Ft (snippet); identiGO (ár ismeretlen) |
| (d) Újraszűrés és hiánylista | 15 ezer Ft/hó | 25 ezer Ft/hó | 40 ezer Ft/hó | Belső munkaóra |
| (d) Pilot | 20 ügyfél aktájának átvilágítása 100 ezer Ft-ért | 150 ezer Ft | – | – |

**Megjegyzés:** az árak saját, nem validált hipotézisek, `accounting_deep_dive.md` 7. fejezete és a stratégiai jelentés (bevezetés 200–800 ezer + havi 50–200 ezer Ft) alapján. Az interjúban **tájékoztató sávként** mondjuk ki („ilyen nagyságrendben gondolkodunk”), ne ajánlatként. Egy 200 ügyfeles irodánál a (b) havidíja 30–80 ügyfélnél kb. 9–64 ezer Ft/hó, ami a SaaS-horgonyok fölött, de a stratégiai sáv alján van. Ha az irodák szerint ez olcsó, emeljük; ha drága, a szolgáltatásmodell nem áll meg.

**Rögzítendő:** az első spontán reakció szó szerint; mihez hasonlította; az elköteleződési lépcső melyik fokára lépett.

### 6.4 Elköteleződési lépcső

A lépcsőn mindig **egy fokkal feljebb** kérünk, mint ahol az alany van. Ha nemet mond, az is adat: rögzítjük az okát.

| Szint | Kérés | Mit ad az iroda | Megfogalmazás |
|---|---|---|---|
| 0 | – | Csak bók vagy „szóljanak, ha kész” | (nem számít elköteleződésnek) |
| 1 | Követő találkozó | 30 perc 2–3 héten belül, **a döntéshozóval** | „Visszajöhetünk [dátum] körül egy félórára, és megmutatjuk, mit raktunk össze az Önök esete alapján?” |
| 2 | Bemutatás | 1–2 kolléga vagy multiplikátor neve, bemutató üzenettel | „Kinek mutatná meg ezt elsőként a szakmában?” |
| 3 | Adatminta vagy munkamegfigyelés titoktartással | Anonimizált export (főkönyv, ÁFA-analitika vagy Pmt.-lista), vagy 1–2 óra, amíg nézzük, ahogy egy ügyfelet végigegyeztetnek | „Titoktartási megállapodás után adna egy anonimizált mintát egy ügyfélről, hogy kipróbáljuk az exportjukon?” |
| 4 | Szándéknyilatkozat (LOI) árral | Aláírt egyoldalas nyilatkozat: „ha X-ig működik Y-on, akkor Z áron bevezetjük” (nem kötelező erejű) | „Ha a próbafuttatás a novemberi bevalláson működik, aláírna egy egyoldalas nyilatkozatot, hogy januártól [ár]-ért használnák?” |
| 5 | **Fizetett pilot** | Megrendelés, előleg vagy díjbekérő kifizetése | „A pilot díja [ár], novemberben indulunk, és a januári bevallásig tart. Mehet a megrendelő?” |

Az 5. szint a legerősebb jel, a 4. szint a döntés küszöbe. A 3. szint technikai megvalósíthatóságot igazol, fizetési hajlandóságot nem.

---

## 7. Jegyzetelési sablon és pontozás

### 7.1 Jegyzetsablon (interjúnként egy példány, a beszélgetés után 2 órán belül kitöltve)

Fájlnév: `I-XX_[dátum].md` (vagy egy közös táblázat egy sora). **Ügyfélnevet, adószámot nem írunk bele.** Az iroda nevét csak a külön, korlátozott hozzáférésű kódtáblában kötjük az interjúkódhoz.

```
INTERJÚ: I-__        Dátum: 2026-__-__     Helyszín: személyes / online
Kérdező: ________    Jegyzetelő: ________  Felvétel: igen (hozzájárult) / nem
Alany szerepe: tulajdonos / vezető könyvelő / egyéb    Döntéshozó? igen / nem
Toborzás: meleg (ki által) / hideg / szervezet / FB

-- A. PROFIL --
Létszám: __  Ügyfélszám: __  ÁFA-s: __ (havi bevalló: __)  Jogi személy: __%
Agrár: igen/nem   Idegen nyelvű ügyfelek: ____   Szegmens: solo / 3-9 / 10-25
Digitalizáltság (1–5): __   Hely: Szeged / vármegye (település: ____)
Felvesz-e munkatársat? ____

-- B–C. HAVI CIKLUS, DOKUMENTUMBEKÉRÉS --
Legnagyobb időrabló (alany szavaival): "..."
Időmegoszlás (becslés %): bekérés __ / rögzítés __ / egyeztetés __ / bevallás __ / bér __ / ügyfélkérdés __
Hiánytalanul beküldők aránya: __%    Bekérés havi órája: __
Csatornák: ____

-- D. NAV–BANK–FŐKÖNYV --
Jelenlegi lépések: ____
Ügyfelenkénti idő: __ perc   Havi összes: __ óra
Utolsó konkrét eltéréseset (mi, mikor, következmény): ____
NAV-megkeresés az elmúlt 12 hónapban: igen/nem

-- E. eÁFA --
eÁFA-tapasztalat: nincs / tervezet megnézve / beadva   Fő aggodalom: "..."
Szoftverszállító felkészültsége (alany szerint): ____
Halasztásra vár? igen/nem

-- F. Pmt./AML --
Utolsó teljes aktaátnézés: ____   Hiányos akták becsült aránya: __%
Újraszűrés 2026 óta: igen/nem/részben   Eszköz: ____   Éves ráfordítás: __ Ft / __ óra
Ellenőrzési tapasztalat (saját/kolléga): ____   Nyugalom-skála (1–5): __

-- G. ÜGYFÉLKOMMUNIKÁCIÓ --
Heti megkeresések száma: __   Csatornák: ____   Visszatérő kérdések: ____

-- H–I. SZOFTVER, ESZKÖZÖK --
Könyvelőprogram + verzió: ____   Helyi/felhő: ____
NAV-adat beérkezése: ____   Bankkivonat: ____
Export (formátum, látott-e): ____
Egyéb eszközök (M365/Google, Billingo stb.): ____
Kipróbált/használt versenytárs: ÜgyfélSegéd / Zeuss / Kulcs Connect / Optimato / Acounto / identiGO / egyéb: ____
AI-használat: ____

-- J. DÖNTÉS, KÖLTSÉGKERET --
Ki dönt: ____   Utolsó vásárlás és átfutás: ____
Éves szoftver/szolgáltatás költés: __ Ft   Döntési időszak: ____

-- MEGOLDÁS-PRÓBA (ha volt) --
Mutatott: (b) / (d) / egyik sem      Tesztelt árpont: ____
Első reakció (szó szerint): "..."
Mihez hasonlította: ____
Elköteleződési szint (0–5): __     Kért következő lépés + dátum: ____

-- LEGJOBB 3 IDÉZET --
1. "..."
2. "..."
3. "..."

-- MEGLEPETÉS / ÚJ HIPOTÉZIS --
____

-- AJÁNLÁSOK (kit javasolt) --
____
```

### 7.2 Pontozási rubrika (interjúnként, a két alapító közösen tölti ki, eltérés esetén megvitatják)

Minden dimenzió 1–5. A fájdalmat **(a), (b) és (d) külön** pontozzuk.

| Dimenzió | 1 | 3 | 5 |
|---|---|---|---|
| **Fájdalom** (a/b/d külön) | Nem említi, rávezetésre is „nem gond” | Említi, van múltbeli példa, de „megoldjuk” | Spontán hozza fel, friss konkrét eset, következménnyel (önellenőrzés, túlóra, bírságfélelem), érzelmi töltettel |
| **Gyakoriság / volumen** | Évente egyszer, kevés ügyfélnél | Havonta, az ügyfelek egy részénél | Havonta, az ügyfelek nagy részénél, vagy nagy egyszeri hátralék (d) |
| **Jelenlegi ráfordítás** | < 5 óra/hó az irodának, és semmit nem költött rá | 5–20 óra/hó, saját Excel vagy sablon | > 20 óra/hó, vagy már fizetett érte (szoftver, külső segítség, túlóra) |
| **Költségkeret** | „Csak ingyenes lehet”, nincs szoftverköltés | Havi néhány tízezer Ft-ot költ eszközökre | Havi 100 ezer Ft fölötti eszközköltés, vagy kimondja, hogy a tesztelt árponton megéri |
| **Sürgősség** | Nincs határidő-érzet | 2027 első félévében foglalkozna vele | November–decemberben lépne, vagy konkrét időpontot ad |
| **Illeszkedés** (technikai és szervezeti) | Nincs export, zárt rendszer, mindent elutasít | Van export, de kérdéses; fenntartásokkal nyitott | Ismert program, látott export, döntéshozó a teremben, korábbi sikeres bevezetés |
| **Elköteleződés** (0–5) | 6.4 szerinti szint | | |

**Összesítő jelölések:**
- **„Erős jelölt”:** fájdalom (b) vagy (d) ≥ 4 **és** költségkeret ≥ 3 **és** illeszkedés ≥ 3 **és** elköteleződés ≥ 3.
- **„Pilot”:** elköteleződés ≥ 4.
- **„Kizárt”:** illeszkedés = 1 vagy költségkeret = 1.

Mindegyik pontszám mellé egy mondatos indoklás kell („mert…”), különben a pontozás utólag nem ellenőrizhető.

---

## 8. Szintézis és döntés

### 8.1 Ötösével összegzés (60–90 perces közös ülés minden 5. interjú után)

1. **Hipotézistábla frissítése:** H1–H12 mindegyikénél megerősítő, cáfoló és bizonytalan esetek száma, interjúkóddal. Példa: „H1: 3 megerősít (I-01, I-03, I-05), 1 cáfol (I-02), 1 bizonytalan”.
2. **Fájdalom-hőtérkép:** sorokban az interjúk, oszlopokban (a)/(b)/(d)/(c)/(e: bérszámfejtés)/egyéb, cellákban a pontszám. Mely szegmensben magas mi?
3. **Szoftvertérkép:** programonként hány iroda használja, látott-e exportot, milyen formátumot.
4. **Idézetfal:** a legerősebb 10 idézet, fájdalom szerint csoportosítva. Ezekből lesz később az ajánlat szövege.
5. **Kérdéssor módosítása:** mi nem működött, mit kell élesíteni, mit lehet elhagyni. Az elhangzó új fájdalmakat (például bérszámfejtés, KATA 2027-es ügyfélhullám) új hipotézisként vesszük fel.
6. **Kvóta-ellenőrzés:** melyik szegmens hiányzik? A következő megkereséseket ennek megfelelően választjuk a top 20-ból és a tartalékból.
7. **Torzítás-ellenőrzés:** a meleg bemutatású interjúk udvariasabbak lehetnek. A meleg és a hideg alanyok pontszámait külön is nézzük meg.

**Az 5. interjú utáni gyors fordulópont:** ha az első 5-ből egynél sem jön ki ≥ 4-es fájdalom sem (b)-re, sem (d)-re, a 6–10. interjúkban a B blokkot (havi ciklus) bővítjük, és nyitottan keressük, mi a valódi fő fájdalom. Ilyenkor a makettet nem mutatjuk.

### 8.2 Döntési kritériumok (a 7–8. hét végén, 15–20 interjú után)

| Döntés | Feltétel (mind teljesüljön) |
|---|---|
| **GO (b)-vel** | (1) Az interjúk ≥ 40%-ában a (b) fájdalom ≥ 4; (2) legalább 3 iroda ≥ 4. szintű elköteleződése (LOI árral vagy fizetett pilot) (b)-re, ebből **legalább 1 fizetett pilot**; (3) legalább 2 különböző könyvelőprogramból látott, használható export; (4) a tesztelt árpontok közül legalább a középsőt (B) senki nem utasította el reflexből a pilotjelöltek közül. |
| **GO (d)-vel** | Ugyanez (d)-re. A (3) helyett: az irodák ≥ 50%-a beismeri a hiányos aktákat vagy az elmaradt újraszűrést, és legalább 2 iroda ad anonimizált Pmt.-listát vagy -mintát titoktartással. |
| **GO mindkettővel** | Mindkét feltételcsomag teljesül. **Akkor is csak egyet indítunk el először**, azt, amelyiknél több a fizetett pilot. A fejlesztő kapacitása 6–10 ügyfél (stratégiai jelentés). |
| **Részleges / várakoztató** | Magas fájdalom (≥ 40%), de < 3 ≥ 4. szintű elköteleződés. A fájdalom valós, de az ár, az időzítés vagy a bizalom nem áll. Döntés: időzítés-pivot (lásd 8.4) vagy újabb 5 interjú más szegmensben. |
| **NO-GO** | Sem (b), sem (d) fájdalma nem éri el a 25%-ot, **vagy** a többség szerint a szoftverük vagy egy SaaS megoldja, **vagy** 0 elköteleződés 3. szint felett. |

A számok **előre rögzítettek**. Ha utólag módosítani akarjuk, írásban indokoljuk, miért, és ezt a végső összefoglalóban jelezzük.

### 8.3 Végső összefoglaló (a 8. hét végére, belső dokumentum)

A tartalma:
- a minta leírása;
- a hipotézisek eredménye;
- fájdalom- és szoftvertérkép;
- a pilotjelöltek listája árral;
- a döntés és indoklása;
- a következő 90 nap terve.

Ebből készül a résztvevőknek küldött anonim változat („Mit láttunk N szegedi irodánál”).

### 8.4 Pivot-lehetőségek

| Ha… | Akkor… |
|---|---|
| A fájdalom valós, de „majd az első eÁFA-hónapok után” | **Időzítés-pivot:** a (b)-t „eÁFA első 3 ciklus utólagos rendbetétele”ként ajánljuk 2027 február–áprilisban. Januárban rövid levelet küldünk az interjúalanyoknak („hogy ment?”). |
| (a) dokumentumbekérés a legnagyobb fájdalom, de csak SaaS-árat fizetnének | **Partner-pivot:** az ÜgyfélSegéd vagy a Zeuss szegedi/dél-alföldi bevezető partnere leszünk (bevezetés, NAV technikai felhasználók beállítása, betanítás), és erre építünk Viber/WhatsApp-csatornát vagy egyedi exportot. |
| A Pmt. fáj, de a „szoftver” helyett tanácsadást várnak | **Szolgáltatás-pivot:** egyszeri „Pmt.-akta rendbetétel” projekt egy Pmt.-ben jártas jogász vagy szakértő partnerrel, mi visszük a folyamatot és az eszközt. |
| Gyakran előjön a bérszámfejtési adatbekérés (2026-os anyai és családi kedvezmények, adóelőleg-nyilatkozatok, januári csúcs) | **(e) bérszámfejtési adatbekérés** ajánlat vizsgálata. Különleges adat (egészség, gyermekek) miatt szigorúbb adatvédelem kell. |
| A KATA 2027-es visszanyitása sok új kisügyfelet hoz | **Ügyfélfelvételi (onboarding) csomag:** KYC + dokumentumbekérés + ügyfél-GYIK az új KATA-sok tömeges felvételéhez. |
| A digitálisan fejlett irodák már megoldották a problémát, a hagyományosak pedig nem vezetnek be semmit | **Szegmens-pivot:** a 10–25 fős irodák vagy a vármegyén kívüli, országos online irodák felé, illetve a stratégiai jelentés 2. (AI-jártassági képzés) vagy 3. (feldolgozóipar) vertikuma felé. |
| Senkinél nincs érdemi fájdalom | **Vertikum-pivot:** a stratégiai jelentés 3. pontja (szegedi feldolgozóipar és beszállítói dokumentáció). Az interjútechnika ugyanez, más kérdéssorral. |

---

## 9. Ütemezés (8 hét, 2026. október 5. – november 29.)

**Ütemezési szabályok:**
- **Hónap közepén ne kérjünk interjút.** A havi csúcs kb. 5-étől 20-áig tart: 12-én a bérek és járulékok, 20-án az ÁFA. Ez a jegyzetek szerint interjúhipotézis, nem igazolt naptár. Kerülendő napok: október 12. és 20., november 12. és 20. Legjobb ablakok: **október 21–30. és november 3–6.**, másodsorban november 23–30. Ha az alany szerint a hónap közepe is jó neki, elfogadjuk.
- Október 23. (péntek) nemzeti ünnep. November 1. (vasárnap) mindenszentek, november 2. (hétfő) halottak napja: munkanap, de sokan szabadságon vannak, erre a napra ne tegyünk interjút.
- **December–január tabu** új bevezetés szempontjából (zárás, első eÁFA-bevallás, nyugtaszankciók, KATA-változások). Ekkor csak a megállapodott pilotok technikai előkészítése folyhat.
- Heti cél: 3–4 interjú. Ez a két alapító mellékállású kapacitásával reális; a fejlesztő főállásban dolgozik, ezért az interjúkat lehetőleg délutánra vagy egy hosszabb napra csoportosítsuk.

| Hét | Dátum | Fókusz | Feladatok | Kimenet / mérce |
|---|---|---|---|---|
| **0** | okt. 3–4. (hétvége) | Indítás | Az interjúterv átolvasása, szerepek, a fejlesztő munkaszerződés-ellenőrzésének elindítása (10. fejezet) | Közös megértés |
| **1** | okt. 5–11. | Előkészítés + első megkeresések | Top 20 ellenőrzése (cégjegyzék, névrokonok); meleg utak feltérképezése; eÁFA-ellenőrzőlista megírása és szakmai átnézése; adatkezelési tájékoztató és egyoldalas NDA-sablon; ÁNYK-halasztás ellenőrzése; **az 1. hullám 8 irodájának megkeresése (meleg utakkal kezdve)**; CSMKIK, MKOE és MinKE (RÓ) megkeresése | 8 megkeresés kint, legalább 3 időpont az okt. 21–31. ablakra |
| **2** | okt. 12–18. | Próbainterjú + makettek | 1 próbainterjú egy barátságos könyvelővel a hálózatból (nem számít a kvótába); a kérdéssor finomítása; a (b) és (d) makett elkészítése fiktív adattal; 2. hullám első fele (6 iroda) + hideg megkeresések; utánkövetések. Kerülendő: okt. 12. és 20. körüli napok | Kipróbált kérdéssor, makettek, összesen 15+ megkeresés |
| **3** | okt. 19–25. | Interjúk 1–4. | Interjúk okt. 21–22-én (23-a ünnep, 24–25. hétvége); szerep: az értékesítő kérdez; 24 órán belül jegyzet és pontozás | 2–4 interjú |
| **4** | okt. 26.–nov. 1. | Interjúk 5–8. + **1. szintézis** | Interjúk okt. 26–30. között; az 5. után az 1. szintézisülés (8.1), kérdéssor-módosítás, kvótahiányok; 2. hullám második fele + vármegyei hideg megkeresések | 8 interjú, első hipotézistábla |
| **5** | nov. 2–8. | Interjúk 9–12. | Interjúk nov. 3–6. között (a legjobb ablak); szerepcsere; a megoldás-próba élesben (ahol magas a fájdalom); CSMKIK-előadás vagy -reggeli, ha összejött | 12 interjú; az első 3–4. szintű elköteleződések |
| **6** | nov. 9–15. | **2. szintézis** + követő találkozók | Csak 1–2 interjú (hónap közepe); a 10. interjú utáni 2. szintézis; követő találkozók a 3+ szintű alanyokkal (adatminta titoktartással, munkamegfigyelés); a fejlesztő megnézi a kapott exportokat | Megvalósíthatósági jegyzet szoftverenként; LOI-tervezet |
| **7** | nov. 16–22. | Interjúk 13–16. + pilotajánlatok | Interjúk csak ott, ahol az alany a 20-i ÁFA-határidő előtt is vállalja (egyébként a 8. hétre tolódnak); pilotajánlatok és LOI-k kiküldése a jelölteknek; a 15. után a 3. szintézis | 15–16 interjú; kiküldött pilotajánlatok |
| **8** | nov. 23–29. | Döntés | Utolsó 2–4 interjú nov. 23–27. között (kvótahiányok); végső szintézis; **GO / részleges / NO-GO döntés a 8.2 szerint**; aláírt pilotok vagy LOI-k begyűjtése; köszönőlevelek, az anonim összefoglaló vázlata | Döntés, legalább 3 aláírt pilot vagy LOI (cél) |
| *utána* | nov. 30.–dec. 18. | Pilot előkészítés | Pilotszerződés, adatfeldolgozói megállapodás; főpróba a novemberi bevalláson (dec. 20.) csak ott, ahol az iroda kéri; az anonim összefoglaló kiküldése december elején | – |
| *utána* | 2027. jan.–febr. | Pilot éles + időzítés-pivot | Az élő (b) futás a decemberi eÁFA-bevallásra; a többi interjúalanynak rövid „hogy ment?” levél február elején | – |

---

## 10. Jogi és etikai megjegyzések

> Ez a fejezet gyakorlati ellenőrzőlista, nem jogi tanács. A szerződéseket és az adatkezelési dokumentumokat ügyvéddel kell véglegesíteni (lásd a stratégiai jelentés 6–12. heti lépését).

### 10.1 A fejlesztő munkaszerződésének ellenőrzése (**az első megkeresés előtt**)

- **Versenytilalmi és összeférhetetlenségi kikötés:** érinti-e a munkáltató tevékenységi körét vagy ügyfélkörét egy könyvelőirodáknak szóló automatizálási szolgáltatás? Van-e a munkáltatónak könyvelőiroda-ügyfele vagy könyvelési szoftverterméke?
- **Mellékfoglalkozás vagy más jogviszony bejelentési vagy engedélyezési kötelezettsége:** egy saját Kft.-ben vállalt tulajdonosi és munkavégzési szerep is ide tartozhat.
- **Szellemi tulajdon:** a munkaszerződés kiterjed-e a munkaidőn kívül, saját eszközzel készült fejlesztésekre? Semmit ne fejlesszünk a munkáltató gépén, fiókján, idejében, és a munkahelyi e-mailt se használjuk.
- **Titoktartás:** a munkáltató ügyfeleinek adatai és megoldásai nem kerülhetnek a Kft.-be.
- Eredmény: írásos „zöld jelzés” (ügyvédtől vagy a munkáltatótól). Ha nincs meg, az interjúkat az értékesítő vezeti, a fejlesztő pedig csak jegyzetel, és nem a saját nevén keres meg senkit, amíg ez nem tisztázott.

### 10.2 Titoktartás (NDA) és adatminták kezelése

- **Az interjúhoz nem kell NDA,** mert ügyféladatot nem kérünk. Kérjük az alanyt, hogy ne mondjon ügyfélnevet vagy adószámot. Ha mégis elhangzik, a jegyzetből kihagyjuk.
- **Adatminta (3. szint) előtt:** egyoldalas, **kölcsönös titoktartási megállapodás**. Tartalma: a cél (kizárólag a megvalósíthatóság vizsgálata), a megőrzés (legfeljebb 60 nap, utána igazolt törlés), harmadik félnek nem adható tovább, és nem használható modelltanításra.
- **Az adatminimalizálás sorrendje**, mindig a legkisebb szükséges lépéssel:
  1. Képernyőn mutatja, mi nem kapunk adatot.
  2. **Szintetikus vagy anonimizált export:** az iroda kicseréli az ügyfélnevet, az adószámot, a bankszámlaszámot és a személyneveket. Ebben segítünk egy egyszerű útmutatóval, de az anonimizálást ő végzi.
  3. **Valódi ügyféladat** csak fizetett pilotban, **adatfeldolgozói szerződéssel (GDPR 28. cikk)**. Az iroda az adatkezelő, a Kft. az adatfeldolgozó, egy esetleges LLM-szolgáltató pedig al-adatfeldolgozó, csak ha a szerződés ezt kifejezetten engedi.
- **Pmt.-adatok:** személyazonosító okmány-másolatot és tényleges tulajdonosi adatot interjú vagy pilot előtt **semmilyen formában ne vegyünk át**. A (d) próba csak struktúrát mutat (milyen mezők, milyen hiányok), valódi okmányt nem.
- **Technikai szabályok:**
  - titkosított, EU-ban tárolt, hozzáféréssel korlátozott tárhely;
  - ügyféladat nem kerülhet fogyasztói AI-felületre (ingyenes ChatGPT és hasonlók);
  - LLM-et csak olyan céges API-n keresztül használunk, amely nem tanít az adaton, és van adatfeldolgozói feltétele;
  - minden adathozzáférést naplózunk.
- **Könyvelői titoktartás:** a könyvelőt titoktartási kötelezettség köti az ügyfelei felé, és a Pmt. is előír titoktartási és adatmegőrzési szabályokat. Nem kérhetünk tőle olyat, amivel ezt megsértené. Ha egy iroda „csak úgy” odaadná a teljes adatbázisát, ne fogadjuk el.

### 10.3 Az interjúalanyok adatai

- Egy rövid **adatkezelési tájékoztató** (fél oldal), az első e-mailben linkként vagy mellékletként. Tartalma:
  - ki az adatkezelő (a Kft.), milyen adat (név, elérhetőség, interjújegyzet, felvétel), milyen célra (piackutatás);
  - jogalap: hozzájárulás vagy jogos érdek;
  - megőrzés: a felvétel legfeljebb 30 nap, a jegyzet a kutatás végéig, illetve legfeljebb 12 hónap, ha további kapcsolatot kért;
  - törlési jog, és a NAIH mint felügyeleti hatóság.
- A felvételt csak kifejezett hozzájárulással készítjük (4.3), és a hozzájárulást rögzítjük.
- Idézni csak névtelenül szabad; az anonim összefoglalóban egyetlen iroda se legyen felismerhető.
- A toborzási adatokra a 3.4 vonatkozik: üzleti elérhetőség, nincs tömeges levél a PM-névjegyzékből, leiratkozási lehetőség.

### 10.4 Nem adunk adótanácsot

- Az adótanácsadói tevékenység nyilvántartásba vételhez kötött. A Kft. **nem ad adó-, számviteli vagy Pmt.-jogi tanácsot**, sem az interjún, sem az ellenőrzőlistában, sem a makettben.
- Ha az alany adókérdést tesz fel („ezt hogyan kell az eÁFA-ban?”), a válasz: „Ebben nem vagyunk illetékesek. A NAV tájékoztatója vagy a szoftverszállító tud pontos választ adni.” Ez egyben jó adat is arról, hol bizonytalanok.
- Az ellenőrzőlista és minden anyag lábjegyzete: „Tájékoztató jellegű, nyilvános NAV-forrásokon alapul, nem minősül adótanácsadásnak; állapot: [dátum].”
- A (b) és a (d) ajánlat pozicionálása: **„jelzések emberi felülvizsgálatra”**, nem döntés. A bevallásért és a Pmt.-megfelelésért az iroda felel. Ezt a pilotszerződésben felelősségkorlátozással is rögzíteni kell (a stratégiai jelentés szerint például a 12 havi díjig).

### 10.5 Etikai alapszabályok

- **Az „interjú, nem eladás” ígéretet betartjuk.** Ha a megoldás-próba után az alany nem kér többet, nem küldünk ajánlatot.
- A meleg bemutatásnál nem használjuk ki a közös ismerőst vagy az ügyfélkapcsolatot nyomásgyakorlásra (például: „az ügyfele is ezt szeretné”).
- Versenytársakról tényszerűen beszélünk, nem becsmérelünk (ÜgyfélSegéd, Zeuss, Optimato, identiGO, Acounto).
- Az érdemi információkat (például egy iroda belső folyamatát) más irodának nem adjuk tovább, csak anonim, összesített formában.
- Ha a beszélgetésben jogsértésre utaló információ hangzik el (például valaki szándékosan nem végez ügyfélátvilágítást), nem kommentáljuk és nem rögzítjük azonosítható formában. A kutatásban nem vagyunk sem hatóság, sem tanácsadó.

---

## Függelék: egyoldalas puska az interjúhoz

1. „Tanulni jöttünk, nem árulni.” Felvétel csak engedéllyel.
2. **Múltról kérdezz:** „Mesélje el a legutóbbit…”
3. **Számokat kérj:** óra, ügyfél, alkalom, forint.
4. **Hallgass:** a moderátor a beszélgetés kevesebb mint 30%-ában beszél.
5. **A 35. perc előtt nincs megoldás és nincs ár.**
6. Bók = 0 pont. Elköteleződés = minden.
7. Adókérdésre: „Ebben nem vagyunk illetékesek.”
8. Zárás: „Mit nem kérdeztünk? Kit ajánlana? Visszajöhetünk?”
9. A beszélgetés után 15 perc: jegyzet + pontozás, még aznap.
