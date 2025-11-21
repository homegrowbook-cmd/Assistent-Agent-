# API Documentation

## Vision Model Integration Guide

This document describes how to integrate a real AI vision model with the Plant Analysis Lab application.

## Current Implementation

The current implementation uses a mock analysis function in `src/lib/analysis.ts`. This simulates the behavior of an AI vision model but doesn't perform actual image analysis.

## Integration Options

### Option 1: GitHub Actions Workflow

Create a workflow that processes images using a vision API:

```yaml
name: Plant Vision Analysis
on:
  workflow_dispatch:
    inputs:
      image_data:
        description: 'Base64 encoded image'
        required: true
      plant_id:
        description: 'Plant identifier'
        required: true

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: |
          pip install openai Pillow
      
      - name: Analyze Image
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          python scripts/analyze_plant.py \
            --image "${{ inputs.image_data }}" \
            --plant-id "${{ inputs.plant_id }}"
      
      - name: Save Results
        uses: actions/upload-artifact@v3
        with:
          name: analysis-results
          path: analysis-output.json
```

### Option 2: Serverless Function

Deploy a serverless function (Vercel, Netlify, AWS Lambda) that handles image analysis:

```typescript
// api/analyze.ts
import { Configuration, OpenAIApi } from 'openai';

export default async function handler(req, res) {
  const { image, plantId } = req.body;
  
  const configuration = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
  });
  const openai = new OpenAIApi(configuration);

  const response = await openai.createChatCompletion({
    model: "gpt-4-vision-preview",
    messages: [
      {
        role: "user",
        content: [
          { type: "text", text: ANALYSIS_PROMPT },
          { type: "image_url", image_url: image }
        ],
      },
    ],
    max_tokens: 1000,
  });

  const analysis = parseAnalysisResponse(response.data);
  
  return res.json(analysis);
}
```

### Option 3: Backend Service

Create a dedicated backend service:

```python
# server.py
from flask import Flask, request, jsonify
from openai import OpenAI
import base64

app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/api/analyze', methods=['POST'])
def analyze_plant():
    data = request.json
    image_data = data['image']
    plant_id = data['plant_id']
    
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": ANALYSIS_PROMPT},
                    {"type": "image_url", "image_url": {"url": image_data}}
                ],
            }
        ],
        max_tokens=1000,
    )
    
    analysis = parse_response(response.choices[0].message.content)
    return jsonify(analysis)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Analysis Prompt Template

```
Analyze this plant image and provide a detailed assessment in JSON format:

{
  "flower_volume": "Assess the overall volume of flowers/buds (Low/Moderate/High/Very High)",
  "flower_density": "Assess how dense the flowers/buds are (Sparse/Moderate/Dense/Very Dense)",
  "color_health": "Describe the color and vibrancy of leaves (be specific)",
  "leaf_condition": "Describe leaf condition including any spots, damage, or discoloration",
  "stress_signs": "Identify any signs of stress: light burn, overwatering, nutrient deficiency, etc.",
  "general_structure": "Describe the overall plant structure and branching",
  "trichome_development": "If visible, describe trichome development (clear/cloudy/amber ratio)",
  "overall_health_score": "Score from 0-100 based on overall plant health"
}

Be specific, detailed, and accurate. Use descriptive language.
```

## Response Parsing

```typescript
function parseAnalysisResponse(apiResponse: string): PlantAnalysis {
  // Parse the API response and map to our format
  const parsed = JSON.parse(apiResponse);
  
  return {
    timestamp: new Date().toISOString(),
    plant_id: plantId,
    image_url: imageData,
    analysis: {
      flower_volume: parsed.flower_volume,
      flower_density: parsed.flower_density,
      color_health: parsed.color_health,
      leaf_condition: parsed.leaf_condition,
      stress_signs: parsed.stress_signs,
      general_structure: parsed.general_structure,
      trichome_development: parsed.trichome_development,
      overall_health_score: parseInt(parsed.overall_health_score),
    }
  };
}
```

## Updating the Frontend

To connect the frontend to a real API:

```typescript
// src/lib/analysis.ts

export const analyzePlantImage = async (
  imageData: string,
  plantId: string,
  previousAnalysis?: PlantAnalysis
): Promise<PlantAnalysis> => {
  
  // Call your API endpoint
  const response = await fetch('/api/analyze', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      image: imageData,
      plant_id: plantId,
      previous_analysis: previousAnalysis,
    }),
  });

  if (!response.ok) {
    throw new Error('Analysis failed');
  }

  const analysis = await response.json();
  
  // Add change detection if previous analysis exists
  if (previousAnalysis) {
    analysis.changes_detected = detectChanges(previousAnalysis, analysis);
  }
  
  return analysis;
};
```

## Security Considerations

1. **API Keys**: Never expose API keys in client-side code
2. **Rate Limiting**: Implement rate limiting on your backend
3. **Image Size**: Limit image upload sizes (e.g., 5MB max)
4. **Authentication**: Consider adding user authentication
5. **CORS**: Configure CORS properly for production
6. **Input Validation**: Validate all inputs on the backend

## Cost Considerations

- **GPT-4 Vision**: ~$0.01-0.03 per image (varies by size)
- **Google Vision**: ~$1.50 per 1000 images
- **AWS Rekognition**: ~$1.00 per 1000 images

Consider implementing:
- Image caching to avoid duplicate analyses
- Image compression before sending to API
- Usage quotas per user
- Batch processing for multiple images

## Testing

Example test image for development:

```javascript
// test-data.ts
export const TEST_IMAGE_BASE64 = 'data:image/jpeg;base64,/9j/4AAQSkZJRg...';

export const EXPECTED_RESPONSE = {
  timestamp: '2024-01-15T10:30:00.000Z',
  plant_id: 'test-plant',
  analysis: {
    flower_volume: 'High',
    flower_density: 'Dense',
    // ... etc
  }
};
```

## Monitoring

Track these metrics:
- API response times
- Success/failure rates
- Cost per analysis
- User satisfaction
- Accuracy of predictions (if ground truth available)
