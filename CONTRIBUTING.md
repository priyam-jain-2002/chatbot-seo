# Contributing to Chatbot SEO Skill

Thank you for your interest in contributing! This document provides guidelines for contributing to the Chatbot SEO Optimization Skill.

## 🌟 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Environment details** (OS, Python version, etc.)
- **Screenshots** if applicable

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear use case** - Why is this enhancement needed?
- **Proposed solution** - How should it work?
- **Alternatives considered** - What other approaches did you think about?

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the coding standards below
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Write clear commit messages**
6. **Submit a pull request**

## 📝 Development Guidelines

### Skill Structure

This project follows the standard Claude Skills structure:

```
chatbot-seo/
├── SKILL.md              # Main skill documentation
├── scripts/              # Executable utilities
│   ├── audit_content.py
│   └── schema_generator.py
└── references/           # Reference documentation
    ├── query_patterns.md
    ├── citation_triggers.md
    └── platform_preferences.md
```

### Coding Standards

#### Python Scripts

- Follow **PEP 8** style guide
- Use **meaningful variable names**
- Add **docstrings** to functions and classes
- Include **error handling** with helpful messages
- Keep scripts **self-contained** with minimal dependencies

Example:
```python
def audit_content(url_or_file):
    """
    Audit content for chatbot optimization.
    
    Args:
        url_or_file: URL or file path to audit
        
    Returns:
        dict: Audit results with score and recommendations
    """
    # Implementation
```

#### Markdown Documentation

- Use **clear headings** hierarchy (H1 → H2 → H3)
- Include **code examples** where appropriate
- Keep paragraphs **concise** (3-4 sentences max)
- Use **bullet points** for lists
- Add **emojis** sparingly for visual breaks

### Testing Your Changes

Before submitting a PR:

1. **Test scripts** on sample content:
   ```bash
   python scripts/audit_content.py test-content.html
   python scripts/schema_generator.py
   ```

2. **Validate skill** structure:
   ```bash
   python /path/to/skill-creator/scripts/validate_skill.py chatbot-seo/
   ```

3. **Check markdown** rendering (use a markdown previewer)

4. **Test on different platforms** if making platform-specific changes

## 🎯 Types of Contributions We're Looking For

### High Priority

- **New platform integrations** (e.g., SearchGPT, other AI search engines)
- **Additional audit checks** for content quality
- **Real-world case studies** with before/after examples
- **Bug fixes** and error handling improvements

### Medium Priority

- **Documentation improvements** and clarifications
- **Additional schema types** in generator
- **Performance optimizations** for scripts
- **Internationalization** support

### Nice to Have

- **Visual examples** and screenshots
- **Video tutorials** or guides
- **Integration examples** with popular CMS platforms
- **Community templates** for different industries

## 📚 Adding New Content

### Adding a New Platform

When adding a new AI platform (e.g., SearchGPT):

1. **Research the platform** thoroughly
   - How does it retrieve content?
   - What ranking signals does it use?
   - What unique features does it have?

2. **Add platform section** to `references/platform_preferences.md`:
   ```markdown
   ## [Platform Name]
   
   ### Overview
   [Brief description]
   
   ### How It Works
   [Technical details]
   
   ### Optimization Priorities
   [Specific recommendations]
   ```

3. **Update SKILL.md** if needed
4. **Test recommendations** with real queries
5. **Document sources** for your findings

### Adding Audit Checks

To add a new content audit check in `scripts/audit_content.py`:

```python
def check_new_feature(self):
    """Check for [feature description]"""
    points = 0
    max_points = 10
    issues = []
    
    # Your check logic here
    
    self.results["checks"].append({
        "category": "Feature Name",
        "score": points,
        "max_score": max_points,
        "issues": issues
    })
    return points
```

Then add it to the `audit()` method.

### Adding Schema Types

To add a new schema type to `scripts/schema_generator.py`:

```python
def generate_[type]_schema(params):
    """Generate [Type] schema markup"""
    schema = {
        "@context": "https://schema.org",
        "@type": "[Type]",
        # Schema properties
    }
    return schema
```

Add corresponding interactive function and menu option.

## 🔍 Research Standards

When adding optimization recommendations:

1. **Cite sources** - Link to official documentation or research
2. **Test recommendations** - Verify they work in practice
3. **Provide evidence** - Include examples or data
4. **Be platform-specific** - Don't generalize across all platforms
5. **Stay current** - Note when recommendations were last verified

## 💬 Communication

- **Be respectful** and constructive in all interactions
- **Ask questions** if anything is unclear
- **Share your expertise** - Your insights help everyone
- **Stay on topic** in issues and PRs

## 🏷️ Issue Labels

- `bug` - Something isn't working
- `enhancement` - New feature or improvement
- `documentation` - Documentation improvements
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention needed
- `platform-specific` - Related to specific AI platform
- `scripts` - Related to utility scripts
- `skill-content` - Related to SKILL.md or references

## 📦 Release Process

Major changes go through this process:

1. **Feature branch** - Development happens in feature branches
2. **Testing** - Thorough testing of all changes
3. **Documentation** - Update all relevant docs
4. **PR Review** - At least one approval required
5. **Merge** - Squash and merge to main
6. **Release** - Version bump and changelog update
7. **Package** - Create new .skill file for release

## ❓ Questions?

- Check existing [Issues](https://github.com/yourusername/chatbot-seo-skill/issues)
- Start a [Discussion](https://github.com/yourusername/chatbot-seo-skill/discussions)
- Review closed PRs for similar changes

## 📄 Code of Conduct

- Be welcoming and inclusive
- Be respectful of differing viewpoints
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards others

---

Thank you for contributing to make content more discoverable in the AI-powered search era! 🚀
