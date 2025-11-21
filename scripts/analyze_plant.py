#!/usr/bin/env python3
"""
Example Python script for plant image analysis using OpenAI's GPT-4 Vision API.
This script demonstrates how to integrate a real AI vision model with the application.

Usage:
    python analyze_plant.py --image path/to/image.jpg --plant-id plant-001

Requirements:
    pip install openai Pillow
"""

import argparse
import base64
import json
import os
import sys
from pathlib import Path

try:
    from openai import OpenAI
    from PIL import Image
except ImportError:
    print("Error: Required packages not installed.")
    print("Install with: pip install openai Pillow")
    sys.exit(1)


ANALYSIS_PROMPT = """
Analyze this plant image and provide a detailed health assessment.

Provide your response ONLY as a JSON object with this exact structure:
{
  "flower_volume": "Assess the overall volume of flowers/buds. Use: Low, Moderate, High, or Very High",
  "flower_density": "Assess how dense the flowers/buds are. Use: Sparse, Moderate, Dense, or Very Dense",
  "color_health": "Describe the color and vibrancy of leaves in 1-2 sentences",
  "leaf_condition": "Describe leaf condition including any spots, damage, or discoloration in 1-2 sentences",
  "stress_signs": "Identify any signs of stress: light burn, overwatering, nutrient deficiency, etc. in 1-2 sentences",
  "general_structure": "Describe the overall plant structure and branching in 1-2 sentences",
  "trichome_development": "If visible, describe trichome development (clear/cloudy/amber ratio). If not visible, say 'Not visible at this magnification'",
  "overall_health_score": "Score from 0-100 based on overall plant health"
}

Be specific, detailed, and accurate. The overall_health_score should be a number between 0 and 100.
"""


def encode_image(image_path: str) -> str:
    """Encode image to base64 string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def compress_image(image_path: str, max_size: tuple = (1920, 1920)) -> str:
    """Compress image if it's too large."""
    img = Image.open(image_path)
    
    # Convert RGBA to RGB if needed
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    # Resize if too large
    if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
    
    # Save to temporary file
    temp_path = "/tmp/compressed_plant_image.jpg"
    img.save(temp_path, "JPEG", quality=85, optimize=True)
    
    return temp_path


def analyze_plant(image_path: str, plant_id: str, api_key: str = None) -> dict:
    """
    Analyze plant image using OpenAI's GPT-4 Vision API.
    
    Args:
        image_path: Path to the plant image
        plant_id: Identifier for the plant
        api_key: OpenAI API key (if not in environment)
    
    Returns:
        Dictionary containing analysis results
    """
    # Initialize OpenAI client
    if api_key:
        client = OpenAI(api_key=api_key)
    else:
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    # Compress image if needed
    print(f"Processing image: {image_path}")
    compressed_path = compress_image(image_path)
    
    # Encode image
    base64_image = encode_image(compressed_path)
    
    print("Sending request to OpenAI...")
    
    try:
        # Call GPT-4 Vision API
        response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": ANALYSIS_PROMPT},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ],
                }
            ],
            max_tokens=1000,
            temperature=0.7,
        )
        
        # Parse response
        content = response.choices[0].message.content
        print(f"Received response: {content[:100]}...")
        
        # Extract JSON from response
        # Sometimes the model wraps JSON in markdown code blocks
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        
        analysis_data = json.loads(content)
        
        # Ensure overall_health_score is an integer
        if isinstance(analysis_data.get("overall_health_score"), str):
            analysis_data["overall_health_score"] = int(analysis_data["overall_health_score"])
        
        # Build complete response
        result = {
            "timestamp": __import__("datetime").datetime.now().isoformat(),
            "plant_id": plant_id,
            "image_url": f"data:image/jpeg;base64,{base64_image}",
            "analysis": analysis_data
        }
        
        return result
        
    except Exception as e:
        print(f"Error during analysis: {str(e)}", file=sys.stderr)
        raise


def main():
    parser = argparse.ArgumentParser(description="Analyze plant image using AI")
    parser.add_argument("--image", required=True, help="Path to plant image")
    parser.add_argument("--plant-id", required=True, help="Plant identifier")
    parser.add_argument("--output", help="Output JSON file path")
    parser.add_argument("--api-key", help="OpenAI API key (overrides env var)")
    
    args = parser.parse_args()
    
    # Check if image exists
    if not Path(args.image).exists():
        print(f"Error: Image file not found: {args.image}", file=sys.stderr)
        sys.exit(1)
    
    # Check for API key
    if not args.api_key and not os.environ.get("OPENAI_API_KEY"):
        print("Error: OpenAI API key required. Set OPENAI_API_KEY environment variable or use --api-key", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Analyze image
        result = analyze_plant(args.image, args.plant_id, args.api_key)
        
        # Output result
        output_json = json.dumps(result, indent=2)
        
        if args.output:
            with open(args.output, "w") as f:
                f.write(output_json)
            print(f"\nAnalysis saved to: {args.output}")
        else:
            print("\nAnalysis Result:")
            print(output_json)
        
        print(f"\nHealth Score: {result['analysis']['overall_health_score']}/100")
        
    except Exception as e:
        print(f"Analysis failed: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
