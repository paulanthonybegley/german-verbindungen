# Wortverbindungen – Daten-Schema

Jede Kategorie-Datei ist ein JSON-Array von Wortverbindungs-Objekten.

```json
[
  {
    "verbindung": "eine Entscheidung treffen",
    "en": "to make a decision",
    "meaning": "selbst bestimmen, was als Nächstes passiert, nachdem man alle Möglichkeiten abgewogen hat.",
    "example": "Ich muss heute eine wichtige Entscheidung treffen.",
    "natural": "Man sollte nicht zu schnell eine wichtige Entscheidung treffen, sondern erst alle Vor- und Nachteile abwägen.",
    "grammar": "Nomen-Verb-Verbindung · Artikel: eine · Perfekt: ich habe getroffen"
  }
]
```

## Feldhinweise

- `verbindung`: die feste Kollokation in der im Video gesprochenen Form (z. B. „eine Entscheidung treffen“). „sich“ bleibt bei reflexiven Wendungen erhalten.
- `en`: prägnante englische Glosse („to make a decision“).
- `meaning`: deutsche Erklärung auf B1–C1-Niveau.
- `example`: der erste, einfache Beispielsatz (startet meist mit „Ich …“).
- `natural`: der „natürlichere“, umgangssprachliche Varianten-Satz.
- `grammar`: Nomen-Verb-Verbindung / Funktionsverbgefüge · Artikel/Kasus · Perfekt-Hilfsverb.

## Regeln

- Pro Kategorie genau die in der Datei angegebene Anzahl Wortverbindungen extrahieren.
- Keine Verbindungen erfinden – nur solche, die in der Episode wirklich besprochen werden.
- Offensichtliche Transkript-Tippfehler korrigieren (z. B. „einfluss treffen“ → „eine Entscheidung treffen“).
