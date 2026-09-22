# Use-Case 01 · Modul durcharbeiten (Studieren)

**Akteur:** Deutschlernende:r (B1–C1)
**Vorbedingung:** `index.html` der Kurs-App geöffnet

**Hauptablauf**
1. Lernende:r wählt eine Modul-Karte (z. B. „01 Alltag & Wohnen“).
2. App öffnet das Modul `01-alltag-wohnen/index.html`; Tab **Studieren** ist aktiv.
3. Liste aller 18 Wortverbindungen erscheint: **Verbindung · Bedeutung · Bedeutung-EN ·
   Beispielsatz · natürlicher Satz · Grammatik**.
4. Klick auf eine Verbindung oder deren Beispielsatz ▶ spricht sie deutsch aus (de-DE).
5. Lernende:r arbeitet in eigenem Tempo durch die Liste.

**Nachbedingung:** Fortschritt unverändert („Studieren“ zählt nicht zum %-Fortschritt);
kein Fehlerfall.

## Varianten
- TTS nicht verfügbar (Browser ohne `speechSynthesis`): Klick ohne Wirkung,
  Liste bleibt voll nutzbar.
- „Studieren“ wird übersprungen (direkt zu Karten): erlaubt, Fortschritt zählt erst
  ab aktiver Übung.
