import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Input_Excel.Patient_Details_Faker import Activities_Data
from Locators import Qprime_Locators

locators = Qprime_Locators.Activities_Locators


class ActivitiesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_on_activities_plus_button(self):
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "k-i-loading")))
        activities_plus_button_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, locators.Activities_Plus_Button)))
        activities_plus_button_element.click()

    def click_on_call_activity_option(self):
        call_activity_option_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, locators.Call_Activity_Option)))
        call_activity_option_element.click()

    def add_CallActivity(self):
        dropdown_arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Category_Dropdown_Arrow)))
        ActionChains(self.driver).move_to_element(dropdown_arrow).click(dropdown_arrow).perform()
        time.sleep(1)
        options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@role='option']")))
        total_options = len(options)
        print(f"Total options available: {total_options}")
        random_index = 1
        random_option = options[random_index - 1]
        time.sleep(1)
        random_option.click()

        subject_textbox = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, locators.Subject_Textbox)))
        subject_textbox.click()
        subject_textbox.send_keys(Activities_Data.Activity_Subject)
        subject_textbox.send_keys(Keys.RETURN)

        assigned_to_user_textbox = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, locators.Assigned_To_Dropdown)))
        assigned_to_user_textbox.click()
        assigned_to_user_textbox.send_keys(Activities_Data.Assigned_To_User)
        assigned_to_user_textbox.send_keys(Keys.RETURN)
        time.sleep(2)
        save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Save_Button)))
        save_button.click()

    def click_on_form_activity_option(self):
        self.click_on_activities_plus_button()
        time.sleep(2)
        call_activity_option_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, locators.Form_Option)))
        call_activity_option_element.click()
        time.sleep(1)

    def add_Form_Activity(self):
        Form_Box = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Form_Box)))
        Form_Box.click()
        Form_Box.send_keys(Activities_Data.Form)
        Form_Box.send_keys(Keys.RETURN)
        time.sleep(2)
        Form_subject_textbox = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, locators.Form_Subject_Box)))
        Form_subject_textbox.click()
        Form_subject_textbox.send_keys(Activities_Data.Form_Subject)
        Form_subject_textbox.send_keys(Keys.RETURN)

        save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Save_Button_Form)))
        save_button.click()
        time.sleep(2)

    def find_and_click_activity(self):
        Subject = Activities_Data.Activity_Subject
        xpath_expression = "//ion-card-content[.//ion-text[contains(@class, 'body2-txt') and contains(text(), '{0}')]]".format(
            Subject)
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_expression)))
        element.click()
        assert element.is_displayed(), f"Activity '{Subject}' is not found"
