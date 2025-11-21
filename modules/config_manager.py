"""
Configuration Manager Module
=============================

Manages configuration settings for the assistant
"""

import logging
import yaml
from pathlib import Path

logger = logging.getLogger(__name__)


class ConfigManager:
    """Manages configuration settings"""
    
    def __init__(self, config_path='config.yaml'):
        """Initialize configuration manager
        
        Args:
            config_path: Path to configuration file
        """
        self.config_path = Path(config_path)
        self.config = self._load_config()
        logger.info(f"Configuration loaded from {config_path}")
    
    def _load_config(self):
        """Load configuration from file
        
        Returns:
            Configuration dictionary
        """
        if not self.config_path.exists():
            logger.warning(f"Config file not found: {self.config_path}, using defaults")
            return self._get_default_config()
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            return config or self._get_default_config()
        except Exception as e:
            logger.error(f"Error loading config: {e}, using defaults")
            return self._get_default_config()
    
    def _get_default_config(self):
        """Get default configuration
        
        Returns:
            Default configuration dictionary
        """
        return {
            'image_analysis': {
                'supported_formats': ['jpg', 'jpeg', 'png'],
                'max_size_mb': 10,
                'archive_after_days': 30
            },
            'data_evaluation': {
                'check_interval_hours': 24,
                'temperature_range': [18, 28],
                'humidity_range': [40, 70]
            },
            'post_generation': {
                'auto_generate': True,
                'include_hashtags': True,
                'max_length': 500
            },
            'directories': {
                'uploads': 'images/uploads',
                'analyzed': 'images/analyzed',
                'archive': 'images/archive',
                'data': 'data',
                'output': 'output'
            }
        }
    
    def get(self, key, default=None):
        """Get configuration value
        
        Args:
            key: Configuration key (supports dot notation, e.g., 'image_analysis.max_size_mb')
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key, value):
        """Set configuration value
        
        Args:
            key: Configuration key (supports dot notation)
            value: Value to set
        """
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def save(self):
        """Save configuration to file"""
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                yaml.dump(self.config, f, default_flow_style=False)
            logger.info(f"Configuration saved to {self.config_path}")
        except Exception as e:
            logger.error(f"Error saving config: {e}")
