# Repository Structure

```
chatbot-seo-skill/
│
├── 📄 Core Skill Files
│   ├── SKILL.md                          # Main skill documentation
│   ├── skill.json                        # skill.sh configuration
│   └── requirements.txt                  # Python dependencies
│
├── 📚 Documentation
│   ├── README.md                         # Main project documentation
│   ├── QUICKSTART.md                     # 5-minute quick start guide
│   ├── INSTALL.md                        # Detailed installation guide
│   ├── CHANGELOG.md                      # Version history
│   ├── CONTRIBUTING.md                   # Contribution guidelines
│   └── LICENSE                           # MIT License
│
├── 🛠️ Scripts
│   ├── audit_content.py                  # Content optimization auditor
│   ├── schema_generator.py               # Schema markup generator
│   └── test.py                           # Test suite
│
├── 📖 References
│   ├── query_patterns.md                 # Natural language query frameworks
│   ├── citation_triggers.md              # Citation-worthy content elements
│   └── platform_preferences.md           # Platform-specific optimization
│
├── 🧪 Examples
│   ├── README.md                         # Examples guide
│   ├── good-example.html                 # Well-optimized content sample
│   └── bad-example.html                  # Poorly optimized content sample
│
└── 🔧 GitHub Configuration
    ├── .github/
    │   ├── workflows/
    │   │   └── validate.yml              # CI/CD workflow
    │   ├── ISSUE_TEMPLATE/
    │   │   ├── bug_report.md            # Bug report template
    │   │   └── feature_request.md       # Feature request template
    │   └── pull_request_template.md     # PR template
    └── .gitignore                        # Git ignore rules
```

## File Purposes

### Core Skill Files

**SKILL.md**
- Main skill documentation loaded by AI assistants
- Contains optimization workflow and best practices
- Uses progressive disclosure (core info + references)

**skill.json**
- Configuration for skill.sh compatibility
- Metadata and dependency information
- Installation and execution scripts

**requirements.txt**
- Python package dependencies
- Used for manual installation
- Scripts auto-install if missing

### Scripts

**audit_content.py** (1,200+ lines)
- Analyzes content for chatbot-friendliness
- 7 quality checks (structure, data, metadata, etc.)
- Generates scores and actionable recommendations
- Supports URLs and local files

**schema_generator.py** (300+ lines)
- Interactive schema markup creation
- Supports Article, FAQ, HowTo, Person schemas
- Outputs ready-to-use JSON-LD
- Includes examples mode

**test.py** (400+ lines)
- Comprehensive test suite
- Validates skill structure and functionality
- Tests scripts on sample content
- Ensures quality before packaging

### References

**query_patterns.md** (2,500+ words)
- Natural language search frameworks
- Question types and modifiers
- Industry-specific patterns
- Long-tail query strategies

**citation_triggers.md** (3,500+ words)
- Elements that increase citations
- Data points and authority signals
- Platform-specific preferences
- Anti-patterns to avoid

**platform_preferences.md** (4,000+ words)
- Detailed optimization for each platform
- ChatGPT, Gemini, Perplexity, Claude
- Comparative analysis
- Testing strategies

### Examples

**good-example.html**
- Well-optimized article (75+ score)
- Demonstrates all best practices
- Includes schema markup
- Answer-first structure

**bad-example.html**
- Poorly optimized article (30- score)
- Shows common mistakes
- Used for testing and comparison

### GitHub Configuration

**validate.yml**
- Automated testing on push/PR
- Validates skill structure
- Tests scripts functionality
- Packages releases automatically

**Issue/PR Templates**
- Standardized bug reports
- Feature request format
- Pull request checklist
- Improves contribution quality

## Total Size

- **Documentation**: ~10,000 words
- **Code**: ~2,000 lines Python
- **References**: ~10,000 words
- **Examples**: ~1,000 lines HTML
- **Total**: Comprehensive, production-ready skill

## Key Features

✅ **skill.sh compatible** - Install with one command
✅ **Self-contained** - Scripts auto-install dependencies
✅ **Well-tested** - Comprehensive test suite
✅ **Well-documented** - Quick start to deep dive
✅ **CI/CD ready** - GitHub Actions integration
✅ **Open source** - MIT license, contribution-friendly
✅ **Production-ready** - Real-world examples and testing
