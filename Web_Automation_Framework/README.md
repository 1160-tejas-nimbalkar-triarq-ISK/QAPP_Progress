# Qpathways Test Automation Framework

## 📁 Project Structure

```
Triarq_Automation _Backup/
├── features/
│   ├── web/
│   │   ├── QPathways_Value/
│   │   │   ├── Features/
│   │   │   │   ├── patient_registration.feature
│   │   │   │   └── qpathways_login.feature
│   │   │   └── steps/
│   │   │       ├── patient_registration_steps.py
│   │   │       └── qpathways_login_steps.py
│   │   └── Qpathways_Clinical/
│   │       ├── Features/
│   │       │   ├── patient_registration.feature
│   │       │   └── qpathways_clinical_login.feature
│   │       └── Steps/
│   │           ├── patient_registration_steps.py
│   │           └── qpathways_clinical_login_steps.py
│   ├── api/
│   │   ├── user.feature
│   │   └── steps/
│   │       └── user_steps.py
│   └── environment.py
├── pages/
│   ├── QPathways_Value/
│   │   ├── patient_registration_page.py
│   │   └── qpathways_login_page.py
│   └── QPathaways_Clinical/
│       ├── patient_registration_page.py
│       └── qpathways_clinical_login_page.py
├── utils/
│   ├── config.py
│   └── api_helpers.py
├── test_data/
│   └── patient_data_generator.py
├── reports/               # Test reports directory
├── screenshots/           # Screenshots directory
├── behave.ini            # Behave configuration
├── config.env.template   # Environment variables template
├── requirements.txt      # Python dependencies
├── setup.py             # Setup script
├── run_tests.py         # Test runner script
└── clean_cache.py       # Cache management utility
```

## 🚀 Setup

### Automated Setup (Recommended)
```bash
# Run setup script (creates venv, installs dependencies automatically)
python setup.py

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### Manual Setup (Alternative)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies with trusted hosts
pip install --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org -r requirements.txt
```

## 🏃‍♂️ Commands

### Test Runner Commands

```bash
# Run all tests
python run_tests.py --all

# Run web tests only  
python run_tests.py --web

# Run API tests only
python run_tests.py --api

# Run Qpathways Value tests only
python run_tests.py --qpathways

# Run tests with specific tags
python run_tests.py --tags @smoke

# Run tests with JSON output
python run_tests.py --format json
```

### Direct Behave Commands

```bash
# Run all tests
behave

# Run Qpathways Value tests
behave features/web/QPathways_Value/

# Run specific feature
behave features/web/QPathways_Value/Features/qpathways_login.feature

# Run with tags
behave --tags=@smoke

# Run with JSON output
behave --format=json --outfile=reports/results.json
```

### Cache Management

```bash
# Clean existing cache files and prevent future cache creation
python clean_cache.py
``` 