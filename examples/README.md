# Example Content for Testing

This directory contains sample content files for testing the chatbot SEO optimization tools.

## Files

- `good-example.html` - Well-optimized content example
- `bad-example.html` - Poorly optimized content example
- `sample-article.md` - Markdown article for testing

## Usage

Test the audit script on these examples:

```bash
# Test on good example
python scripts/audit_content.py examples/good-example.html

# Test on bad example
python scripts/audit_content.py examples/bad-example.html

# Compare the scores
```

## Expected Results

- **good-example.html**: Should score 75-90/100
- **bad-example.html**: Should score 20-40/100

Use these to understand what makes content chatbot-friendly!
