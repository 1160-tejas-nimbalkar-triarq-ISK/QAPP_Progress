import random
import time
import re
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Input_Excel.Patient_Details_Faker import Utilization_Data
from Locators import Qprime_Locators

locators = Qprime_Locators.Utilization_Locators


class UtilizationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_On_Utilization_Plus_Button(self):
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "k-i-loading")))
        Utilization_plus_button_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, locators.Plus_Button_Utilization)))
        self.driver.execute_script("arguments[0].scrollIntoView();", Utilization_plus_button_element)
        Utilization_plus_button_element.click()

    def open_Add_Utilization_Screen_for_Inpatient(self):
        Inpatient_Utilization = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Inpatient_Utilization)))
        Inpatient_Utilization.click()

    def Add_Inpatient_Utilization(self):
        dropdown_arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Facility_Dropdown_Arrow)))
        ActionChains(self.driver).move_to_element(dropdown_arrow).click(dropdown_arrow).perform()
        options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@role='option']")))
        total_options = len(options)
        print(f"Total options available: {total_options}")
        random_index = random.randint(0, total_options - 1)
        random_option = options[random_index]
        random_option.click()

        dropdown_arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Provider_Dropdown_Arrow)))
        ActionChains(self.driver).move_to_element(dropdown_arrow).click(dropdown_arrow).perform()
        options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@role='option']")))
        total_options = len(options)
        print(f"Total options available: {total_options}")
        random_index = random.randint(0, total_options - 1)
        random_option = options[random_index]
        random_option.click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Estimated_Amount))).send_keys("10")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Save_Button))).click()

    def Add_Outpatient_Utilization(self):
        Outpatient_Utilization = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, locators.Outpatient_Utilization)))
        Outpatient_Utilization.click()
        dropdown_arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Facility_Dropdown_Arrow)))
        ActionChains(self.driver).move_to_element(dropdown_arrow).click(dropdown_arrow).perform()
        options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@role='option']")))
        total_options = len(options)
        print(f"Total options available: {total_options}")
        random_index = random.randint(0, total_options - 1)
        random_option = options[random_index]
        random_option.click()

        dropdown_arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Provider_Dropdown_Arrow)))
        ActionChains(self.driver).move_to_element(dropdown_arrow).click(dropdown_arrow).perform()
        options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@role='option']")))
        total_options = len(options)
        print(f"Total options available: {total_options}")
        random_index = random.randint(0, total_options - 1)
        random_option = options[random_index]
        random_option.click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Estimated_Amount_Outpatient))).send_keys("10")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Save_Button))).click()

    def Add_SNF_Utilization(self):
        SNF_Utilization = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.SNF_Utilization)))
        SNF_Utilization.click()
        dropdown_arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Facility_Dropdown_Arrow)))
        ActionChains(self.driver).move_to_element(dropdown_arrow).click(dropdown_arrow).perform()
        options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@role='option']")))
        total_options = len(options)
        print(f"Total options available: {total_options}")
        random_index = random.randint(0, total_options - 1)
        random_option = options[random_index]
        random_option.click()

        dropdown_arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Provider_Dropdown_Arrow)))
        ActionChains(self.driver).move_to_element(dropdown_arrow).click(dropdown_arrow).perform()
        options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@role='option']")))
        total_options = len(options)
        print(f"Total options available: {total_options}")
        random_index = random.randint(0, total_options - 1)
        random_option = options[random_index]
        random_option.click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Estimated_Amount_SNF))).send_keys("10")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Save_Button))).click()

    def Add_Home_Health_Utilization(self):
        Home_Health_Utilization = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, locators.Home_Health_Utilization)))
        Home_Health_Utilization.click()
        Facility_Dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Facility_Dropdown)))
        Facility_Dropdown.click()
        Facility_Dropdown.send_keys(Utilization_Data.Utilization_Facility)
        Facility_Dropdown.send_keys(Keys.RETURN)

        Provider_Dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Provider_Dropdown)))
        Provider_Dropdown.click()
        Provider_Dropdown.send_keys(Utilization_Data.Provider_name)
        Provider_Dropdown.send_keys(Keys.RETURN)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Estimated_Amount_HHA))).send_keys("10")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Save_Button))).click()
