from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PatientRegistrationPage:
    """Page Object Model for Patient Registration in Qpathways Clinical"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        
    # Locators based on user's script
    PATIENTS_TAB = (By.XPATH, "//ion-tab-button[contains(.,'Patients')]")
    PATIENT_REGISTRATION_ICON = (By.XPATH, "//ion-button[contains(@slot,'only-icon')]")
    NEW_PATIENT_BUTTON = (By.XPATH, "//ion-text[@color='gray80'][contains(.,'New Patient')]")
    
    # Patient form fields
    FIRST_NAME_FIELD = (By.XPATH, "//input[@placeholder='*First Name']")
    MIDDLE_NAME_FIELD = (By.XPATH, "//input[@placeholder='Middle Name']")
    LAST_NAME_FIELD = (By.XPATH, "//input[contains(@placeholder,'*Last Name')]")
    DOB_FIELD = (By.XPATH, "//input[@id='datepicker-3']")
    GENDER_FIELD = (By.XPATH, "//input[@placeholder='*Gender']")
    ADDRESS_FIELD = (By.XPATH, "//input[contains(@placeholder,'Address 1')]")
    ZIP_FIELD = (By.XPATH, "//input[@placeholder='*Zip']")
    MOBILE_FIELD = (By.XPATH, "(//input[contains(@type,'text')])[1]")
    EMAIL_FIELD = (By.XPATH, "//input[contains(@placeholder,'Email')]")
    VALUE_PROGRAM_FIELD = (By.XPATH, "//input[@placeholder='*Value Program']")
    
    def click_patients_tab(self):
        """Click on Patients tab"""
        patients_tab = self.wait.until(EC.element_to_be_clickable(self.PATIENTS_TAB))
        patients_tab.click()
        
    def click_patient_registration_icon(self):
        """Click on patient registration icon"""
        registration_icon = self.wait.until(EC.element_to_be_clickable(self.PATIENT_REGISTRATION_ICON))
        registration_icon.click()
        
    def click_new_patient_button(self):
        """Click on New Patient button"""
        new_patient_button = self.wait.until(EC.element_to_be_clickable(self.NEW_PATIENT_BUTTON))
        new_patient_button.click()
        
    def enter_first_name(self, first_name):
        """Enter first name"""
        first_name_field = self.wait.until(EC.presence_of_element_located(self.FIRST_NAME_FIELD))
        first_name_field.send_keys(first_name)
        
    def enter_middle_name(self, middle_name):
        """Enter middle name"""
        middle_name_field = self.wait.until(EC.presence_of_element_located(self.MIDDLE_NAME_FIELD))
        middle_name_field.send_keys(middle_name)
        
    def enter_last_name(self, last_name):
        """Enter last name"""
        last_name_field = self.wait.until(EC.presence_of_element_located(self.LAST_NAME_FIELD))
        last_name_field.send_keys(last_name)
        
    def enter_dob(self, dob):
        """Enter date of birth"""
        dob_field = self.wait.until(EC.element_to_be_clickable(self.DOB_FIELD))
        dob_field.click()
        dob_field.send_keys(dob)
        
    def enter_gender(self, gender):
        """Enter gender"""
        gender_field = self.wait.until(EC.presence_of_element_located(self.GENDER_FIELD))
        gender_field.send_keys(gender)
        
    def enter_address(self, address):
        """Enter address"""
        address_field = self.wait.until(EC.presence_of_element_located(self.ADDRESS_FIELD))
        address_field.send_keys(address)
        
    def enter_zip(self, zip_code):
        """Enter ZIP code"""
        zip_field = self.wait.until(EC.presence_of_element_located(self.ZIP_FIELD))
        zip_field.send_keys(zip_code)
        
    def enter_mobile(self, mobile_number):
        """Enter mobile number"""
        mobile_field = self.wait.until(EC.presence_of_element_located(self.MOBILE_FIELD))
        mobile_field.send_keys(mobile_number)
        
    def enter_email(self, email):
        """Enter email"""
        email_field = self.wait.until(EC.presence_of_element_located(self.EMAIL_FIELD))
        email_field.send_keys(email)
        
    def enter_value_program(self, value_program):
        """Enter value program"""
        value_program_field = self.wait.until(EC.presence_of_element_located(self.VALUE_PROGRAM_FIELD))
        value_program_field.send_keys(value_program)
        value_program_field.send_keys(Keys.RETURN) 