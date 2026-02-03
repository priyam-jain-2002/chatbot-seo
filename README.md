# 🤖 Chatbot SEO Optimization Skill

> Optimize your content for AI-powered search engines and chatbots (ChatGPT, Gemini, Claude, Perplexity)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Compatible with skill.sh](https://img.shields.io/badge/skill.sh-compatible-blue.svg)](https://skill.sh)

## 📋 Overview

As AI chatbots become the new search interface, traditional SEO is evolving. This skill helps you optimize content for how Large Language Models retrieve, parse, and cite information—a practice known as **AEO** (Answer Engine Optimization) or **GEO** (Generative Engine Optimization).

### What You'll Learn

- ✅ How chatbots discover and cite content
- ✅ Answer-first content architecture
- ✅ Platform-specific optimization (ChatGPT, Gemini, Perplexity, Claude)
- ✅ Schema markup implementation
- ✅ Natural language keyword research
- ✅ Citation-worthy content creation

## 🚀 Quick Start

### Installation via skill.sh

```bash
# Install the skill
skill install chatbot-seo

# Or install from this repository
skill install https://github.com/yourusername/chatbot-seo-skill
```

### Manual Installation

1. Download the `.skill` file from [Releases](https://github.com/yourusername/chatbot-seo-skill/releases)
2. Import into Claude or your AI assistant
3. Start optimizing!

## 🛠️ Tools Included

### 1. Content Audit Script

Analyze your content for chatbot-friendliness:

```bash
python scripts/audit_content.py https://yoursite.com/article
# or
python scripts/audit_content.py content.html
```

**Sample Output:**
```
📊 OVERALL SCORE: 73/100 (73%)

✅ Excellent chatbot optimization

📋 DETAILED RESULTS:

Content Structure: 12/15 (80%)
  ✓ Single H1 tag found
  ✓ 5 H2 subheadings found
  ✗ No H3 subheadings - add deeper hierarchy

Answer-First Structure: 10/15 (67%)
  ✓ First paragraph is 45 words (ideal: 20-100)
  ~ First paragraph could directly address common questions
```

### 2. Schema Markup Generator

Create optimized structured data:

```bash
python scripts/schema_generator.py
```

Supports:
- Article schema
- FAQ schema  
- HowTo schema
- Person/Author schema
- Breadcrumb schema

### 3. Comprehensive Reference Guides

- **Query Patterns** - Natural language search frameworks
- **Citation Triggers** - Elements that increase citation likelihood
- **Platform Preferences** - Detailed optimization for each AI platform

## 📚 Core Concepts

### How Chatbots Discover Content

1. **Web Search Integration**: Most chatbots use search APIs that prioritize:
   - Recent, authoritative content
   - Clear, well-structured pages
   - Original sources over aggregators

2. **Content Parsing**: LLMs extract information by:
   - Scanning for direct answers
   - Identifying authoritative statements
   - Extracting structured data (tables, lists, statistics)

3. **Citation Logic**: Chatbots cite sources that:
   - Directly answer the query
   - Provide unique insights or data
   - Include specific facts and statistics
   - Come from trusted domains

### The Answer-First Architecture

```markdown
# [Clear, specific H1 with target question]

[Direct answer in first 1-2 sentences]

[Supporting details follow]

## Key Points
- Bullet point 1 with specific data
- Bullet point 2 with specific data

## Detailed Explanation
[Comprehensive context]
```

**Why it works:**
- ✅ LLMs can quickly extract the core answer
- ✅ Users get immediate value
- ✅ Supports various query intents

## 🎯 Optimization Workflow

### Step 1: Content Audit
```bash
python scripts/audit_content.py your-content.html
```

### Step 2: Keyword Research
Focus on natural language queries:
- ❌ "best running shoes"
- ✅ "What are the best running shoes for flat feet?"

See [`references/query_patterns.md`](references/query_patterns.md) for frameworks.

### Step 3: Add Citation-Worthy Elements
- 📊 Original research and statistics
- 👤 Author credentials
- 📅 Recent publication dates
- 🔗 Primary source citations

### Step 4: Implement Schema Markup
```bash
python scripts/schema_generator.py
```

### Step 5: Test & Monitor
Query ChatGPT Search, Perplexity, or Claude about your topic and check if your content is cited.

## 🌐 Platform-Specific Tips

### ChatGPT Search
- ⚡ Heavily favors recent content
- 📝 Prefers clear, concise answers
- 🔗 Often cites 3-5 sources per response

### Google Gemini
- 🎓 Strong E-E-A-T emphasis (Experience, Expertise, Authoritativeness, Trust)
- 🏛️ Prefers established, authoritative domains
- 📐 Values comprehensive schema markup

### Perplexity
- 🔢 Excellent at finding specific data points
- 📚 Values primary research and original studies
- 🎯 Good at surfacing niche, specialized content

### Claude
- 🤝 Synthesizes from multiple high-quality sources
- 📌 Explicit citation of specific claims
- 📖 Prefers comprehensive, well-structured content

## 📖 Documentation

- [SKILL.md](SKILL.md) - Complete skill guide
- [Query Patterns Reference](references/query_patterns.md) - Natural language query frameworks
- [Citation Triggers Reference](references/citation_triggers.md) - Elements that increase citations
- [Platform Preferences Guide](references/platform_preferences.md) - Platform-specific strategies

## 🧪 Examples

### Before Optimization
```markdown
# Running Shoes Guide

Running shoes are important for runners. There are many types available.
Different shoes work for different people.
```

### After Optimization
```markdown
# What Are the Best Running Shoes for Flat Feet? (Updated Feb 2024)

The best running shoes for flat feet are stability shoes with motion control,
such as the Brooks Adrenaline GTS 23 and ASICS GT-2000 12, which provide
arch support and reduce overpronation by 34% according to a 2024 biomechanics study.

## Key Recommendations
- **Brooks Adrenaline GTS 23**: Best overall stability ($140, 4.8/5 rating)
- **ASICS GT-2000 12**: Best value ($130, reduces pronation 32%)
- **Saucony Guide 16**: Best for wide feet ($150, extended width options)

[Detailed content with specific data...]
```

## ✅ Optimization Checklist

- [ ] Answer-first content structure
- [ ] Clear, descriptive headings (H1, H2, H3)
- [ ] Specific data points and statistics
- [ ] Author credentials visible
- [ ] Publication/update date prominent
- [ ] Schema markup implemented
- [ ] Mobile-friendly and fast-loading
- [ ] Primary source links included
- [ ] Unique insights or original research
- [ ] Natural language optimized for questions
- [ ] Key points in scannable format
- [ ] Comprehensive but concise answers

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built for the Claude AI Skills ecosystem
- Inspired by the evolution of search from keywords to natural language
- Thanks to the SEO and AI communities for sharing optimization insights

## 📬 Contact

- Issues: [GitHub Issues](https://github.com/yourusername/chatbot-seo-skill/issues)
- Discussions: [GitHub Discussions](https://github.com/yourusername/chatbot-seo-skill/discussions)

## 🔗 Related Resources

- [Anthropic Claude Documentation](https://docs.anthropic.com)
- [skill.sh](https://skill.sh) - AI Skills ecosystem
- [Schema.org Documentation](https://schema.org)

---

**Star ⭐ this repository if you find it helpful!**

Made with ❤️ for the AI-powered search era
