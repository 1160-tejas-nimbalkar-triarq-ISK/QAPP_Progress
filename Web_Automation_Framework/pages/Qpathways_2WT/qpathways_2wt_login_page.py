from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

class Qpathways2WTLoginPage:
    """Page Object Model for Qpathways 2WT Login Page"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        
    # Locators
    USERNAME_FIELD = (By.XPATH, "//input[@name='username']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//ion-button[contains(.,'Login')]")
    
    def launch_login_page(self, url):
        """Launch the Qpathways 2WT login page"""
        print(f"Launching Qpathways 2WT login page: {url}")
        self.driver.get(url)
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        time.sleep(2)
        print("Login page loaded successfully")
        
    def enter_username(self, username):
        """Enter username in the username field"""
        print(f"Entering username: {username}")
        username_field = self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD))
        username_field.send_keys(username)
        print("Username entered successfully")
            
    def enter_password(self, password):
        """Enter password in the password field"""
        print("Entering password")
        password_field = self.wait.until(EC.presence_of_element_located(self.PASSWORD_FIELD))
        password_field.send_keys(password)
        print("Password entered successfully")
            
    def click_login_button(self):
        """Click the login button"""
        print("Clicking login button")
        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()
        time.sleep(40)  # Wait for login as per user's script
        print("Login button clicked successfully")
        
    def _find_element(self, locators):
        """Find element using multiple locator strategies"""
        for locator in locators:
            try:
                element = self.wait.until(EC.presence_of_element_located(locator))
                if element.is_displayed() and element.is_enabled():
                    return element
            except TimeoutException:
                continue
        
        # Try without wait as fallback
        for locator in locators:
            try:
                return self.driver.find_element(*locator)
            except NoSuchElementException:
                continue
        return None 