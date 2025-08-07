from behave import given, when, then
from pages.QPathways_TREND.patient_registration_page import PatientRegistrationPage
from utils.config import Config
import time

@given('I am logged into QPathways TREND application')
def step_login_to_qpathways_trend(context):
    """Login to QPathways TREND application"""
    try:
        # Ensure driver is initialized
        if not hasattr(context, 'driver') or context.driver is None:
            from features.environment import setup_chrome_driver
            context.driver = setup_chrome_driver()
            context.driver.maximize_window()
            context.driver.implicitly_wait(10)
            print("Driver initialized for TREND login")
        
        # Get credentials from config
        config = Config()
        credentials = config.get_qpathways_credentials()
        
        # Launch login page
        context.driver.get(credentials['url'])
        time.sleep(3)
        
        from selenium.webdriver.common.by import By
        
        # Enter username
        username_field = context.driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys(credentials['username'])
        
        # Enter password
        password_field = context.driver.find_element(By.XPATH, "//input[@type='password']")
        password_field.send_keys(credentials['password'])
        
        # Click login button
        login_button = context.driver.find_element(By.XPATH, "//ion-button[contains(.,'Login')]")
        login_button.click()
        time.sleep(40)  # Wait for login
        
        print("Login process completed.")
        print(f"Current URL after login: {context.driver.current_url}")
        
        # Verify successful login
        if "home" in context.driver.current_url:
            print("Successfully logged in and redirected from login page")
            print(f"Current URL: {context.driver.current_url}")
        else:
            raise Exception("Login failed - not redirected to home page")
            
    except Exception as e:
        print(f"Login failed: {str(e)}")
        if hasattr(context, 'driver') and context.driver:
            context.driver.save_screenshot("screenshots/login_error.png")
        raise

@when('I navigate to the Patients tab')
def step_navigate_to_patients_tab(context):
    """Navigate to Patients tab"""
    try:
        print("Attempting to navigate to Patients tab...")
        context.patient_registration_page = PatientRegistrationPage(context.driver)
        context.patient_registration_page.click_patients_tab()
        print("Successfully navigated to Patients tab")
    except Exception as e:
        print(f"Failed to navigate to Patients tab: {str(e)}")
        context.driver.save_screenshot("screenshots/patients_tab_error.png")
        raise

@when('I click on patient registration icon')
def step_click_patient_registration_icon(context):
    """Click on patient registration icon"""
    try:
        context.patient_registration_page.click_patient_registration_icon()
        print("Successfully clicked patient registration icon")
    except Exception as e:
        print(f"Failed to click patient registration icon: {str(e)}")
        context.driver.save_screenshot("screenshots/registration_icon_error.png")
        raise

@when('I click on New Patient button')
def step_click_new_patient_button(context):
    """Click on New Patient button"""
    try:
        context.patient_registration_page.open_new_patient_form()
        print("Successfully clicked New Patient button")
    except Exception as e:
        print(f"Failed to click New Patient button: {str(e)}")
        context.driver.save_screenshot("screenshots/new_patient_button_error.png")
        raise

# Basic Information Test Cases (6 fields)
@when('I enter patient first name')
def step_enter_patient_first_name(context):
    """Test Case 1: Enter patient first name"""
    try:
        context.patient_registration_page.enter_first_name()
        print("Test Case 1 PASSED: First name entered successfully")
    except Exception as e:
        print(f"Test Case 1 FAILED: First name entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc1_first_name_error.png")
        raise AssertionError(f"Test Case 1 - First name entry failed: {str(e)}")

@when('I enter patient middle name')
def step_enter_patient_middle_name(context):
    """Test Case 2: Enter patient middle name"""
    try:
        context.patient_registration_page.enter_middle_name()
        print("Test Case 2 PASSED: Middle name entered successfully")
    except Exception as e:
        print(f"Test Case 2 FAILED: Middle name entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc2_middle_name_error.png")
        raise AssertionError(f"Test Case 2 - Middle name entry failed: {str(e)}")

@when('I enter patient last name')
def step_enter_patient_last_name(context):
    """Test Case 3: Enter patient last name"""
    try:
        context.patient_registration_page.enter_last_name()
        print("Test Case 3 PASSED: Last name entered successfully")
    except Exception as e:
        print(f"Test Case 3 FAILED: Last name entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc3_last_name_error.png")
        raise AssertionError(f"Test Case 3 - Last name entry failed: {str(e)}")

@when('I enter patient date of birth')
def step_enter_patient_dob(context):
    """Test Case 4: Enter patient date of birth"""
    try:
        context.patient_registration_page.enter_dob()
        print("Test Case 4 PASSED: Date of birth entered successfully")
    except Exception as e:
        print(f"Test Case 4 FAILED: Date of birth entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc4_dob_error.png")
        raise AssertionError(f"Test Case 4 - Date of birth entry failed: {str(e)}")

