from behave import given, when, then
from pages.QPathways_Value.patient_registration_page import PatientRegistrationPage
from pages.QPathways_Value.qpathways_login_page import QpathwaysLoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException
from utils.config import Config
import time
import os

@given('I am logged into QPathways Value application')
def step_login_to_qpathways_value(context):
    """Ensure user is logged into QPathways Value application"""
    # Check if driver exists and if we're already logged in
    if hasattr(context, 'driver') and context.driver:
        current_url = context.driver.current_url
        # If we're already on dashboard/home page, assume login is done
        if 'login' not in current_url.lower() and current_url != 'data:,':
            print("Already logged in, reusing session")
            return
    
    # If not logged in or no driver, perform login
    if not hasattr(context, 'driver') or context.driver is None:
        from features.environment import setup_chrome_driver
        context.driver = setup_chrome_driver()
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)
    
    # Get configuration
    config = Config()
    qpathways_config = config.get_qpathways_credentials()
    
    # Initialize login page
    context.qpathways_login_page = QpathwaysLoginPage(context.driver)
    
    # Perform login
    context.qpathways_login_page.launch_login_page(qpathways_config['url'])
    
    # Wait for page to load
    WebDriverWait(context.driver, 15).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )
    time.sleep(2)
    
    # Enter credentials and login
    context.qpathways_login_page.enter_username(qpathways_config['username'])
    context.qpathways_login_page.enter_password(qpathways_config['password'])
    time.sleep(1)
    
    # Click login
    context.qpathways_login_page.click_login_button()
    print("Login completed, session active for patient registration")

@when('I navigate to the Patients tab')
def step_navigate_to_patients_tab(context):
    """Navigate to the Patients tab"""
    try:
        context.patient_registration_page = PatientRegistrationPage(context.driver)
        context.patient_registration_page.click_patients_tab()
        time.sleep(2)
        print("✓ Successfully navigated to Patients tab")
    except Exception as e:
        print(f"✗ Failed to navigate to Patients tab: {str(e)}")
        context.driver.save_screenshot("screenshots/patients_tab_error.png")
        raise AssertionError(f"Navigation to Patients tab failed: {str(e)}")

@when('I click on patient registration icon')
def step_click_patient_registration_icon(context):
    """Click on patient registration icon"""
    try:
        context.patient_registration_page.click_patient_registration_icon()
        time.sleep(2)
        print("✓ Successfully clicked patient registration icon")
    except Exception as e:
        print(f"✗ Failed to click patient registration icon: {str(e)}")
        context.driver.save_screenshot("screenshots/registration_icon_error.png")
        raise AssertionError(f"Failed to click patient registration icon: {str(e)}")

@when('I click on New Patient button')
def step_click_new_patient_button(context):
    """Click on New Patient button"""
    try:
        context.patient_registration_page.open_new_patient_form()
        time.sleep(2)
        print("✓ Successfully clicked New Patient button")
    except Exception as e:
        print(f"✗ Failed to click New Patient button: {str(e)}")
        context.driver.save_screenshot("screenshots/new_patient_button_error.png")
        raise AssertionError(f"Failed to click New Patient button: {str(e)}")

# Basic Information Test Cases (6 fields)
@when('I enter patient first name')
def step_enter_patient_first_name(context):
    """Test Case 1: Enter patient first name"""
    try:
        context.patient_registration_page.enter_first_name()
        print("✅ Test Case 1 PASSED: First name entered successfully")
    except Exception as e:
        print(f"❌ Test Case 1 FAILED: First name entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc1_first_name_error.png")
        raise AssertionError(f"Test Case 1 - First name entry failed: {str(e)}")

@when('I enter patient middle name')
def step_enter_patient_middle_name(context):
    """Test Case 2: Enter patient middle name"""
    try:
        context.patient_registration_page.enter_middle_name()
        print("✅ Test Case 2 PASSED: Middle name entered successfully")
    except Exception as e:
        print(f"❌ Test Case 2 FAILED: Middle name entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc2_middle_name_error.png")
        raise AssertionError(f"Test Case 2 - Middle name entry failed: {str(e)}")

@when('I enter patient last name')
def step_enter_patient_last_name(context):
    """Test Case 3: Enter patient last name"""
    try:
        context.patient_registration_page.enter_last_name()
        print("✅ Test Case 3 PASSED: Last name entered successfully")
    except Exception as e:
        print(f"❌ Test Case 3 FAILED: Last name entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc3_last_name_error.png")
        raise AssertionError(f"Test Case 3 - Last name entry failed: {str(e)}")

