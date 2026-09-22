# german-verbindungen · Interaktiver Wortverbindungs-Kurs (B1–C1)

Statische, offline-fähige Übungs-Apps als Begleitung zur YouTube-Episode
**„Deutsch lernen B1 B2 C1 | 5.000 deutsche Wortverbindungen für natürliches
Deutsch“** von *Einfach deutsch, easy deutsch.* (Episoden-URL:
<https://www.youtube.com/watch?v=2tygr202mYI>).

## Start
Doppelklick auf `index.html` (Startseite) → wähle eines der 7 Module.
Kein Server, kein Internet, keine externen Dateien – alles ist eingebettet.

## Aufbau
```
index.html                  Startseite (7 Modul-Karten + Fortschrittsbalken)
01-alltag-wohnen/           Modul 1 · Alltag & Wohnen (18)
02-kommunikation-gefuehle/  Modul 2 · Kommunikation & Gefühle (20)
03-arbeit-aufgaben/         Modul 3 · Arbeit & Aufgaben (20)
04-bewegung-aktivitaeten/   Modul 4 · Bewegung & Aktivitäten (16)
05-denken-entscheiden/      Modul 5 · Denken & Entscheiden (16)
06-beziehungen-soziales-leben/ Modul 6 · Beziehungen & soziales Leben (20)
07-finale/                  Modul 7 · Das große Finale (9)
data/verbindungen.json      Master-Daten (119 Verbindungen)
docs/                       Lesson-Plan, Übungen, Lösungen, ADRs, Use-Cases
_work/                      Quell-Kategorien cat1..7.json + CSS/JS-Templates
_merge.py · _generate.py    Build-Pipeline (siehe docs/BUILD-STATUS.md)
```

## Übungsarten (pro Modul)
- **Lernen** – Verbindung + DE/EN-Bedeutung + Beispiel + natürlicher Satz + Grammatik
- **Karten** – Karte umdrehen, Bedeutung erinnern, 🔊 anhören
- **Lücken** – Beispielsatz vervollständigen (Nomen-Verb-Verbindung einsetzen)
- **Quiz** – 10 gemischte Fragen (Übersetzung, Bedeutung, Im Satz, Grammatik)

**Audio:** Web Speech API (de-DE) · **Fortschritt:** `localStorage` (pro Modul).

## Build (nur bei Inhaltsänderung)
```bash
python3 _merge.py     # _work/cat*.json → data/verbindungen.json
python3 _generate.py  # data/verbindungen.json → index.html + 7 Module
```
Details und Status: `docs/BUILD-STATUS.md`.
