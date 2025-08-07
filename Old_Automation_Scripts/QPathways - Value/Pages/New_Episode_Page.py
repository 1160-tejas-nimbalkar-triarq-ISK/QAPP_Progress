import random
import time
import pytest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Qprime_Locators
from Input_Excel.Patient_Details_Faker import Patient_data

locators = Qprime_Locators.Episodes_Locators


class EpisodePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enter_Episode_Description(self):
        Description_Box = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Description_Box)))
        Description_Box.send_keys(Patient_data.Episode_Description)

    def select_PGP_dropdown(self):
        PGP_Box = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.PGP_Box)))
        PGP_Box.click()
        PGP_Box.send_keys(Patient_data.PGP)
        print("Attribute value:", PGP_Box.get_attribute("value"))

    def select_Physician(self):
        Physician_Dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Physician_Box)))
        assert Physician_Dropdown.is_displayed(), "Physician dropdown is not displayed"

    def select_Program(self):
        Program_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Program_Dropdown)))
        Program_dropdown.click()
        Program_dropdown.send_keys(Patient_data.random_program)
        Program_dropdown.send_keys(Keys.ENTER)

    def select_Facility(self):
        Facility_Arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Facility_Dropdown_Arrow)))
        Facility_Arrow.click()
        time.sleep(1)
        options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@role='option']")))
        total_options = len(options)
        print(f"Total options available: {total_options}")
        random_index = 1
        random_option = options[random_index - 1]
        random_option.click()

    def select_surgery_Date(self):
        Surgery_Date = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Surgery_Date)))
        Surgery_Date.click()
        time.sleep(1)
        Surgery_Date.send_keys(Patient_data.todays_date)
        Surgery_Date.send_keys(Keys.ENTER)

    def select_type(self):
        Type = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Type)))
        Type.send_keys("Inpatient" if random.choice(["Inpatient", "Outpatient"]) == "Inpatient" else "Outpatient")
        Type.send_keys(Keys.ENTER)

    def select_Surgery_For_Box(self):
        Buttons = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locators.Surgery_Type)))
        random_button = random.choice(Buttons)
        random_button.click()

    def click_on_Save_button(self):
        Save_Button = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Save_Button)))
        Save_Button.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Patient_Tab))).click()
        time.sleep(3)

    def select_risk(self):
        Risk_Button = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Risk_Button)))
        Risk_Button.click()
        time.sleep(3)
        Risk_Option = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Medium_Risk)))
        Risk_Option.click()
        time.sleep(2)

    def enter_target_Price(self):
        Target_Price_Field = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Target_Price)))
        Target_Price_Field.click()
        time.sleep(1)
        Target_Price_Box = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Target_Price_Box)))
        Target_Price_Box.send_keys(Patient_data.target_price)
        time.sleep(1)

    def enter_Episode_Note(self):
        Episode_Note_Button = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Episode_Notes)))
        Episode_Note_Button.click()
        time.sleep(2)
        Episode_Note_Box = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Episode_Note_Box)))
        Episode_Note_Box.clear()
        time.sleep(2)
        Episode_Note_Box.send_keys("This is Bundle Payment Episode")
        Add_Note_Tick = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Add_Note_Tick)))
        Add_Note_Tick.click()

    def select_care_Plan(self):
        Care_Plan_Field = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Care_Plan_Field)))
        Care_Plan_Field.click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Select_Index1_CarePlan))).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Next_Button))).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Save_Button_2))).click()
        time.sleep(5)

    def Click_On_Initiate_Button(self):
        Initiate_Button = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Initiate_Buttton)))
        Initiate_Button.click()
        time.sleep(5)
