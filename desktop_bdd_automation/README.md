# Desktop BDD Automation Framework

A production-ready **Behavior-Driven Development (BDD)** framework for automating **Windows desktop applications** using **Python**, **Behave**, and **pywinauto**.

## 🚀 Features

- **BDD Framework**: Uses Behave for readable test scenarios
- **Desktop Automation**: Automates Windows applications using pywinauto
- **Comprehensive Logging**: Detailed logging with timestamps
- **Robust Error Handling**: Graceful error handling and cleanup
- **Modular Structure**: Well-organized project structure
- **Production Ready**: Ready for CI/CD integration

## 📁 Project Structure

```
desktop_bdd_automation/
│
├── features/
│   ├── steps/
│   │   ├── __init__.py
│   │   └── test_notepad_steps.py     # Step definitions for Notepad tests
│   ├── __init__.py
│   ├── environment.py                # Setup/teardown hooks
│   └── notepad.feature              # Feature file with test scenarios
│
├── tests/
│   └── __init__.py
│
├── logs/                            # Test execution logs
│
├── requirements.txt                 # Python dependencies
├── behave.ini                       # Behave configuration
└── README.md                        # This file
```

## 🛠️ Prerequisites

- **Windows 10/11** (Required for desktop automation)
- **Python 3.8+** installed
- **VS Code** (Recommended)
- **Git** (Optional, for version control)

## 📦 Installation & Setup

### 1. Virtual Environment Setup

```powershell
# Navigate to project directory
cd desktop_bdd_automation

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If execution policy error occurs:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. Install Dependencies

```powershell
# Install required packages
pip install -r requirements.txt

# Verify installation
pip list
```

### 3. VS Code Configuration

1. **Open VS Code** in the project directory:
   ```powershell
   code .
   ```

2. **Select Python Interpreter**:
   - Press `Ctrl+Shift+P`
   - Type "Python: Select Interpreter"
   - Choose the interpreter from `.\venv\Scripts\python.exe`

3. **Install VS Code Extensions** (Recommended):
   - Python
   - Behave VSCode
   - Python Test Explorer

## 🏃‍♂️ Running Tests

### Run All Tests

```powershell
# From project root directory
behave
```

### Run Specific Scenarios

```powershell
# Run tests with specific tags
behave --tags=@smoke

# Run specific feature file
behave features/notepad.feature

# Run with verbose output
behave --verbose

# Run with specific formatter
behave --format=progress
```

### Run Tests with Allure Reports

```powershell
# Generate Allure report
behave --format=allure_behave.formatter:AllureFormatter --outdir=allure-results

# View report (requires Allure CLI)
allure serve allure-results
```

## 🧪 Sample Test Scenarios

The framework includes the following sample scenarios for **Notepad** automation:

### 1. Basic Functionality Test
- Launch Notepad
- Type text
- Verify text appears
- Close without saving

### 2. Text Manipulation Test
- Copy and paste operations
- Text selection
- Keyboard shortcuts (Ctrl+A, Ctrl+C, Ctrl+V)

### 3. File Operations Test
- Save file with specific name
- Verify file saved successfully
- Close application

### 4. Error Handling Test
- Handle unsaved changes dialog
- Test "Don't Save" functionality

## 📊 Logging

Test execution logs are automatically generated in the `logs/` directory with timestamp:
- **Format**: `test_execution_YYYYMMDD_HHMMSS.log`
- **Level**: INFO, WARNING, ERROR
- **Output**: Both file and console

## 🔧 Configuration

### behave.ini
Configuration file for Behave behavior:
- **Format**: Pretty output with colors
- **Logging**: Detailed logging enabled
- **JUnit**: XML reports generated
- **Tags**: Skip tests marked with `@skip`

### environment.py
Setup and teardown hooks:
- **before_all**: Initialize logging, desktop access
- **before_scenario**: Setup scenario-specific variables
- **after_scenario**: Cleanup applications and processes
- **after_all**: Final cleanup

## 🎯 Extending the Framework

### Adding New Application Tests

1. **Create Feature File**:
   ```gherkin
   # features/calculator.feature
   Feature: Calculator Desktop Application
   
   Scenario: Basic calculation
       Given I launch Calculator application
       When I click number "5"
       And I click "+" button
       And I click number "3"
       And I click "=" button
       Then I should see result "8"
   ```

2. **Create Step Definitions**:
   ```python
   # features/steps/calculator_steps.py
   from behave import given, when, then
   
   @given('I launch Calculator application')
   def step_launch_calculator(context):
       context.current_app = launch_application(context, "calc.exe")
   ```

### Adding New Step Definitions

1. Import required modules
2. Use `@given`, `@when`, `@then` decorators
3. Access context variables
4. Use helper functions from `environment.py`

## 🚨 Troubleshooting

### Common Issues

1. **pywinauto not finding application**:
   - Ensure application is installed
   - Check application path in step definitions
   - Verify Windows permissions

2. **Element not found errors**:
   - Increase timeout values
   - Use `inspect.exe` to identify elements
   - Check class names and titles

3. **Virtual environment issues**:
   - Recreate virtual environment
   - Verify Python path in VS Code
   - Check execution policy

### Debug Tips

1. **Enable verbose logging**:
   ```python
   logging.basicConfig(level=logging.DEBUG)
   ```

2. **Use pywinauto inspect tools**:
   ```python
   from pywinauto import Desktop
   Desktop().windows()
   ```

3. **Add debug breakpoints**:
   ```python
   import pdb; pdb.set_trace()
   ```

## 📈 CI/CD Integration

### GitHub Actions Example

```yaml
name: Desktop Automation Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: windows-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run tests
      run: behave --format=junit --outdir=test-results
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🆘 Support

For issues and questions:
- Check the troubleshooting section
- Review logs in `logs/` directory
- Create an issue in the repository

---

**Happy Testing! 🎉** 