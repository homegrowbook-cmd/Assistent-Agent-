# 🗺️ AI-Integration Roadmap / KI-Integrations-Fahrplan

**Ziel / Goal:** Integration echter KI-basierter Bildauswertung nach dem Upload  
**Current Status:** Mock-Analyse implementiert, Infrastruktur vorbereitet  
**Target:** Vollständige AI Vision Model Integration

---

## 📍 Aktueller Status / Current State

### ✅ Was bereits funktioniert / What's Already Working

1. **Frontend Upload-System**
   - Bildauswahl und Vorschau
   - Base64-Kodierung für Speicherung
   - Plant ID Management
   - Responsive UI für Mobile & Desktop

2. **Mock-Analyse Engine** (`src/lib/analysis.ts`)
   - Simuliert KI-Analyse
   - Generiert alle 8 Gesundheitsmetriken:
     - Blütenvolumen (flower_volume)
     - Blütendichte (flower_density)
     - Farbgesundheit (color_health)
     - Blattzustand (leaf_condition)
     - Stressindikatoren (stress_signs)
     - Allgemeine Struktur (general_structure)
     - Trichom-Entwicklung (trichome_development)
     - Gesundheitsscore 0-100 (overall_health_score)

3. **Change Detection**
   - Vergleich mit vorherigen Analysen
   - Trend-Erkennung (verbessert/stabil/schlechter)

4. **Datenpersistenz**
   - LocalStorage für Analysehistorie
   - JSON-Export Funktionalität

5. **Beispiel-Integration** (`scripts/analyze_plant.py`)
   - Python-Script mit OpenAI GPT-4 Vision API
   - Voll funktionsfähig, ready-to-use
   - Bildkompression und -verarbeitung

### ❌ Was noch fehlt / What's Missing

- Tatsächliche KI-Bildauswertung nach Upload
- API-Backend oder Serverless Function
- Sichere API-Key-Verwaltung
- Produktions-Deployment der KI-Integration
- Fehlerbehandlung für echte API-Aufrufe
- Rate Limiting und Kostenmanagement

---

## 🎯 Integrationspfad / Integration Path

### Phase 1: Backend-Setup (1-2 Tage)

**Option A: Serverless Function (Empfohlen für einfaches Setup)**

#### Schritt 1.1: Vercel Serverless Function erstellen

1. **Vercel Account erstellen**
   ```bash
   npm install -g vercel
   vercel login
   ```

