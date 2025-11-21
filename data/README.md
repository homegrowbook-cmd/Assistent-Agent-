# Data Directory

Store your grow data files here.

## Format
JSON files with the following structure:

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
      "notes": "First week of vegetative stage"
    }
  ]
}
```

## Example Files
Check `data/example_data.json` for a complete example (coming soon)

## Data Collection
- Manual entry via text editor
- CSV import (coming soon)
- Sensor integration (planned)
