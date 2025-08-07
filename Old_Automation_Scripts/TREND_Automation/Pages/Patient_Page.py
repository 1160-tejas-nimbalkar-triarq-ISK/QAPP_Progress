# Pages/Patient_Page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Input_Data.Patient_Details import Patient_data
from Locators.Qpathways_Locators import Patients_Locators
from selenium.webdriver.common.keys import Keys
import random
locators = Patients_Locators


class PatientPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_patients_tab(self):
        patients_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Patient_Tab)))
        patients_tab.click()

    def click_patient_registration_icon(self):
        registration_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Patient_Reg_Icon)))
        registration_icon.click()

    def open_new_patient_form(self):
        new_patient_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.New_Patient_Button)))
        new_patient_button.click()


    def enter_first_name(self):
        first_name_field = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.FIRST_NAME_BOX)))
        first_name_field.send_keys(Patient_data.first_name)

    def enter_middle_name(self):
        middle_name_field = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.MIDDLE_NAME_BOX)))
        middle_name_field.send_keys(Patient_data.middle_name)

    def enter_last_name(self):
        last_name_field = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.LAST_NAME_BOX)))
        last_name_field.send_keys(Patient_data.last_name)

    def enter_dob(self):
        dob_field = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.BIRTHDATE_FIELD)))
        dob_field.click()
        
        dob_field.send_keys(Patient_data.dob)

    def enter_gender(self):
        gender_field = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.GENDER_BOX)))
        gender_field.send_keys(Patient_data.gender)

    def select_value_program(self):
        value_program_field = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Value_Program_BOX)))
        value_program_field.send_keys(Patient_data.Value_Program)
        value_program_field.send_keys(Keys.RETURN)

    def select_pcp_group(self):
        pcp_group_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.PCP_Group)))
        pcp_group_dropdown.send_keys("CANADA COLLEGE HEALTH CENTER")  
        pcp_group_dropdown.send_keys(Keys.RETURN)  

    def select_pcp_provider(self):
        pcp_provider_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.PCP_Provider))) # Use correct locator for PCP Provider
        pcp_provider_dropdown.click()
        pcp_provider_options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'k-item')]")))
        random_pcp_provider = random.choice(pcp_provider_options)
        random_pcp_provider.click()

    def select_pgp_group(self):
        pgp_group_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.PGP_Group)))
        pgp_group_dropdown.send_keys("Awesome Thought PGP")  
        pgp_group_dropdown.send_keys(Keys.RETURN)  
        
    def select_provider(self): # This is assumed to be the PGP Provider selection
        provider_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Provider))) 
        provider_dropdown.click()
        provider_options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'k-item')]")))
        random_provider = random.choice(provider_options)
        random_provider.click()

    def enter_email(self):
        email_field = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.EMAIL_BOX)))
        email_field.send_keys(Patient_data.email)