2. **API Route erstellen**
   - Datei: `pages/api/analyze.ts` (oder `app/api/analyze/route.ts` für App Router)
   
   ```typescript
   // pages/api/analyze.ts
   import { NextApiRequest, NextApiResponse } from 'next';
   import OpenAI from 'openai';
   
   const client = new OpenAI({
     apiKey: process.env.OPENAI_API_KEY,
   });
   
   const ANALYSIS_PROMPT = `Analyze this plant image and provide a detailed health assessment.
   
   Provide your response ONLY as a JSON object with this exact structure:
   {
     "flower_volume": "Low | Moderate | High | Very High",
     "flower_density": "Sparse | Moderate | Dense | Very Dense",
     "color_health": "Describe the color and vibrancy of leaves in 1-2 sentences",
     "leaf_condition": "Describe leaf condition including any spots, damage, or discoloration in 1-2 sentences",
     "stress_signs": "Identify any signs of stress: light burn, overwatering, nutrient deficiency, etc. in 1-2 sentences",
     "general_structure": "Describe the overall plant structure and branching in 1-2 sentences",
     "trichome_development": "If visible, describe trichome development. If not visible, say 'Not visible at this magnification'",
     "overall_health_score": 85
   }
   
   Be specific, detailed, and accurate. The overall_health_score must be a number between 0 and 100.`;
   
   export default async function handler(
     req: NextApiRequest,
     res: NextApiResponse
   ) {
     if (req.method !== 'POST') {
       return res.status(405).json({ error: 'Method not allowed' });
     }
   
     try {
       const { image, plant_id } = req.body;
       
       if (!image || !plant_id) {
         return res.status(400).json({ error: 'Missing image or plant_id' });
       }
       
       // Validate image size (max 5MB)
       const imageSizeInBytes = Math.ceil((image.length * 3) / 4);
       if (imageSizeInBytes > 5 * 1024 * 1024) {
         return res.status(400).json({ error: 'Image too large. Max 5MB.' });
       }
   
       // Call OpenAI Vision API
       const response = await client.chat.completions.create({
         model: "gpt-4-vision-preview",
         messages: [
           {
             role: "user",
             content: [
               { type: "text", text: ANALYSIS_PROMPT },
               {
                 type: "image_url",
                 image_url: { url: image }
               }
             ],
           }
         ],
         max_tokens: 1000,
         temperature: 0.7,
       });
   
       // Parse response
       let content = response.choices[0].message.content || '{}';
       
       // Extract JSON if wrapped in markdown
       if (content.includes('```json')) {
         content = content.split('```json')[1].split('```')[0].trim();
       } else if (content.includes('```')) {
         content = content.split('```')[1].split('```')[0].trim();
       }
       
       const analysisData = JSON.parse(content);
       
       // Ensure health score is a number
       if (typeof analysisData.overall_health_score === 'string') {
         analysisData.overall_health_score = parseInt(analysisData.overall_health_score);
       }
       
       // Return formatted response
       return res.status(200).json({
         timestamp: new Date().toISOString(),
         plant_id: plant_id,
         analysis: analysisData
       });
       
     } catch (error: any) {
       console.error('Analysis error:', error);
       return res.status(500).json({ 
         error: 'Analysis failed',
         message: error.message 
       });
     }
   }
   
   // Increase max body size for images
   export const config = {
     api: {
       bodyParser: {
         sizeLimit: '10mb',
       },
     },
   };
   ```

3. **Environment Variables konfigurieren**
   
   Lokale Entwicklung (`.env.local`):
   ```bash
   OPENAI_API_KEY=sk-your-api-key-here
   ```
   
   Vercel Dashboard:
   - Settings → Environment Variables
   - Key: `OPENAI_API_KEY`
   - Value: Dein OpenAI API Key
   - Apply to: Production, Preview, Development

4. **Deployment**
   ```bash
   vercel --prod
   ```

**Option B: GitHub Actions Workflow**

#### Schritt 1.2: GitHub Actions Workflow erstellen

1. **Workflow-Datei erstellen:** `.github/workflows/analyze-image.yml`

   ```yaml
   name: Analyze Plant Image
   
   on:
     workflow_dispatch:
       inputs:
         image_base64:
           description: 'Base64 encoded image data'
           required: true
           type: string
         plant_id:
           description: 'Plant identifier'
           required: true
           type: string
         analysis_id:
           description: 'Unique ID for this analysis'
           required: true
           type: string
   
   jobs:
     analyze:
       runs-on: ubuntu-latest
       permissions:
         contents: write
       
       steps:
         - name: Checkout repository
           uses: actions/checkout@v4
         
         - name: Setup Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.10'
             cache: 'pip'
         
         - name: Install dependencies
           run: |
             pip install openai Pillow
         
         - name: Save image to file
           run: |
             echo "${{ inputs.image_base64 }}" | base64 -d > /tmp/plant-image.jpg
         
         - name: Analyze image
           env:
             OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
           run: |
             python scripts/analyze_plant.py \
               --image /tmp/plant-image.jpg \
               --plant-id "${{ inputs.plant_id }}" \
               --output "public/analysis/${{ inputs.analysis_id }}.json"
         
         - name: Commit and push results
           run: |
             git config --global user.name "GitHub Actions Bot"
             git config --global user.email "actions@github.com"
             git add public/analysis/${{ inputs.analysis_id }}.json
             git commit -m "Add analysis for ${{ inputs.plant_id }}"
             git push
         
         - name: Upload artifact
           uses: actions/upload-artifact@v3
           with:
             name: analysis-result
             path: public/analysis/${{ inputs.analysis_id }}.json
   ```

2. **GitHub Secret hinzufügen**
   - Repository → Settings → Secrets and variables → Actions
   - New repository secret: `OPENAI_API_KEY`

**Option C: Eigener Backend-Server (Für größere Deployments)**

#### Schritt 1.3: Flask/FastAPI Backend

```python
# server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAI
import base64
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

