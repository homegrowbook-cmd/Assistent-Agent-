// Type definitions for plant analysis
export interface PlantAnalysis {
  timestamp: string;
  plant_id: string;
  image_url?: string;
  analysis: {
    flower_volume: string;
    flower_density: string;
    color_health: string;
    leaf_condition: string;
    stress_signs: string;
    general_structure: string;
    trichome_development: string;
    overall_health_score: number;
  };
  changes_detected?: {
    growth_change: string;
    density_change: string;
    color_change: string;
    health_trend: 'improved' | 'stable' | 'worse';
  };
}

export interface PlantHistory {
  plant_id: string;
  plant_name?: string;
  analyses: PlantAnalysis[];
}
