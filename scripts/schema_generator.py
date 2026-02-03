#!/usr/bin/env python3
"""
Schema Markup Generator for Chatbot SEO

Generates appropriate schema.org markup for different content types.
"""

import json
import sys
from datetime import datetime


def generate_article_schema(title, author, organization, date_published, date_modified=None):
    """Generate Article schema markup"""
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "author": {
            "@type": "Person",
            "name": author
        },
        "publisher": {
            "@type": "Organization",
            "name": organization,
            "logo": {
                "@type": "ImageObject",
                "url": "https://example.com/logo.png"  # Replace with actual logo URL
            }
        },
        "datePublished": date_published,
        "dateModified": date_modified or date_published
    }
    return schema


def generate_howto_schema(name, description, steps):
    """Generate HowTo schema markup"""
    schema = {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": name,
        "description": description,
        "step": []
    }
    
    for i, step in enumerate(steps, 1):
        schema["step"].append({
            "@type": "HowToStep",
            "name": f"Step {i}",
            "text": step,
            "position": i
        })
    
    return schema


def generate_faq_schema(qa_pairs):
    """Generate FAQ schema markup"""
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }
    
    for question, answer in qa_pairs:
        schema["mainEntity"].append({
            "@type": "Question",
            "name": question,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": answer
            }
        })
    
    return schema


def generate_breadcrumb_schema(items):
    """Generate BreadcrumbList schema markup"""
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": []
    }
    
    for i, (name, url) in enumerate(items, 1):
        schema["itemListElement"].append({
            "@type": "ListItem",
            "position": i,
            "name": name,
            "item": url
        })
    
    return schema


def generate_person_schema(name, job_title, organization, description, url=None):
    """Generate Person schema markup for author bio"""
    schema = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": name,
        "jobTitle": job_title,
        "worksFor": {
            "@type": "Organization",
            "name": organization
        },
        "description": description
    }
    
    if url:
        schema["url"] = url
    
    return schema


def format_schema_html(schema):
    """Format schema as HTML script tag"""
    json_str = json.dumps(schema, indent=2)
    return f'<script type="application/ld+json">\n{json_str}\n</script>'


def interactive_article():
    """Interactive article schema generator"""
    print("\n📝 Article Schema Generator")
    print("-" * 40)
    
    title = input("Article title: ")
    author = input("Author name: ")
    organization = input("Organization/Publisher: ")
    date_published = input("Publication date (YYYY-MM-DD) [Today]: ").strip() or datetime.now().strftime("%Y-%m-%d")
    date_modified = input("Modified date (YYYY-MM-DD) [Same as published]: ").strip()
    
    schema = generate_article_schema(title, author, organization, date_published, date_modified or None)
    
    print("\n✅ Generated Article Schema:")
    print(format_schema_html(schema))


def interactive_howto():
    """Interactive HowTo schema generator"""
    print("\n📋 HowTo Schema Generator")
    print("-" * 40)
    
    name = input("HowTo title: ")
    description = input("Brief description: ")
    
    print("\nEnter steps (one per line, empty line to finish):")
    steps = []
    i = 1
    while True:
        step = input(f"Step {i}: ").strip()
        if not step:
            break
        steps.append(step)
        i += 1
    
    if not steps:
        print("No steps provided!")
        return
    
    schema = generate_howto_schema(name, description, steps)
    
    print("\n✅ Generated HowTo Schema:")
    print(format_schema_html(schema))


def interactive_faq():
    """Interactive FAQ schema generator"""
    print("\n❓ FAQ Schema Generator")
    print("-" * 40)
    
    print("\nEnter Q&A pairs (empty question to finish):")
    qa_pairs = []
    i = 1
    while True:
        question = input(f"\nQuestion {i}: ").strip()
        if not question:
            break
        answer = input(f"Answer {i}: ").strip()
        if not answer:
            print("Answer cannot be empty!")
            continue
        qa_pairs.append((question, answer))
        i += 1
    
    if not qa_pairs:
        print("No Q&A pairs provided!")
        return
    
    schema = generate_faq_schema(qa_pairs)
    
    print("\n✅ Generated FAQ Schema:")
    print(format_schema_html(schema))


def interactive_person():
    """Interactive Person schema generator"""
    print("\n👤 Person/Author Schema Generator")
    print("-" * 40)
    
    name = input("Full name: ")
    job_title = input("Job title: ")
    organization = input("Organization: ")
    description = input("Brief bio: ")
    url = input("Profile URL (optional): ").strip() or None
    
    schema = generate_person_schema(name, job_title, organization, description, url)
    
    print("\n✅ Generated Person Schema:")
    print(format_schema_html(schema))


def show_examples():
    """Show example schemas"""
    print("\n📚 Schema Examples\n")
    
    print("1. Article Schema Example:")
    print("-" * 40)
    article_example = generate_article_schema(
        "How to Optimize for Chatbot SEO",
        "Jane Smith",
        "SEO Experts Inc",
        "2024-02-01",
        "2024-02-15"
    )
    print(format_schema_html(article_example))
    
    print("\n2. FAQ Schema Example:")
    print("-" * 40)
    faq_example = generate_faq_schema([
        ("What is chatbot SEO?", "Chatbot SEO is the practice of optimizing content for discovery by AI-powered search engines and chatbots."),
        ("Why is it important?", "As more users rely on AI assistants for information, optimizing for chatbot discovery ensures your content remains visible.")
    ])
    print(format_schema_html(faq_example))
    
    print("\n3. HowTo Schema Example:")
    print("-" * 40)
    howto_example = generate_howto_schema(
        "How to Add Schema Markup",
        "Learn to implement schema.org structured data on your website",
        [
            "Choose the appropriate schema type for your content",
            "Generate the JSON-LD markup using a schema generator",
            "Add the script tag to your HTML head section",
            "Validate using Google's Rich Results Test"
        ]
    )
    print(format_schema_html(howto_example))


def main():
    print("\n🎯 Schema Markup Generator for Chatbot SEO")
    print("=" * 50)
    
    if len(sys.argv) > 1 and sys.argv[1] == "--examples":
        show_examples()
        return
    
    while True:
        print("\nChoose schema type:")
        print("1. Article")
        print("2. HowTo")
        print("3. FAQ")
        print("4. Person/Author")
        print("5. Show Examples")
        print("6. Exit")
        
        choice = input("\nEnter choice (1-6): ").strip()
        
        if choice == "1":
            interactive_article()
        elif choice == "2":
            interactive_howto()
        elif choice == "3":
            interactive_faq()
        elif choice == "4":
            interactive_person()
        elif choice == "5":
            show_examples()
        elif choice == "6":
            print("\n👋 Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        cont = input("\nGenerate another schema? (y/n): ").strip().lower()
        if cont != 'y':
            break


if __name__ == "__main__":
    main()
