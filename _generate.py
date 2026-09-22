#!/usr/bin/env python3
"""
Generate the "Wortverbindungen B1-C1" interactive course.

Reads data/verbindungen.json and produces:
  - index.html                (landing page)
  - <slug>/index.html         (7 self-contained module apps)

A faithful interactive companion to the YouTube episode
"Deutsch lernen B1 B2 C1 | 5.000 deutsche Wortverbindungen für natürliches Deutsch"
(Einfach deutsch, easy deutsch. - https://www.youtube.com/watch?v=2tygr202mYI).

Each module app is fully self-contained (no external assets): Study /
Cards / Fill-in-the-blank / Quiz modes with Web Speech (de-DE) audio and
localStorage progress. Templates are reused verbatim from the german-verbs
project (_work/module.css, _work/module.js, _work/index.css).
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(HERE, "data", "verbindungen.json"), encoding="utf-8") as f:
    DATA = json.load(f)

CATS = DATA["categories"]
MASTER = DATA["verbindungen"]


def esc(s):
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def verbs_for(cat):
    start = sum(c["verbs"] for c in CATS[: cat["id"] - 1])
    return MASTER[start : start + cat["verbs"]]


def load(path):
    with open(os.path.join(HERE, "_work", path), encoding="utf-8") as f:
        return f.read()


def render_index():
    INDEX_CSS = load("index.css")
    cats_js = json.dumps([{"id": c["id"], "verbs": c["verbs"]} for c in CATS])
    cards = []
    for c in CATS:
        verbs = verbs_for(c)
        cards.append(
            f"""
<div class="card">
  <div class="card-body">
    <div class="num">Modul {c['id']} · {len(verbs)} Wortverbindungen</div>
    <h3>{c['emoji']} {esc(c['title'])}</h3>
    <p>{esc(c['description'])}</p>
    <div class="meta">
      <span>🔊 Audio</span><span>🃏 Karten</span><span>🎯 Quiz</span>
      <div class="bar"><div class="fill" id="bar{c['id']}" style="width:0%"></div></div>
      <span id="pct{c['id']}">0%</span>
    </div>
    <a class="btn" href="{c['slug']}/index.html">Start Modul →</a>
  </div>
</div>"""
        )
    total = len(MASTER)
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Wortverbindungen B1–C1 · Interaktive Karteikarten</title>
<style>{INDEX_CSS}</style>
</head>
<body>
<header>
  <h1>🧩 Deutsche Wortverbindungen – B1/C1</h1>
  <p>Trainiere die wichtigsten deutschen Nomen-Verb-Verbindungen und festen Wortverbindungen auf B1–C1: Lernen, Karten, Lückentexte und Quiz – mit natürlichen Beispielsätzen, Grammatik-Hinweis und Audio.</p>
</header>
<div class="container">
  <div class="intro">
    <h2>Über diesen Kurs</h2>
    <p>Eine interaktive Begleitung zur YouTube-Episode
    <a href="https://www.youtube.com/watch?v=2tygr202mYI" target="_blank" rel="noopener" style="color:var(--red)"><strong>„Deutsch lernen B1 B2 C1 | 5.000 deutsche Wortverbindungen für natürliches Deutsch“</strong></a>
    von <strong>Einfach deutsch, easy deutsch.</strong> Die Episode ist zum passiven Hören gedacht – dieser Kurs verwandelt sie in ein aktives Übungsprogramm: Du übst jede Wortverbindung mit deutscher Erklärung, natürlichem Beispielsatz und Grammatik-Hinweis und sprichst sie mit der Browser-Stimme nach.</p>
    <p style="margin-top:.5rem">Klicke jede Wortverbindung an, um sie laut zu hören. Dein Fortschritt wird automatisch gespeichert. Die Module 1–6 folgen den Kategorien des Videos (Alltag, Kommunikation &amp; Gefühle, Arbeit, Bewegung, Denken &amp; Entscheiden, Beziehungen); Modul 7 ist das große Finale der wichtigsten Verbindungen.</p>
  </div>
  <div class="course-grid">{''.join(cards)}</div>
  <div class="stats">
    <div class="stat"><b>{total}</b> Wortverbindungen</div>
    <div class="stat"><b>7</b> Module</div>
    <div class="stat"><b>4</b> Übungsarten</div>
    <div class="stat"><b>🔊</b> Deutsche Aussprache</div>
  </div>
  <div class="intro" style="margin-top:1.4rem">
    <h2>🎥 Zur Video-Episode</h2>
    <p>Hör dir zuerst die Episode an, während du kochst oder pendelst, und arbeite danach die Module aktiv durch. Kanal: <a href="https://www.youtube.com/@einfachdeutscheasydeutsch" target="_blank" rel="noopener" style="color:var(--red)">Einfach deutsch, easy deutsch.</a> · Wortverbindungen werden mit der Browser-Stimme (Deutsch) ausgesprochen.</p>
  </div>
</div>
<footer>
  <p>Basierend auf <a href="https://www.youtube.com/watch?v=2tygr202mYI" target="_blank">„Deutsch lernen B1 B2 C1 | 5.000 deutsche Wortverbindungen für natürliches Deutsch“</a> von Einfach deutsch, easy deutsch.</p>
  <p>Kursübersicht <a href="../index.html">german-verbindungen</a> · Audio via Web Speech API (de-DE)</p>
</footer>
<script>
const CATS = {cats_js};
function fmt(){{
  CATS.forEach(c=>{{
    const p = parseInt(localStorage.getItem('gvw-progress-'+c.id)||'0',10);
    document.getElementById('pct'+c.id).textContent = Math.round(p)+'%';
    document.getElementById('bar'+c.id).style.width = Math.round(p)+'%';
  }});
}}
fmt();
window.addEventListener('storage', fmt);
</script>
</body>
</html>
"""
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote index.html")


