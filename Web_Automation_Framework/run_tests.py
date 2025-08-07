#!/usr/bin/env python3
"""
Test runner script for Behave BDD Automation Framework
This script provides different options to run tests with various configurations.
"""

import os
import sys
import subprocess
import argparse
from datetime import datetime

# Prevent Python from generating cache files (.pyc and __pycache__)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

def run_command(command, description):
    """Run a command and handle the output"""
    print(f"\n{'='*50}")
    print(f"🚀 {description}")
    print(f"{'='*50}")
    print(f"Command: {command}")
    print("-" * 50)
    
    try:
        # Set environment variable for subprocess to prevent cache files
        env = os.environ.copy()
        env['PYTHONDONTWRITEBYTECODE'] = '1'
        
        result = subprocess.run(command, shell=True, capture_output=False, text=True, env=env)
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
        else:
            print(f"❌ {description} failed with return code: {result.returncode}")
        return result.returncode
    except Exception as e:
        print(f"❌ Error running command: {e}")
        return 1

def run_web_tests():
    """Run web automation tests"""
    return run_command("behave features/web/", "Running Web Tests")

def run_api_tests():
    """Run API tests"""
    return run_command("behave features/api/", "Running API Tests")

def run_qpathways_tests():
    """Run Qpathways Value tests"""
    return run_command("behave features/web/QPathways_Value/", "Running Qpathways Value Tests")

def run_all_tests():
    """Run all tests"""
    return run_command("behave", "Running All Tests")

def run_tests_with_tags(tags):
    """Run tests with specific tags"""
    return run_command(f"behave --tags={tags}", f"Running Tests with Tags: {tags}")

def run_tests_with_format(format_type):
    """Run tests with specific format"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if format_type == "json":
        return run_command(f"behave --format=json --outfile=reports/results_{timestamp}.json", 
                          "Running Tests with JSON Output")
    elif format_type == "html":
        return run_command(f"behave --format=html --outfile=reports/report_{timestamp}.html", 
                          "Running Tests with HTML Output")
    elif format_type == "allure":
        return run_command(f"behave --format=allure_behave.formatter:AllureFormatter --outdir=reports/allure_{timestamp}", 
                          "Running Tests with Allure Output")
    else:
        return run_command("behave --format=pretty", "Running Tests with Pretty Output")

def check_environment():
    """Check if the environment is set up correctly"""
    print("🔍 Checking Environment Setup...")
    
    # Check if required directories exist
    required_dirs = ['features', 'pages', 'utils', 'reports', 'screenshots']
    missing_dirs = []
    
    for directory in required_dirs:
        if not os.path.exists(directory):
            missing_dirs.append(directory)
    
    if missing_dirs:
        print(f"❌ Missing directories: {', '.join(missing_dirs)}")
        print("Run 'python setup.py' to create required directories")
        return False
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("⚠️  .env file not found. Using default configuration.")
        if os.path.exists('config.env.template'):
            print("You can create .env file from template: cp config.env.template .env")
    
    # Check if requirements are installed
    try:
        import selenium
        import requests
        import behave
        print("✅ All required packages are installed")
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Run 'pip install -r requirements.txt' to install required packages")
        return False
    
    print("✅ Environment setup is correct")
    return True

def main():
    """Main function to handle command line arguments"""
    parser = argparse.ArgumentParser(description='Behave BDD Test Runner')
    parser.add_argument('--web', action='store_true', help='Run web tests only')
    parser.add_argument('--api', action='store_true', help='Run API tests only')
    parser.add_argument('--qpathways', action='store_true', help='Run Qpathways Value tests only')
    parser.add_argument('--all', action='store_true', help='Run all tests')
    parser.add_argument('--tags', type=str, help='Run tests with specific tags (e.g., @smoke)')
    parser.add_argument('--format', choices=['pretty', 'json', 'html', 'allure'], 
                       default='pretty', help='Output format')
    parser.add_argument('--check', action='store_true', help='Check environment setup')
    
    args = parser.parse_args()
    
    # Check environment first
    if args.check or not check_environment():
        if args.check:
            return
        else:
            sys.exit(1)
    
    # Create reports directory if it doesn't exist
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    # Create screenshots directory if it doesn't exist
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    
    # Run tests based on arguments
    if args.web:
        return_code = run_web_tests()
    elif args.api:
        return_code = run_api_tests()
    elif args.qpathways:
        return_code = run_qpathways_tests()
    elif args.tags:
        return_code = run_tests_with_tags(args.tags)
    elif args.all:
        return_code = run_all_tests()
    else:
        # Default behavior based on format
        return_code = run_tests_with_format(args.format)
    
    # Summary
    print(f"\n{'='*50}")
    if return_code == 0:
        print("🎉 Test execution completed successfully!")
    else:
        print("❌ Test execution failed!")
    print(f"{'='*50}")
    
    sys.exit(return_code)

if __name__ == "__main__":
    main() 