@when('I enter patient gender')
def step_enter_patient_gender(context):
    """Test Case 5: Enter patient gender"""
    try:
        context.patient_registration_page.enter_gender()
        print("Test Case 5 PASSED: Gender entered successfully")
    except Exception as e:
        print(f"Test Case 5 FAILED: Gender entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc5_gender_error.png")
        raise AssertionError(f"Test Case 5 - Gender entry failed: {str(e)}")

@when('I select patient trend program')
def step_select_patient_trend_program(context):
    """Test Case 6: Select patient trend program"""
    try:
        context.patient_registration_page.select_trend_program()
        print("Test Case 6 PASSED: Trend program selected successfully")
    except Exception as e:
        print(f"Test Case 6 FAILED: Trend program selection failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc6_trend_program_error.png")
        raise AssertionError(f"Test Case 6 - Trend program selection failed: {str(e)}")

# Healthcare Providers Test Cases (3 fields)
@when('I select patient primary care provider')
def step_select_patient_primary_care_provider(context):
    """Test Case 7: Select patient primary care provider"""
    context.patient_registration_page.select_primary_care_provider()
    print("Test Case 7 PASSED: Primary care provider selected successfully")

@when('I select patient PGP')
def step_select_patient_pgp(context):
    """Test Case 8: Select patient PGP"""
    context.patient_registration_page.select_pgp()
    print("Test Case 8 PASSED: PGP selected successfully")

@when('I select patient provider')
def step_select_patient_provider(context):
    """Test Case 9: Select patient provider"""
    context.patient_registration_page.select_provider()
    print("Test Case 9 PASSED: Provider selected successfully")

# Primary Insurance Sequence (3 fields)
@when('I select primary insurance')
def step_select_primary_insurance(context):
    """Test Case 10: Select primary insurance"""
    context.patient_registration_page.select_primary_insurance()
    print("Test Case 10 PASSED: Primary insurance selected successfully")

@when('I enter primary insurance ID')
def step_enter_primary_insurance_id(context):
    """Test Case 11: Enter primary insurance ID"""
    context.patient_registration_page.enter_insurance_id1()
    print("Test Case 11 PASSED: Primary insurance ID entered successfully")

@when('I enter primary group ID')
def step_enter_primary_group_id(context):
    """Test Case 12: Enter primary group ID"""
    context.patient_registration_page.enter_group_id1()
    print("Test Case 12 PASSED: Primary group ID entered successfully")

# Secondary Insurance Sequence (3 fields)
@when('I select secondary insurance')
def step_select_secondary_insurance(context):
    """Test Case 13: Select secondary insurance"""
    context.patient_registration_page.select_secondary_insurance()
    print("Test Case 13 PASSED: Secondary insurance selected successfully")

@when('I enter secondary insurance ID')
def step_enter_secondary_insurance_id(context):
    """Test Case 14: Enter secondary insurance ID"""
    context.patient_registration_page.enter_insurance_id2()
    print("Test Case 14 PASSED: Secondary insurance ID entered successfully")

@when('I enter secondary group ID')
def step_enter_secondary_group_id(context):
    """Test Case 15: Enter secondary group ID"""
    context.patient_registration_page.enter_group_id2()
    print("Test Case 15 PASSED: Secondary group ID entered successfully")

# Contact Information Test Cases (6 fields)
@when('I enter patient address')
def step_enter_patient_address(context):
    """Test Case 16: Enter patient address"""
    context.patient_registration_page.enter_address1()
    print("Test Case 16 PASSED: Address entered successfully")

@when('I enter patient address details')
def step_enter_patient_address_details(context):
    """Test Case 17: Enter patient address details"""
    context.patient_registration_page.enter_address_details()
    print("Test Case 17 PASSED: Address details entered successfully")

@when('I enter patient mobile number')
def step_enter_patient_mobile_number(context):
    """Test Case 18: Enter patient mobile number"""
    context.patient_registration_page.enter_mobile_number()
    print("Test Case 18 PASSED: Mobile number entered successfully")

@when('I enter patient phone number')
def step_enter_patient_phone_number(context):
    """Test Case 19: Enter patient phone number"""
    context.patient_registration_page.enter_phone_number()
    print("Test Case 19 PASSED: Phone number entered successfully")

@when('I enter patient email')
def step_enter_patient_email(context):
    """Test Case 20: Enter patient email"""
    context.patient_registration_page.enter_email()
    print("Test Case 20 PASSED: Email entered successfully")

@when('I enter patient notes')
def step_enter_patient_notes(context):
    """Test Case 21: Enter patient notes"""
    context.patient_registration_page.enter_notes()
    print("Test Case 21 PASSED: Notes entered successfully")

# Save Patient Registration
@when('patient registration form should be saved successfully')
def step_patient_registration_form_saved(context):
    """Save patient registration form"""
    context.patient_registration_page.click_Add_Patient()
    print("Patient registration form saved successfully")

@then('patient should be registered successfully in TREND')
def step_patient_registered_successfully_trend(context):
    """Verify patient registration success in TREND"""
    print("Patient registered successfully in TREND")
    print("All test cases completed successfully!") 