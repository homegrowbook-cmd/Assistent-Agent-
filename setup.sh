#!/bin/bash

# Grow Documentation Assistant - Setup Script
# This script helps set up the environment for the assistant

echo "🌱 Grow Documentation Assistant - Setup"
echo "========================================"
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Create necessary directories
echo "Creating directories..."
mkdir -p images/uploads images/analyzed images/archive
mkdir -p data docs output
echo "✓ Directories created"
echo ""

# Check if config.yaml exists
if [ ! -f "config.yaml" ]; then
    echo "⚠ Warning: config.yaml not found"
    echo "  Please create config.yaml from config.yaml.example"
else
    echo "✓ Configuration file found"
fi
echo ""

echo "========================================"
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Add images to images/uploads/"
echo "3. (Optional) Add data JSON files to data/"
echo "4. Run the assistant: python assistant.py"
echo ""
echo "For more information, see README.md"
