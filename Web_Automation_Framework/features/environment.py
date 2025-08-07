import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.config import Config
from utils.report_generator import report_generator

# Prevent Python from generating cache files
import os
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

def take_screenshot(context, scenario, status="failure"):
    """Take screenshot and save it with timestamp and scenario name"""
    try:
        if hasattr(context, 'driver') and context.driver:
            # Create screenshots directory if it doesn't exist
            screenshots_dir = "screenshots"
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)
            
            # Generate filename with timestamp and scenario name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            scenario_name = scenario.name.replace(" ", "_").replace("/", "_").replace("\\", "_")
            filename = f"{screenshots_dir}/{timestamp}_{status}_{scenario_name}.png"
            
            # Take screenshot
            context.driver.save_screenshot(filename)
            print(f"📸 Screenshot saved: {filename}")
            
            # Add screenshot to report
            report_generator.add_screenshot(filename, scenario.name, status)
            
            return filename
    except Exception as e:
        print(f"❌ Failed to take screenshot: {e}")

def before_all(context):
    """Setup executed before all scenarios"""
    context.config = Config()
    context.driver = None  # Initialize driver as None
    
    # Start test run tracking
    report_generator.start_test_run()
    print("🚀 Starting test execution...")

def before_feature(context, feature):
    """Setup executed before each feature"""
    print(f"📋 Feature: {feature.name}")
    print(f"DEBUG: Feature filename: {feature.filename}")
    print(f"DEBUG: Checking if 'web' in filename: {'web' in feature.filename}")
    print(f"DEBUG: Checking if 'QPathways_Value' in filename: {'QPathways_Value' in feature.filename}")
    
    if 'web' in feature.filename or 'QPathways_Value' in feature.filename or 'QPathways_TREND' in feature.filename:
        # Only create driver if it doesn't exist (single session across features)
        if not hasattr(context, 'driver') or context.driver is None:
            print("DEBUG: Initializing web driver...")
            context.driver = setup_chrome_driver()
            context.driver.maximize_window()
            context.driver.implicitly_wait(10)
            print("DEBUG: Web driver initialized successfully")
        else:
            print("DEBUG: Reusing existing web driver session")
    else:
        print("DEBUG: No web driver initialization - not a web feature")
    
def after_feature(context, feature):
    """Cleanup executed after each feature"""
    # Add feature results to report
    report_generator.add_feature_result(feature)
    
    # Don't close driver after each feature - keep session alive
    print(f"✅ Feature completed: {feature.name}")

def after_all(context):
    """Cleanup executed after all scenarios"""
    if hasattr(context, 'driver') and context.driver:
        print("DEBUG: Closing browser session after all features")
        context.driver.quit()
    
    # Generate comprehensive reports
    report_generator.end_test_run()

def before_scenario(context, scenario):
    """Setup executed before each scenario"""
    print(f"  🔄 Scenario: {scenario.name}")
    # Record start time for duration calculation
    scenario.start_time = datetime.now()

def after_scenario(context, scenario):
    """Cleanup executed after each scenario"""
    # Calculate duration
    if hasattr(scenario, 'start_time'):
        scenario.duration = datetime.now() - scenario.start_time
    
    # Track scenario results and take screenshots on failure
    if scenario.status == "failed":
        print(f"    ❌ FAILED: {scenario.name}")
        # Take screenshot on failure
        screenshot_path = take_screenshot(context, scenario, "FAILED")
        
        # Add error to report
        if hasattr(scenario, 'error_message'):
            report_generator.add_error(scenario.error_message, scenario.name)
        else:
            report_generator.add_error("Scenario failed", scenario.name)
            
    elif scenario.status == "passed":
        print(f"    ✅ PASSED: {scenario.name}")
    elif scenario.status == "skipped":
        print(f"    ⏭️  SKIPPED: {scenario.name}")

def after_step(context, step):
    """Executed after each step"""
    if step.status == "failed":
        print(f"      ❌ Step failed: {step.name}")
        # Take screenshot on step failure
        screenshot_path = take_screenshot(context, step.scenario, "STEP_FAILED")
        
        # Add error to report
        error_message = getattr(step, 'error_message', 'Step failed')
        report_generator.add_error(error_message, step.scenario.name, step.name)

def setup_chrome_driver():
    """Setup Chrome driver with appropriate options"""
    chrome_options = Options()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.add_argument('--disable-notifications')
    
    # Uncomment the following line to run in headless mode
    # chrome_options.add_argument('--headless')
    
    try:
        # Try to install ChromeDriver with explicit version handling
        print("Installing ChromeDriver...")
        driver_path = ChromeDriverManager().install()
        print(f"ChromeDriver path: {driver_path}")
        
        # Fix path issue - ensure we have the actual chromedriver.exe
        import os
        if os.path.isdir(driver_path):
            # If path is a directory, find the chromedriver.exe inside
            for file in os.listdir(driver_path):
                if file.lower().startswith('chromedriver') and file.lower().endswith('.exe'):
                    driver_path = os.path.join(driver_path, file)
                    break
        elif not driver_path.lower().endswith('.exe'):
            # If path doesn't end with .exe, look for chromedriver.exe in the same directory
            dir_path = os.path.dirname(driver_path)
            for file in os.listdir(dir_path):
                if file.lower().startswith('chromedriver') and file.lower().endswith('.exe'):
                    driver_path = os.path.join(dir_path, file)
                    break
        
        print(f"Final ChromeDriver path: {driver_path}")
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Remove webdriver property to avoid detection
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        return driver
    except Exception as e:
        print(f"Error setting up Chrome driver: {e}")
        print("Trying alternative approach...")
        
        # Alternative approach: try system Chrome
        try:
            service = Service()  # Let selenium find the driver
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            return driver
        except Exception as e2:
            print(f"Alternative approach also failed: {e2}")
            raise Exception(f"Could not initialize Chrome driver. Error 1: {e}, Error 2: {e2}") 