# ADR-0001 · Wortverbindungs-Kurs als statische, generierte Web-App

**Status:** Angenommen · **Datum:** 2026-09-20

## Kontext
Wir bauen die interaktive Begleitung zur YouTube-Episode
„Deutsch lernen B1 B2 C1 | 5.000 deutsche Wortverbindungen für natürliches
Deutsch“ (Kanal *Einfach deutsch, easy deutsch.*). Der Python/JS/CSS-Stack von
`german-verbs` existiert bereits und produziert 100 % statische, offline-fähige
Modul-Apps – dieses Muster übernehmen wir.

## Entscheidung
- Der Kurs wird **vollständig statisch generiert** (kein Server, keine
  Laufzeit-Abhängigkeit, offline per `file://`).
- `_merge.py` baut aus `_work/cat1..7.json` die Master-Datei
  `data/verbindungen.json` (119 Verbindungen, eindeutige Keys
  `v/en/meaning/example/natural/grammar`).
- `_generate.py` rendert aus dem Master **1 Startseite + 7 eigenständige
  Modul-Apps** (`index.html` + `0X-*/index.html`).
- Jede Modul-App ist ein in sich geschlossenes HTML-Dokument mit Inline-CSS/JS
  und eingebettetem `const VERBS = […]` (kein externes Asset, kein Fetch).

## Konsequenzen
- ✅ Öffnet doppelklickbar (offline), funktioniert per `file://`.
- ✅ Fortschritt (localStorage) + Web Speech (de-DE) ohne Server.
- ⚠️ Größere HTML-Dateien (jede App enthält ihre Daten inline); akzeptiert.
- ⚠️ Inhaltsänderung ⇒ `_merge.py && _generate.py` erneut ausführen
  (in `docs/BUILD-STATUS.md` dokumentiert).
