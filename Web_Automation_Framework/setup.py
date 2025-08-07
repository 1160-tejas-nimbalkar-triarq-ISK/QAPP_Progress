#!/usr/bin/env python3
"""
Setup script for Behave BDD Automation Framework
This script helps initialize the framework with required directories and files.
"""

import os
import shutil
import sys

# Prevent Python from generating cache files
import os
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

def create_directories():
    """Create required directories"""
    directories = [
        'reports',
        'screenshots',
        'test_data'
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✓ Created directory: {directory}")
        else:
            print(f"✓ Directory already exists: {directory}")

def create_env_file():
    """Create .env file from template"""
    if not os.path.exists('.env'):
        if os.path.exists('config.env.template'):
            shutil.copy('config.env.template', '.env')
            print("✓ Created .env file from template")
            print("  Please update .env with your specific configuration values")
        else:
            print("✗ Template file not found: config.env.template")
    else:
        print("✓ .env file already exists")

def create_gitignore():
    """Create .gitignore file"""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Testing
.coverage
.pytest_cache/
.tox/
.nox/
htmlcov/

# Behave
reports/
screenshots/
test_data/
*.log

# Environment
.env
.env.local
.env.production

# OS
.DS_Store
Thumbs.db
"""
    
    if not os.path.exists('.gitignore'):
        with open('.gitignore', 'w') as f:
            f.write(gitignore_content)
        print("✓ Created .gitignore file")
    else:
        print("✓ .gitignore file already exists")

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("✗ Python 3.8 or higher is required")
        print(f"  Current version: {sys.version}")
        return False
    else:
        print(f"✓ Python version: {sys.version}")
        return True

def create_virtual_environment():
    """Create virtual environment if it doesn't exist"""
    import subprocess
    
    if not os.path.exists('venv'):
        print("Creating virtual environment...")
        try:
            result = subprocess.run([sys.executable, '-m', 'venv', 'venv'], 
                                   capture_output=True, text=True)
            if result.returncode == 0:
                print("✓ Virtual environment created successfully")
                return True
            else:
                print(f"✗ Failed to create virtual environment: {result.stderr}")
                return False
        except Exception as e:
            print(f"✗ Error creating virtual environment: {e}")
            return False
    else:
        print("✓ Virtual environment already exists")
        return True

def install_dependencies():
    """Install dependencies from requirements.txt using venv"""
    import subprocess
    
    # Path to venv pip
    venv_pip = os.path.join('venv', 'Scripts', 'pip.exe') if os.name == 'nt' else os.path.join('venv', 'bin', 'pip')
    
    # Check if venv pip exists
    if not os.path.exists(venv_pip):
        print("✗ Virtual environment pip not found. Please create venv first.")
        return False
    
    try:
        print("Installing dependencies with trusted hosts...")
        cmd = [
            venv_pip, 'install',
            '--trusted-host=pypi.python.org',
            '--trusted-host=pypi.org', 
            '--trusted-host=files.pythonhosted.org',
            '-r', 'requirements.txt'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ Dependencies installed successfully in virtual environment")
            return True
        else:
            print(f"✗ Failed to install dependencies: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ Error installing dependencies: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up Behave BDD Automation Framework...")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Create .env file
    create_env_file()
    
    # Create .gitignore
    create_gitignore()
    
    # Create virtual environment
    if not create_virtual_environment():
        print("✗ Setup failed - could not create virtual environment")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("✗ Setup failed - could not install dependencies")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("✅ Setup completed successfully!")
    print("\nNext steps:")
    print("1. Activate virtual environment:")
    print("   Windows: venv\\Scripts\\activate")
    print("   Linux/Mac: source venv/bin/activate")
    print("2. Update .env file with your configuration")
    print("3. Run tests with: behave")
    print("4. Run specific tests with: behave features/web/ or behave features/api/")
    print("\nFor more information, check the README.md file")

if __name__ == "__main__":
    main() 