ANALYSIS_PROMPT = """..."""  # Same as above

@app.route('/api/analyze', methods=['POST'])
def analyze_plant():
    try:
        data = request.json
        image_data = data.get('image')
        plant_id = data.get('plant_id')
        
        if not image_data or not plant_id:
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Call OpenAI
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
            temperature=0.7,
        )
        
        content = response.choices[0].message.content
        
        # Parse JSON
        if '```json' in content:
            content = content.split('```json')[1].split('```')[0].strip()
        
        analysis_data = json.loads(content)
        
        return jsonify({
            'timestamp': datetime.now().isoformat(),
            'plant_id': plant_id,
            'analysis': analysis_data
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Deployment auf Heroku/Railway/DigitalOcean.

---

### Phase 2: Frontend-Integration (1 Tag)

#### Schritt 2.1: Analysis Service aktualisieren

1. **API-Konfiguration hinzufügen** (`src/lib/config.ts`)

   ```typescript
   export const API_CONFIG = {
     // For serverless/backend
     endpoint: process.env.NEXT_PUBLIC_API_URL || '/api/analyze',
     
     // For GitHub Actions
     useGitHubActions: process.env.NEXT_PUBLIC_USE_GITHUB_ACTIONS === 'true',
     
     // Timeout for analysis
     timeout: 30000, // 30 seconds
   };
   ```

2. **Analysis Service umschreiben** (`src/lib/analysis.ts`)

   ```typescript
   import { PlantAnalysis } from '@/types';
   import { API_CONFIG } from './config';
   
   export const analyzePlantImage = async (
     imageData: string,
     plantId: string,
     previousAnalysis?: PlantAnalysis
   ): Promise<PlantAnalysis> => {
     
     try {
       // Call real API
       const controller = new AbortController();
       const timeoutId = setTimeout(() => controller.abort(), API_CONFIG.timeout);
       
       const response = await fetch(API_CONFIG.endpoint, {
         method: 'POST',
         headers: {
           'Content-Type': 'application/json',
         },
         body: JSON.stringify({
           image: imageData,
           plant_id: plantId,
         }),
         signal: controller.signal,
       });
       
       clearTimeout(timeoutId);
       
       if (!response.ok) {
         throw new Error(`API Error: ${response.status} ${response.statusText}`);
       }
       
       const result = await response.json();
       
       // Add image URL to result
       result.image_url = imageData;
       
       // Add change detection if previous analysis exists
       if (previousAnalysis) {
         result.changes_detected = detectChanges(previousAnalysis, result);
       }
       
       return result;
       
     } catch (error) {
       console.error('Real analysis failed, using mock:', error);
       
       // Fallback to mock analysis if API fails
       return mockAnalyzePlantImage(imageData, plantId, previousAnalysis);
     }
   };
   
   // Keep existing mock function as fallback
   const mockAnalyzePlantImage = async (
     imageData: string,
     plantId: string,
     previousAnalysis?: PlantAnalysis
   ): Promise<PlantAnalysis> => {
     // Existing mock implementation...
   };
   
   function detectChanges(
     previous: PlantAnalysis,
     current: PlantAnalysis
   ): PlantAnalysis['changes_detected'] {
     // Existing change detection logic...
   }
   ```

#### Schritt 2.2: Error Handling & Loading States verbessern

1. **ImageUpload Component aktualisieren**

   ```typescript
   // src/components/ImageUpload.tsx
   const handleAnalyze = async () => {
     if (!selectedImage || !plantId.trim()) {
       alert('Please select an image and enter a plant ID');
       return;
     }
   
     setIsAnalyzing(true);
     setError(null);
     
     try {
       const history = getPlantHistory(plantId);
       const previousAnalysis = history?.analyses[history.analyses.length - 1];
   
       const analysis = await analyzePlantImage(selectedImage, plantId, previousAnalysis);
       
       saveAnalysis(analysis);
       onAnalysisComplete(analysis);
       
       // Reset form
       setSelectedImage(null);
       setPlantId('');
       if (fileInputRef.current) {
         fileInputRef.current.value = '';
       }
       
     } catch (error) {
       console.error('Analysis failed:', error);
       setError(
         error instanceof Error 
           ? error.message 
           : 'Failed to analyze image. Please try again.'
       );
     } finally {
       setIsAnalyzing(false);
     }
   };
   ```

2. **Loading Indicator hinzufügen**

   ```typescript
   {isAnalyzing && (
     <div className="loading-indicator">
       <div className="spinner"></div>
       <p>Analyzing plant with AI...</p>
       <p className="text-sm">This may take 10-30 seconds</p>
     </div>
   )}
   
   {error && (
     <div className="error-message">
       <p>❌ {error}</p>
       <button onClick={() => setError(null)}>Dismiss</button>
     </div>
   )}
   ```

---

### Phase 3: Testing & Validierung (1 Tag)

#### Schritt 3.1: Manuelle Tests

**Testszenarien:**

1. ✅ Bild hochladen und analysieren
2. ✅ Mehrere Pflanzen nacheinander analysieren
3. ✅ Gleiche Pflanze mehrmals analysieren (Change Detection)
4. ✅ Fehlerbehandlung: Ungültige Bilder
5. ✅ Fehlerbehandlung: API-Timeout
6. ✅ Fehlerbehandlung: Keine Internetverbindung
7. ✅ Mobile Upload & Analyse
8. ✅ Große Bilder (>5MB)

#### Schritt 3.2: E2E Testing (Optional)

```typescript
// cypress/e2e/ai-analysis.cy.ts
describe('AI Plant Analysis', () => {
  it('should upload and analyze an image', () => {
    cy.visit('/');
    
    // Upload image
    cy.get('input[type="file"]').selectFile('cypress/fixtures/plant.jpg');
    
    // Enter plant ID
    cy.get('input[id="plantId"]').type('test-plant-001');
    
    // Click analyze
    cy.get('button').contains('Analyze').click();
    
    // Wait for analysis
    cy.get('.loading-indicator', { timeout: 40000 }).should('be.visible');
    
    // Check results
    cy.get('.analysis-result', { timeout: 40000 }).should('be.visible');
    cy.get('.health-score').should('exist');
  });
});
```

---

### Phase 4: Optimierung & Produktion (2-3 Tage)

#### Schritt 4.1: Performance-Optimierungen

1. **Bildkompression vor Upload**

   ```typescript
   // src/lib/imageProcessing.ts
   export async function compressImage(
     imageDataUrl: string,
     maxWidth: number = 1920,
     maxHeight: number = 1920,
     quality: number = 0.85
   ): Promise<string> {
     return new Promise((resolve, reject) => {
       const img = new Image();
       img.onload = () => {
         const canvas = document.createElement('canvas');
         let width = img.width;
         let height = img.height;
         
         // Calculate new dimensions
         if (width > maxWidth || height > maxHeight) {
           const ratio = Math.min(maxWidth / width, maxHeight / height);
           width *= ratio;
           height *= ratio;
         }
         
         canvas.width = width;
         canvas.height = height;
         
         const ctx = canvas.getContext('2d');
         ctx?.drawImage(img, 0, 0, width, height);
         
         resolve(canvas.toDataURL('image/jpeg', quality));
       };
       img.onerror = reject;
       img.src = imageDataUrl;
     });
   }
   ```

2. **Caching für wiederholte Analysen**

   ```typescript
   // src/lib/cache.ts
   const ANALYSIS_CACHE_KEY = 'plant_analysis_cache';
   
   export function getCachedAnalysis(imageHash: string): PlantAnalysis | null {
     const cache = localStorage.getItem(ANALYSIS_CACHE_KEY);
     if (!cache) return null;
     
     const parsed = JSON.parse(cache);
     return parsed[imageHash] || null;
   }
   
   export function cacheAnalysis(imageHash: string, analysis: PlantAnalysis) {
     const cache = localStorage.getItem(ANALYSIS_CACHE_KEY);
     const parsed = cache ? JSON.parse(cache) : {};
     
     parsed[imageHash] = analysis;
     localStorage.setItem(ANALYSIS_CACHE_KEY, JSON.stringify(parsed));
   }
   ```

#### Schritt 4.2: Rate Limiting & Kostenmanagement

1. **Client-Side Rate Limiting**

   ```typescript
   // src/lib/rateLimiter.ts
   const RATE_LIMIT_KEY = 'analysis_rate_limit';
   const MAX_REQUESTS_PER_HOUR = 10;
   
   export function checkRateLimit(): boolean {
     const data = localStorage.getItem(RATE_LIMIT_KEY);
     if (!data) {
       resetRateLimit();
       return true;
     }
     
     const { count, resetTime } = JSON.parse(data);
     
     if (Date.now() > resetTime) {
       resetRateLimit();
       return true;
     }
     
     if (count >= MAX_REQUESTS_PER_HOUR) {
       return false;
     }
     
     localStorage.setItem(RATE_LIMIT_KEY, JSON.stringify({
       count: count + 1,
       resetTime
     }));
     
     return true;
   }
   
   function resetRateLimit() {
     const resetTime = Date.now() + (60 * 60 * 1000); // 1 hour
     localStorage.setItem(RATE_LIMIT_KEY, JSON.stringify({
       count: 1,
       resetTime
     }));
   }
   ```

2. **Backend Rate Limiting** (für Vercel/Backend)

   ```typescript
   // pages/api/analyze.ts
   import rateLimit from 'express-rate-limit';
   
   const limiter = rateLimit({
     windowMs: 60 * 60 * 1000, // 1 hour
     max: 10, // 10 requests per hour
     message: 'Too many analysis requests, please try again later.'
   });
   
   export default async function handler(req, res) {
     // Apply rate limit
     await limiter(req, res);
     
     // ... rest of handler
   }
   ```

#### Schritt 4.3: Monitoring & Logging

```typescript
// src/lib/analytics.ts
export function logAnalysis(
  plantId: string,
  success: boolean,
  duration: number,
  error?: string
) {
  // Log to console in development
  console.log('[Analysis]', {
    plantId,
    success,
    duration,
    error,
    timestamp: new Date().toISOString()
  });
  
  // In production, send to analytics service
  if (process.env.NODE_ENV === 'production') {
    // Send to PostHog, Google Analytics, etc.
  }
}
```

---

## 💰 Kostenabschätzung / Cost Estimation

### OpenAI GPT-4 Vision API

**Preise (Stand 2024):**
- Input: ~$0.01 per Bild (bei durchschnittlicher Größe)
- Max Tokens: 1000 tokens ≈ $0.01-0.03 pro Analyse

**Beispielrechnung:**
- 100 Analysen/Monat: ~$2-3
- 1000 Analysen/Monat: ~$20-30
- 10.000 Analysen/Monat: ~$200-300

### Alternativen:

1. **Google Vision API**
   - $1.50 per 1000 images
   - Günstiger für high-volume

2. **AWS Rekognition**
   - $1.00 per 1000 images
   - Custom Models möglich

3. **Self-Hosted Open Source**
   - CLIP, BLIP, LLaVA
   - Kostenlos, aber erfordert GPU-Server
   - ~$50-200/Monat für Server

---

## 🔒 Sicherheit / Security

### Checklist:

- [ ] API-Keys niemals im Frontend-Code
- [ ] Environment Variables für alle Secrets
- [ ] HTTPS für alle API-Aufrufe
- [ ] Input-Validierung (Bildgröße, Format)
- [ ] Rate Limiting implementiert
- [ ] CORS richtig konfiguriert
- [ ] Error Messages enthalten keine sensiblen Infos
- [ ] Logging ohne persönliche Daten

---

## 📈 Success Metrics

Nach der Integration messen:

1. **Technische Metriken:**
   - API Response Time (Ziel: <15s)
   - Success Rate (Ziel: >95%)
   - Error Rate (Ziel: <5%)
   - Cache Hit Rate (Ziel: >30%)

2. **Business Metriken:**
   - Analysen pro Monat
   - Kosten pro Analyse
   - User Retention
   - Fehlerrate

3. **Qualitätsmetriken:**
   - Genauigkeit der Analysen (User Feedback)
   - Nützlichkeit der Empfehlungen
   - Time-to-Value (Upload → Ergebnis)

---

## 🚀 Nächste Schritte / Next Steps

### Sofort (Diese Woche):

1. **Entscheidung treffen:** Welche Option (Vercel vs. GitHub Actions vs. Backend)?
   - **Empfehlung:** Vercel Serverless für einfachsten Start

2. **OpenAI API Key besorgen:**
   - Account auf platform.openai.com
   - Billing einrichten ($5 Startguthaben)
   - API Key generieren

3. **Phase 1 implementieren:**
   - Backend-Endpunkt erstellen
   - Lokal testen mit `analyze_plant.py`
   - API Key als Secret speichern

### Mittelfristig (Nächste 2 Wochen):

4. **Phase 2 implementieren:**
   - Frontend mit Backend verbinden
   - Error Handling verbessern
   - Loading States optimieren

5. **Phase 3: Testing**
   - Manuelle Tests mit echten Pflanzenbildern
   - Edge Cases testen
   - Mobile Testing

### Langfristig (Nächster Monat):

6. **Phase 4: Optimierung**
   - Performance-Tuning
   - Caching implementieren
   - Monitoring aufsetzen

7. **Advanced Features:**
   - Batch-Upload
   - Vergleichsansichten
   - Export-Funktionen
   - Sharing Features

---

## 📚 Ressourcen / Resources

### Dokumentation:
- [OpenAI Vision API Docs](https://platform.openai.com/docs/guides/vision)
- [Vercel Serverless Functions](https://vercel.com/docs/functions/serverless-functions)
- [Next.js API Routes](https://nextjs.org/docs/api-routes/introduction)
- [GitHub Actions Workflows](https://docs.github.com/en/actions/using-workflows)

### Code-Beispiele:
- `scripts/analyze_plant.py` - Vollständiges Python-Beispiel
- `API_DOCUMENTATION.md` - Integration-Guides
- `DEVELOPMENT.md` - Development-Setup

### Support:
- GitHub Issues für Bugs
- Discussions für Fragen
- Discord Community (optional)

---

## ✅ Checkliste für Go-Live / Launch Checklist

Vor dem Production-Deployment:

- [ ] API-Integration funktioniert lokal
- [ ] Alle Tests bestanden
- [ ] Error Handling implementiert
- [ ] Rate Limiting aktiv
- [ ] Secrets sicher gespeichert
- [ ] Monitoring eingerichtet
- [ ] Kosten-Alerts konfiguriert
- [ ] Backup-Plan für API-Ausfall
- [ ] Dokumentation aktualisiert
- [ ] User Guide erstellt

---

**Stand:** November 2024  
**Version:** 1.0  
**Maintainer:** Plant Analysis Lab Team
