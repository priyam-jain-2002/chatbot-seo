#!/usr/bin/env python3
"""
Test suite for Chatbot SEO Skill

Run tests to verify all components are working correctly.
"""

import sys
import os
import subprocess
from pathlib import Path

# Colors for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'


def print_test(message):
    print(f"\n{BOLD}Testing:{RESET} {message}")


def print_success(message):
    print(f"{GREEN}✓{RESET} {message}")


def print_failure(message):
    print(f"{RED}✗{RESET} {message}")


def print_warning(message):
    print(f"{YELLOW}⚠{RESET} {message}")


def test_skill_structure():
    """Test that all required files exist"""
    print_test("Skill structure")
    
    required_files = [
        'SKILL.md',
        'README.md',
        'LICENSE',
        'skill.json',
        'scripts/audit_content.py',
        'scripts/schema_generator.py',
        'references/query_patterns.md',
        'references/citation_triggers.md',
        'references/platform_preferences.md'
    ]
    
    all_exist = True
    for file_path in required_files:
        if Path(file_path).exists():
            print_success(f"{file_path} exists")
        else:
            print_failure(f"{file_path} missing")
            all_exist = False
    
    return all_exist


def test_skill_frontmatter():
    """Test SKILL.md has valid frontmatter"""
    print_test("SKILL.md frontmatter")
    
    try:
        with open('SKILL.md', 'r') as f:
            content = f.read()
        
        if not content.startswith('---'):
            print_failure("SKILL.md must start with YAML frontmatter")
            return False
        
        required_fields = ['name:', 'description:']
        for field in required_fields:
            if field in content:
                print_success(f"Found {field}")
            else:
                print_failure(f"Missing {field}")
                return False
        
        # Check name is correct
        if 'name: chatbot-seo' in content:
            print_success("Skill name is correct")
        else:
            print_failure("Skill name should be 'chatbot-seo'")
            return False
        
        return True
    except Exception as e:
        print_failure(f"Error reading SKILL.md: {e}")
        return False


def test_python_dependencies():
    """Test that Python dependencies are available"""
    print_test("Python dependencies")
    
    dependencies = ['requests', 'bs4', 'lxml']
    all_available = True
    
    for dep in dependencies:
        try:
            __import__(dep)
            print_success(f"{dep} is available")
        except ImportError:
            print_warning(f"{dep} not installed (scripts will auto-install)")
    
    return True


def test_audit_script():
    """Test the audit content script"""
    print_test("Audit script functionality")
    
    # Test with README
    try:
        result = subprocess.run(
            ['python3', 'scripts/audit_content.py', 'README.md'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0 and 'OVERALL SCORE' in result.stdout:
            print_success("Audit script runs successfully")
            print_success("Produces expected output format")
            return True
        else:
            print_failure("Audit script failed or produced unexpected output")
            print(result.stdout)
            print(result.stderr)
            return False
    except subprocess.TimeoutExpired:
        print_failure("Audit script timed out")
        return False
    except Exception as e:
        print_failure(f"Error running audit script: {e}")
        return False


def test_schema_generator():
    """Test the schema generator script"""
    print_test("Schema generator functionality")
    
    try:
        # Test with examples flag
        result = subprocess.run(
            ['python3', 'scripts/schema_generator.py', '--examples'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            output = result.stdout
            if 'Article Schema Example' in output and '@context' in output:
                print_success("Schema generator runs successfully")
                print_success("Generates valid JSON-LD output")
                return True
            else:
                print_failure("Schema output format unexpected")
                return False
        else:
            print_failure("Schema generator exited with error")
            return False
    except subprocess.TimeoutExpired:
        print_failure("Schema generator timed out")
        return False
    except Exception as e:
        print_failure(f"Error running schema generator: {e}")
        return False


def test_json_validity():
    """Test that skill.json is valid"""
    print_test("skill.json validity")
    
    try:
        import json
        with open('skill.json', 'r') as f:
            data = json.load(f)
        
        required_fields = ['name', 'version', 'description']
        for field in required_fields:
            if field in data:
                print_success(f"Found {field}: {data[field]}")
            else:
                print_failure(f"Missing required field: {field}")
                return False
        
        return True
    except json.JSONDecodeError as e:
        print_failure(f"Invalid JSON: {e}")
        return False
    except Exception as e:
        print_failure(f"Error reading skill.json: {e}")
        return False


def test_examples():
    """Test example files"""
    print_test("Example files")
    
    example_dir = Path('examples')
    if not example_dir.exists():
        print_warning("Examples directory not found (optional)")
        return True
    
    # Test good example if it exists
    good_example = example_dir / 'good-example.html'
    if good_example.exists():
        try:
            result = subprocess.run(
                ['python3', 'scripts/audit_content.py', str(good_example)],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if 'OVERALL SCORE' in result.stdout:
                # Extract score
                import re
                score_match = re.search(r'OVERALL SCORE: (\d+)/100', result.stdout)
                if score_match:
                    score = int(score_match.group(1))
                    if score >= 60:
                        print_success(f"Good example scores well: {score}/100")
                    else:
                        print_warning(f"Good example score lower than expected: {score}/100")
                return True
        except Exception as e:
            print_warning(f"Could not test good example: {e}")
    
    return True


def run_all_tests():
    """Run all tests and report results"""
    print(f"\n{BOLD}{'='*60}{RESET}")
    print(f"{BOLD}Chatbot SEO Skill Test Suite{RESET}")
    print(f"{BOLD}{'='*60}{RESET}")
    
    tests = [
        ("Skill Structure", test_skill_structure),
        ("Frontmatter", test_skill_frontmatter),
        ("Python Dependencies", test_python_dependencies),
        ("JSON Validity", test_json_validity),
        ("Audit Script", test_audit_script),
        ("Schema Generator", test_schema_generator),
        ("Examples", test_examples)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print_failure(f"Test {name} crashed: {e}")
            results.append((name, False))
    
    # Summary
    print(f"\n{BOLD}{'='*60}{RESET}")
    print(f"{BOLD}Test Summary{RESET}")
    print(f"{BOLD}{'='*60}{RESET}\n")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = f"{GREEN}PASS{RESET}" if result else f"{RED}FAIL{RESET}"
        print(f"{status} - {name}")
    
    print(f"\n{BOLD}Results: {passed}/{total} tests passed{RESET}")
    
    if passed == total:
        print(f"\n{GREEN}{BOLD}✓ All tests passed!{RESET}\n")
        return 0
    else:
        print(f"\n{RED}{BOLD}✗ Some tests failed{RESET}\n")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
