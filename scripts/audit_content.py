#!/usr/bin/env python3
"""
Content Audit Script for Chatbot SEO Optimization

Analyzes content for chatbot-friendliness and provides recommendations.
"""

import sys
import re
import json
from urllib.parse import urlparse
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Installing required packages...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--break-system-packages", "requests", "beautifulsoup4", "lxml"])
    import requests
    from bs4 import BeautifulSoup


class ContentAuditor:
    def __init__(self, source):
        self.source = source
        self.is_url = source.startswith(('http://', 'https://'))
        self.soup = None
        self.text_content = ""
        self.results = {
            "source": source,
            "score": 0,
            "max_score": 100,
            "checks": []
        }
    
    def fetch_content(self):
        """Fetch content from URL or file"""
        if self.is_url:
            try:
                response = requests.get(self.source, timeout=10)
                response.raise_for_status()
                self.soup = BeautifulSoup(response.text, 'html.parser')
                self.text_content = self.soup.get_text()
                return True
            except Exception as e:
                print(f"Error fetching URL: {e}")
                return False
        else:
            try:
                with open(self.source, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if self.source.endswith('.html'):
                        self.soup = BeautifulSoup(content, 'html.parser')
                        self.text_content = self.soup.get_text()
                    else:
                        self.text_content = content
                return True
            except Exception as e:
                print(f"Error reading file: {e}")
                return False
    
    def check_structure(self):
        """Check heading structure and hierarchy"""
        points = 0
        max_points = 15
        issues = []
        
        if self.soup:
            # Check for H1
            h1_tags = self.soup.find_all('h1')
            if len(h1_tags) == 1:
                points += 5
                issues.append("✓ Single H1 tag found")
            elif len(h1_tags) == 0:
                issues.append("✗ No H1 tag found - add a clear main heading")
            else:
                issues.append(f"✗ Multiple H1 tags ({len(h1_tags)}) - use only one")
            
            # Check for heading hierarchy
            h2_tags = self.soup.find_all('h2')
            h3_tags = self.soup.find_all('h3')
            
            if h2_tags:
                points += 5
                issues.append(f"✓ {len(h2_tags)} H2 subheadings found")
            else:
                issues.append("✗ No H2 subheadings - add section headers")
            
            if h3_tags and h2_tags:
                points += 5
                issues.append(f"✓ {len(h3_tags)} H3 subheadings found (good hierarchy)")
            
        else:
            # For plain text/markdown
            lines = self.text_content.split('\n')
            h1_count = sum(1 for line in lines if line.startswith('# '))
            h2_count = sum(1 for line in lines if line.startswith('## '))
            
            if h1_count == 1:
                points += 5
                issues.append("✓ Single H1 heading found")
            else:
                issues.append(f"✗ Found {h1_count} H1 headings - use exactly one")
            
            if h2_count > 0:
                points += 10
                issues.append(f"✓ {h2_count} H2 subheadings found")
        
        self.results["checks"].append({
            "category": "Content Structure",
            "score": points,
            "max_score": max_points,
            "issues": issues
        })
        return points
    
    def check_answer_first(self):
        """Check if content has answer-first structure"""
        points = 0
        max_points = 15
        issues = []
        
        # Get first paragraph
        if self.soup:
            paragraphs = self.soup.find_all('p')
            first_para = paragraphs[0].get_text() if paragraphs else ""
        else:
            paragraphs = [p for p in self.text_content.split('\n\n') if p.strip()]
            first_para = paragraphs[0] if paragraphs else ""
        
        first_para_length = len(first_para.split())
        
        if 20 <= first_para_length <= 100:
            points += 10
            issues.append(f"✓ First paragraph is {first_para_length} words (ideal: 20-100)")
        elif first_para_length < 20:
            issues.append(f"✗ First paragraph is too short ({first_para_length} words) - provide more context")
        else:
            issues.append(f"✗ First paragraph is too long ({first_para_length} words) - be more concise")
        
        # Check if first paragraph answers key question words
        question_words = ['what', 'how', 'why', 'when', 'where', 'who']
        if any(word in first_para.lower() for word in question_words):
            points += 5
            issues.append("✓ First paragraph addresses question words")
        else:
            issues.append("~ First paragraph could directly address common questions")
        
        self.results["checks"].append({
            "category": "Answer-First Structure",
            "score": points,
            "max_score": max_points,
            "issues": issues
        })
        return points
    
    def check_citations_data(self):
        """Check for citation-worthy data points"""
        points = 0
        max_points = 20
        issues = []
        
        # Look for numbers and statistics
        number_pattern = r'\d+%|\d+\.\d+%|\$\d+|\d+,\d+|\d+ (million|billion|thousand)'
        numbers = re.findall(number_pattern, self.text_content)
        
        if len(numbers) >= 5:
            points += 10
            issues.append(f"✓ Found {len(numbers)} specific data points")
        elif len(numbers) >= 2:
            points += 5
            issues.append(f"~ Found {len(numbers)} data points - add more statistics")
        else:
            issues.append("✗ Few or no specific statistics - add concrete data")
        
        # Look for year mentions (indicating recency)
        year_pattern = r'20\d{2}'
        years = re.findall(year_pattern, self.text_content)
        current_years = [y for y in years if int(y) >= 2023]
        
        if current_years:
            points += 5
            issues.append(f"✓ References recent data ({', '.join(set(current_years))})")
        else:
            issues.append("✗ No recent year references - add current data")
        
        # Look for source citations
        citation_patterns = ['according to', 'research shows', 'study found', 'data from']
        citations = sum(1 for pattern in citation_patterns if pattern in self.text_content.lower())
        
        if citations >= 3:
            points += 5
            issues.append(f"✓ Found {citations} source attribution phrases")
        elif citations > 0:
            points += 2
            issues.append(f"~ Found {citations} citations - add more source attributions")
        else:
            issues.append("✗ No clear source attributions - cite your sources")
        
        self.results["checks"].append({
            "category": "Citation-Worthy Data",
            "score": points,
            "max_score": max_points,
            "issues": issues
        })
        return points
    
    def check_metadata(self):
        """Check metadata and schema markup"""
        points = 0
        max_points = 15
        issues = []
        
        if not self.soup:
            issues.append("~ Cannot check metadata (not HTML)")
            self.results["checks"].append({
                "category": "Metadata & Schema",
                "score": 0,
                "max_score": max_points,
                "issues": issues
            })
            return 0
        
        # Check title
        title = self.soup.find('title')
        if title and 30 <= len(title.get_text()) <= 70:
            points += 3
            issues.append("✓ Title length is optimal (30-70 chars)")
        elif title:
            issues.append(f"~ Title length is {len(title.get_text())} chars (optimal: 30-70)")
        else:
            issues.append("✗ No title tag found")
        
        # Check meta description
        meta_desc = self.soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            desc_length = len(meta_desc['content'])
            if 120 <= desc_length <= 160:
                points += 3
                issues.append("✓ Meta description length is optimal")
            else:
                issues.append(f"~ Meta description is {desc_length} chars (optimal: 120-160)")
        else:
            issues.append("✗ No meta description found")
        
        # Check for author
        author = self.soup.find('meta', attrs={'name': 'author'})
        if author:
            points += 2
            issues.append("✓ Author metadata present")
        else:
            issues.append("✗ No author metadata - add for authority")
        
        # Check for date
        date_selectors = [
            {'property': 'article:published_time'},
            {'name': 'publish_date'},
            {'itemprop': 'datePublished'}
        ]
        has_date = any(self.soup.find('meta', attrs=sel) for sel in date_selectors)
        if has_date:
            points += 2
            issues.append("✓ Publication date metadata present")
        else:
            issues.append("✗ No publication date - add for recency signal")
        
        # Check for schema markup
        schema = self.soup.find('script', attrs={'type': 'application/ld+json'})
        if schema:
            points += 5
            issues.append("✓ Schema.org markup found")
        else:
            issues.append("✗ No schema markup - add Article or FAQ schema")
        
        self.results["checks"].append({
            "category": "Metadata & Schema",
            "score": points,
            "max_score": max_points,
            "issues": issues
        })
        return points
    
    def check_scannability(self):
        """Check if content is scannable with lists, bold, etc."""
        points = 0
        max_points = 15
        issues = []
        
        if self.soup:
            # Check for lists
            ul_tags = self.soup.find_all('ul')
            ol_tags = self.soup.find_all('ol')
            total_lists = len(ul_tags) + len(ol_tags)
            
            if total_lists >= 2:
                points += 5
                issues.append(f"✓ Found {total_lists} lists (good scannability)")
            elif total_lists == 1:
                points += 3
                issues.append("~ Found 1 list - add more for better scannability")
            else:
                issues.append("✗ No lists found - use bullets for key points")
            
            # Check for bold text
            bold_tags = self.soup.find_all(['b', 'strong'])
            if len(bold_tags) >= 3:
                points += 5
                issues.append(f"✓ Found {len(bold_tags)} bold elements")
            elif len(bold_tags) > 0:
                points += 2
                issues.append(f"~ Found {len(bold_tags)} bold elements - emphasize more key terms")
            else:
                issues.append("✗ No bold text - highlight key terms")
            
            # Check for tables
            tables = self.soup.find_all('table')
            if tables:
                points += 5
                issues.append(f"✓ Found {len(tables)} table(s) for structured data")
        else:
            # Check markdown formatting
            if '- ' in self.text_content or '* ' in self.text_content:
                points += 5
                issues.append("✓ Bullet points found")
            else:
                issues.append("✗ No bullet points - use lists for key points")
            
            if '**' in self.text_content:
                points += 5
                issues.append("✓ Bold text found")
            else:
                issues.append("✗ No bold text - emphasize key terms")
            
            if '|' in self.text_content:
                points += 5
                issues.append("✓ Table formatting found")
        
        self.results["checks"].append({
            "category": "Scannability",
            "score": points,
            "max_score": max_points,
            "issues": issues
        })
        return points
    
    def check_content_length(self):
        """Check content length"""
        points = 0
        max_points = 10
        issues = []
        
        word_count = len(self.text_content.split())
        
        if 800 <= word_count <= 2500:
            points += 10
            issues.append(f"✓ Content length is {word_count} words (ideal range)")
        elif word_count < 300:
            issues.append(f"✗ Content is too short ({word_count} words) - add more depth")
        elif word_count < 800:
            points += 5
            issues.append(f"~ Content is {word_count} words - could be more comprehensive")
        else:
            points += 7
            issues.append(f"~ Content is {word_count} words - ensure it stays focused")
        
        self.results["checks"].append({
            "category": "Content Length",
            "score": points,
            "max_score": max_points,
            "issues": issues
        })
        return points
    
    def check_unique_value(self):
        """Check for indicators of unique value"""
        points = 0
        max_points = 10
        issues = []
        
        unique_indicators = [
            ('our research', 5),
            ('we found', 3),
            ('our analysis', 5),
            ('case study', 4),
            ('we tested', 4),
            ('our survey', 5),
            ('proprietary', 4)
        ]
        
        found = []
        for indicator, pts in unique_indicators:
            if indicator in self.text_content.lower():
                points = min(points + pts, max_points)
                found.append(indicator)
        
        if found:
            issues.append(f"✓ Found unique value indicators: {', '.join(found)}")
        else:
            issues.append("✗ No unique value indicators - add original insights or data")
        
        self.results["checks"].append({
            "category": "Unique Value",
            "score": points,
            "max_score": max_points,
            "issues": issues
        })
        return points
    
    def audit(self):
        """Run all audits"""
        print(f"\n🔍 Auditing: {self.source}\n")
        print("=" * 60)
        
        if not self.fetch_content():
            print("Failed to fetch content")
            return
        
        # Run all checks
        score = 0
        score += self.check_structure()
        score += self.check_answer_first()
        score += self.check_citations_data()
        score += self.check_metadata()
        score += self.check_scannability()
        score += self.check_content_length()
        score += self.check_unique_value()
        
        self.results["score"] = score
        
        # Print results
        print(f"\n📊 OVERALL SCORE: {score}/{self.results['max_score']}")
        print(f"   ({score/self.results['max_score']*100:.0f}%)")
        
        # Categorize score
        if score >= 80:
            print("\n✅ Excellent chatbot optimization")
        elif score >= 60:
            print("\n🟡 Good, with room for improvement")
        elif score >= 40:
            print("\n🟠 Needs optimization")
        else:
            print("\n🔴 Significant optimization needed")
        
        print("\n" + "=" * 60)
        print("\n📋 DETAILED RESULTS:\n")
        
        for check in self.results["checks"]:
            pct = check['score'] / check['max_score'] * 100 if check['max_score'] > 0 else 0
            print(f"{check['category']}:")
            print(f"  Score: {check['score']}/{check['max_score']} ({pct:.0f}%)")
            for issue in check['issues']:
                print(f"  {issue}")
            print()
        
        # Recommendations
        print("=" * 60)
        print("\n💡 TOP RECOMMENDATIONS:\n")
        
        # Priority recommendations based on score gaps
        recommendations = []
        for check in self.results["checks"]:
            pct = check['score'] / check['max_score'] if check['max_score'] > 0 else 0
            if pct < 0.5:
                recommendations.append((check['category'], check['issues']))
        
        if recommendations:
            for i, (category, issues) in enumerate(recommendations[:3], 1):
                print(f"{i}. {category}")
                for issue in issues:
                    if issue.startswith('✗'):
                        print(f"   {issue}")
                print()
        else:
            print("Content is well-optimized! Focus on maintaining quality and freshness.")
        
        return self.results


def main():
    if len(sys.argv) < 2:
        print("Usage: python audit_content.py <url_or_file>")
        print("\nExample:")
        print("  python audit_content.py https://example.com/article")
        print("  python audit_content.py content.html")
        print("  python audit_content.py article.md")
        sys.exit(1)
    
    source = sys.argv[1]
    auditor = ContentAuditor(source)
    auditor.audit()


if __name__ == "__main__":
    main()
