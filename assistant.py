"""
Grow Documentation Assistant Agent
===================================

Main entry point for the documentation assistant that:
- Analyzes grow data
- Processes and analyzes images
- Prepares social media posts
- Manages documentation

Author: Grow Documentation Team
"""

import os
import sys
import logging
from datetime import datetime
from pathlib import Path

# Add modules directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules'))

from image_analyzer import ImageAnalyzer
from data_evaluator import DataEvaluator
from post_generator import PostGenerator
from config_manager import ConfigManager

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('assistant.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class GrowAssistant:
    """Main assistant class for grow documentation"""
    
    def __init__(self, config_path='config.yaml'):
        """Initialize the grow assistant
        
        Args:
            config_path: Path to configuration file
        """
        logger.info("Initializing Grow Documentation Assistant")
        
        self.config = ConfigManager(config_path)
        self.image_analyzer = ImageAnalyzer(self.config)
        self.data_evaluator = DataEvaluator(self.config)
        self.post_generator = PostGenerator(self.config)
        
        # Ensure image directories exist
        self._ensure_directories()
    
    def _ensure_directories(self):
        """Ensure all required directories exist"""
        directories = [
            'images/uploads',
            'images/analyzed',
            'images/archive',
            'data',
            'docs',
            'output'
        ]
        
        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
            logger.debug(f"Ensured directory exists: {directory}")
    
    def process_new_images(self):
        """Process new images in the uploads directory"""
        logger.info("Processing new images...")
        
        upload_dir = Path('images/uploads')
        image_files = list(upload_dir.glob('*.jpg')) + \
                     list(upload_dir.glob('*.jpeg')) + \
                     list(upload_dir.glob('*.png'))
        
        if not image_files:
            logger.info("No new images to process")
            return []
        
        results = []
        for image_path in image_files:
            try:
                logger.info(f"Analyzing image: {image_path.name}")
                analysis = self.image_analyzer.analyze(str(image_path))
                results.append({
                    'filename': image_path.name,
                    'analysis': analysis,
                    'timestamp': datetime.now().isoformat()
                })
                
                # Move to analyzed directory
                analyzed_path = Path('images/analyzed') / image_path.name
                image_path.rename(analyzed_path)
                logger.info(f"Moved to analyzed: {analyzed_path}")
                
            except Exception as e:
                logger.error(f"Error processing {image_path.name}: {e}")
        
        return results
    
    def evaluate_data(self):
        """Evaluate grow data and generate insights"""
        logger.info("Evaluating grow data...")
        
        try:
            insights = self.data_evaluator.evaluate()
            logger.info(f"Generated {len(insights)} insights")
            return insights
        except Exception as e:
            logger.error(f"Error evaluating data: {e}")
            return []
    
    def generate_post(self, image_analysis=None, data_insights=None):
        """Generate a social media post
        
        Args:
            image_analysis: Optional image analysis results
            data_insights: Optional data insights
            
        Returns:
            Generated post content
        """
        logger.info("Generating post...")
        
        try:
            post = self.post_generator.generate(
                image_analysis=image_analysis,
                data_insights=data_insights
            )
            
            # Save post to output directory
            output_dir = Path('output')
            output_dir.mkdir(exist_ok=True)
            
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = output_dir / f'post_{timestamp}.txt'
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(post)
            
            logger.info(f"Post saved to: {output_file}")
            return post
            
        except Exception as e:
            logger.error(f"Error generating post: {e}")
            return None
    
    def run_full_cycle(self):
        """Run a complete processing cycle"""
        logger.info("=" * 50)
        logger.info("Starting full processing cycle")
        logger.info("=" * 50)
        
        # Process images
        image_results = self.process_new_images()
        
        # Evaluate data
        data_insights = self.evaluate_data()
        
        # Generate post if we have content
        if image_results or data_insights:
            post = self.generate_post(
                image_analysis=image_results,
                data_insights=data_insights
            )
            
            if post:
                logger.info("Post generated successfully")
                logger.info("-" * 50)
                logger.info(post)
                logger.info("-" * 50)
        else:
            logger.info("No new content to process")
        
        logger.info("=" * 50)
        logger.info("Processing cycle complete")
        logger.info("=" * 50)


def main():
    """Main entry point"""
    logger.info("Starting Grow Documentation Assistant")
    
    try:
        assistant = GrowAssistant()
        assistant.run_full_cycle()
        
    except KeyboardInterrupt:
        logger.info("Assistant stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
