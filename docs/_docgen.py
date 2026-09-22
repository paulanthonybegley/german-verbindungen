#!/usr/bin/env python3
"""
Generate docs/exercises.md and docs/solutions.md straight from
data/verbindungen.json so counts and strings can never drift from the app.

Each module gets the same 4-part exercise block mapped to its own verbs:
A) Study (Lernen)   - read each collocation, its meaning + example
B) Cards (Karten)   - view collocation, recall the English
C) Cloze (Lücken)   - fill the missing noun/verb in the example sentence
D) Quiz             - 6 mixed recognition questions on the collocations
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

with open(os.path.join(ROOT, "data", "verbindungen.json"), encoding="utf-8") as f:
    DATA = json.load(f)

CATS = DATA["categories"]
MASTER = DATA["verbindungen"]


def verbs_for(c):
    start = sum(x["verbs"] for x in CATS[: c["id"] - 1])
    return MASTER[start : start + c["verbs"]]


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def cloze(v):
    ex = v["example"]
    return ex


exercises = []
solutions = []

for c in CATS:
    vs = verbs_for(c)
    exercises.append(f"# {c['emoji']} Modul {c['id']}: {c['title']} ({len(vs)} Verbindungen)\n")
    solutions.append(f"# {c['emoji']} Modul {c['id']}: {c['title']} ({len(vs)} Verbindungen)\n")

    e = ["## A · Lernen (Study)",
         f"Arbeite jede der {len(vs)} Wortverbindungen durch: lies Bedeutung, \u00f6ffne das Beispiel und h\u00f6re die Aussprache an."]
    s = ["## A · L\u00f6sungen",
         f"Alle {len(vs)} Verbindungen sind im Modul (Reihenfolge = Quiz/Mischung variiert):"]

    for v in vs:
        e.append(f"- **{v['v']}** – {v['en']} · {v['natural']}")
        s.append(f"- **{v['v']}** (`{v['en']}`) · Beispiel: _{v['example']}_")

    e.append("## B · Karten (Drill)")
    e.append(f"Drehe {len(vs)} Karten. Sieh die Verbindung, versuche die englische Bedeutung + ein nat\u00fcrliches Beispiel zu erinnern.")
    s.append("## B · L\u00f6sungen (englische Kerne)")
    s.append(", ".join(f"**{v['v']}** = {v['en']}" for v in vs))

    e.append("## C · L\u00fccken (Cloze)")
    e.append("Vervollst\u00e4ndige den Beispielsatz. (Das Modul blendet immer den gleichen Satztyp aus.)")
    for i, v in enumerate(vs, 1):
        e.append(f"{i}. _„{v['example']}“_ → gesucht: die fehlende Verbindung _„___“")
        s.append(f"{i}. {v['v']} — {v['example']}")

    # D quiz: pick 6, one per verb? Just self-check prompt + answer key reaches on page.
    e.append("## D · Quiz")
    e.append("Modul mischt 6 selbstkontrollierte Fragen (DE→EN, Bedeutung, Satz, Grammatik). Punkte erscheinen direkt im Modul.")
    s.append("## D · L\u00f6sungen")
    s.append("Selbstkontrolle im Modul; alle Antworten sind auf dieser Seite und in Modul A/B/C dokumentiert.")

    exercises.append("\n".join(e) + "\n")
    solutions.append("\n".join(s) + "\n")

os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
with open(os.path.join(ROOT, "docs", "exercises.md"), "w", encoding="utf-8") as f:
    f.write("# \u00dcbungen \u2013 german-verbindungen (B1\u2013C1)\n\n")
    f.write("Der Kurs baut auf der YouTube-Episode \u201eDeutsch lernen B1 B2 C1 | 5.000 deutsche Wortverbindungen\u201c\n")
    f.write("von **Einfach deutsch, easy deutsch.** auf. Bearbeite die \u00dcbungen **je Modul** nach dem Muster A\u2013D, dann pr\u00fcfe in `solutions.md`.\n\n")
    f.write("\n".join(exercises))

with open(os.path.join(ROOT, "docs", "solutions.md"), "w", encoding="utf-8") as f:
    f.write("# L\u00f6sungen \u2013 german-verbindungen (B1\u2013C1)\n\n")
    f.write("Referenz zu `exercises.md`. Alle Wortverbindungen exakt wie im interaktiven Kurs und im Video.\n\n")
    f.write("\n".join(solutions))

print(f"Wrote docs/exercises.md + docs/solutions.md for {len(CATS)} module blocks")

# quick sanity print of module totals
print("Per module:", [len(verbs_for(c)) for c in CATS], "-> total", len(MASTER))
