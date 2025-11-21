# Usage Guide

## Grundlegende Verwendung

### Bilder analysieren

1. **Bilder vorbereiten**
   - Verwende hochauflösende Bilder (mindestens 800x600 Pixel)
   - Gutes, gleichmäßiges Licht
   - Fokussiere auf die Pflanze
   - Vermeide starke Schatten

2. **Bilder hochladen**
   ```bash
   cp /pfad/zu/bildern/*.jpg images/uploads/
   ```

3. **Assistent ausführen**
   ```bash
   python assistant.py
   ```

4. **Ergebnisse prüfen**
   - Log-Datei: `assistant.log`
   - Analysierte Bilder: `images/analyzed/`
   - Generierte Posts: `output/`

### Daten auswerten

1. **Daten sammeln**
   - Temperatur
   - Luftfeuchtigkeit
   - Pflanzenhöhe
   - Wachstumsphase
   - Notizen

2. **JSON-Datei erstellen**
   ```json
   {
     "environment": {
       "temperature": 24,
       "humidity": 55,
       "date": "2025-11-21"
     },
     "growth": {
       "height": 25,
       "stage": "vegetative"
     }
   }
   ```

3. **Datei speichern**
   ```bash
   # Speichere als data/mein_grow_DATUM.json
   nano data/my_grow_2025-11-21.json
   ```

4. **Auswertung durchführen**
   ```bash
   python assistant.py
   ```

### Posts erstellen

Posts werden automatisch erstellt, wenn:
- Neue Bilder analysiert wurden
- Neue Daten ausgewertet wurden
- Änderungen erkannt wurden

**Manuell:**
```python
from assistant import GrowAssistant

assistant = GrowAssistant()
post = assistant.generate_post()
print(post)
```

## Erweiterte Verwendung

### Batch-Verarbeitung

Mehrere Bilder auf einmal verarbeiten:

```bash
# Alle Bilder in ein Verzeichnis kopieren
cp /pfad/zu/vielen/bildern/*.jpg images/uploads/

# Einmal ausführen
python assistant.py
```

### Automatisierung

#### Linux/Mac (Cron)

```bash
# Crontab bearbeiten
crontab -e

# Täglich um 9 Uhr ausführen
0 9 * * * cd /pfad/zu/Assistent-Agent- && /pfad/zu/venv/bin/python assistant.py
```

#### Windows (Task Scheduler)

1. Task Scheduler öffnen
2. "Aufgabe erstellen"
3. Trigger: Täglich, 9:00 Uhr
4. Aktion: Python-Script ausführen
5. Script: `C:\pfad\zu\assistant.py`

### Konfiguration anpassen

Bearbeite `config.yaml`:

```yaml
# Bildanalyse-Einstellungen
image_analysis:
  supported_formats:
    - jpg
    - png
  max_size_mb: 10

# Datenauswertung
data_evaluation:
  temperature_range:
    min: 18
    max: 28

# Post-Generierung
post_generation:
  auto_generate: true
  include_hashtags: true
```

### Module einzeln verwenden

#### Nur Bildanalyse

```python
from modules.image_analyzer import ImageAnalyzer
from modules.config_manager import ConfigManager

config = ConfigManager()
analyzer = ImageAnalyzer(config)

result = analyzer.analyze('path/to/image.jpg')
print(result)
```

#### Nur Datenauswertung

```python
from modules.data_evaluator import DataEvaluator
from modules.config_manager import ConfigManager

config = ConfigManager()
evaluator = DataEvaluator(config)

insights = evaluator.evaluate()
for insight in insights:
    print(insight['message'])
```

#### Nur Post-Generierung

```python
from modules.post_generator import PostGenerator
from modules.config_manager import ConfigManager

config = ConfigManager()
generator = PostGenerator(config)

post = generator.generate(
    image_analysis=[...],
    data_insights=[...]
)
print(post)
```

## Best Practices

### Bildaufnahme

1. **Konsistenz**
   - Gleicher Standort
   - Gleiche Tageszeit
   - Gleicher Winkel
   - Gleiche Beleuchtung

2. **Qualität**
   - Mindestens 1920x1080 Pixel
   - Gute Beleuchtung
   - Scharfer Fokus
   - Keine Unschärfe

3. **Dokumentation**
   - Datumsstempel im Dateinamen
   - Pflanzen-ID im Namen
   - Wachstumsphase im Namen
   - Beispiel: `2025-11-21_plant-A_veg_week2.jpg`

### Datenpflege

1. **Regelmäßigkeit**
   - Täglich: Temperatur, Luftfeuchtigkeit
   - Wöchentlich: Höhe, Entwicklung
   - Bei Bedarf: Besonderheiten

2. **Genauigkeit**
   - Verwende Messinstrumente
   - Dokumentiere Änderungen
   - Notiere Probleme

3. **Backup**
   - Sichere `data/` regelmäßig
   - Sichere `images/` regelmäßig
   - Verwende Git für Versionskontrolle

### Post-Optimierung

1. **Hashtags**
   - Relevant und spezifisch
   - Mix aus allgemein und speziell
   - 5-10 Hashtags pro Post

2. **Zeitpunkt**
   - Optimale Zeit für deine Zielgruppe
   - Konsistenter Zeitplan
   - Automatisierung nutzen

3. **Inhalt**
   - Klare Bilder
   - Informative Daten
   - Interessante Insights

## Fehlerbehebung

### "No module named 'PIL'"

```bash
pip install Pillow
```

### "Config file not found"

Der Assistent verwendet Standard-Einstellungen.  
Optional: Kopiere `config.yaml` und passe an.

### "No images to process"

Stelle sicher, dass:
- Bilder in `images/uploads/` liegen
- Format ist JPG oder PNG
- Dateien sind nicht beschädigt

### "Error analyzing image"

Prüfe:
- Bildformat (JPG, PNG)
- Bildgröße (< 10MB)
- Datei ist nicht beschädigt
- Leseberechtigung vorhanden

## Tipps & Tricks

1. **Verwende aussagekräftige Dateinamen**
   ```
   2025-11-21_plant-A_day14_morning.jpg
   ```

2. **Erstelle ein Backup-Script**
   ```bash
   #!/bin/bash
   tar -czf backup_$(date +%Y%m%d).tar.gz images/ data/
   ```

3. **Nutze Git für Versionskontrolle**
   ```bash
   git add data/ images/
   git commit -m "Update: $(date +%Y-%m-%d)"
   ```

4. **Erstelle wöchentliche Summaries**
   ```python
   weekly_data = {
       'images_processed': 7,
       'avg_health': 'Good',
       'notes': 'Starkes Wachstum diese Woche'
   }
   post = generator.generate_weekly_summary(weekly_data)
   ```

## Weitere Ressourcen

- [README.md](../README.md) - Übersicht
- [QUICKSTART.md](QUICKSTART.md) - Schnellstart
- [ROADMAP.md](../ROADMAP.md) - Zukünftige Features
- [GitHub Issues](https://github.com/homegrowbook-cmd/Assistent-Agent-/issues) - Support
