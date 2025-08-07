"""
Setup script for Desktop BDD Automation Framework
"""

import os
import sys
import subprocess
import platform

def main():
    """Main setup function"""
    print("🚀 Desktop BDD Automation Framework Setup")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required. Current version:", sys.version)
        sys.exit(1)
    
    # Check if Windows
    if platform.system() != "Windows":
        print("❌ This framework is designed for Windows desktop automation")
        sys.exit(1)
    
    print("✅ Python version check passed")
    print("✅ Windows OS detected")
    
    # Create virtual environment
    print("\n📦 Setting up virtual environment...")
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Virtual environment created successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create virtual environment: {e}")
        sys.exit(1)
    
    # Install dependencies
    print("\n📥 Installing dependencies...")
    try:
        if platform.system() == "Windows":
            pip_path = os.path.join("venv", "Scripts", "pip.exe")
        else:
            pip_path = os.path.join("venv", "bin", "pip")
        
        subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        sys.exit(1)
    
    # Create logs directory
    if not os.path.exists("logs"):
        os.makedirs("logs")
        print("✅ Logs directory created")
    
    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Activate virtual environment:")
    print("   .\\venv\\Scripts\\Activate.ps1")
    print("2. Run tests:")
    print("   behave")
    print("3. Run specific scenarios:")
    print("   behave --tags=@smoke")

if __name__ == "__main__":
    main() 