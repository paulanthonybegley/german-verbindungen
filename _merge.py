#!/usr/bin/env python3
"""Merge the 7 category JSONs into a single master file data/verbindungen.json.

Faithful interactive companion to the YouTube episode
"Deutsch lernen B1 B2 C1 | 5.000 deutsche Wortverbindungen für natürliches Deutsch"
(Einfach deutsch, easy deutsch. - https://www.youtube.com/watch?v=2tygr202mYI).

Key naming matches what _work/module.js consumes: v, en, meaning, example,
natural, grammar.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, "_work")

CATEGORIES = [
    {
        "id": 1,
        "slug": "01-alltag-wohnen",
        "emoji": "🛏️",
        "title": "Alltag & Wohnen",
        "titleEn": "Everyday Life & Living",
        "file": "cat1.json",
        "verbs": 18,
        "description": "Fragen stellen, Antworten geben, Entscheidungen treffen - die alltäglichen Wortverbindungen rund ums Leben und Wohnen.",
    },
    {
        "id": 2,
        "slug": "02-kommunikation-gefuehle",
        "emoji": "💬",
        "title": "Kommunikation & Gefühle",
        "titleEn": "Communication & Feelings",
        "file": "cat2.json",
        "verbs": 20,
        "description": "Ein Gespräch führen, Komplimente machen, Rücksicht nehmen - die Wortverbindungen der Begegnung.",
    },
    {
        "id": 3,
        "slug": "03-arbeit-aufgaben",
        "emoji": "💼",
        "title": "Arbeit & Aufgaben",
        "titleEn": "Work & Tasks",
        "file": "cat3.json",
        "verbs": 20,
        "description": "Aufgaben erledigen, Aufträge übernehmen, Termine vereinbaren - die Sprache des Berufs.",
    },
    {
        "id": 4,
        "slug": "04-bewegung-aktivitaeten",
        "emoji": "🏃",
        "title": "Bewegung & Aktivitäten",
        "titleEn": "Movement & Activities",
        "file": "cat4.json",
        "verbs": 16,
        "description": "Spaziergänge machen, Sport treiben, Touren buchen - die Sprache des Körpers und der Freizeit.",
    },
    {
        "id": 5,
        "slug": "05-denken-entscheiden",
        "emoji": "🧠",
        "title": "Denken & Entscheiden",
        "titleEn": "Thinking & Deciding",
        "file": "cat5.json",
        "verbs": 16,
        "description": "Überlegungen anstellen, Schlüsse ziehen, Entscheidungen fällen - die Sprache des Geistes.",
    },
    {
        "id": 6,
        "slug": "06-beziehungen-soziales-leben",
        "emoji": "🤝",
        "title": "Beziehungen & soziales Leben",
        "titleEn": "Relationships & Social Life",
        "file": "cat6.json",
        "verbs": 20,
        "description": "Kontakt aufnehmen, Komplimente machen, Rücksicht nehmen - die Sprache der Verbindungen.",
    },
    {
        "id": 7,
        "slug": "07-finale",
        "emoji": "🏁",
        "title": "Das große Finale",
        "titleEn": "The Grand Finale",
        "file": "cat7.json",
        "verbs": 16,
        "description": "Die wichtigsten Wortverbindungen aus allen sieben Modulen - das große Abschlussfinale.",
    },
]

MASTER = []
for c in CATEGORIES:
    with open(os.path.join(WORK, c["file"]), encoding="utf-8") as f:
        data = json.load(f)
    c["verbs"] = len(data)
    for v in data:
        entry = {
            "v": v["v"],
            "en": v["en"],
            "meaning": v["meaning"],
            "example": v["example"],
            "natural": v["natural"],
            "grammar": v["grammar"],
        }
        entry = {k: (str(val).strip() if isinstance(val, str) else val) for k, val in entry.items()}
        MASTER.append(entry)
    print(f"Modul {c['id']} ({c['title']}): {len(data)}")

TOTAL = len(MASTER)
print("TOTAL Wortverbindungen:", TOTAL)

out = {
    "source": {
        "title": "Deutsch lernen B1 B2 C1 | 5.000 deutsche Wortverbindungen für natürliches Deutsch",
        "channel": "Einfach deutsch, easy deutsch.",
        "url": "https://www.youtube.com/watch?v=2tygr202mYI",
        "duration_s": 3100,
    },
    "categories": CATEGORIES,
    "verbindungen": MASTER,
}

os.makedirs(os.path.join(HERE, "data"), exist_ok=True)
with open(os.path.join(HERE, "data", "verbindungen.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("Wrote data/verbindungen.json")
