# ADR-0004 · Offline-Fallback für leere Daten (`data-empty`)

**Status:** Angenommen · **Datum:** 2026-09-20

## Kontext
Die generierten Seiten betten `const VERBS = [...]` direkt ein – falls also
jemand eine Modul-`index.html` **vor** dem Mergen/Generieren öffnet oder die
Generator-Datenkette unterbrochen wird, darf die App nicht abstürzen,
sondern muss einen klaren Hinweis zeigen.

## Entscheidung
- `_work/module.js` beginnt mit einer **Robustheitsprüfung**:
  ```js
  if (typeof VERBS === "undefined" || !Array.isArray(VERBS) || VERBS.length === 0) {
    document.getElementById("studyList").innerHTML =
      "<p class='empty-note'>Noch keine Daten. Öffne zuerst die Kursübersicht oder baue den Kurs: python3 _merge.py && python3 _generate.py</p>";
    return; // Quiz/Karten/Lücken deaktivieren sich automatisch (leere Arrays)
  }
  ```
- Gleiche Prüfung für die Kategorie-Zusammenfassung auf `index.html`
  (wenn `data/verbindungen.json` fehlt → freundlicher „Noch nicht generiert“-Hinweis).
- Die Startseiten-Leiste (`context.md`/`index.css`) fällt ebenso auf „0 %“ ohne Fehler.

## Konsequenzen
- ✅ Kurs öffnet immer, auch halb gebaut / leer – Fehlerquellen (Tippfehler,
  vergessenes Mergen) werden sichtbar statt stillschweigend falsch.
- ✅ Kleine, wartbare Absicherung an genau einer Stelle (`module.js`/`index.js`).
- ⚠️ Kein „lebender“ Leerkurs – der Hinweis ist bewusst keine Teststrecke.
