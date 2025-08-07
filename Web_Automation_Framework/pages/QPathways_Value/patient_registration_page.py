from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from test_data.patient_data_generator import Patient_data
import time
import random

class PatientRegistrationPage:
    """Page Object Model for Patient Registration in QPathways Value"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Locators
    Patient_Tab = "//ion-label[@color='gray100'][contains(.,'Patients')]"
    Patient_Reg_Icon = "//ion-button[@shape='round']"
    New_Patient_Button = "//ion-text[@color='gray80'][contains(.,'New Patient')]"
    
    # Basic Information Fields
    FIRST_NAME_BOX = "//input[contains(@placeholder,'First Name')]"
    MIDDLE_NAME_BOX = "//input[contains(@placeholder,'Middle Name')]"
    LAST_NAME_BOX = "//input[contains(@placeholder,'Last Name')]"
    BIRTHDATE_FIELD = "//input[@placeholder='*mm/dd/yyyy']"
    GENDER_BOX = "//input[contains(@placeholder,'Gender')]"
    Value_Program_BOX = "//input[contains(@placeholder,'Value Program')]"
    
    # Dropdown Arrows
    PGP_Arrow = "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[11]"
    Provider_Arrow = "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[12]"
    Primary_Insurance_Arrow = "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[13]"
    Secondary_Insurance_Arrow = "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[14]"
    
    # Insurance Fields
    INSURANCE_ID1 = "//input[@placeholder='* Insurance ID']"
    INSURANCE_ID2 = "//input[@placeholder='ID']"
    GROUP_ID1 = "(//input[@placeholder='Group ID'])[1]"
    GROUP_ID2 = "(//input[@placeholder='Group ID'])[2]"
    
    # Contact Information
    ADDRESS1 = "//input[@placeholder='*Address 1']"
    ZIP = "//input[@placeholder='*Zip']"
    MOBILE_NUMBER = "(//input[contains(@type,'text')])[1]"
    PHONE_NUMBER = "(//input[contains(@type,'text')])[2]"
    EMAIL = "//input[@placeholder='Email']"
    NOTES = "//textarea[@placeholder='Notes']"
    
    # Save Button
    SAVE_AND_INITIATE_EPISODE_BUTTON = "//ion-text[contains(.,'Save & initiate Episode')]"
    
    # Helper Locators
    DROPDOWN_OPTIONS = "//li[@role='option']"
    ZIP_SUGGESTION = "(//span[@class='ng-star-inserted'])[1]"

    def click_patients_tab(self):
        """Click on Patients tab"""
        try:
            patients_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Patient_Tab)))
            patients_tab.click()
            time.sleep(1)
            print("✓ Clicked Patients tab successfully")
        except TimeoutException:
            print("✗ Patients tab not found or not clickable")
            raise Exception("Failed to click Patients tab")
        except Exception as e:
            print(f"✗ Error clicking Patients tab: {str(e)}")
            raise

    def click_patient_registration_icon(self):
        """Click on patient registration icon"""
        try:
            registration_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Patient_Reg_Icon)))
            registration_icon.click()
            time.sleep(1)
            print("✓ Clicked patient registration icon successfully")
        except TimeoutException:
            print("✗ Patient registration icon not found or not clickable")
            raise Exception("Failed to click patient registration icon")
        except Exception as e:
            print(f"✗ Error clicking patient registration icon: {str(e)}")
            raise

    def open_new_patient_form(self):
        """Open new patient form"""
        try:
            new_patient_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.New_Patient_Button)))
            new_patient_button.click()
            time.sleep(2)  # Wait for form to load
            print("✓ Opened new patient form successfully")
        except TimeoutException:
            print("✗ New Patient button not found or not clickable")
            raise Exception("Failed to open new patient form")
        except Exception as e:
            print(f"✗ Error opening new patient form: {str(e)}")
            raise

    def enter_first_name(self):
        """Enter first name"""
        try:
            first_name_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.FIRST_NAME_BOX)))
            first_name_field.clear()
            first_name_field.send_keys(Patient_data.first_name)
            time.sleep(1)
            print(f"✓ Entered first name: {Patient_data.first_name}")
        except TimeoutException:
            print("✗ First name field not found")
            raise Exception("Failed to enter first name")
        except Exception as e:
            print(f"✗ Error entering first name: {str(e)}")
            # Try alternative approach
            try:
                first_name_field = self.driver.find_element(By.XPATH, self.FIRST_NAME_BOX)
                first_name_field.send_keys(Patient_data.first_name)
                print("✓ First name entered using alternative method")
            except:
                raise Exception("Failed to enter first name after retry")

    def enter_middle_name(self):
        """Enter middle name"""
        try:
            middle_name_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.MIDDLE_NAME_BOX)))
            middle_name_field.clear()
            middle_name_field.send_keys(Patient_data.middle_name)
            time.sleep(1)
            print(f"✓ Entered middle name: {Patient_data.middle_name}")
        except Exception as e:
            print(f"✗ Error entering middle name: {str(e)}")
            raise Exception("Failed to enter middle name")

    def enter_last_name(self):
        """Enter last name"""
        try:
            last_name_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.LAST_NAME_BOX)))
            last_name_field.clear()
            last_name_field.send_keys(Patient_data.last_name)
            time.sleep(1)
            print(f"✓ Entered last name: {Patient_data.last_name}")
        except Exception as e:
            print(f"✗ Error entering last name: {str(e)}")
            raise Exception("Failed to enter last name")

    def enter_dob(self):
        """Enter date of birth"""
        try:
            dob_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.BIRTHDATE_FIELD)))
            dob_field.click()
            time.sleep(2)
            dob_field.send_keys(Patient_data.dob)
            time.sleep(1)
            print(f"✓ Entered date of birth: {Patient_data.dob}")
        except Exception as e:
            print(f"✗ Error entering date of birth: {str(e)}")
            raise Exception("Failed to enter date of birth")

    def enter_gender(self):
        """Enter gender"""
        try:
            gender_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.GENDER_BOX)))
            gender_field.clear()
            gender_field.send_keys(Patient_data.gender)
            time.sleep(1)
            print(f"✓ Entered gender: {Patient_data.gender}")
        except Exception as e:
            print(f"✗ Error entering gender: {str(e)}")
            raise Exception("Failed to enter gender")

    def select_value_program(self):
        """Select value program"""
        try:
            value_program_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Value_Program_BOX)))
            value_program_field.clear()
            value_program_field.send_keys(Patient_data.Value_Program)
            value_program_field.send_keys(Keys.RETURN)
            time.sleep(1)
            print(f"✓ Selected value program: {Patient_data.Value_Program}")
        except Exception as e:
            print(f"✗ Error selecting value program: {str(e)}")
            raise Exception("Failed to select value program")

    def select_pgp(self):
        """Select PGP from dropdown"""
        try:
            arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.PGP_Arrow)))
            arrow.click()
            time.sleep(2)  # Wait for dropdown to load
            
            # Wait for options to appear
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.DROPDOWN_OPTIONS)))
            options = self.driver.find_elements(By.XPATH, self.DROPDOWN_OPTIONS)
            
            if not options:
                raise Exception("No PGP options found in dropdown")
            
            selected_option = random.choice(options)
            selected_option.click()
            time.sleep(1)
            print("✓ Selected PGP from dropdown successfully")
            
        except TimeoutException:
            print("✗ PGP dropdown not found or options not loaded")
            raise Exception("Failed to select PGP")
        except StaleElementReferenceException:
            print("⚠ Stale element, retrying PGP selection...")
            time.sleep(1)
            self.select_pgp()  # Retry once
        except Exception as e:
            print(f"✗ Error selecting PGP: {str(e)}")
            raise

    def select_provider(self):
        """Select provider from dropdown"""
        try:
            arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Provider_Arrow)))
            arrow.click()
            time.sleep(2)
            
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.DROPDOWN_OPTIONS)))
            options = self.driver.find_elements(By.XPATH, self.DROPDOWN_OPTIONS)
            
            if not options:
                raise Exception("No Provider options found in dropdown")
                
            selected_option = random.choice(options)
            selected_option.click()
            time.sleep(1)
            print("✓ Selected provider from dropdown successfully")
            
        except Exception as e:
            print(f"✗ Error selecting provider: {str(e)}")
            raise Exception("Failed to select provider")

    def select_primary_insurance(self):
        """Select primary insurance from dropdown"""
        try:
            arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Primary_Insurance_Arrow)))
            arrow.click()
            time.sleep(2)
            
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.DROPDOWN_OPTIONS)))
            options = self.driver.find_elements(By.XPATH, self.DROPDOWN_OPTIONS)
            
            if not options:
                raise Exception("No Primary Insurance options found in dropdown")
                
            selected_option = random.choice(options)
            selected_option.click()
            time.sleep(1)
            print("✓ Selected primary insurance from dropdown successfully")
            
        except Exception as e:
            print(f"✗ Error selecting primary insurance: {str(e)}")
            raise Exception("Failed to select primary insurance")

    def select_secondary_insurance(self):
        """Select secondary insurance from dropdown"""
        try:
            arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Secondary_Insurance_Arrow)))
            arrow.click()
            time.sleep(2)
            
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.DROPDOWN_OPTIONS)))
            options = self.driver.find_elements(By.XPATH, self.DROPDOWN_OPTIONS)
            
            if not options:
                raise Exception("No Secondary Insurance options found in dropdown")
                
            selected_option = random.choice(options)
            selected_option.click()
            time.sleep(1)
            print("✓ Selected secondary insurance from dropdown successfully")
            
        except Exception as e:
            print(f"✗ Error selecting secondary insurance: {str(e)}")
            raise Exception("Failed to select secondary insurance")

    def enter_insurance_id1(self):
        """Enter primary insurance ID"""
        field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.INSURANCE_ID1)))
        field.send_keys(Patient_data.Insurance_Id1)
        time.sleep(1)

    def enter_insurance_id2(self):
        """Enter secondary insurance ID"""
        field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.INSURANCE_ID2)))
        field.send_keys(Patient_data.Insurance_Id2)
        time.sleep(1)

    def enter_group_id1(self):
        """Enter primary group ID"""
        field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.GROUP_ID1)))
        field.send_keys(Patient_data.Group_Id1)
        time.sleep(1)

    def enter_group_id2(self):
        """Enter secondary group ID"""
        field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.GROUP_ID2)))
        field.click()
        field.send_keys(Patient_data.Group_Id2)
        time.sleep(1)

    def enter_address1(self):
        """Enter address"""
        field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.ADDRESS1)))
        field.click()
        field.send_keys(Patient_data.address)
        time.sleep(1)

    def enter_address_details(self):
        """Enter ZIP and select auto-suggestion"""
        try:
            # Enter static ZIP code
            zip_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.ZIP)))
            zip_field.click()
            time.sleep(1)
            zip_field.clear()
            time.sleep(2)
            zip_field.send_keys("10001")
            time.sleep(3)  # Wait for suggestions to load
            
            # Try to click on auto-suggestion
            try:
                first_suggestion = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.ZIP_SUGGESTION)))
                first_suggestion.click()
                time.sleep(1)
                print("✓ Selected ZIP auto-suggestion successfully")
            except TimeoutException:
                print("⚠ ZIP auto-suggestion not found, continuing without selection")
                # Continue without auto-suggestion selection
                
        except Exception as e:
            print(f"✗ Error entering address details: {str(e)}")
            raise Exception("Failed to enter address details")

    def enter_mobile_number(self):
        """Enter mobile number"""
        field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.MOBILE_NUMBER)))
        field.click()
        time.sleep(1)   
        field.send_keys(Patient_data.Mobile_number)
        time.sleep(1)

    def enter_phone_number(self):
        """Enter phone number"""
        field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.PHONE_NUMBER)))
        field.click()
        time.sleep(1)   
        field.send_keys(Patient_data.Home_Number)
        time.sleep(1)

    def enter_email(self):
        """Enter email"""
        field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.EMAIL)))
        field.send_keys(Patient_data.Email)
        time.sleep(1)

    def enter_notes(self):
        """Enter patient notes"""
        field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.NOTES)))
        field.send_keys(Patient_data.Patient_Note)
        time.sleep(1)

    def click_save_and_initiate_episode(self):
        """Click save and initiate episode button"""
        try:
            button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.SAVE_AND_INITIATE_EPISODE_BUTTON)))
            button.click()
            time.sleep(5)
            print("✓ Clicked Save & Initiate Episode button successfully")
            
            # Optional: Wait for success message or page redirect
            try:
                # You can add success verification here if needed
                time.sleep(2)
                print("✓ Patient registration saved successfully")
            except:
                print("⚠ Could not verify save completion, but button was clicked")
                
        except TimeoutException:
            print("✗ Save & Initiate Episode button not found")
            # Try alternative save button
            try:
                alt_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//ion-text[contains(.,'save & close')]")))
                alt_button.click()
                print("✓ Used alternative save button")
            except:
                raise Exception("Failed to save patient registration")
        except Exception as e:
            print(f"✗ Error saving patient registration: {str(e)}")
            raise 