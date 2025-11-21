'use client';

import { useState, useRef, ChangeEvent } from 'react';
import Image from 'next/image';
import { analyzePlantImage } from '@/lib/analysis';
import { saveAnalysis, getPlantHistory } from '@/lib/storage';
import { PlantAnalysis } from '@/types';

interface ImageUploadProps {
  onAnalysisComplete: (analysis: PlantAnalysis) => void;
}

export default function ImageUpload({ onAnalysisComplete }: ImageUploadProps) {
  const [selectedImage, setSelectedImage] = useState<string | null>(null);
  const [plantId, setPlantId] = useState<string>('');
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleImageSelect = (e: ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setSelectedImage(reader.result as string);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleAnalyze = async () => {
    if (!selectedImage || !plantId.trim()) {
      alert('Please select an image and enter a plant ID');
      return;
    }

    setIsAnalyzing(true);
    try {
      // Get previous analysis for change detection
      const history = getPlantHistory(plantId);
      const previousAnalysis = history?.analyses[history.analyses.length - 1];

      // Analyze the image
      const analysis = await analyzePlantImage(selectedImage, plantId, previousAnalysis);
      
      // Save analysis
      saveAnalysis(analysis);
      
      // Notify parent
      onAnalysisComplete(analysis);
      
      // Reset form
      setSelectedImage(null);
      setPlantId('');
      if (fileInputRef.current) {
        fileInputRef.current.value = '';
      }
    } catch (error) {
      console.error('Analysis failed:', error);
      alert('Failed to analyze image. Please try again.');
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="upload-container">
      <h2>Upload Plant Image</h2>
      
      <div className="form-group">
        <label htmlFor="plantId">Plant ID / Name:</label>
        <input
          id="plantId"
          type="text"
          value={plantId}
          onChange={(e) => setPlantId(e.target.value)}
          placeholder="e.g., plant-001 or My Blue Dream"
          disabled={isAnalyzing}
        />
      </div>

      <div className="form-group">
        <label htmlFor="imageInput">Select Image:</label>
        <input
          id="imageInput"
          ref={fileInputRef}
          type="file"
          accept="image/*"
          onChange={handleImageSelect}
          disabled={isAnalyzing}
        />
      </div>

      {selectedImage && (
        <div className="image-preview">
          <Image src={selectedImage} alt="Selected plant" width={800} height={600} style={{ width: '100%', height: 'auto' }} />
        </div>
      )}

      <button
        onClick={handleAnalyze}
        disabled={!selectedImage || !plantId.trim() || isAnalyzing}
        className="analyze-button"
      >
        {isAnalyzing ? 'Analyzing...' : 'Analyze Plant'}
      </button>
    </div>
  );
}
