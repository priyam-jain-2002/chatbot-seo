# Installation Guide

Multiple ways to install and use the Chatbot SEO Optimization Skill.

## 📦 Method 1: Via skill.sh (Recommended)

If you have skill.sh installed:

```bash
# Install directly from GitHub
skill install https://github.com/yourusername/chatbot-seo-skill

# Or install from npm/skill registry (if published)
skill install chatbot-seo

# Verify installation
skill list
```

## 💾 Method 2: Download .skill File

1. Go to [Releases](https://github.com/yourusername/chatbot-seo-skill/releases)
2. Download the latest `chatbot-seo-vX.X.X.skill` file
3. Import into your AI assistant:
   - **Claude**: Upload the .skill file in the Skills menu
   - **Other platforms**: Follow platform-specific import instructions

## 🔧 Method 3: Clone Repository

For development or manual installation:

```bash
# Clone the repository
git clone https://github.com/yourusername/chatbot-seo-skill.git
cd chatbot-seo-skill

# Optional: Install Python dependencies
pip install -r requirements.txt

# Use scripts directly
python scripts/audit_content.py your-content.html
python scripts/schema_generator.py
```

## 🐍 Method 4: Standalone Scripts

If you only need the scripts without the full skill:

```bash
# Download individual scripts
curl -O https://raw.githubusercontent.com/yourusername/chatbot-seo-skill/main/scripts/audit_content.py
curl -O https://raw.githubusercontent.com/yourusername/chatbot-seo-skill/main/scripts/schema_generator.py

# Install dependencies
pip install requests beautifulsoup4 lxml

# Run scripts
python audit_content.py https://yoursite.com/article
python schema_generator.py
```

## ✅ Verify Installation

After installation, verify everything works:

```bash
# Test audit script
python scripts/audit_content.py README.md

# Test schema generator
python scripts/schema_generator.py

# Check version
cat skill.json | grep version
```

Expected output:
```
🔍 Auditing: README.md
...
📊 OVERALL SCORE: XX/100
```

## 🔄 Updating

### Via skill.sh
```bash
skill update chatbot-seo
```

### Manual update
```bash
cd chatbot-seo-skill
git pull origin main
```

### From releases
Download the latest .skill file and re-import

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'requests'"

Install Python dependencies:
```bash
pip install requests beautifulsoup4 lxml
```

### "Permission denied" when running scripts

Make scripts executable:
```bash
chmod +x scripts/*.py
```

### "SKILL.md not found"

Ensure you're in the correct directory:
```bash
cd chatbot-seo-skill
ls -la SKILL.md
```

### Scripts not working on Windows

Use Python explicitly:
```bash
python scripts/audit_content.py your-file.html
```

Instead of:
```bash
./scripts/audit_content.py your-file.html
```

## 📋 Requirements

- **Python**: 3.7 or higher
- **Packages**: requests, beautifulsoup4, lxml (auto-installed by scripts if missing)
- **Optional**: skill.sh for easy management

## 🌐 Platform-Specific Notes

### Claude (claude.ai)
- Upload .skill file in Skills menu
- Skill will be available in all conversations
- Can be enabled/disabled per conversation

### Local Development
- Clone repository for full access
- Modify scripts as needed
- Submit PRs for improvements

### Other AI Platforms
- Check platform-specific skill import documentation
- May need to adapt file structure

## 🆘 Getting Help

If you encounter issues:

1. Check [Troubleshooting](#-troubleshooting) section above
2. Review [GitHub Issues](https://github.com/yourusername/chatbot-seo-skill/issues)
3. Create a new issue with:
   - Your installation method
   - Python version (`python --version`)
   - Error message (full stack trace)
   - Operating system

## 🎓 Next Steps

After installation:

1. Read the [README.md](README.md) for an overview
2. Review [SKILL.md](SKILL.md) for complete documentation
3. Try the audit script on your content
4. Explore reference guides in `references/`
5. Generate schema markup for your pages

---

Happy optimizing! 🚀
