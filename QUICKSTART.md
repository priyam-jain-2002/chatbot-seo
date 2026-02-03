# Quick Start Guide

Get up and running with Chatbot SEO optimization in 5 minutes.

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/chatbot-seo-skill.git
cd chatbot-seo-skill

# Install dependencies (optional - scripts auto-install)
pip install -r requirements.txt
```

## 📝 Your First Content Audit

Audit your first piece of content:

```bash
python scripts/audit_content.py https://yourwebsite.com/article
```

**Example output:**
```
🔍 Auditing: https://yourwebsite.com/article

📊 OVERALL SCORE: 65/100 (65%)

🟡 Good, with room for improvement

💡 TOP RECOMMENDATIONS:

1. Citation-Worthy Data
   ✗ Few or no specific statistics - add concrete data
   ✗ No recent year references - add current data

2. Metadata & Schema
   ✗ No schema markup - add Article or FAQ schema
```

## ⚡ Quick Optimization

Based on the audit, make these improvements:

### 1. Add Specific Data
```markdown
❌ Before: "Many users prefer this approach"
✅ After: "73% of users prefer this approach (2024 survey, n=5,000)"
```

### 2. Answer-First Structure
```markdown
❌ Before:
# Guide to Running Shoes
Running shoes are important...

✅ After:
# What Are the Best Running Shoes for Flat Feet?
The best running shoes for flat feet are stability shoes 
with motion control, such as Brooks Adrenaline GTS 23...
```

### 3. Add Schema Markup
```bash
python scripts/schema_generator.py
# Choose option 1 (Article)
# Fill in the prompts
# Copy the generated schema to your HTML
```

## 🧪 Test Your Changes

Re-run the audit to see improvements:

```bash
python scripts/audit_content.py updated-article.html
```

You should see a higher score!

## 🎯 Advanced Usage

### Platform-Specific Optimization

Check the platform guides:

```bash
# Read about ChatGPT optimization
cat references/platform_preferences.md | grep -A 20 "ChatGPT Search"

# Read about Perplexity optimization  
cat references/platform_preferences.md | grep -A 20 "Perplexity"
```

### Natural Language Keywords

Review query patterns for keyword ideas:

```bash
cat references/query_patterns.md
```

### Check Citation Triggers

See what makes content citation-worthy:

```bash
cat references/citation_triggers.md
```

## 📚 Full Documentation

- **Complete guide**: [SKILL.md](SKILL.md)
- **Detailed README**: [README.md](README.md)
- **Installation help**: [INSTALL.md](INSTALL.md)

## ✅ Optimization Checklist

Use this checklist for every piece of content:

```markdown
- [ ] Answer-first paragraph (1-2 sentences)
- [ ] Clear H1 with target question
- [ ] 2-3 specific data points with sources
- [ ] Author credentials visible
- [ ] Publication date in 2024+
- [ ] Schema markup added
- [ ] Bullet points for key info
- [ ] Table for comparisons (if applicable)
- [ ] Links to primary sources
```

## 🎓 Next Steps

1. **Audit your top 10 pages**
   ```bash
   for url in url1 url2 url3; do
     python scripts/audit_content.py $url >> audit-results.txt
   done
   ```

2. **Create schema for all articles**
   ```bash
   python scripts/schema_generator.py
   ```

3. **Test in AI chatbots**
   - Query ChatGPT about your topic
   - Check Perplexity
   - See if your content gets cited

4. **Iterate based on results**
   - Not cited? Add more data
   - Cited incorrectly? Improve structure
   - Low prominence? Strengthen authority

## 💡 Pro Tips

1. **Update regularly** - Add "Updated [Month Year]" to titles
2. **Be specific** - "34% increase" beats "significant increase"  
3. **Show your work** - Explain methodology for original research
4. **Use real examples** - Better than generic explanations
5. **Think questions** - Optimize for "How/What/Why" queries

## ❓ Common Questions

**Q: How long does optimization take?**
A: Initial audit: 2 minutes. Making changes: 30-60 minutes per article.

**Q: Will this hurt traditional SEO?**
A: No! Chatbot SEO best practices align with modern SEO.

**Q: Which platform should I optimize for first?**
A: Start with universal best practices (answer-first, data, schema) - they work for all platforms.

**Q: How do I measure success?**
A: Manually query AI chatbots about your topics. Track citations over time.

## 🆘 Need Help?

- Check [examples/](examples/) for before/after samples
- Review closed [issues](https://github.com/yourusername/chatbot-seo-skill/issues?q=is%3Aissue+is%3Aclosed)
- Start a [discussion](https://github.com/yourusername/chatbot-seo-skill/discussions)

---

Ready to optimize? Start with your most important content first! 🚀
