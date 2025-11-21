'use client';

import { useEffect, useState } from 'react';
import { PlantHistory } from '@/types';
import { getAllPlants, deletePlant } from '@/lib/storage';

interface PlantListProps {
  onSelectPlant: (plantId: string) => void;
  refreshTrigger?: number;
}

export default function PlantList({ onSelectPlant, refreshTrigger }: PlantListProps) {
  const [plants, setPlants] = useState<PlantHistory[]>([]);

  useEffect(() => {
    loadPlants();
  }, [refreshTrigger]);

  const loadPlants = () => {
    const allPlants = getAllPlants();
    // Sort by most recent analysis
    allPlants.sort((a, b) => {
      const aTime = new Date(a.analyses[a.analyses.length - 1].timestamp).getTime();
      const bTime = new Date(b.analyses[b.analyses.length - 1].timestamp).getTime();
      return bTime - aTime;
    });
    setPlants(allPlants);
  };

  const handleDelete = (plantId: string, e: React.MouseEvent) => {
    e.stopPropagation();
    if (confirm(`Delete all data for plant "${plantId}"?`)) {
      deletePlant(plantId);
      loadPlants();
    }
  };

  const getLatestScore = (plant: PlantHistory): number => {
    return plant.analyses[plant.analyses.length - 1].analysis.overall_health_score;
  };

  const getHealthColor = (score: number): string => {
    if (score >= 90) return '#4caf50';
    if (score >= 75) return '#8bc34a';
    if (score >= 60) return '#ffc107';
    return '#f44336';
  };

  if (plants.length === 0) {
    return (
      <div className="plant-list empty">
        <p>No plants tracked yet. Upload your first plant image to get started!</p>
      </div>
    );
  }

  return (
    <div className="plant-list">
      <h2>Your Plants ({plants.length})</h2>
      <div className="plant-grid">
        {plants.map((plant) => {
          const latestAnalysis = plant.analyses[plant.analyses.length - 1];
          return (
            <div
              key={plant.plant_id}
              className="plant-card"
              onClick={() => onSelectPlant(plant.plant_id)}
            >
              <div className="plant-card-header">
                <h3>{plant.plant_name || plant.plant_id}</h3>
                <button
                  className="delete-button"
                  onClick={(e) => handleDelete(plant.plant_id, e)}
                  title="Delete plant"
                >
                  🗑️
                </button>
              </div>
              
              {latestAnalysis.image_url && (
                <div className="plant-card-image">
                  <img 
                    src={latestAnalysis.image_url} 
                    alt={plant.plant_id}
                    style={{ width: '100%', height: 'auto' }}
                  />
                </div>
              )}
              
              <div className="plant-card-info">
                <div className="info-row">
                  <span className="info-label">Health Score:</span>
                  <span 
                    className="info-value"
                    style={{ color: getHealthColor(getLatestScore(plant)) }}
                  >
                    {getLatestScore(plant)}/100
                  </span>
                </div>
                
                <div className="info-row">
                  <span className="info-label">Analyses:</span>
                  <span className="info-value">{plant.analyses.length}</span>
                </div>
                
                <div className="info-row">
                  <span className="info-label">Last Updated:</span>
                  <span className="info-value">
                    {new Date(latestAnalysis.timestamp).toLocaleDateString()}
                  </span>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
