# Pages/Login_Page.py
from Locators.Qpathways_Locators import Login_Locators  # Ensure correct import
from Config import Contents # Import your configuration


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = Login_Locators.User_Name_Field # Initialize locators
        self.password_field = Login_Locators.Password_Field
        self.login_button = Login_Locators.Login_Button

    def Login_Qpathways(self):
        self.driver.find_element("xpath", self.username_field).send_keys(Contents.USERNAME)
        self.driver.find_element("xpath", self.password_field).send_keys(Contents.PASSWORD)
        self.driver.find_element("xpath", self.login_button).click()