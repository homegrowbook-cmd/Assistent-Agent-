'use client';

import { useState } from 'react';

const ROADMAP_URL = 'https://github.com/homegrowbook-cmd/Assistent-Agent-/blob/main/ROADMAP.md';

export default function AboutAI() {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <div className="about-ai-container">
      <button 
        className="about-toggle"
        onClick={() => setIsExpanded(!isExpanded)}
        aria-expanded={isExpanded}
      >
        <span className="toggle-icon">{isExpanded ? '▼' : '▶'}</span>
        <span className="toggle-text">ℹ️ Wie funktioniert die KI-Analyse? / How does AI analysis work?</span>
      </button>
      
      {isExpanded && (
        <div className="about-content">
          <div className="about-section">
            <h3>🚀 Sofort einsatzbereit / Ready to Use</h3>
            <p>
              <strong>Keine Installation notwendig!</strong> Die Anwendung ist direkt nutzbar:<br/>
              <strong>No installation required!</strong> The application is ready to use immediately:
            </p>
            <ul>
              <li>✅ Bilder hochladen / Upload images</li>
              <li>✅ Sofortige Analyse erhalten / Get instant analysis</li>
              <li>✅ Pflanzenverlauf verfolgen / Track plant history</li>
              <li>✅ Daten lokal speichern / Store data locally</li>
            </ul>
          </div>

          <div className="about-section">
            <h3>🤖 Aktuelle Funktionsweise / Current Implementation</h3>
            <p>
              <strong>DE:</strong> Die App verwendet derzeit eine <strong>Mock-KI-Analyse</strong>, 
              die realistische Gesundheitsbewertungen simuliert. Sie können sofort Bilder hochladen 
              und detaillierte Analysen erhalten, ohne zusätzliche Software zu installieren.
            </p>
            <p>
              <strong>EN:</strong> The app currently uses a <strong>mock AI analysis</strong> that 
              simulates realistic health assessments. You can immediately upload images and receive 
              detailed analyses without installing additional software.
            </p>
            <div className="feature-grid">
              <div className="feature-item">
                <span className="feature-icon">📊</span>
                <div>8 Gesundheitsmetriken / 8 health metrics</div>
              </div>
              <div className="feature-item">
                <span className="feature-icon">📈</span>
                <div>Veränderungserkennung / Change detection</div>
              </div>
              <div className="feature-item">
                <span className="feature-icon">💾</span>
                <div>Automatische Speicherung / Auto-save</div>
              </div>
              <div className="feature-item">
                <span className="feature-icon">📱</span>
                <div>Mobile-optimiert / Mobile-optimized</div>
              </div>
            </div>
          </div>

          <div className="about-section advanced">
            <h3>🔬 Echte KI-Integration / Real AI Integration</h3>
            <p>
              <strong>DE:</strong> Für echte Bildauswertung mit KI-Modellen (z.B. OpenAI GPT-4 Vision) 
              siehe die <a href={ROADMAP_URL} target="_blank" rel="noopener noreferrer">ROADMAP.md</a> für:
            </p>
            <p>
              <strong>EN:</strong> For real image analysis with AI models (e.g., OpenAI GPT-4 Vision), 
              see <a href={ROADMAP_URL} target="_blank" rel="noopener noreferrer">ROADMAP.md</a> for:
            </p>
            <ul>
              <li>🔧 Serverless Function Setup (Vercel/Netlify)</li>
              <li>🔄 GitHub Actions Integration</li>
              <li>🖥️ Backend Service Options (Flask/FastAPI)</li>
              <li>🔐 API-Key Verwaltung / API key management</li>
            </ul>
            <p className="note">
              <strong>Hinweis:</strong> Echte KI-Integration ist optional und erfordert API-Keys und Setup.<br/>
              <strong>Note:</strong> Real AI integration is optional and requires API keys and setup.
            </p>
          </div>

          <div className="about-section">
            <h3>📋 Was wird analysiert? / What is analyzed?</h3>
            <div className="analysis-metrics">
              <div className="metric">🌸 Blütenvolumen / Flower volume</div>
              <div className="metric">🌺 Blütendichte / Flower density</div>
              <div className="metric">🍃 Farbgesundheit / Color health</div>
              <div className="metric">🌿 Blattzustand / Leaf condition</div>
              <div className="metric">⚠️ Stressindikatoren / Stress signs</div>
              <div className="metric">🌳 Struktur / Structure</div>
              <div className="metric">💎 Trichome / Trichomes</div>
              <div className="metric">💯 Gesundheitsscore / Health score</div>
            </div>
          </div>

          <div className="about-section faq">
            <h3>❓ FAQ</h3>
            <details>
              <summary>Muss ich etwas installieren? / Do I need to install anything?</summary>
              <p>
                <strong>Nein!</strong> Die App läuft im Browser und benötigt keine Installation. 
                Laden Sie einfach ein Bild hoch und erhalten Sie sofort eine Analyse.<br/>
                <strong>No!</strong> The app runs in your browser and requires no installation. 
                Just upload an image and get instant analysis.
              </p>
            </details>
            <details>
              <summary>Ist die Analyse wirklich KI-basiert? / Is the analysis really AI-based?</summary>
              <p>
                <strong>Aktuell:</strong> Die App verwendet Mock-Daten für Demo-Zwecke. 
                Sie können später eine echte KI-Integration hinzufügen (siehe ROADMAP.md).<br/>
                <strong>Currently:</strong> The app uses mock data for demonstration purposes. 
                You can add real AI integration later (see ROADMAP.md).
              </p>
            </details>
            <details>
              <summary>Wo werden meine Daten gespeichert? / Where is my data stored?</summary>
              <p>
                <strong>Lokal im Browser (LocalStorage).</strong> Ihre Daten verlassen niemals Ihr Gerät.<br/>
                <strong>Locally in browser (LocalStorage).</strong> Your data never leaves your device.
              </p>
            </details>
            <details>
              <summary>Kostet die Nutzung etwas? / Does it cost anything?</summary>
              <p>
                <strong>Nein!</strong> Die Basisversion ist komplett kostenlos. 
                Echte KI-APIs können Kosten verursachen (ca. $0.01-0.03 pro Bild).<br/>
                <strong>No!</strong> The basic version is completely free. 
                Real AI APIs may incur costs (approx. $0.01-0.03 per image).
              </p>
            </details>
          </div>
        </div>
      )}
    </div>
  );
}
