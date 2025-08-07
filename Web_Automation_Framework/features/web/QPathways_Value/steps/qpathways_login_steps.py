from behave import given, when, then
from pages.QPathways_Value.qpathways_login_page import QpathwaysLoginPage
from selenium.webdriver.support.ui import WebDriverWait
from utils.config import Config
import time

def replace_config_placeholders(value):
    """Replace configuration placeholders with actual values from config.py"""
    config = Config()
    qpathways_config = config.get_qpathways_credentials()
    
    # Replace placeholders with actual values
    if value == "<QPATHWAYS_BASE_URL>":
        return qpathways_config['url']
    elif value == "<QPATHWAYS_USERNAME>":
        return qpathways_config['username']
    elif value == "<QPATHWAYS_PASSWORD>":
        return qpathways_config['password']
    elif value == "<QPATHWAYS_DASHBOARD_URL>":
        return qpathways_config['dashboard_url']
    else:
        return value

@given('I launch the Qpathways Value login page "{url}"')
def step_launch_qpathways_login_page(context, url):
    """Launch the Qpathways Value login page"""
    # Replace config placeholders
    actual_url = replace_config_placeholders(url)
    
    if not hasattr(context, 'driver'):
        from features.environment import setup_chrome_driver
        context.driver = setup_chrome_driver()
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)
    
    context.qpathways_login_page = QpathwaysLoginPage(context.driver)
    context.qpathways_login_page.launch_login_page(actual_url)
    
    # Wait for page to load
    WebDriverWait(context.driver, 15).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )
    time.sleep(2)

@when('I enter the username "{username}"')
def step_enter_username(context, username):
    """Enter username in the username field"""
    # Replace config placeholders
    actual_username = replace_config_placeholders(username)
    context.qpathways_login_page.enter_username(actual_username)

@when('I enter the password "{password}"')
def step_enter_password(context, password):
    """Enter password in the password field"""
    # Replace config placeholders
    actual_password = replace_config_placeholders(password)
    context.qpathways_login_page.enter_password(actual_password)
    time.sleep(1)  # Brief wait after entering password

@when('I click the login button')
def step_click_login_button(context):
    """Click the login button"""
    context.qpathways_login_page.click_login_button()
    print("Login process completed.")

@then('I should be successfully logged in')
def step_verify_successful_login(context):
    """Verify successful login by checking URL or dashboard elements"""
    import time
    time.sleep(3)  # Wait for page to load after login
    
    current_url = context.driver.current_url
    print(f"Current URL after login: {current_url}")
    
    # Check if we're no longer on login page
    assert 'login' not in current_url.lower(), f"Still on login page: {current_url}"
    print("✓ Successfully logged in and redirected from login page")

 