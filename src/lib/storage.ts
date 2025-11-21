import { PlantAnalysis, PlantHistory } from '@/types';

// Storage functions for plant analyses
export const saveAnalysis = (analysis: PlantAnalysis): void => {
  if (typeof window === 'undefined') return;
  
  const storageKey = `plant_${analysis.plant_id}`;
  const existing = localStorage.getItem(storageKey);
  
  let history: PlantHistory;
  if (existing) {
    history = JSON.parse(existing);
    history.analyses.push(analysis);
  } else {
    history = {
      plant_id: analysis.plant_id,
      analyses: [analysis]
    };
  }
  
  localStorage.setItem(storageKey, JSON.stringify(history));
};

export const getPlantHistory = (plantId: string): PlantHistory | null => {
  if (typeof window === 'undefined') return null;
  
  const storageKey = `plant_${plantId}`;
  const data = localStorage.getItem(storageKey);
  
  return data ? JSON.parse(data) : null;
};

export const getAllPlants = (): PlantHistory[] => {
  if (typeof window === 'undefined') return [];
  
  const plants: PlantHistory[] = [];
  
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    if (key && key.startsWith('plant_')) {
      const data = localStorage.getItem(key);
      if (data) {
        plants.push(JSON.parse(data));
      }
    }
  }
  
  return plants;
};

export const deletePlant = (plantId: string): void => {
  if (typeof window === 'undefined') return;
  localStorage.removeItem(`plant_${plantId}`);
};
