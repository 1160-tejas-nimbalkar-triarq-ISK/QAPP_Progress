# Pages/Login_Page.py
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Qprime_Locators
from Config import Contents

locators = Qprime_Locators.Login_Locators
username = Contents.USERNAME
password = Contents.PASSWORD


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Login_Qpathways(self):
        username_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
        username_field.clear()
        username_field.send_keys(username)
        password_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//ion-button[contains(.,'Login')]")))
        login_button.click()
        time.sleep(15)
