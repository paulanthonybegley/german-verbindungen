# german-verbindungen · build status (resume point)

## Location
- Course root: `/Users/paulbegley/Documents/irish-lessons/german-verbindungen/`
- Reference (architecture + _work templates): `/Users/paulbegley/Documents/irish-lessons/german-verbs/`

## Build pipeline (all working — tested, no placeholders)
```
python3 _merge.py      # _work/cat1..7.json -> data/verbindungen.json (119 Wortverbindungen)
python3 _generate.py   # data/verbindungen.json -> index.html + 7 self-contained module apps
```

## Generated output (8 html files, verified clean 2026-09-20)
- `index.html`                            (course landing)
- `01-alltag-wohnen/index.html`           (18)  Alltag & Wohnen
- `02-kommunikation-gefuehle/index.html`  (20)  Kommunikation & Gefühle
- `03-arbeit-aufgaben/index.html`         (20)  Arbeit & Aufgaben
- `04-bewegung-aktivitaeten/index.html`   (16)  Bewegung & Aktivitäten
- `05-denken-entscheiden/index.html`      (16)  Denken & Entscheiden
- `06-beziehungen-soziales-leben/index.html`(20) Beziehungen & soziales Leben
- `07-finale/index.html`                  (09)  Das große Finale
- TOTAL: 119 Wortverbindungen

Each module app is fully self-contained (no external assets): Study / Cards /
Fill-in-the-blank / Quiz with Web Speech (de-DE) audio, localStorage progress,
grammar hints. Schema keys consumed by _work/module.js: v.en meaning example
natural grammar — matches data exactly.

## Source
- YouTube: «Deutsch lernen B1 B2 C1 | 5.000 deutsche Wortverbindungen für
  natürliches Deutsch» (Einfach deutsch, easy deutsch.)
- URL: https://www.youtube.com/watch?v=2tygr202mYI
- Channel: https://www.youtube.com/@einfachdeutscheasydeutsch

## Authoring assets in _work/
- cat1..7.json (119 items · schema v/en/meaning/example/natural/grammar)
- module.css module.js module.bak.js index.css (copied verbatim from german-verbs)
- schema.md (data contract)
Note: module.js is the stock german-verbs practice engine (cloze verb-root logic);
it blanks the verb part inside the example — the item's cloze highlight targets
the Nomen-Verb-Verbindung's verb, appropriate for this collocation course.

## Docs (in docs/)
- use-cases/  adr/

## NOT YET DONE (candidate next steps)
1. docs/: lesson-plan.md, exercises.md, solutions.md (per OLD.txt framework)
2. README.md at course root
3. Any remaining tuned JS per Italian-style personalized shutdown
