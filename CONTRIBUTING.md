# Contributing to Plant Analysis Lab

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what's best for the community
- Show empathy towards others

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/homegrowbook-cmd/Assistent-Agent-/issues)
2. Use the bug report template
3. Include detailed steps to reproduce
4. Add screenshots if applicable

### Suggesting Features

1. Check if the feature has been suggested
2. Use the feature request template
3. Clearly describe the use case
4. Explain how it benefits users

### Contributing Code

1. **Fork the repository**
2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow existing code style
   - Write clear commit messages
   - Add comments for complex logic
   - Update documentation if needed

4. **Test your changes**
   - Run `npm run lint`
   - Run `npm run build`
   - Test manually in browser
   - Test on mobile if UI changes

5. **Commit your changes**
   ```bash
   git commit -m "feat: add new feature"
   ```
   
   Use conventional commits:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation
   - `style:` for formatting
   - `refactor:` for code refactoring
   - `test:` for tests
   - `chore:` for maintenance

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Use the PR template
   - Link related issues
   - Describe your changes
   - Add screenshots for UI changes

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Assistent-Agent-.git

# Install dependencies
cd Assistent-Agent-
npm install

# Start development server
npm run dev

# Open browser
open http://localhost:3000
```

## Code Style

### TypeScript
- Use explicit types
- Avoid `any` type
- Define interfaces for objects
- Use meaningful variable names

### React
- Use functional components
- Use TypeScript with props interfaces
- Keep components focused and small
- Use `'use client'` for client components

### CSS
- Use semantic class names
- Follow mobile-first approach
- Keep styles scoped to components
- Use CSS variables for common values

## Testing

Before submitting:

```bash
# Lint your code
npm run lint

# Build to check for errors
npm run build

# Test manually
npm run dev
```

## Documentation

Update documentation when:
- Adding new features
- Changing APIs
- Modifying configuration
- Adding dependencies

Files to update:
- `README.md` - Main documentation
- `API_DOCUMENTATION.md` - API integration
- `DEVELOPMENT.md` - Development guide
- `TESTING.md` - Testing procedures

## Pull Request Guidelines

### PR Checklist

- [ ] Code follows project style
- [ ] All tests pass (`npm run build`)
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] Branch is up to date with main
- [ ] Screenshots included (UI changes)
- [ ] Tested on multiple browsers

### PR Description

Include:
- What changed and why
- How to test the changes
- Related issues (fixes #123)
- Screenshots/GIFs for UI changes
- Breaking changes (if any)

## Areas for Contribution

### High Priority
- [ ] Real AI vision model integration
- [ ] Backend API for image processing
- [ ] Automated testing suite
- [ ] Image comparison slider
- [ ] Growth prediction algorithms

### Medium Priority
- [ ] Environmental data logging
- [ ] Watering schedules
- [ ] PDF report generation
- [ ] Dark mode
- [ ] Internationalization (i18n)

### Low Priority
- [ ] Community features
- [ ] Social sharing
- [ ] Advanced analytics
- [ ] Mobile app
- [ ] Desktop app (Electron)

## Getting Help

- Read the [README](README.md)
- Check [existing issues](https://github.com/homegrowbook-cmd/Assistent-Agent-/issues)
- Review [documentation](DEVELOPMENT.md)
- Ask in discussions

## Recognition

Contributors will be:
- Listed in README
- Credited in release notes
- Mentioned in project updates

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Plant Analysis Lab! 🌱
