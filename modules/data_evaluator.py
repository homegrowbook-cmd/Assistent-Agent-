"""
Data Evaluator Module
======================

Evaluates grow data including:
- Environmental conditions
- Growth metrics
- Historical trends
- Optimization suggestions
"""

import logging
import json
from datetime import datetime, timedelta
from pathlib import Path

logger = logging.getLogger(__name__)


class DataEvaluator:
    """Evaluates grow data and generates insights"""
    
    def __init__(self, config):
        """Initialize data evaluator
        
        Args:
            config: Configuration manager instance
        """
        self.config = config
        self.data_dir = Path('data')
        logger.info("DataEvaluator initialized")
    
    def evaluate(self):
        """Evaluate all available data
        
        Returns:
            List of insights and recommendations
        """
        logger.info("Starting data evaluation")
        
        insights = []
        
        # Check for data files
        data_files = list(self.data_dir.glob('*.json'))
        
        if not data_files:
            logger.info("No data files found")
            return self._generate_welcome_insights()
        
        # Process each data file
        for data_file in data_files:
            try:
                insights.extend(self._evaluate_file(data_file))
            except Exception as e:
                logger.error(f"Error evaluating {data_file.name}: {e}")
        
        return insights
    
    def _evaluate_file(self, file_path):
        """Evaluate a single data file
        
        Args:
            file_path: Path to data file
            
        Returns:
            List of insights from this file
        """
        logger.info(f"Evaluating data file: {file_path.name}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            insights = []
            
            # Environmental data
            if 'environment' in data:
                insights.extend(self._evaluate_environment(data['environment']))
            
            # Growth metrics
            if 'growth' in data:
                insights.extend(self._evaluate_growth(data['growth']))
            
            # Historical trends
            if 'history' in data:
                insights.extend(self._evaluate_trends(data['history']))
            
            return insights
            
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in {file_path.name}: {e}")
            return []
    
    def _evaluate_environment(self, env_data):
        """Evaluate environmental conditions
        
        Args:
            env_data: Environmental data dictionary
            
        Returns:
            List of insights
        """
        insights = []
        
        # Temperature check
        if 'temperature' in env_data:
            temp = env_data['temperature']
            if temp < 18:
                insights.append({
                    'type': 'warning',
                    'category': 'temperature',
                    'message': f'Temperature is low ({temp}°C). Consider increasing heat.'
                })
            elif temp > 28:
                insights.append({
                    'type': 'warning',
                    'category': 'temperature',
                    'message': f'Temperature is high ({temp}°C). Consider cooling.'
                })
            else:
                insights.append({
                    'type': 'info',
                    'category': 'temperature',
                    'message': f'Temperature is optimal ({temp}°C).'
                })
        
        # Humidity check
        if 'humidity' in env_data:
            humidity = env_data['humidity']
            if humidity < 40:
                insights.append({
                    'type': 'warning',
                    'category': 'humidity',
                    'message': f'Humidity is low ({humidity}%). Consider humidifier.'
                })
            elif humidity > 70:
                insights.append({
                    'type': 'warning',
                    'category': 'humidity',
                    'message': f'Humidity is high ({humidity}%). Increase ventilation.'
                })
            else:
                insights.append({
                    'type': 'info',
                    'category': 'humidity',
                    'message': f'Humidity is good ({humidity}%).'
                })
        
        return insights
    
    def _evaluate_growth(self, growth_data):
        """Evaluate growth metrics
        
        Args:
            growth_data: Growth data dictionary
            
        Returns:
            List of insights
        """
        insights = []
        
        if 'height' in growth_data:
            height = growth_data['height']
            insights.append({
                'type': 'info',
                'category': 'growth',
                'message': f'Current plant height: {height}cm'
            })
        
        if 'stage' in growth_data:
            stage = growth_data['stage']
            insights.append({
                'type': 'info',
                'category': 'growth',
                'message': f'Current growth stage: {stage}'
            })
        
        return insights
    
    def _evaluate_trends(self, history_data):
        """Evaluate historical trends
        
        Args:
            history_data: Historical data list
            
        Returns:
            List of insights
        """
        insights = []
        
        if not history_data or len(history_data) < 2:
            return insights
        
        # Analyze growth rate
        if len(history_data) >= 2:
            insights.append({
                'type': 'info',
                'category': 'trend',
                'message': f'Historical data available for {len(history_data)} data points'
            })
        
        return insights
    
    def _generate_welcome_insights(self):
        """Generate welcome insights for new setup
        
        Returns:
            List of welcome insights
        """
        return [
            {
                'type': 'info',
                'category': 'setup',
                'message': 'Welcome to Grow Documentation Assistant!'
            },
            {
                'type': 'info',
                'category': 'setup',
                'message': 'Place images in images/uploads/ directory to analyze them'
            },
            {
                'type': 'info',
                'category': 'setup',
                'message': 'Add JSON data files to data/ directory for evaluation'
            }
        ]
    
    def save_insights(self, insights, output_path='data/insights.json'):
        """Save insights to file
        
        Args:
            insights: List of insights
            output_path: Path to save insights
        """
        try:
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'timestamp': datetime.now().isoformat(),
                    'insights': insights
                }, f, indent=2)
            
            logger.info(f"Insights saved to {output_path}")
            
        except Exception as e:
            logger.error(f"Error saving insights: {e}")
