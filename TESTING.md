# Testing Guide

## Manual Testing Instructions

This guide walks you through testing all features of the Plant Analysis Lab application.

## Prerequisites

1. Start the development server:
```bash
npm run dev
```

2. Open browser to `http://localhost:3000`

## Test Scenarios

### 1. Upload and Analyze First Plant

**Objective**: Test basic image upload and analysis functionality

**Steps**:
1. Navigate to "New Analysis" tab (should be default)
2. Enter a Plant ID: `test-plant-001`
3. Click "Choose File" and select an image
4. Verify image preview appears
5. Click "Analyze Plant" button
6. Wait for analysis to complete (2-second delay)
7. Verify analysis results display:
   - Health score (70-100)
   - All 7 metrics populated
   - Image thumbnail visible
   - No "Changes Detected" section (first analysis)

**Expected Result**: Analysis completes successfully and displays comprehensive results.

---

### 2. View Plant in Dashboard

**Objective**: Test plant list functionality

**Steps**:
1. Click "My Plants" tab
2. Verify plant card appears with:
   - Plant ID: `test-plant-001`
   - Health score
   - Analysis count: 1
   - Last updated date
   - Thumbnail image

**Expected Result**: Plant appears in grid with correct information.

---

### 3. Upload Second Analysis (Change Detection)

**Objective**: Test change detection between analyses

**Steps**:
1. Click "New Analysis" tab
2. Enter same Plant ID: `test-plant-001`
3. Upload a different image (or same image)
4. Click "Analyze Plant"
5. Wait for analysis to complete
6. Verify "Changes Detected" section appears with:
   - Growth change description
   - Density change description
   - Color change description
   - Health trend (improved/stable/worse)

**Expected Result**: Change detection section appears showing comparison with previous analysis.

---

### 4. View Plant Timeline

**Objective**: Test timeline visualization

**Steps**:
1. Click "My Plants" tab
2. Click on the plant card for `test-plant-001`
3. Verify timeline modal opens with:
   - Plant name/ID in header
   - Download JSON button
   - Close button
   - Timeline items in chronological order (newest at top)
   - Each item shows:
     - Timestamp
     - Image
     - Health score
     - Key metrics
     - Changes (if applicable)

**Expected Result**: Timeline displays full history of plant analyses.

---

### 5. Download Plant Data

**Objective**: Test JSON export functionality

**Steps**:
1. Open timeline for a plant
2. Click "Download JSON" button
3. Verify file downloads: `plant_test-plant-001_history.json`
4. Open JSON file and verify structure:
   - `plant_id`
   - `analyses` array
   - Each analysis has all required fields

**Expected Result**: JSON file downloads with complete plant history.

---

### 6. Delete Plant

**Objective**: Test plant deletion

**Steps**:
1. Click "My Plants" tab
2. Click trash icon (🗑️) on a plant card
3. Confirm deletion in dialog
4. Verify plant disappears from list
5. Refresh page and verify plant doesn't reappear

**Expected Result**: Plant is permanently deleted from localStorage.

---

### 7. Multiple Plants

**Objective**: Test managing multiple plants

**Steps**:
1. Upload analyses for 3 different plants:
   - `plant-001`
   - `plant-002`
   - `plant-003`
2. Go to "My Plants" tab
3. Verify all 3 plants appear in grid
4. Click each plant to view timeline
5. Verify each has independent history

**Expected Result**: Multiple plants can be tracked independently.

---

### 8. Responsive Design

**Objective**: Test mobile responsiveness

**Steps**:
1. Resize browser window to mobile size (375px width)
2. Test all features:
   - Navigation buttons stack or stay horizontal
   - Upload form remains usable
   - Plant grid becomes single column
   - Timeline modal fits on screen
   - All buttons remain clickable

**Expected Result**: All features work on mobile screen sizes.

---

### 9. Form Validation

**Objective**: Test input validation

**Steps**:
1. Click "New Analysis" tab
2. Try to click "Analyze Plant" without entering Plant ID
   - **Expected**: Button remains disabled
3. Enter Plant ID but don't select image
   - **Expected**: Button remains disabled
4. Select image but clear Plant ID
   - **Expected**: Button becomes disabled again
5. Complete both fields
   - **Expected**: Button becomes enabled

**Expected Result**: Form validates properly before allowing submission.

---

### 10. Empty States

**Objective**: Test UI with no data

**Steps**:
1. Clear browser localStorage: `localStorage.clear()`
2. Refresh page
3. Click "My Plants" tab
4. Verify empty state message appears

**Expected Result**: Helpful message displays when no plants exist.

---

## Browser Testing

Test the application in multiple browsers:

- [ ] Chrome/Edge (Chromium)
- [ ] Firefox
- [ ] Safari (if available)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Mobile (Android)

## Performance Testing

1. **Large Images**: Upload images of 5MB+
2. **Many Analyses**: Add 10+ analyses to one plant
3. **Many Plants**: Track 20+ different plants
4. **Browser Storage**: Check localStorage size

## Accessibility Testing

1. **Keyboard Navigation**:
   - Tab through all interactive elements
   - Press Enter on buttons
   - Navigate forms with keyboard

2. **Screen Reader** (if available):
   - Test with NVDA (Windows) or VoiceOver (Mac)
   - Verify all content is readable
   - Check image alt text

## Known Limitations

1. **Mock Analysis**: Current implementation uses simulated AI analysis
2. **Storage Limit**: localStorage has 5-10MB limit per domain
3. **No Authentication**: Anyone with browser access can view data
4. **No Backend**: Data is stored locally, not synced across devices
5. **Base64 Images**: Large images can slow down the app

## Production Testing

After deploying to GitHub Pages:

1. Visit deployed URL: `https://homegrowbook-cmd.github.io/Assistent-Agent-/`
2. Test all scenarios above
3. Check browser console for errors
4. Verify assets load correctly
5. Test on mobile device

## Automated Testing

Currently, the project has no automated tests. To add tests:

```bash
# Install testing libraries
npm install --save-dev @testing-library/react @testing-library/jest-dom jest-environment-jsdom

# Run tests
npm test
```

Example test structure:

```typescript
// __tests__/ImageUpload.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import ImageUpload from '@/components/ImageUpload';

describe('ImageUpload', () => {
  it('disables button when form incomplete', () => {
    render(<ImageUpload onAnalysisComplete={() => {}} />);
    const button = screen.getByText('Analyze Plant');
    expect(button).toBeDisabled();
  });
});
```

## Bug Reporting

If you find issues, report them with:
- Steps to reproduce
- Expected behavior
- Actual behavior
- Browser and OS version
- Screenshots if applicable

## Performance Benchmarks

Expected performance:
- Initial page load: < 2 seconds
- Image upload: < 1 second
- Analysis completion: 2-3 seconds (mock)
- Timeline render: < 500ms
- Plant list render: < 500ms (up to 50 plants)
