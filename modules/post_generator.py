"""
Post Generator Module
======================

Generates social media posts based on:
- Image analysis results
- Data insights
- Growth milestones
- Best practices
"""

import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class PostGenerator:
    """Generates social media posts"""
    
    def __init__(self, config):
        """Initialize post generator
        
        Args:
            config: Configuration manager instance
        """
        self.config = config
        logger.info("PostGenerator initialized")
    
    def generate(self, image_analysis=None, data_insights=None):
        """Generate a post based on available data
        
        Args:
            image_analysis: Optional image analysis results
            data_insights: Optional data insights
            
        Returns:
            Generated post text
        """
        logger.info("Generating post")
        
        post_parts = []
        
        # Header
        post_parts.append("🌱 Grow Update 🌱")
        post_parts.append("")
        post_parts.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        post_parts.append("")
        
        # Image analysis section
        if image_analysis:
            post_parts.append("📸 Image Analysis:")
            post_parts.append(self._format_image_analysis(image_analysis))
            post_parts.append("")
        
        # Data insights section
        if data_insights:
            post_parts.append("📊 Data Insights:")
            post_parts.append(self._format_data_insights(data_insights))
            post_parts.append("")
        
        # Footer
        post_parts.append("---")
        post_parts.append("#grow #plants #documentation #gardening")
        
        return "\n".join(post_parts)
    
    def _format_image_analysis(self, image_analysis):
        """Format image analysis for post
        
        Args:
            image_analysis: Image analysis results
            
        Returns:
            Formatted text
        """
        lines = []
        
        if isinstance(image_analysis, list):
            for idx, result in enumerate(image_analysis, 1):
                if 'filename' in result:
                    lines.append(f"  Image {idx}: {result['filename']}")
                
                if 'analysis' in result:
                    analysis = result['analysis']
                    
                    if 'estimated_health' in analysis:
                        lines.append(f"    Health: {analysis['estimated_health']}")
                    
                    if 'color_analysis' in analysis and 'green_dominance' in analysis['color_analysis']:
                        green_dom = analysis['color_analysis']['green_dominance']
                        lines.append(f"    Green dominance: {green_dom:.2f}")
                    
                    if 'brightness' in analysis:
                        lines.append(f"    Brightness: {analysis['brightness']:.1f}/255")
                
                lines.append("")
        
        return "\n".join(lines)
    
    def _format_data_insights(self, data_insights):
        """Format data insights for post
        
        Args:
            data_insights: Data insights list
            
        Returns:
            Formatted text
        """
        lines = []
        
        # Group insights by category
        warnings = [i for i in data_insights if i.get('type') == 'warning']
        infos = [i for i in data_insights if i.get('type') == 'info']
        
        if warnings:
            lines.append("  ⚠️ Warnings:")
            for warning in warnings:
                lines.append(f"    • {warning.get('message', 'Unknown warning')}")
            lines.append("")
        
        if infos:
            lines.append("  ℹ️ Information:")
            for info in infos[:5]:  # Limit to 5 info items
                lines.append(f"    • {info.get('message', 'Unknown info')}")
        
        return "\n".join(lines)
    
    def generate_milestone_post(self, milestone_type, details):
        """Generate a post for a growth milestone
        
        Args:
            milestone_type: Type of milestone (e.g., 'germination', 'flowering')
            details: Details about the milestone
            
        Returns:
            Generated post text
        """
        logger.info(f"Generating milestone post: {milestone_type}")
        
        post_parts = []
        
        # Milestone-specific emoji and title
        milestones = {
            'germination': '🌱 Germination Milestone!',
            'vegetative': '🌿 Entered Vegetative Stage!',
            'flowering': '🌸 Flowering Has Begun!',
            'harvest': '🎉 Harvest Time!',
        }
        
        title = milestones.get(milestone_type, '🌱 Growth Milestone!')
        
        post_parts.append(title)
        post_parts.append("")
        post_parts.append(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
        post_parts.append("")
        
        if details:
            post_parts.append("Details:")
            if isinstance(details, dict):
                for key, value in details.items():
                    post_parts.append(f"  • {key}: {value}")
            else:
                post_parts.append(f"  {details}")
        
        post_parts.append("")
        post_parts.append("---")
        post_parts.append(f"#grow #milestone #{milestone_type}")
        
        return "\n".join(post_parts)
    
    def generate_weekly_summary(self, weekly_data):
        """Generate a weekly summary post
        
        Args:
            weekly_data: Data collected over the week
            
        Returns:
            Generated post text
        """
        logger.info("Generating weekly summary post")
        
        post_parts = []
        
        post_parts.append("📅 Weekly Grow Summary 📅")
        post_parts.append("")
        post_parts.append(f"Week ending: {datetime.now().strftime('%Y-%m-%d')}")
        post_parts.append("")
        
        if 'images_processed' in weekly_data:
            post_parts.append(f"📸 Images processed: {weekly_data['images_processed']}")
        
        if 'avg_health' in weekly_data:
            post_parts.append(f"🌱 Average health: {weekly_data['avg_health']}")
        
        if 'growth_rate' in weekly_data:
            post_parts.append(f"📈 Growth rate: {weekly_data['growth_rate']}")
        
        if 'notes' in weekly_data:
            post_parts.append("")
            post_parts.append("Notes:")
            post_parts.append(weekly_data['notes'])
        
        post_parts.append("")
        post_parts.append("---")
        post_parts.append("#grow #weeklysummary #progress")
        
        return "\n".join(post_parts)
