# Development Guide

## Getting Started

### System Requirements
- Node.js 18.x or higher
- npm 9.x or higher
- Git
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Initial Setup

1. **Clone and Install**
```bash
git clone https://github.com/homegrowbook-cmd/Assistent-Agent-.git
cd Assistent-Agent-
npm install
```

2. **Start Development Server**
```bash
npm run dev
```

3. **Open Browser**
Navigate to `http://localhost:3000`

## Development Workflow

### File Structure

```
src/
├── app/              # Next.js App Router
│   ├── page.tsx      # Main page component
│   ├── layout.tsx    # Root layout
│   └── globals.css   # Global styles
├── components/       # React components
│   ├── ImageUpload.tsx
│   ├── AnalysisResult.tsx
│   ├── PlantList.tsx
│   └── PlantTimeline.tsx
├── lib/              # Utility functions
│   ├── analysis.ts   # AI analysis logic
│   └── storage.ts    # Local storage wrapper
└── types/            # TypeScript types
    └── index.ts
```

### Code Style

#### TypeScript
- Use TypeScript for all new files
- Define explicit types for function parameters and returns
- Use interfaces for object shapes
- Avoid `any` type

```typescript
// Good
interface PlantData {
  id: string;
  name: string;
  score: number;
}

function processPlant(data: PlantData): void {
  // ...
}

// Avoid
function processPlant(data: any) {
  // ...
}
```

#### React Components
- Use functional components with hooks
- Use 'use client' directive for client components
- Keep components small and focused
- Extract reusable logic into custom hooks

```typescript
'use client';

import { useState, useEffect } from 'react';

export default function MyComponent() {
  const [data, setData] = useState<string>('');
  
  useEffect(() => {
    // Load data
  }, []);
  
  return <div>{data}</div>;
}
```

#### CSS
- Use semantic class names
- Follow mobile-first approach
- Keep selectors specific but not overly nested
- Use CSS variables for common values

```css
/* Good */
.plant-card {
  padding: 20px;
  border-radius: 10px;
}

.plant-card-header {
  font-size: 1.2rem;
}

/* Avoid deep nesting */
.plant-card .header .title .text {
  /* ... */
}
```

## Building Features

### Adding a New Component

1. Create component file in `src/components/`
```typescript
// src/components/NewComponent.tsx
'use client';

interface NewComponentProps {
  data: string;
}

export default function NewComponent({ data }: NewComponentProps) {
  return <div>{data}</div>;
}
```

2. Import and use in page
```typescript
// src/app/page.tsx
import NewComponent from '@/components/NewComponent';

export default function Home() {
  return <NewComponent data="test" />;
}
```

### Modifying Analysis Logic

The analysis logic is in `src/lib/analysis.ts`:

```typescript
export const analyzePlantImage = async (
  imageData: string,
  plantId: string,
  previousAnalysis?: PlantAnalysis
): Promise<PlantAnalysis> => {
  // Add your custom analysis logic here
  // This is where you'd integrate with a real AI API
};
```

### Adding New Storage Functions

Storage functions are in `src/lib/storage.ts`:

```typescript
export const customStorageFunction = (): void => {
  // Use localStorage API
  localStorage.setItem('key', 'value');
};
```

## Testing

### Manual Testing Checklist

- [ ] Image upload works on desktop
- [ ] Image upload works on mobile
- [ ] Analysis completes successfully
- [ ] Results display correctly
- [ ] Plant list shows all plants
- [ ] Timeline view opens and displays history
- [ ] JSON export downloads correctly
- [ ] Delete plant removes data
- [ ] Responsive design works on all screen sizes

### Testing with Example Data

```typescript
// Add to your code for testing
const mockAnalysis: PlantAnalysis = {
  timestamp: new Date().toISOString(),
  plant_id: 'test-plant',
  analysis: {
    flower_volume: 'High',
    flower_density: 'Dense',
    color_health: 'Vibrant green',
    leaf_condition: 'Excellent',
    stress_signs: 'None',
    general_structure: 'Well-developed',
    trichome_development: 'Cloudy',
    overall_health_score: 90,
  },
};
```

## Building and Deployment

### Local Build

```bash
npm run build
```

This creates an optimized production build in the `out` directory.

### Preview Production Build

```bash
npm run build
npx serve out
```

### Deploy to GitHub Pages

Push to main branch or the feature branch, and GitHub Actions will automatically deploy.

## Debugging

### Common Issues

#### 1. Build Fails
```bash
# Clear cache and reinstall
rm -rf .next node_modules
npm install
npm run build
```

#### 2. TypeScript Errors
```bash
# Check types
npx tsc --noEmit
```

#### 3. LocalStorage Not Working
- Check browser privacy settings
- Verify window is defined (SSR issue)
- Use typeof window !== 'undefined' checks

#### 4. Images Not Loading
- Check image paths
- Verify basePath in next.config.js
- Ensure images are in public directory

### Browser DevTools

Use Chrome DevTools:
1. **Console**: Check for errors
2. **Network**: Monitor API calls
3. **Application**: Inspect localStorage
4. **Elements**: Debug CSS issues
5. **Performance**: Profile slow operations

## Performance Optimization

### Image Handling
- Compress images before upload
- Use WebP format when possible
- Implement lazy loading for plant list

### Code Splitting
Next.js automatically code-splits, but you can optimize further:

```typescript
import dynamic from 'next/dynamic';

const HeavyComponent = dynamic(() => import('@/components/HeavyComponent'), {
  loading: () => <p>Loading...</p>,
});
```

### Memoization
```typescript
import { useMemo, useCallback } from 'react';

function MyComponent({ data }: Props) {
  const processed = useMemo(() => {
    return expensiveOperation(data);
  }, [data]);
  
  const handler = useCallback(() => {
    // Handler logic
  }, []);
  
  return <div>{processed}</div>;
}
```

## Contributing Guidelines

### Before Submitting PR

1. Run linter
```bash
npm run lint
```

2. Build successfully
```bash
npm run build
```

3. Test manually
4. Update documentation if needed
5. Write clear commit messages

### Commit Message Format
```
type: brief description

Detailed explanation if needed

Fixes #123
```

Types: feat, fix, docs, style, refactor, test, chore

### Code Review Checklist
- [ ] Code follows style guidelines
- [ ] No console.log statements
- [ ] Types are properly defined
- [ ] Components are properly documented
- [ ] Responsive design maintained
- [ ] Accessibility considerations
- [ ] Performance impact considered

## Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [React Documentation](https://react.dev)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [MDN Web Docs](https://developer.mozilla.org/)

## Getting Help

- Check existing documentation
- Search GitHub issues
- Review example files
- Ask in discussions