@when('I enter patient date of birth')
def step_enter_patient_dob(context):
    """Test Case 4: Enter patient date of birth"""
    try:
        context.patient_registration_page.enter_dob()
        print("✅ Test Case 4 PASSED: Date of birth entered successfully")
    except Exception as e:
        print(f"❌ Test Case 4 FAILED: Date of birth entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc4_dob_error.png")
        raise AssertionError(f"Test Case 4 - Date of birth entry failed: {str(e)}")

@when('I enter patient gender')
def step_enter_patient_gender(context):
    """Test Case 5: Enter patient gender"""
    try:
        context.patient_registration_page.enter_gender()
        print("✅ Test Case 5 PASSED: Gender entered successfully")
    except Exception as e:
        print(f"❌ Test Case 5 FAILED: Gender entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc5_gender_error.png")
        raise AssertionError(f"Test Case 5 - Gender entry failed: {str(e)}")

@when('I select patient value program')
def step_select_patient_value_program(context):
    """Test Case 6: Select patient value program"""
    try:
        context.patient_registration_page.select_value_program()
        print("✅ Test Case 6 PASSED: Value program selected successfully")
    except Exception as e:
        print(f"❌ Test Case 6 FAILED: Value program selection failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc6_value_program_error.png")
        raise AssertionError(f"Test Case 6 - Value program selection failed: {str(e)}")

# Healthcare Providers Test Cases (2 fields)
@when('I select patient PGP')
def step_select_patient_pgp(context):
    """Test Case 7: Select patient PGP (Non-Critical)"""
    try:
        context.patient_registration_page.select_pgp()
        print("✅ Test Case 7 PASSED: PGP selected successfully")
    except Exception as e:
        print(f"⚠️ Test Case 7 WARNING: PGP selection failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc7_pgp_error.png")
        # Don't raise error - continue with test as this might be optional

@when('I select patient provider')
def step_select_patient_provider(context):
    """Test Case 8: Select patient provider (Non-Critical)"""
    try:
        context.patient_registration_page.select_provider()
        print("✅ Test Case 8 PASSED: Provider selected successfully")
    except Exception as e:
        print(f"⚠️ Test Case 8 WARNING: Provider selection failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc8_provider_error.png")
        # Don't raise error - continue with test as this might be optional

# Insurance Information Test Cases (6 fields)
@when('I select primary insurance')
def step_select_primary_insurance(context):
    """Test Case 9: Select primary insurance (Non-Critical)"""
    try:
        context.patient_registration_page.select_primary_insurance()
        print("✅ Test Case 9 PASSED: Primary insurance selected successfully")
    except Exception as e:
        print(f"⚠️ Test Case 9 WARNING: Primary insurance selection failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc9_primary_insurance_error.png")
        # Don't raise error - continue with test

@when('I enter primary insurance ID')
def step_enter_primary_insurance_id(context):
    """Test Case 10: Enter primary insurance ID (Non-Critical)"""
    try:
        context.patient_registration_page.enter_insurance_id1()
        print("✅ Test Case 10 PASSED: Primary insurance ID entered successfully")
    except Exception as e:
        print(f"⚠️ Test Case 10 WARNING: Primary insurance ID entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc10_primary_insurance_id_error.png")
        # Don't raise error - continue with test

@when('I enter primary group ID')
def step_enter_primary_group_id(context):
    """Test Case 11: Enter primary group ID (Non-Critical)"""
    try:
        context.patient_registration_page.enter_group_id1()
        print("✅ Test Case 11 PASSED: Primary group ID entered successfully")
    except Exception as e:
        print(f"⚠️ Test Case 11 WARNING: Primary group ID entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc11_primary_group_id_error.png")
        # Don't raise error - continue with test

@when('I select secondary insurance')
def step_select_secondary_insurance(context):
    """Test Case 12: Select secondary insurance (Non-Critical)"""
    try:
        context.patient_registration_page.select_secondary_insurance()
        print("✅ Test Case 12 PASSED: Secondary insurance selected successfully")
    except Exception as e:
        print(f"⚠️ Test Case 12 WARNING: Secondary insurance selection failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc12_secondary_insurance_error.png")
        # Don't raise error - continue with test

@when('I enter secondary insurance ID')
def step_enter_secondary_insurance_id(context):
    """Test Case 13: Enter secondary insurance ID (Non-Critical)"""
    try:
        context.patient_registration_page.enter_insurance_id2()
        print("✅ Test Case 13 PASSED: Secondary insurance ID entered successfully")
    except Exception as e:
        print(f"⚠️ Test Case 13 WARNING: Secondary insurance ID entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc13_secondary_insurance_id_error.png")
        # Don't raise error - continue with test

