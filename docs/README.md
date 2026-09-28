# Bence tippjáték 👶

Egyszerű weboldal, ahol a család megtippelheti Bence születési adatait, a születés után pedig pontozott eredménytábla készül.

- `index.html` – maga az oldal (egyetlen fájl, nincs build)
- `config.js` – Supabase URL + anon kulcs (üresen hagyva demó mód: jelszó `bence`, szülői `admin`)
- `setup.sql` – az adatbázis létrehozása Supabase-ben (itt kell átírni a két jelszót)

## Beüzemelés
1. Supabase projektben futtasd le a `setup.sql`-t (előtte írd át a `CSALADI_JELSZO` és `SZULOI_JELSZO` értékeket).
2. Töltsd ki a `config.js`-t (Project Settings → API: Project URL, anon/publishable key).
3. Publikálás: GitHub Pages (Settings → Pages → branch, `/docs` mappa) vagy Vercel (Root directory: `docs`).

## Használat
- Családi jelszóval belépve: név + tippek beküldése, eredménytábla megtekintése.
- Szülői jelszóval belépve: „Valós adatok” fül – mentés után a tippelés lezárul, a tábla zöld/sárga/piros lesz.

## Pontozás (max. 100)
| Adat | Pont |
|---|---|
| Súly | 25, minden 20 g eltérés −1 (500 g-tól 0) |
| Hossz | 15, 5 cm eltérésnél 0 |
| Születés napja | 20, naponta −2 (10 naptól 0) |
| Időpont | 15, 6 óra eltérésnél 0 |
| Napszak (az időpontból) | 5 |
| Haj mennyisége | 5 (szomszédos kategória: 2) |
| Haj színe / szemszín / kire hasonlít | 5-5 |
