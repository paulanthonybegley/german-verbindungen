# ADR-0003 · Audio = Web Speech API (de-DE), kein Audioclip

**Status:** Angenommen · **Datum:** 2026-09-20

## Kontext
`module.js` spricht deutsche Wörter und Sätze per „Klick auf das Wort“ aus.
Die Episode liefert keinen separaten Audio-Datei-Stream; wir hosten bewusst
keine MP3-Dateien (Lizenz/Reihe deutscher Stimmen nicht geklärt fürs Repo).

## Entscheidung
- Aussprache über die **Web Speech API** (`speechSynthesis`, Stimme `de-DE`,
  Rate ~0.95), reine Browser-Stimme – kein externer TTS-Dienst.
- Jede Verbindung + jeder Beispielsatz ist hörbar (Schaltfläche 🔊 / Wortklick).

## Konsequenzen
- ✅ 100 % offline, keine Lizenzprobleme, kein Server.
- ⚠️ Stimme variiert je Browser/OS (Chrome de-DE am stabilsten). Hinweis auf
  Startseite: „Stimme hängt vom Browser ab“.
- ⚠️ Kein Menü mit von Menschen besprochenem Audio wie im Original-Video –
  der Kurs ist **Übungsbegleiter**, nicht Ersatz für die Episode.
- ⚠️ `speechSynthesis` braucht Nutzerinteraktion (Klick) – im Quiz/Study immer
  durch Klick ausgelöst, nie automatisch beim Laden.
