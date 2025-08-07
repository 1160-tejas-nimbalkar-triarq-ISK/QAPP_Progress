# Pages/Patient_Page.py
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Input_Excel.Patient_Details_Faker import Patient_data
from Locators import Qprime_Locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
locators = Qprime_Locators.Patients_Locators


class PatientPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_patients_tab(self):
        Patients_Tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Patient_Tab)))
        Patients_Tab.click()

    def click_patient_registration_icon(self):
        Patient_Reg_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Patient_Reg_Icon)))
        Patient_Reg_icon.click()

    def open_new_patient_form(self):
        New_Patient_Button = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.New_Patient_Button)))
        New_Patient_Button.click()

    def select_PGP_dropdown(self):
        PGP_Box = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.PGP_BOX)))
        PGP_Box.click()
        PGP_Box.send_keys(Patient_data.PGP)

    def enter_first_name(self):
        First_Name = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.FIRST_NAME_BOX)))
        First_Name.send_keys(Patient_data.first_name)
        assert isinstance(Patient_data.first_name, str), "First name should be a string."

    def enter_middle_name(self):
        Middle_Name = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.MIDDLE_NAME_BOX)))
        Middle_Name.send_keys(Patient_data.middle_name)
        assert isinstance(Patient_data.middle_name, str), "Middle name should be a string."

    def enter_last_name(self):
        Last_Name = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.LAST_NAME_BOX)))
        Last_Name.send_keys(Patient_data.last_name)
        assert isinstance(Patient_data.last_name, str), "Last name should be a string."

    def enter_dob(self):
        DOB = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.BIRTHDATE_FIELD)))
        DOB.click()
        DOB.send_keys(Patient_data.dob)
        assert re.match(r'^\d{2}-\d{2}-\d{4}$', Patient_data.dob), "Invalid date format. Please use MM-DD-YYYY format."

    def enter_gender(self):
        Gender = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.GENDER_BOX)))
        Gender.send_keys(Patient_data.gender)
        assert Patient_data.gender in ["Male", "Female"], "Invalid gender specified."

    def enter_address(self):
        Address = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.ADDRESS_FIELD)))
        Address.send_keys(Patient_data.address)

    def enter_zip(self):
        Zip = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.ZIP_CODE_BOX)))
        Zip.send_keys(Patient_data.zip_code)
        Zip.submit()  # Press Enter key after entering the ZIP code

    def enter_Mobile_No(self):
        Mobile_No = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.MOBILE_NUMBER_FIELD)))
        Mobile_No.clear()
        Mobile_No.click()
        Mobile_No.send_keys(Patient_data.mobile_number)

    def enter_home_no(self):
        Home_No = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.HOME_NUMBER_FIELD)))
        Home_No.clear()
        Home_No.click()
        Home_No.send_keys(Patient_data.Home_Number)

    def see_office_number_option(self):
        Plus_Button = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Plus_Button_Office)))
        Plus_Button.click()

    def enter_office_number(self):
        Office_No_Option = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Office_No_Option)))
        Office_No_Option.click()
        Office_No = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Office_Number_Box)))
        Office_No.clear()
        Office_No.click()
        Office_No.send_keys(Patient_data.office_number)

    def see_fax_number_option(self):
        Plus_Button = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Plus_Button_Fax)))
        Plus_Button.click()

    def enter_fax_number(self):
        Fax_No_Option = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Fax_Number_Option)))
        Fax_No_Option.click()
        Fax_No = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Fax_No_Box)))
        Fax_No.clear()
        Fax_No.click()
        Fax_No.send_keys(Patient_data.fax_number)

    def enter_email(self):
        Email = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.EMAIL_BOX)))
        Email.send_keys(Patient_data.email)
        assert re.match(r'^[\w\.-]+@[\w\.-]+$', Patient_data.email), "Invalid email format."
        time.sleep(5)

    def select_physician(self):
        dropdown_arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Physician_Dropdown_Arrow)))
        ActionChains(self.driver).move_to_element(dropdown_arrow).click(dropdown_arrow).perform()
        time.sleep(1)
        options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@role='option']")))
        total_options = len(options)
        print(f"Total options available: {total_options}")
        random_index = 1
        random_option = options[random_index - 1]
        random_option.click()

    def select_insurance(self):
        dropdown_arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Insurance_Dropdown_Arrow)))
        ActionChains(self.driver).move_to_element(dropdown_arrow).click(dropdown_arrow).perform()
        time.sleep(1)
        options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@role='option']")))
        total_options = len(options)
        print(f"Total options available: {total_options}")
        random_index = 1
        random_option = options[random_index - 1]
        random_option.click()

    def enter_Insurance_ID(self):
        Insurance_ID = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.INSURANCE_ID_BOX)))
        Insurance_ID.send_keys(Patient_data.insurance_id)
        assert re.match(r'^[A-Za-z0-9]+$', Patient_data.insurance_id), "Insurance ID should be alphanumeric."

    def enter_Group_ID(self):
        Group_ID = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Group_ID_Box)))
        Group_ID.send_keys(Patient_data.Group_id)
        assert re.match(r'^[A-Za-z0-9]+$', Patient_data.Group_id), "Group ID should be alphanumeric."

    def enter_Patient_Note(self):
        Patient_Note = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Note_Box)))
        Patient_Note.send_keys(Patient_data.Patient_Note)

    def check_exclude_Report_ceckbox(self):
        Exclude_patient_Checkbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Exclude_Report_Box)))
        Exclude_patient_Checkbox.click()

    def see_save_button(self):
        Save_and_Close_Button = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Save_Patient_button)))
        assert Save_and_Close_Button.is_enabled()

    def see_save_and_initiate_button(self):
        Save_and_Initiate_Button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, locators.SAVE_INITIATE_EPISODE_BUTTON)))
        assert Save_and_Initiate_Button.is_enabled()

    def open_New_Episode_Screen(self):
        Save_and_Initiate_Button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, locators.SAVE_INITIATE_EPISODE_BUTTON)))
        Save_and_Initiate_Button.click()
