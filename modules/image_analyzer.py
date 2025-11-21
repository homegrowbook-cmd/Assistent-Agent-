"""
Image Analyzer Module
=====================

Analyzes images of plants to detect:
- Plant health
- Growth stage
- Potential issues
- Environmental conditions
"""

import logging
from pathlib import Path
from PIL import Image
import numpy as np

logger = logging.getLogger(__name__)


class ImageAnalyzer:
    """Analyzes plant images"""
    
    def __init__(self, config):
        """Initialize image analyzer
        
        Args:
            config: Configuration manager instance
        """
        self.config = config
        logger.info("ImageAnalyzer initialized")
    
    def analyze(self, image_path):
        """Analyze a single image
        
        Args:
            image_path: Path to image file
            
        Returns:
            Dictionary with analysis results
        """
        logger.info(f"Analyzing image: {image_path}")
        
        try:
            # Load image
            img = Image.open(image_path)
            img_array = np.array(img)
            
            # Basic analysis
            analysis = {
                'dimensions': {
                    'width': img.width,
                    'height': img.height
                },
                'format': img.format,
                'mode': img.mode,
                'color_analysis': self._analyze_colors(img_array),
                'brightness': self._calculate_brightness(img_array),
                'estimated_health': self._estimate_health(img_array)
            }
            
            logger.info(f"Analysis complete for {image_path}")
            return analysis
            
        except Exception as e:
            logger.error(f"Error analyzing image {image_path}: {e}")
            raise
    
    def _analyze_colors(self, img_array):
        """Analyze color composition of image
        
        Args:
            img_array: Numpy array of image
            
        Returns:
            Dictionary with color analysis
        """
        if len(img_array.shape) < 3:
            return {'error': 'Image is not in color format'}
        
        # Calculate average RGB values
        avg_red = np.mean(img_array[:, :, 0])
        avg_green = np.mean(img_array[:, :, 1])
        avg_blue = np.mean(img_array[:, :, 2])
        
        # Calculate green dominance (indicator of healthy vegetation)
        green_dominance = avg_green / (avg_red + avg_blue + 1e-6)
        
        return {
            'average_rgb': {
                'red': float(avg_red),
                'green': float(avg_green),
                'blue': float(avg_blue)
            },
            'green_dominance': float(green_dominance)
        }
    
    def _calculate_brightness(self, img_array):
        """Calculate overall brightness
        
        Args:
            img_array: Numpy array of image
            
        Returns:
            Brightness value (0-255)
        """
        if len(img_array.shape) == 3:
            # Convert to grayscale
            brightness = np.mean(img_array)
        else:
            brightness = np.mean(img_array)
        
        return float(brightness)
    
    def _estimate_health(self, img_array):
        """Estimate plant health based on image analysis
        
        Args:
            img_array: Numpy array of image
            
        Returns:
            Health estimation string
        """
        colors = self._analyze_colors(img_array)
        
        if 'error' in colors:
            return 'Unknown'
        
        green_dom = colors['green_dominance']
        
        if green_dom > 1.3:
            return 'Excellent - Strong green coloration'
        elif green_dom > 1.1:
            return 'Good - Healthy green color'
        elif green_dom > 0.9:
            return 'Fair - Moderate green color'
        else:
            return 'Poor - Low green coloration, check plant health'
    
    def batch_analyze(self, image_directory):
        """Analyze multiple images in a directory
        
        Args:
            image_directory: Path to directory containing images
            
        Returns:
            List of analysis results
        """
        results = []
        image_dir = Path(image_directory)
        
        image_patterns = ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG']
        image_files = []
        
        for pattern in image_patterns:
            image_files.extend(image_dir.glob(pattern))
        
        logger.info(f"Found {len(image_files)} images to analyze")
        
        for image_path in image_files:
            try:
                analysis = self.analyze(str(image_path))
                results.append({
                    'filename': image_path.name,
                    'analysis': analysis
                })
            except Exception as e:
                logger.error(f"Failed to analyze {image_path.name}: {e}")
        
        return results
