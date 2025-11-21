'use client';

import { useState } from 'react';
import ImageUpload from '@/components/ImageUpload';
import AnalysisResult from '@/components/AnalysisResult';
import PlantList from '@/components/PlantList';
import PlantTimeline from '@/components/PlantTimeline';
import { PlantAnalysis } from '@/types';

export default function Home() {
  const [currentAnalysis, setCurrentAnalysis] = useState<PlantAnalysis | null>(null);
  const [selectedPlantId, setSelectedPlantId] = useState<string | null>(null);
  const [refreshTrigger, setRefreshTrigger] = useState(0);
  const [activeView, setActiveView] = useState<'upload' | 'plants'>('upload');

  const handleAnalysisComplete = (analysis: PlantAnalysis) => {
    setCurrentAnalysis(analysis);
    setRefreshTrigger(prev => prev + 1);
  };

  const handleSelectPlant = (plantId: string) => {
    setSelectedPlantId(plantId);
  };

  const handleCloseTimeline = () => {
    setSelectedPlantId(null);
  };

  return (
    <main className="main-container">
      <header className="app-header">
        <h1>🌱 Plant Analysis Lab</h1>
        <p className="tagline">AI-Powered Plant Health Tracking & Growth Analysis</p>
      </header>

      <nav className="main-nav">
        <button 
          className={`nav-button ${activeView === 'upload' ? 'active' : ''}`}
          onClick={() => setActiveView('upload')}
        >
          📸 New Analysis
        </button>
        <button 
          className={`nav-button ${activeView === 'plants' ? 'active' : ''}`}
          onClick={() => setActiveView('plants')}
        >
          🌿 My Plants
        </button>
      </nav>

      <div className="content-container">
        {activeView === 'upload' ? (
          <div className="upload-view">
            <div className="left-panel">
              <ImageUpload onAnalysisComplete={handleAnalysisComplete} />
            </div>
            
            <div className="right-panel">
              {currentAnalysis ? (
                <AnalysisResult analysis={currentAnalysis} />
              ) : (
                <div className="placeholder">
                  <h2>Welcome! 👋</h2>
                  <p>Upload an image of your plant to get started with AI-powered analysis.</p>
                  <div className="features">
                    <div className="feature">✓ Flower volume & density analysis</div>
                    <div className="feature">✓ Health score & stress detection</div>
                    <div className="feature">✓ Change tracking over time</div>
                    <div className="feature">✓ Trichome development monitoring</div>
                  </div>
                </div>
              )}
            </div>
          </div>
        ) : (
          <PlantList 
            onSelectPlant={handleSelectPlant} 
            refreshTrigger={refreshTrigger}
          />
        )}
      </div>

      {selectedPlantId && (
        <PlantTimeline 
          plantId={selectedPlantId} 
          onClose={handleCloseTimeline}
        />
      )}

      <footer className="app-footer">
        <p>Built with Next.js • Deployed on GitHub Pages</p>
      </footer>
    </main>
  );
}
