# Use-Case 04 · Quiz (10 gemischte Fragen)

**Akteur:** Deutschlernende:r (B1–C1)
**Vorbedingung:** Modul-App geöffnet, Tab **Quiz** gewählt

**Hauptablauf**
1. App wählt 10 Verbindungen (zufällig, aus dem gesamten Modul) und baut einen
   gemischten Fragepfeil: ✓ DE→EN · ✓ EN→DE · ✓ Bedeutung Wort · ✓ Beispiel
   einsetzen · ✓ Grammatik.
2. Pro Frage:
   a. Fragetyp-Label oben („Übersetzung“, „Bedeutung“, „Im Satz“, „Grammatik“).
   b. Lernende:r antwortet per Button-Wahl (4 Optionen).
   c. Sofort-Feedback ✅/❌ + ggf. richtige Antwort + 🔊.
3. Nach 10 Fragen: Endbildschirm mit **Punkte X/Y** und „Neu mischen“ (neue Fragen).

**Nachbedingung:** Score + Fortschritt in `localStorage`; Wiederholung möglich.

## Sonderfall (AD-0004)
Wenn `data/verbindungen.json` leer/fehlt, beginnt jede Modul-App mit einer
`OF`-Prüfung (`VERBS.length === 0`) und zeigt eine leere Anzeige
„Noch keine Daten – baue den Kurs mit `python3 _merge.py`“ statt der Quiz-Fragen.