def render_module(cat):
    verbs = verbs_for(cat)
    verbs_js = json.dumps(
        [
            {"v": v["v"], "en": v["en"], "meaning": v["meaning"],
             "example": v["example"], "natural": v["natural"], "grammar": v["grammar"]}
            for v in verbs
        ],
        ensure_ascii=False,
    )
    mod_css = load("module.css")
    mod_js = load("module.js")
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Modul {cat['id']}: {esc(cat['title'])} – Wortverbindungen B1-C1</title>
<style>{mod_css}</style>
</head>
<body>
<div class="topbar"><a href="../index.html">← Kursübersicht</a><span class="title">{cat['emoji']} Modul {cat['id']}: {esc(cat['title'])}</span><span>🔊 de-DE</span></div>
<header class="hdr"><h1>{cat['emoji']} {esc(cat['title'])}</h1><p>{esc(cat['titleEn'])} · {len(verbs)} Wortverbindungen · B1–C1</p></header>
<div class="container">
  <div class="progressbox">
    <span>Fortschritt</span>
    <div class="bar"><div class="fill" id="progFill" style="width:0%"></div></div>
    <span id="progPct">0%</span>
    <button class="btn ghost" onclick="resetProg()">Zurücksetzen</button>
  </div>

  <div class="tabs">
    <button class="tabbtn active" data-tab="study">📚 Lernen</button>
    <button class="tabbtn" data-tab="drill">🃏 Karten</button>
    <button class="tabbtn" data-tab="fill">✍️ Lücken</button>
    <button class="tabbtn" data-tab="quiz">🎯 Quiz</button>
  </div>

  <section class="panel active" id="panel-study">
    <h2>Lernen</h2>
    <p class="lede">Arbeite die {len(verbs)} Wortverbindungen dieser Kategorie durch. Klicke eine Verbindung an, um sie zu hören.</p>
    <div id="studyList"></div>
  </section>

  <section class="panel" id="panel-drill">
    <h2>Karten</h2>
    <p class="lede">Sieh die deutsche Wortverbindung und versuche die englische Bedeutung zu erinnern. Dreh die Karte um, um die Lösung zu sehen.</p>
    <div class="progressbox"><span>Karte</span><span id="drillPos">1 / {len(verbs)}</span><div class="bar"><div class="fill" id="drillFill" style="width:0%"></div></div></div>
    <div class="flipcard" id="flipcard" onclick="flip()">
      <div class="inner">
        <div class="face front">
          <div class="speak" id="drillVerb"></div>
          <div class="hint">Klicke für die Auflösung</div>
        </div>
        <div class="face back"><div class="en" id="drillEn"></div><div class="sent" id="drillSent"></div></div>
      </div>
    </div>
    <div class="navbtns">
      <button class="btn ghost" onclick="drillPrev()">← Zurück</button>
      <button class="btn" onclick="drillNext()">Weiter →</button>
    </div>
    <p class="empty-note">Karten durchlaufen die Wortverbindungen in zufälliger Reihenfolge.</p>
  </section>

  <section class="panel" id="panel-fill">
    <h2>Lücken füllen</h2>
    <p class="lede">Vervollständige den Beispielsatz mit dem passenden Schlüsselwort der Wortverbindung.</p>
    <div class="progressbox"><span>Frage</span><span id="fillPos">1 / 10</span><div class="bar"><div class="fill" id="fillFill" style="width:0%"></div></div><span>Punkte</span><span id="fillScore">0 / 0</span></div>
    <div id="fillQ"></div>
    <div class="navbtns"><button class="btn ghost" onclick="fillReset()">Neu mischen</button></div>
    <p class="empty-note">10 zufällige Sätze aus dieser Kategorie. Wähle die richtige Ergänzung und klicke auf „Weiter“.</p>
  </section>

  <section class="panel" id="panel-quiz">
    <h2>Quiz</h2>
    <p class="lede">10 gemischte Fragetypen: Übersetzung, Bedeutung, Verbindung im Satz und Grammatik. Jede Frage ist oben beschriftet – antworte und klicke auf „Weiter“.</p>
    <div class="progressbox"><span>Frage</span><span id="quizPos">1 / 10</span><div class="bar"><div class="fill" id="quizFill" style="width:0%"></div></div><span>Punkte</span><span id="quizScore">0 / 0</span></div>
    <div id="quizQ"></div>
    <div class="navbtns"><button class="btn ghost" onclick="quizReset()">Neu mischen</button></div>
    <p class="empty-note">10 Fragen, gemischt aus allen {len(verbs)} Wortverbindungen.</p>
  </section>
</div>
<footer style="text-align:center;padding:1.6rem;color:var(--grey);font-size:.88rem">
  <p>Modul {cat['id']} von 7 · Basierend auf „Deutsch lernen B1 B2 C1 | 5.000 deutsche Wortverbindungen“ (Einfach deutsch, easy deutsch.) · <a href="../index.html" style="color:var(--red)">Kursübersicht</a></p>
</footer>
<script>
const VERBS = {verbs_js};
const CATID = {cat['id']};
{mod_js}
</script>
</body>
</html>
"""
    os.makedirs(os.path.join(HERE, cat["slug"]), exist_ok=True)
    with open(os.path.join(HERE, cat["slug"], "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {cat['slug']}/index.html")


if __name__ == "__main__":
    render_index()
    for c in CATS:
        render_module(c)
    print(f"Done. {len(CATS)} modules + index.")