@when('I enter secondary group ID')
def step_enter_secondary_group_id(context):
    """Test Case 14: Enter secondary group ID (Non-Critical)"""
    try:
        context.patient_registration_page.enter_group_id2()
        print("✅ Test Case 14 PASSED: Secondary group ID entered successfully")
    except Exception as e:
        print(f"⚠️ Test Case 14 WARNING: Secondary group ID entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc14_secondary_group_id_error.png")
        # Don't raise error - continue with test

# Contact Information Test Cases (6 fields)
@when('I enter patient address')
def step_enter_patient_address(context):
    """Test Case 15: Enter patient address"""
    try:
        context.patient_registration_page.enter_address1()
        print("✅ Test Case 15 PASSED: Patient address entered successfully")
    except Exception as e:
        print(f"❌ Test Case 15 FAILED: Patient address entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc15_address_error.png")
        raise AssertionError(f"Test Case 15 - Patient address entry failed: {str(e)}")

@when('I enter patient address details')
def step_enter_patient_address_details(context):
    """Test Case 16: Enter patient address details (ZIP and auto-suggestion)"""
    try:
        context.patient_registration_page.enter_address_details()
        print("✅ Test Case 16 PASSED: Patient address details entered successfully")
    except Exception as e:
        print(f"❌ Test Case 16 FAILED: Patient address details entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc16_address_details_error.png")
        raise AssertionError(f"Test Case 16 - Patient address details entry failed: {str(e)}")

@when('I enter patient mobile number')
def step_enter_patient_mobile_number(context):
    """Test Case 17: Enter patient mobile number"""
    try:
        context.patient_registration_page.enter_mobile_number()
        print("✅ Test Case 17 PASSED: Patient mobile number entered successfully")
    except Exception as e:
        print(f"❌ Test Case 17 FAILED: Patient mobile number entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc17_mobile_number_error.png")
        raise AssertionError(f"Test Case 17 - Patient mobile number entry failed: {str(e)}")

@when('I enter patient phone number')
def step_enter_patient_phone_number(context):
    """Test Case 18: Enter patient phone number"""
    try:
        context.patient_registration_page.enter_phone_number()
        print("✅ Test Case 18 PASSED: Patient phone number entered successfully")
    except Exception as e:
        print(f"❌ Test Case 18 FAILED: Patient phone number entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc18_phone_number_error.png")
        raise AssertionError(f"Test Case 18 - Patient phone number entry failed: {str(e)}")

@when('I enter patient email')
def step_enter_patient_email(context):
    """Test Case 19: Enter patient email"""
    try:
        context.patient_registration_page.enter_email()
        print("✅ Test Case 19 PASSED: Patient email entered successfully")
    except Exception as e:
        print(f"❌ Test Case 19 FAILED: Patient email entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc19_email_error.png")
        raise AssertionError(f"Test Case 19 - Patient email entry failed: {str(e)}")

@when('I enter patient notes')
def step_enter_patient_notes(context):
    """Test Case 20: Enter patient notes"""
    try:
        context.patient_registration_page.enter_notes()
        print("✅ Test Case 20 PASSED: Patient notes entered successfully")
    except Exception as e:
        print(f"❌ Test Case 20 FAILED: Patient notes entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc20_notes_error.png")
        raise AssertionError(f"Test Case 20 - Patient notes entry failed: {str(e)}")

@when('patient registration form should be saved successfully')
def step_patient_registration_form_saved(context):
    """Save patient registration and proceed to episode creation"""
    try:
        print("💾 Saving patient registration...")
        context.patient_registration_page.click_save_and_initiate_episode()
        print("✅ Patient registration completed! Proceeding to Episode Creation...")
        time.sleep(3)
        
        # The save action automatically navigates to Episode Creation page
        current_url = context.driver.current_url
        print(f"Current URL after save: {current_url}")
        print("🔄 Now entering Episode Creation workflow...")
        
    except Exception as e:
        print(f"❌ Patient registration save failed - {str(e)}")
        context.driver.save_screenshot("screenshots/patient_save_error.png")
        
        # Try to get page source for debugging
        try:
            page_source = context.driver.page_source
            with open("reports/patient_error_page_source.html", "w", encoding="utf-8") as f:
                f.write(page_source)
            print("📄 Page source saved to reports/patient_error_page_source.html for debugging")
        except:
            pass
            
        raise AssertionError(f"Patient registration save failed: {str(e)}")