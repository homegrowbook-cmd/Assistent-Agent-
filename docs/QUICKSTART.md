# Quick Start Guide

## 🚀 In 5 Minuten starten

### 1. Installation (2 Minuten)

```bash
# Repository klonen
git clone https://github.com/homegrowbook-cmd/Assistent-Agent-.git
cd Assistent-Agent-

# Automatisches Setup (Linux/Mac)
bash setup.sh

# Oder manuell:
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Erste Bilder hinzufügen (1 Minute)

```bash
# Kopiere deine Pflanzenbilder
cp /pfad/zu/deinen/bildern/*.jpg images/uploads/

# Oder erstelle Test-Bilder
# (Füge beliebige Pflanzenfotos hinzu)
```

### 3. Assistenten starten (1 Minute)

```bash
python assistant.py
```

### 4. Ergebnisse ansehen (1 Minute)

```bash
# Logs ansehen
cat assistant.log

# Generierte Posts ansehen
ls output/
cat output/post_*.txt

# Analysierte Bilder prüfen
ls images/analyzed/
```

## 📝 Daten hinzufügen (Optional)

Erstelle `data/my_grow.json`:

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

Dann erneut ausführen:
```bash
python assistant.py
```

## 🎯 Nächste Schritte

1. Lies die vollständige [README.md](README.md)
2. Schau dir die [ROADMAP.md](ROADMAP.md) an
3. Passe [config.yaml](config.yaml) an deine Bedürfnisse an
4. Automatisiere mit Cron oder Task Scheduler

## 💡 Tipps

- **Gute Bildqualität**: Nutze gutes Licht und konstante Winkel
- **Regelmäßige Updates**: Füge regelmäßig neue Bilder hinzu
- **Daten tracken**: Führe ein Datenlog für bessere Einblicke
- **Backup**: Sichere dein `images/` Verzeichnis regelmäßig

## 🆘 Probleme?

- Prüfe `assistant.log` für Fehlermeldungen
- Stelle sicher, dass Python 3.8+ installiert ist
- Überprüfe, ob alle Abhängigkeiten installiert sind
- Öffne ein [Issue](https://github.com/homegrowbook-cmd/Assistent-Agent-/issues) auf GitHub

## 🎉 Fertig!

Der Assistent läuft jetzt und analysiert deine Bilder automatisch!
