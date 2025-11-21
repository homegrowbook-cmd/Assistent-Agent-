# Contributing to Grow Documentation Assistant

Vielen Dank für dein Interesse, zu diesem Projekt beizutragen! 🌱

## Wie kann ich beitragen?

### 1. Fehler melden (Bug Reports)

Wenn du einen Fehler gefunden hast:

1. Prüfe, ob der Fehler bereits [gemeldet](https://github.com/homegrowbook-cmd/Assistent-Agent-/issues) wurde
2. Erstelle ein neues Issue mit:
   - Klarer Beschreibung des Problems
   - Schritten zur Reproduktion
   - Erwartetes vs. tatsächliches Verhalten
   - Python-Version und Betriebssystem
   - Relevante Log-Ausgaben

### 2. Feature-Vorschläge

Hast du eine Idee für eine neue Funktion?

1. Prüfe die [Roadmap](ROADMAP.md)
2. Schaue in die [Diskussionen](https://github.com/homegrowbook-cmd/Assistent-Agent-/discussions)
3. Erstelle ein Issue mit:
   - Beschreibung des Features
   - Anwendungsfall
   - Mögliche Implementierung

### 3. Code-Beiträge

#### Vorbereitung

1. **Fork das Repository**
   ```bash
   # Auf GitHub auf "Fork" klicken
   ```

2. **Clone deinen Fork**
   ```bash
   git clone https://github.com/DEIN-USERNAME/Assistent-Agent-.git
   cd Assistent-Agent-
   ```

3. **Erstelle einen Branch**
   ```bash
   git checkout -b feature/meine-neue-funktion
   # oder
   git checkout -b fix/fehler-beschreibung
   ```

4. **Setup Development Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Falls vorhanden
   ```

#### Development

1. **Mache deine Änderungen**
   - Halte Änderungen fokussiert und klein
   - Folge dem bestehenden Code-Stil
   - Kommentiere komplexen Code

2. **Teste deine Änderungen**
   ```bash
   # Syntax-Check
   python3 -m py_compile assistant.py modules/*.py
   
   # Funktionstest
   python3 assistant.py
   ```

3. **Commit deine Änderungen**
   ```bash
   git add .
   git commit -m "feat: Beschreibung der Änderung"
   ```

   **Commit-Nachricht-Format:**
   - `feat:` - Neue Funktion
   - `fix:` - Fehlerbehebung
   - `docs:` - Dokumentation
   - `style:` - Formatierung
   - `refactor:` - Code-Refactoring
   - `test:` - Tests
   - `chore:` - Maintenance

4. **Push zu deinem Fork**
   ```bash
   git push origin feature/meine-neue-funktion
   ```

5. **Erstelle einen Pull Request**
   - Gehe zu deinem Fork auf GitHub
   - Klicke "New Pull Request"
   - Beschreibe deine Änderungen
   - Verlinke relevante Issues

### 4. Dokumentation

Hilf uns, die Dokumentation zu verbessern:

- README.md ergänzen
- Beispiele hinzufügen
- Tutorials schreiben
- Kommentare verbessern
- Übersetzungen

### 5. Tests

- Teste neue Features
- Berichte Probleme
- Gib Feedback zu Usability
- Teile deine Erfahrungen

## Code-Stil

### Python

- Folge [PEP 8](https://pep8.org/)
- Verwende aussagekräftige Variablennamen
- Schreibe Docstrings für Funktionen und Klassen
- Halte Funktionen kurz und fokussiert

**Beispiel:**
```python
def analyze_image(image_path):
    """Analyze a plant image.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Dictionary with analysis results
        
    Raises:
        FileNotFoundError: If image doesn't exist
    """
    # Implementation
    pass
```

### Dokumentation

- Schreibe klare, präzise Dokumentation
- Nutze Beispiele
- Formatiere mit Markdown
- Verwende Emoji sparsam aber hilfreich

## Projekt-Struktur

```
Assistent-Agent-/
├── assistant.py           # Hauptskript - Entry point
├── modules/               # Kern-Module
│   ├── image_analyzer.py # Bildanalyse
│   ├── data_evaluator.py # Datenauswertung
│   └── post_generator.py # Post-Generierung
├── images/               # Bild-Management
├── data/                 # Daten-Storage
└── docs/                 # Dokumentation
```

## Review-Prozess

1. **Automatische Checks**
   - Code-Syntax wird geprüft
   - Tests werden ausgeführt (falls vorhanden)

2. **Code Review**
   - Maintainer prüfen deinen Code
   - Feedback wird gegeben
   - Änderungen werden angefragt

3. **Merge**
   - Nach Approval wird der PR gemergt
   - Deine Änderungen sind im Projekt!

## Fragen?

- Öffne ein Issue
- Starte eine Diskussion
- Schau in die Dokumentation

## Code of Conduct

Sei respektvoll und konstruktiv:

- ✅ Hilfsbereit und freundlich
- ✅ Konstruktives Feedback
- ✅ Respektvoller Umgang
- ❌ Beleidigungen
- ❌ Harassment
- ❌ Diskriminierung

## Lizenz

Mit deinem Beitrag stimmst du zu, dass deine Arbeit unter der gleichen Lizenz wie das Projekt veröffentlicht wird.

---

**Danke für deinen Beitrag!** 🙏

Jeder Beitrag, egal wie klein, macht das Projekt besser!
