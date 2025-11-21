# 🌱 Grow Documentation Assistant

Ein intelligenter GitHub-basierter Assistent für die Dokumentation von Grow-Projekten. Der Assistent analysiert automatisch Bilder, wertet Daten aus und erstellt Social-Media-Posts.

## ✨ Features

- 📸 **Bildanalyse**: Automatische Analyse von Pflanzenbildern
  - Gesundheitsbewertung
  - Farbanalyse (Grünanteil, Helligkeit)
  - Wachstumserkennung
  
- 📊 **Datenauswertung**: Intelligente Auswertung von Grow-Daten
  - Umgebungsbedingungen (Temperatur, Luftfeuchtigkeit)
  - Wachstumsmetriken
  - Historische Trends
  - Automatische Warnungen
  
- 📝 **Post-Generierung**: Automatische Erstellung von Social-Media-Posts
  - Basierend auf Bildanalyse
  - Integriert Dateneinblicke
  - Formatiert für verschiedene Plattformen
  
- 🗂️ **Bildspeicherung**: Organisiertes Bildmanagement
  - Upload-Verzeichnis für neue Bilder
  - Analysierte Bilder mit Ergebnissen
  - Archiv für historische Daten

## 🚀 Schnellstart

### Installation

1. **Repository klonen**
```bash
git clone https://github.com/homegrowbook-cmd/Assistent-Agent-.git
cd Assistent-Agent-
```

2. **Virtuelle Umgebung erstellen (empfohlen)**
```bash
python -m venv venv
source venv/bin/activate  # Auf Windows: venv\Scripts\activate
```

3. **Abhängigkeiten installieren**
```bash
pip install -r requirements.txt
```

### Grundlegende Verwendung

1. **Bilder hochladen**
   - Lege deine Pflanzenbilder in `images/uploads/` ab
   - Unterstützte Formate: JPG, JPEG, PNG

2. **Daten hinzufügen (optional)**
   - Erstelle JSON-Dateien in `data/` mit deinen Grow-Daten
   - Siehe `data/README.md` für Format-Beispiele

3. **Assistenten ausführen**
```bash
python assistant.py
```

Der Assistent wird:
- Neue Bilder analysieren
- Daten auswerten
- Posts generieren
- Ergebnisse in `output/` speichern

## 📁 Verzeichnisstruktur

```
Assistent-Agent-/
├── assistant.py              # Hauptskript
├── config.yaml              # Konfigurationsdatei
├── requirements.txt         # Python-Abhängigkeiten
├── ROADMAP.md              # Projekt-Roadmap
│
├── modules/                 # Kernmodule
│   ├── image_analyzer.py   # Bildanalyse
│   ├── data_evaluator.py   # Datenauswertung
│   ├── post_generator.py   # Post-Generierung
│   └── config_manager.py   # Konfigurationsverwaltung
│
├── images/                  # Bildverwaltung
│   ├── uploads/            # Neue Bilder hier ablegen
│   ├── analyzed/           # Analysierte Bilder
│   └── archive/            # Archiv
│
├── data/                    # Grow-Daten
├── docs/                    # Dokumentation
└── output/                  # Generierte Posts
```

## 🔧 Konfiguration

Bearbeite `config.yaml` um anzupassen:

- Bildanalyseparameter
- Datenauswertungsregeln
- Post-Generierungseinstellungen
- Verzeichnispfade
- GitHub-Integration (optional)
- Benachrichtigungen (optional)

## 📊 Beispiel: Datenformat

Erstelle eine JSON-Datei in `data/` mit folgendem Format:

```json
{
  "environment": {
    "temperature": 24,
    "humidity": 55,
    "light_hours": 18,
    "date": "2025-11-21"
  },
  "growth": {
    "height": 25,
    "stage": "vegetative",
    "health": "good"
  },
  "history": [
    {
      "date": "2025-11-14",
      "height": 18,
      "notes": "Erste Woche vegetativ"
    }
  ]
}
```

## 📸 Beispiel: Bildanalyse-Output

```
🌱 Grow Update 🌱

Date: 2025-11-21 10:30

📸 Image Analysis:
  Image 1: plant_day14.jpg
    Health: Good - Healthy green color
    Green dominance: 1.25
    Brightness: 145.3/255

📊 Data Insights:
  ℹ️ Information:
    • Temperature is optimal (24°C).
    • Humidity is good (55%).
    • Current plant height: 25cm
    • Current growth stage: vegetative

---
#grow #plants #documentation #gardening
```

## 🗺️ Roadmap

Siehe [ROADMAP.md](ROADMAP.md) für:
- Aktuelle Phase und Features
- Geplante Funktionen
- Zeitplan
- Langfristige Ziele

**Aktuelle Phase**: Phase 1 (Foundation) ✅  
**Nächste Phase**: Phase 2 (Enhanced Image Analysis)

## 🤝 Beitragen

Wir freuen uns über Beiträge! So kannst du helfen:

1. **Issues melden**: Fehler gefunden? Öffne ein Issue!
2. **Feature-Requests**: Hast du eine Idee? Teile sie mit uns!
3. **Code-Beiträge**: Fork, entwickle, und reiche einen PR ein
4. **Dokumentation**: Hilf uns, die Docs zu verbessern
5. **Tests**: Teste neue Features und gib Feedback

## 📋 Systemanforderungen

- Python 3.8 oder höher
- 2GB RAM (empfohlen: 4GB)
- 500MB freier Festplattenspeicher
- Internetverbindung (für GitHub-Integration)

## 🔐 Sicherheit & Datenschutz

- Alle Daten werden lokal gespeichert
- Keine automatische Übertragung ohne deine Zustimmung
- GitHub-Integration ist optional
- Konfiguriere `.env` für sensible Daten (nicht im Repo)

## 📝 Lizenz

Dieses Projekt ist noch in Entwicklung. Lizenzinformationen folgen.

## 🆘 Support

- **Dokumentation**: Siehe `docs/` Verzeichnis
- **Issues**: [GitHub Issues](https://github.com/homegrowbook-cmd/Assistent-Agent-/issues)
- **Diskussionen**: [GitHub Discussions](https://github.com/homegrowbook-cmd/Assistent-Agent-/discussions)

## 🙏 Danksagungen

Danke an alle Mitwirkenden und die Open-Source-Community!

---

**Version**: 1.0.0  
**Status**: Phase 1 Complete  
**Letztes Update**: 2025-11-21