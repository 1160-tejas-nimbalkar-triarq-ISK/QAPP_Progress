from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from test_data.patient_data_generator import Patient_data
import time
import random

class PatientRegistrationPage:
    """Page Object Model for Patient Registration in QPathways TREND"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Locators - Updated with correct XPaths
    PATIENTS_TAB = "//ion-tab-button[contains(.,'Patients')]"
    PLUS_BUTTON = "//ion-button[contains(@shape,'round')]"
    NEW_PATIENT_BUTTON = "//ion-text[@color='gray80'][contains(.,'New Patient')]"
    
    # Basic Information Fields
    FIRST_NAME_FIELD = "//input[@placeholder='*First Name']"
    MIDDLE_NAME_FIELD = "//input[@placeholder='Middle Name']"
    LAST_NAME_FIELD = "//input[@placeholder='*Last Name']"
    DOB_FIELD = "//input[@placeholder='*mm/dd/yyyy']"
    GENDER_FIELD = "//input[@placeholder='*Gender']"
    VALUE_PROGRAM_FIELD = "//input[@placeholder='*Value Program']"
    
    # Dropdown Arrows
    PRIMARY_CARE_PROVIDER_ARROW = "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[11]"
    PGP_ARROW = "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[12]"
    PROVIDER_ARROW = "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[13]"
    PRIMARY_INSURANCE_ARROW = "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[14]"
    SECONDARY_INSURANCE_ARROW = "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[15]"
    
    # Insurance Fields
    PRIMARY_INSURANCE_ID = "//input[@placeholder='* Insurance ID']"
    PRIMARY_GROUP_ID = "(//input[@placeholder='Group ID'])[1]"
    SECONDARY_INSURANCE_ID = "//input[@placeholder='ID']"
    SECONDARY_GROUP_ID = "(//input[@placeholder='Group ID'])[2]"
    
    # Address Information
    ADDRESS1 = "//input[@placeholder='*Address 1']"
    ZIP = "//input[@placeholder='*Zip']"
    
    # Contact Information
    MOBILE_NUMBER = "(//input[contains(@type,'text')])[1]"
    PHONE_NUMBER = "(//input[contains(@type,'text')])[2]"
    EMAIL = "//input[@placeholder='Email']"
    NOTES = "//textarea[@placeholder='Notes']"
    
    # Save Button
    ADD_PATIENT_BUTTON = "(//div[contains(.,'CancelAdd Patient')])[10]"
    
    # Helper Locators
    DROPDOWN_OPTIONS = "//li[@role='option']"
    
    def find_contact_fields(self):
        """Debug method to find all input fields on the page"""
        print("=== DEBUG: Finding all input fields ===")
        all_inputs = self.driver.find_elements(By.TAG_NAME, "input")
        for i, input_field in enumerate(all_inputs):
            try:
                placeholder = input_field.get_attribute("placeholder") or "No placeholder"
                input_type = input_field.get_attribute("type") or "No type"
                input_id = input_field.get_attribute("id") or "No id"
                input_name = input_field.get_attribute("name") or "No name"
                print(f"Input {i}: placeholder='{placeholder}', type='{input_type}', id='{input_id}', name='{input_name}'")
            except:
                print(f"Input {i}: Could not get attributes")
        print("=== END DEBUG ===")

    def click_patients_tab(self):
        """Click on Patients tab"""
        time.sleep(3)
        patients_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.PATIENTS_TAB)))
        patients_tab.click()
        time.sleep(2)
        print("Clicked Patients tab successfully")

    def click_patient_registration_icon(self):
        """Click on patient registration icon (+ button)"""
        plus_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.PLUS_BUTTON)))
        plus_button.click()
        time.sleep(2)
        print("Clicked + button successfully")

    def open_new_patient_form(self):
        """Open new patient form"""
        new_patient_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.NEW_PATIENT_BUTTON)))
        new_patient_button.click()
        time.sleep(3)
        print("Opened new patient form successfully")

    def enter_first_name(self):
        """Enter first name"""
        first_name_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.FIRST_NAME_FIELD)))
        first_name_field.clear()
        first_name_field.send_keys(Patient_data.first_name)
        time.sleep(1)
        print(f"Entered first name: {Patient_data.first_name}")

    def enter_middle_name(self):
        """Enter middle name"""
        middle_name_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.MIDDLE_NAME_FIELD)))
        middle_name_field.clear()
        middle_name_field.send_keys(Patient_data.middle_name)
        time.sleep(1)
        print(f"Entered middle name: {Patient_data.middle_name}")

    def enter_last_name(self):
        """Enter last name"""
        last_name_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.LAST_NAME_FIELD)))
        last_name_field.clear()
        last_name_field.send_keys(Patient_data.last_name)
        time.sleep(1)
        print(f"Entered last name: {Patient_data.last_name}")

    def enter_dob(self):
        """Enter date of birth"""
        dob_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.DOB_FIELD)))
        dob_field.click()
        time.sleep(2)
        dob_field.send_keys(Patient_data.dob)
        time.sleep(1)
        print(f"Entered date of birth: {Patient_data.dob}")

    def enter_gender(self):
        """Enter gender"""
        gender_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.GENDER_FIELD)))
        gender_field.click()
        time.sleep(1)
        gender_field.send_keys(Patient_data.gender)
        time.sleep(1)
        print(f"Entered gender: {Patient_data.gender}")

    def select_trend_program(self):
        """Select trend program"""
        value_program_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.VALUE_PROGRAM_FIELD)))
        value_program_field.clear()
        value_program_field.send_keys(Patient_data.Value_Program)
        value_program_field.send_keys(Keys.RETURN)
        time.sleep(1)
        print(f"Selected trend program: {Patient_data.Value_Program}")

    def select_primary_care_provider(self):
        """Select primary care provider from dropdown"""
        # Scroll to the element first
        arrow = self.wait.until(EC.presence_of_element_located((By.XPATH, self.PRIMARY_CARE_PROVIDER_ARROW)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", arrow)
        time.sleep(1)
        
        # Click the arrow
        arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.PRIMARY_CARE_PROVIDER_ARROW)))
        arrow.click()
        time.sleep(3)
        
        # Wait for dropdown options to appear and select first option
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.DROPDOWN_OPTIONS)))
        options = self.driver.find_elements(By.XPATH, self.DROPDOWN_OPTIONS)
        options[0].click()
        time.sleep(2)
        print("Selected primary care provider from dropdown successfully")

    def select_pgp(self):
        """Select PGP from dropdown"""
        # Scroll to the element first
        arrow = self.wait.until(EC.presence_of_element_located((By.XPATH, self.PGP_ARROW)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", arrow)
        time.sleep(1)
        
        # Click the arrow
        arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.PGP_ARROW)))
        arrow.click()
        time.sleep(3)
        
        # Wait for dropdown options to appear and select first option
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.DROPDOWN_OPTIONS)))
        options = self.driver.find_elements(By.XPATH, self.DROPDOWN_OPTIONS)
        options[0].click()
        time.sleep(2)
        print("Selected PGP from dropdown successfully")

    def select_provider(self):
        """Select provider from dropdown"""
        # Scroll to the element first
        arrow = self.wait.until(EC.presence_of_element_located((By.XPATH, self.PROVIDER_ARROW)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", arrow)
        time.sleep(1)
        
        # Click the arrow
        arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.PROVIDER_ARROW)))
        arrow.click()
        time.sleep(3)
        
        # Wait for dropdown options to appear and select first option
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.DROPDOWN_OPTIONS)))
        options = self.driver.find_elements(By.XPATH, self.DROPDOWN_OPTIONS)
        options[0].click()
        time.sleep(2)
        print("Selected provider from dropdown successfully")

    def select_primary_insurance(self):
        """Select primary insurance from dropdown"""
        arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.PRIMARY_INSURANCE_ARROW)))
        arrow.click()
        time.sleep(2)
        
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.DROPDOWN_OPTIONS)))
        options = self.driver.find_elements(By.XPATH, self.DROPDOWN_OPTIONS)
        
        if len(options) > 0:
            options[0].click()
            time.sleep(1)
            print("Selected primary insurance from dropdown successfully")

    def enter_insurance_id1(self):
        """Enter primary insurance ID"""
        insurance_id_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.PRIMARY_INSURANCE_ID)))
        insurance_id_field.clear()
        insurance_id_field.send_keys(Patient_data.Insurance_Id1)
        time.sleep(1)
        print(f"Entered primary insurance ID: {Patient_data.Insurance_Id1}")

    def enter_group_id1(self):
        """Enter primary group ID"""
        group_id_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.PRIMARY_GROUP_ID)))
        group_id_field.clear()
        group_id_field.send_keys(Patient_data.Group_Id1)
        time.sleep(1)
        print(f"Entered primary group ID: {Patient_data.Group_Id1}")

    def select_secondary_insurance(self):
        """Select secondary insurance from dropdown"""
        arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.SECONDARY_INSURANCE_ARROW)))
        arrow.click()
        time.sleep(2)
        
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.DROPDOWN_OPTIONS)))
        options = self.driver.find_elements(By.XPATH, self.DROPDOWN_OPTIONS)
        
        if len(options) > 0:
            options[0].click()
            time.sleep(1)
            print("Selected secondary insurance from dropdown successfully")

    def enter_insurance_id2(self):
        """Enter secondary insurance ID"""
        insurance_id_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.SECONDARY_INSURANCE_ID)))
        insurance_id_field.clear()
        insurance_id_field.send_keys(Patient_data.Insurance_Id2)
        time.sleep(1)
        print(f"Entered secondary insurance ID: {Patient_data.Insurance_Id2}")

    def enter_group_id2(self):
        """Enter secondary group ID"""
        group_id_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.SECONDARY_GROUP_ID)))
        group_id_field.clear()
        group_id_field.send_keys(Patient_data.Group_Id2)
        time.sleep(1)
        print(f"Entered secondary group ID: {Patient_data.Group_Id2}")

    def enter_address1(self):
        """Enter address"""
        address_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.ADDRESS1)))
        address_field.clear()
        address_field.send_keys(Patient_data.address)
        time.sleep(1)
        print(f"Entered address: {Patient_data.address}")

    def enter_address_details(self):
        """Enter address details (ZIP and auto-suggestion)"""
        try:
            zip_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.ZIP)))
            zip_field.clear()
            zip_code = str(random.randint(10000, 99999))
            zip_field.send_keys(zip_code)
            time.sleep(3)  # Wait for suggestions to appear
            
            # Click on the first suggestion (index 1)
            suggestion_xpath = "(//li[@role='option'])[1]"
            suggestion = self.wait.until(EC.element_to_be_clickable((By.XPATH, suggestion_xpath)))
            suggestion.click()
            time.sleep(2)
            print(f"Entered ZIP code: {zip_code} and selected first suggestion")
        except Exception as e:
            print(f"Warning: Could not select ZIP suggestion - {str(e)}")
            # Continue without failing the test

    def enter_mobile_number(self):
        """Enter mobile number"""
        field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.MOBILE_NUMBER)))
        field.click()
        time.sleep(1)   
        field.send_keys(Patient_data.Mobile_number)
        time.sleep(1)
        print(f"Entered mobile number: {Patient_data.Mobile_number}")

    def enter_phone_number(self):
        """Enter phone number"""
        field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.PHONE_NUMBER)))
        field.click()
        time.sleep(1)   
        field.send_keys(Patient_data.Home_Number)
        time.sleep(1)
        print(f"Entered phone number: {Patient_data.Home_Number}")

    def enter_email(self):
        """Enter email"""
        email_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.EMAIL)))
        email_field.clear()
        email_field.send_keys(Patient_data.Email)
        time.sleep(1)
        print(f"Entered email: {Patient_data.Email}")

    def enter_notes(self):
        """Enter notes"""
        notes_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.NOTES)))
        
        notes_field.send_keys(Patient_data.Patient_Note)
        time.sleep(1)
        print(f"Entered notes: {Patient_data.Patient_Note}")

    def click_Add_Patient(self):
        """Click Add Patient button"""
        add_patient_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.ADD_PATIENT_BUTTON)))
        add_patient_button.click()
        time.sleep(3)
        print("Clicked Add Patient button successfully") 