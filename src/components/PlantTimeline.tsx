'use client';

import { useEffect, useState } from 'react';
import { PlantHistory, PlantAnalysis } from '@/types';
import { getPlantHistory } from '@/lib/storage';

interface PlantTimelineProps {
  plantId: string;
  onClose: () => void;
}

export default function PlantTimeline({ plantId, onClose }: PlantTimelineProps) {
  const [history, setHistory] = useState<PlantHistory | null>(null);

  useEffect(() => {
    const data = getPlantHistory(plantId);
    setHistory(data);
  }, [plantId]);

  const getHealthColor = (score: number): string => {
    if (score >= 90) return '#4caf50';
    if (score >= 75) return '#8bc34a';
    if (score >= 60) return '#ffc107';
    return '#f44336';
  };

  const downloadJSON = () => {
    if (!history) return;
    
    const dataStr = JSON.stringify(history, null, 2);
    const dataUri = 'data:application/json;charset=utf-8,' + encodeURIComponent(dataStr);
    const exportFileDefaultName = `plant_${plantId}_history.json`;
    
    const linkElement = document.createElement('a');
    linkElement.setAttribute('href', dataUri);
    linkElement.setAttribute('download', exportFileDefaultName);
    linkElement.click();
  };

  if (!history) {
    return (
      <div className="timeline-overlay">
        <div className="timeline-modal">
          <p>Loading...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="timeline-overlay" onClick={onClose}>
      <div className="timeline-modal" onClick={(e) => e.stopPropagation()}>
        <div className="timeline-header">
          <h2>Timeline: {history.plant_name || history.plant_id}</h2>
          <div className="timeline-actions">
            <button onClick={downloadJSON} className="download-button">
              📥 Download JSON
            </button>
            <button onClick={onClose} className="close-button">
              ✕
            </button>
          </div>
        </div>

        <div className="timeline-content">
          {history.analyses.map((analysis, index) => (
            <div key={analysis.timestamp} className="timeline-item">
              <div className="timeline-marker">
                <div className="timeline-dot"></div>
                {index < history.analyses.length - 1 && <div className="timeline-line"></div>}
              </div>
              
              <div className="timeline-card">
                <div className="timeline-date">
                  {new Date(analysis.timestamp).toLocaleString()}
                </div>
                
                {analysis.image_url && (
                  <div className="timeline-image">
                    <img src={analysis.image_url} alt={`Analysis ${index + 1}`} style={{ width: '100%', height: 'auto' }} />
                  </div>
                )}
                
                <div className="timeline-score">
                  <span>Health Score: </span>
                  <strong style={{ color: getHealthColor(analysis.analysis.overall_health_score) }}>
                    {analysis.analysis.overall_health_score}/100
                  </strong>
                </div>
                
                <div className="timeline-details">
                  <div className="timeline-detail">
                    <strong>Flower Volume:</strong> {analysis.analysis.flower_volume}
                  </div>
                  <div className="timeline-detail">
                    <strong>Flower Density:</strong> {analysis.analysis.flower_density}
                  </div>
                  <div className="timeline-detail">
                    <strong>Leaf Condition:</strong> {analysis.analysis.leaf_condition}
                  </div>
                </div>
                
                {analysis.changes_detected && (
                  <div className="timeline-changes">
                    <strong>Changes: </strong>
                    <span className={`trend-${analysis.changes_detected.health_trend}`}>
                      {analysis.changes_detected.health_trend.toUpperCase()}
                    </span>
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
