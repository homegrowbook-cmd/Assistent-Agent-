# Scripts Directory

This directory contains utility scripts for the Plant Analysis Lab application.

## analyze_plant.py

Python script that demonstrates how to integrate a real AI vision model (OpenAI's GPT-4 Vision) with the application.

### Prerequisites

```bash
pip install openai Pillow
```

### Usage

```bash
# Set your OpenAI API key
export OPENAI_API_KEY='your-api-key-here'

# Analyze an image
python scripts/analyze_plant.py \
  --image path/to/plant.jpg \
  --plant-id my-plant-001 \
  --output analysis-result.json
```

### Options

- `--image`: Path to the plant image (required)
- `--plant-id`: Identifier for the plant (required)
- `--output`: Output JSON file path (optional, prints to stdout if not specified)
- `--api-key`: OpenAI API key (optional, overrides environment variable)

### Example Output

```json
{
  "timestamp": "2024-01-15T10:30:00.000000",
  "plant_id": "my-plant-001",
  "image_url": "data:image/jpeg;base64,...",
  "analysis": {
    "flower_volume": "High",
    "flower_density": "Dense",
    "color_health": "Vibrant green with healthy coloration",
    "leaf_condition": "Excellent - minor edge browning on lower leaves",
    "stress_signs": "No significant stress indicators detected",
    "general_structure": "Well-developed branching with good canopy structure",
    "trichome_development": "Cloudy trichomes with approximately 10% amber",
    "overall_health_score": 92
  }
}
```

## Integration with Application

To integrate this script with the web application:

1. Create a GitHub Action that calls this script
2. Store results in the repository or cloud storage
3. Update the frontend to fetch results from the storage location

See API_DOCUMENTATION.md for detailed integration instructions.
