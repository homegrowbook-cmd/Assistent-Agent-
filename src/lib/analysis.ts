import { PlantAnalysis } from '@/types';

// Mock AI analysis function - simulates vision model analysis
export const analyzePlantImage = async (
  imageData: string,
  plantId: string,
  previousAnalysis?: PlantAnalysis
): Promise<PlantAnalysis> => {
  // In a real implementation, this would call a GitHub Action workflow
  // or backend API that uses a vision model
  
  // Simulate API delay
  await new Promise(resolve => setTimeout(resolve, 2000));
  
  // Generate mock analysis based on image characteristics
  const analysis: PlantAnalysis = {
    timestamp: new Date().toISOString(),
    plant_id: plantId,
    image_url: imageData,
    analysis: {
      flower_volume: generateFlowerVolume(),
      flower_density: generateFlowerDensity(),
      color_health: generateColorHealth(),
      leaf_condition: generateLeafCondition(),
      stress_signs: generateStressSigns(),
      general_structure: generateStructure(),
      trichome_development: generateTrichomes(),
      overall_health_score: Math.floor(Math.random() * 30) + 70 // 70-100
    }
  };
  
  // Add change detection if previous analysis exists
  if (previousAnalysis) {
    analysis.changes_detected = detectChanges(previousAnalysis, analysis);
  }
  
  return analysis;
};

function generateFlowerVolume(): string {
  const volumes = ['Low', 'Moderate', 'High', 'Very High'];
  return volumes[Math.floor(Math.random() * volumes.length)];
}

function generateFlowerDensity(): string {
  const densities = ['Sparse', 'Moderate', 'Dense', 'Very Dense'];
  return densities[Math.floor(Math.random() * densities.length)];
}

function generateColorHealth(): string {
  const colors = [
    'Vibrant green with healthy coloration',
    'Deep green with good vitality',
    'Healthy green with minor pale spots',
    'Excellent color with purple undertones'
  ];
  return colors[Math.floor(Math.random() * colors.length)];
}

function generateLeafCondition(): string {
  const conditions = [
    'Pristine - no visible damage',
    'Excellent - minor edge browning',
    'Good - few small spots present',
    'Very good - minimal defects'
  ];
  return conditions[Math.floor(Math.random() * conditions.length)];
}

function generateStressSigns(): string {
  const signs = [
    'No stress indicators detected',
    'Mild light stress on upper leaves',
    'Minor nutrient deficiency signs',
    'Slight overwatering indicators',
    'No significant stress'
  ];
  return signs[Math.floor(Math.random() * signs.length)];
}

function generateStructure(): string {
  const structures = [
    'Well-developed branching structure',
    'Compact and bushy growth pattern',
    'Tall with good internodal spacing',
    'Excellent canopy development'
  ];
  return structures[Math.floor(Math.random() * structures.length)];
}

function generateTrichomes(): string {
  const trichomes = [
    'Cloudy trichomes with 10% amber',
    'Mostly clear, early development',
    'Mixed clear and cloudy trichomes',
    'Dense trichome coverage, mostly cloudy'
  ];
  return trichomes[Math.floor(Math.random() * trichomes.length)];
}

function detectChanges(
  previous: PlantAnalysis,
  current: PlantAnalysis
): PlantAnalysis['changes_detected'] {
  const scoreDiff = current.analysis.overall_health_score - previous.analysis.overall_health_score;
  
  let health_trend: 'improved' | 'stable' | 'worse';
  if (scoreDiff > 5) health_trend = 'improved';
  else if (scoreDiff < -5) health_trend = 'worse';
  else health_trend = 'stable';
  
  return {
    growth_change: 'Noticeable increase in flower volume and density',
    density_change: 'Flower density has increased by approximately 15%',
    color_change: 'Color vibrancy maintained with slight improvement',
    health_trend
  };
}
