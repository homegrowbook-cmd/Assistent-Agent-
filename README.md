# 🌱 Plant Analysis Lab

AI-Powered Plant Health Tracking & Growth Analysis Application

[![Deploy to GitHub Pages](https://github.com/homegrowbook-cmd/Assistent-Agent-/actions/workflows/deploy.yml/badge.svg)](https://github.com/homegrowbook-cmd/Assistent-Agent-/actions/workflows/deploy.yml)

## 📋 Overview

Plant Analysis Lab is a comprehensive web application that uses AI vision models to analyze plant images and track growth over time. Built with Next.js and deployed on GitHub Pages, it provides professional-grade plant health monitoring with a clean, responsive interface inspired by modern grow tracking platforms.

## 📸 Screenshots

### Main Interface
![Plant Analysis Lab - Homepage](https://github.com/user-attachments/assets/dae9171f-b747-47b3-b785-48ff06739022)

### My Plants Dashboard
![My Plants View](https://github.com/user-attachments/assets/a599d60b-58e5-4237-b64f-3415c8659bce)

## ✨ Features

### Core Functionality
- **📸 Image Upload Interface**: Mobile and desktop-optimized image upload with preview
- **🤖 AI-Powered Analysis**: Comprehensive plant health evaluation including:
  - Flower volume and density
  - Leaf and color health assessment
  - Leaf condition (spots, damage, discoloration)
  - General plant structure evaluation
  - Stress indicators (light burn, overwatering, nutrient deficiency)
  - Trichome development monitoring
  - Overall health score (0-100)

### Advanced Features
- **📊 Change Detection**: Automatic comparison with previous analyses to detect:
  - Growth changes
  - Density variations
  - Color changes
  - Health trends (improved/stable/worse)
- **📝 Automatic Documentation**: Each analysis saved as JSON with timestamp
- **📈 Timeline View**: Visual timeline showing plant progression over time
- **💾 Data Export**: Download complete plant history as JSON files
- **🗂️ Multi-Plant Management**: Track multiple plants simultaneously
- **📱 Responsive Design**: Fully responsive UI that works on all devices

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ and npm
- Git

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/homegrowbook-cmd/Assistent-Agent-.git
cd Assistent-Agent-
```

2. **Install dependencies**
```bash
npm install
```

3. **Run development server**
```bash
npm run dev
```

4. **Open browser**
Navigate to [http://localhost:3000](http://localhost:3000)

### Building for Production

```bash
npm run build
```

This creates an optimized production build in the `out` directory.

## 📦 Deployment

### GitHub Pages (Automated)

The application automatically deploys to GitHub Pages when changes are pushed to the main branch or `copilot/build-plant-image-analysis-app` branch.

**Setup Steps:**

1. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Source: "GitHub Actions"

2. **Permissions**
   - Settings → Actions → General → Workflow permissions
   - Enable "Read and write permissions"

3. **Deploy**
   - Push to main or the feature branch
   - GitHub Actions will automatically build and deploy
   - Access at: `https://homegrowbook-cmd.github.io/Assistent-Agent-/`

### Manual Deployment

```bash
npm run export
```

Deploy the contents of the `out` directory to any static hosting service.

## 🗂️ Project Structure

```
Assistent-Agent-/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions deployment workflow
├── public/
│   ├── analysis/               # Example analysis JSON files
│   └── examples/               # Example images (to be added)
├── src/
│   ├── app/
│   │   ├── globals.css        # Global styles
│   │   ├── layout.tsx         # Root layout
│   │   └── page.tsx           # Main application page
│   ├── components/
│   │   ├── ImageUpload.tsx    # Image upload component
│   │   ├── AnalysisResult.tsx # Analysis display component
│   │   ├── PlantList.tsx      # Plant list/grid component
│   │   └── PlantTimeline.tsx  # Timeline visualization
│   ├── lib/
│   │   ├── analysis.ts        # AI analysis logic
│   │   └── storage.ts         # Local storage management
│   └── types/
│       └── index.ts           # TypeScript type definitions
├── next.config.js             # Next.js configuration
├── package.json               # Dependencies and scripts
├── tsconfig.json              # TypeScript configuration
└── README.md                  # This file
```

## 🔧 Configuration

### Next.js Configuration

The `next.config.js` file is configured for GitHub Pages deployment:

```javascript
{
  output: 'export',              // Static export
  images: { unoptimized: true }, // Disable image optimization for static export
  basePath: '/Assistent-Agent-', // GitHub Pages subdirectory
}
```

For local development, the base path is automatically empty.

### Environment Variables

No environment variables required for basic functionality. For future integration with actual AI vision APIs:

```bash
# .env.local (not committed)
NEXT_PUBLIC_API_URL=your-api-url
VISION_API_KEY=your-api-key
```

## 📊 Data Format

### Analysis JSON Structure

```json
{
  "timestamp": "2024-01-15T10:30:00.000Z",
  "plant_id": "plant-001",
  "image_url": "data:image/jpeg;base64,...",
  "analysis": {
    "flower_volume": "High | Moderate | Low | Very High",
    "flower_density": "Dense | Moderate | Sparse | Very Dense",
    "color_health": "Description of leaf color and vitality",
    "leaf_condition": "Description of leaf health and damage",
    "stress_signs": "Description of any stress indicators",
    "general_structure": "Description of plant structure",
    "trichome_development": "Description of trichome state",
    "overall_health_score": 85
  },
  "changes_detected": {
    "growth_change": "Description of growth changes",
    "density_change": "Description of density changes",
    "color_change": "Description of color changes",
    "health_trend": "improved | stable | worse"
  }
}
```

## 🎨 UI Features

### Design Philosophy
- **Clean & Modern**: Minimalistic interface focused on functionality
- **Color-Coded Health Scores**: Visual health indicators
  - 90-100: Green (Excellent)
  - 75-89: Light Green (Good)
  - 60-74: Yellow (Fair)
  - <60: Red (Poor)
- **Responsive Grid**: Adaptive layouts for all screen sizes
- **Smooth Animations**: Polished transitions and interactions

### Key Components

1. **Upload Interface**
   - Drag-and-drop or click to select
   - Live image preview
   - Plant ID/name input
   - One-click analysis

2. **Analysis Display**
   - Large health score display
   - Detailed metrics breakdown
   - Change detection highlights
   - Trend indicators

3. **Plant Dashboard**
   - Grid view of all plants
   - Quick health overview
   - Click to view timeline
   - Delete functionality

4. **Timeline View**
   - Chronological analysis history
   - Visual progress tracking
   - Export to JSON
   - Side-by-side comparisons

## 🔮 Future Enhancements

### Planned Features
- [ ] Real AI vision model integration (GitHub Actions workflow)
- [ ] Backend API for image processing
- [ ] Image comparison slider
- [ ] Growth prediction algorithms
- [ ] Environmental data logging (temperature, humidity)
- [ ] Watering and feeding schedules
- [ ] Community features (share anonymously)
- [ ] Mobile app (React Native)
- [ ] Advanced analytics dashboard
- [ ] PDF report generation

### AI Model Integration

The current implementation uses mock analysis. To integrate a real vision model:

1. Create a GitHub Action that accepts image data
2. Call vision API (OpenAI GPT-4 Vision, Google Vision, etc.)
3. Parse response into the expected format
4. Return analysis JSON

Example workflow structure:
```yaml
name: Analyze Plant Image
on:
  workflow_dispatch:
    inputs:
      image_data:
        description: 'Base64 encoded image'
        required: true
jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - name: Call Vision API
        run: # API call logic
      - name: Return Analysis
        run: # Format and return JSON
```

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [Next.js 14](https://nextjs.org/)
- Deployed on [GitHub Pages](https://pages.github.com/)
- Inspired by [GrowDiaries](https://growdiaries.com/) and similar platforms
- Icon emojis from Unicode Standard

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review example files in `/public/analysis/`

## 🎯 Use Cases

- **Home Growers**: Track personal plant health and growth
- **Commercial Operations**: Monitor multiple plants systematically
- **Research**: Document plant development for studies
- **Education**: Learn about plant health indicators
- **Troubleshooting**: Identify and track plant stress over time

---

**Built with ❤️ for the plant growing community**