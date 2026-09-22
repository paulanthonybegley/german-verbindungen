# ADR-0002 · Fortschritt in `localStorage` (pro Modul)

**Status:** Angenommen · **Datum:** 2026-09-20

## Kontext
Der Kurs soll Fortschritt und Quiz-Punkte dauerhaft merken, damit Wiederholungen
am nächsten Tag weitergehen – aber ohne Account, ohne Backend, offline.

## Entscheidung
- Jede Modul-App speichert unter dem Schlüssel `gvw-<catid>-progress`
  einen Prozentwert (0–100) in `localStorage`.
- Quiz-Fortschritt/Zähler je Sitzung bleiben im Speicher (Session-Reset bei „Neu mischen“).
- Alle Zustände sind **pro Kategorie** isoliert (`CATID` im Scope), nie global.
- `storage`-Event: Aktualisiert die Startseiten-Balken sofort, wenn ein Modul offen ist.

## Konsequenzen
- ✅ Offline & ohne Server; datenschutzfreundlich (nichts verlässt den Browser).
- ⚠️ Nur ein Browser/Gerät (kein Sync). Akzeptiert – das Video ist ein
  gespeichertes Lernziel pro Gerät.
- ⚠️ `localStorage` funktioniert nicht bei `file://` mit deaktivierten
  „zulassen Sie lokal gespeicherte Daten“ – in dem Fall fällt die App auf
  In-Memory-Sitzungsfortschritt zurück (kein Crash).
