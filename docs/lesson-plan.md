# German-verbindungen · Lesson Plan (Rahmen: OLD.txt – „Ein Kurs ist ein System, kein Prompt“)

> Jeder Abschnitt entspricht **einem der 9 Design-Inputs** aus `OLD.txt`.
> Bei jeder Lerneinheit (= Modul) werden genau diese 9 Felder konsistent
> ausgefüllt, damit der Kurs als System funktioniert – nicht als einmaliger Prompt.

Lernende öffnen `index.html` (Startseite) und wählen ein Modul. Jedes Modul ist
eine einzelne, in sich geschlossene HTML-Datei: **Lernen → Karten → Lücken → Quiz**,
Fortschritt wird in `localStorage` gespeichert (offline-fähig, keine Server-Teile).

---

## Design-Input 1 · Learning goal (Lernziel)

**Ziel (Können):** Lernende verwenden am Ende **selbstständig und korrekt 119
deutsche Nomen-Verb-Wortverbindungen** in eigenen Sätzen (B1–C1), analog zur
YouTube-Episode „5.000 deutsche Wortverbindungen für natürliches Deutsch“.

**Erfolg ist eingetreten, wenn** Lernende ohne Hilfestellung
1. die Verbindung + ihre Bedeutung reproduzieren (Study/Karten),
2. die Verbindung in einen Beispielsatz korrekt einfügen (Lücken),
3. Bedeutung, Verwendung und Grammatik in gemischten Quiz-Fragen sicher beantworten.

**Könnens-Stufe:** B1–C1 · **Zielebene:** Produktion + Verstehen, nicht nur Erkennen.

---

## Design-Input 2 · Lesson sequence (Unterrichtssequenz)

7 Module = 7 Blöcke der Episode, in wachsender Progression:

| Modul | Slug | Titel | Anzahl |
|---|---|---|---|
| 1 | `01-alltag-wohnen` | Alltag & Wohnen | 18 |
| 2 | `02-kommunikation-gefuehle` | Kommunikation & Gefühle | 20 |
| 3 | `03-arbeit-aufgaben` | Arbeit & Aufgaben | 20 |
| 4 | `04-bewegung-aktivitaeten` | Bewegung & Aktivitäten | 16 |
| 5 | `05-denken-entscheiden` | Denken & Entscheiden | 16 |
| 6 | `06-beziehungen-soziales-leben` | Beziehungen & soziales Leben | 20 |
| 7 | `07-finale` | Das große Finale | 9 |

Jedes Modul geht durch die **4-Phasen-Sequenz** des interaktiven Apps:
**Study → Drill (Karten) → Fill (Lücken) → Quiz**. Modul 7 (Finale) bündelt die
wichtigsten Verbindungen quer über die Kategorien.

---

## Design-Input 3 · Assessment evidence / EES (Beurteilung durch Evidenz)

Die Beurteilung ist **in die Lernaktivität eingebaut** (EES – „check for understanding at every stage“):

- **Study:** Selbst-Prüfung – „Kann ich es erklären?“
- **Drill (Karten):** aktive Erinnerung der Bedeutung vor dem Umdrehen.
- **Fill (Lücken):** Schriftliches Einsetzen zeigt, ob Satzstellung klickbar ist.
- **Quiz:** 10 Fragen/Kategorie (DE→EN, EN→DE, Bedeutung, Satzkontext, Grammatik)
  mit sofortigem Score.

→ Evidenz = aktuelle Punktzahl + Fortschrittsbalken, sichtbar und gespeichert.

---

## Design-Input 4 · Learner profile (Lernprofil)

- **Wer:** erwachsene Deutschlernende B1–C1 (jugendlich/erwachsen), die die Episode
  bereits gehört haben und jetzt **aktiv** mit den Wortverbindungen üben wollen.
- **Nutzer-Formfaktor:** Desktop/Laptop + Handy; Browser mit Web Speech (de-DE).
- **Pacing:** selbstbestimmt, Wiederholung erlaubt, Fortschritt bleibt dauerhaft.

---

## Design-Input 5 · Prior knowledge (Vorwissen)

Vorausgesetzt (aus `grammar`-Feld der Daten):
- Basisverben A2–B1, Satzstellung Hauptsatz, trennbare Verben, reflexive Verben.
- Nomen-Verb-Verbindungen als **Konzept** im B1–C1-Kurs: die Nomen-Verb-Verbindung
  trägt die Bedeutung („eine Frage stellen“), nicht das einzelne Verb.

Nicht vorausgesetzt: Wortschatz der konkreten Verbindungen – der wird **im Kurs** gelernt.

---

## Design-Input 6 · Learning activities (Lernaktivitäten)

Jede Karte/Verbindung wird in vier Aktivitäten trainiert:

1. **Study / Lernen** – Verbindung + englische Bedeutung + deutsche Bedeutung +
   natürlicher Beispielsatz.
2. **Drill / Karten** – Flashcards: deutsche Verbindung sehen → Bedeutung erinnern,
   dann aufdecken (mit 🔊 Aussprache).
3. **Fill / Lücken** – Beispielsatz mit Lücke → die richtige Verbindung einsetzen.
4. **Quiz** – gemischte Fragen zu allen Verbindungen des Moduls in zufälliger Reihenfolge.

**Alle Beispiele und Verbindungen sind 1:1 aus `data/verbindungen.json`.**
(Generiert von `_merge.py` aus `_work/cat*.json` – keine erfundenen Sätze.)

---

## Design-Input 7 · Output requirements (Output-Forderungen)

- **Reine statische Website** (kein Build zur Laufzeit, keine Server): `index.html`
  + 7 Modul-Ordner `0X-*/index.html`.
- **Self-contained:** CSS + JS inline im HTML; Daten embeddet; funktioniert auch
  per `file://` (data-empty-Fallback, wenn `data/verbindungen.json` fehlt).
- **Audio:** Web Speech API de-DE (Browser-Stimme) für jede Verbindung und jeden
  Beispielsatz – kein externer Dienst.
- **Fortschritt:** `localStorage` (Schlüssel `gvw-*`), `Reset`-Button je Modul.

---

## Design-Input 8 · Accessibility & supports (Barrierefreiheit & Hilfen)

- 🔊 **Hear-it:** jedes Wort/Beispiel laut vorlesbar (de-DE) – macht das Material
  auch als reines Hör-/Mitlese-Kurs nutzbar.
- **Mehrere Repräsentationen:** Schrift + Audio + Übersetzung + Grammatik-Hinweis.
- **Kontrast/farbliche Kennzeichnung** über `_work/module.css` (erbt von german-verbs).
- **Fortschritt = Eigenkontrolle**, keine Bestrafung (kein Timer, freies Wiederholen).

---

## Design-Input 9 · Teacher decisions (Lehrer-Entscheidungen)

- **Didaktische Reihenfolge** wird übernommen und **nicht** umsortiert (Video-Flow).
- **Wiederholungen zwischen Kategorien sind gewollt**: Eine Verbindung wie
  „eine Frage stellen“ taucht bewusst in mehreren Modulen auf (Recycling vor Behalten).
- **Deutsche Bedeutung** (nicht nur EN-Übersetzung) wird immer mitgeliefert –
  Entscheidung für kontextualisiertes, natürliches Lernen.
- **Kanal-Zuordnung:** YouTube-Video `2tygr202mYI` von „Einfach deutsch, easy deutsch.“
