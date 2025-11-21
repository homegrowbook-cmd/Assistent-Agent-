'use client';

import { PlantAnalysis } from '@/types';

interface AnalysisResultProps {
  analysis: PlantAnalysis;
}

export default function AnalysisResult({ analysis }: AnalysisResultProps) {
  const getHealthColor = (score: number): string => {
    if (score >= 90) return '#4caf50';
    if (score >= 75) return '#8bc34a';
    if (score >= 60) return '#ffc107';
    return '#f44336';
  };

  const getTrendIcon = (trend: string): string => {
    switch (trend) {
      case 'improved': return '📈';
      case 'worse': return '📉';
      default: return '➡️';
    }
  };

  return (
    <div className="analysis-result">
      <div className="result-header">
        <h2>Analysis Results</h2>
        <div className="timestamp">
          {new Date(analysis.timestamp).toLocaleString()}
        </div>
      </div>

      {analysis.image_url && (
        <div className="result-image">
          <img src={analysis.image_url} alt="Analyzed plant" />
        </div>
      )}

      <div className="health-score">
        <div className="score-label">Overall Health Score</div>
        <div 
          className="score-value"
          style={{ color: getHealthColor(analysis.analysis.overall_health_score) }}
        >
          {analysis.analysis.overall_health_score}/100
        </div>
      </div>

      <div className="analysis-details">
        <h3>Detailed Analysis</h3>
        
        <div className="detail-item">
          <span className="detail-label">🌸 Flower Volume:</span>
          <span className="detail-value">{analysis.analysis.flower_volume}</span>
        </div>
        
        <div className="detail-item">
          <span className="detail-label">🌺 Flower Density:</span>
          <span className="detail-value">{analysis.analysis.flower_density}</span>
        </div>
        
        <div className="detail-item">
          <span className="detail-label">🎨 Color Health:</span>
          <span className="detail-value">{analysis.analysis.color_health}</span>
        </div>
        
        <div className="detail-item">
          <span className="detail-label">🍃 Leaf Condition:</span>
          <span className="detail-value">{analysis.analysis.leaf_condition}</span>
        </div>
        
        <div className="detail-item">
          <span className="detail-label">⚠️ Stress Signs:</span>
          <span className="detail-value">{analysis.analysis.stress_signs}</span>
        </div>
        
        <div className="detail-item">
          <span className="detail-label">🌿 Structure:</span>
          <span className="detail-value">{analysis.analysis.general_structure}</span>
        </div>
        
        <div className="detail-item">
          <span className="detail-label">✨ Trichomes:</span>
          <span className="detail-value">{analysis.analysis.trichome_development}</span>
        </div>
      </div>

      {analysis.changes_detected && (
        <div className="changes-detected">
          <h3>Changes Detected {getTrendIcon(analysis.changes_detected.health_trend)}</h3>
          
          <div className="change-item">
            <span className="change-label">Growth Change:</span>
            <span className="change-value">{analysis.changes_detected.growth_change}</span>
          </div>
          
          <div className="change-item">
            <span className="change-label">Density Change:</span>
            <span className="change-value">{analysis.changes_detected.density_change}</span>
          </div>
          
          <div className="change-item">
            <span className="change-label">Color Change:</span>
            <span className="change-value">{analysis.changes_detected.color_change}</span>
          </div>
          
          <div className="change-item">
            <span className="change-label">Health Trend:</span>
            <span className={`change-value trend-${analysis.changes_detected.health_trend}`}>
              {analysis.changes_detected.health_trend.toUpperCase()}
            </span>
          </div>
        </div>
      )}
    </div>
  );
}
