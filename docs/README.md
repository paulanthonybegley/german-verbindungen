# docs/ · german-verbindungen

Zentrale Kurs-Dokumentation (auf Deutsch, weil Kurs + Zielgruppe deutsch sind).

## Index

| Dokument | Inhalt |
|---|---|
| `lesson-plan.md` | Vollständiger Lesson-Plan nach OLD.txt (9 Design-Inputs) |
| `exercises.md` | Übungen je Modul (A Studieren · B Karten · C Lücken · D Quiz) |
| `solutions.md` | Lösungen/Schlüssel zu den Übungen (aus denselben Daten generiert) |
| `use-cases/` | 4 Use-Cases (Studieren, Karten, Lücken, Quiz) |
| `adr/` | 4 ADRs (Statik, localStorage, Web-Speech, Offline-Fallback) |
| `BUILD-STATUS.md` | Build-Pipeline, Befehle, aktueller Stand |

## Build (bei Änderung an `_work/cat*.json`)

```bash
python3 _merge.py            # _work/cat*.json → data/verbindungen.json
python3 _generate.py         # data/verbindungen.json → index.html + 7 Module
```

Einmalige Runde: `docs/lesson-plan.md` + Generator in `_work/`.
