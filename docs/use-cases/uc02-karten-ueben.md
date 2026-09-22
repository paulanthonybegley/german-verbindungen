# Use-Case 02 · Modul per Kartenübung (Drill)

**Akteur:** Deutschlernende (B1–C1) · **Auslöser:** Klick auf Tab „Karten“

**Hauptablauf**
1. App zeigt virtuelle Karte mit der deutschen Wortverbindung auf der Vorderseite
   („eine Frage stellen“).
2. Lernende versucht, Bedeutung (DE + EN) zu erinnern.
3. Klick auf die Karte + 🔊 → Karte dreht sich; Rückseite zeigt englische
   Bedeutung, den Beispielsatz und den natürlichen Beispielsatz.
4. Lernende bewertet: „Gewusst“ / „Noch üben“ (→ Karte merkt sich die Verbindung
   als Wiederholungskandidat).
5. App mischt weiter, bis alle Karten durchlaufen sind.

**Nachbedingung:** Kartenfortschritt in `localStorage` (Fortschrittsbalken).

## Variationen
- **TTS fehlt:** Karten funktionieren ohne Ton (Wort bleibt sichtbar, kein Audio).
- **Lernende nutzt „Noch üben“:** betroffene Verbindung erscheint häufiger
  (Recycling statt Endlos-Üben).
