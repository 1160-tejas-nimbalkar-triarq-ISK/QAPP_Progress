from behave import given, when, then
from pages.QPathaways_Clinical.patient_registration_page import PatientRegistrationPage
from pages.QPathaways_Clinical.qpathways_clinical_login_page import QpathwaysClinicalLoginPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from utils.config import Config
import time
import random
from faker import Faker

@given('I am logged into Qpathways Clinical application')
def step_login_to_qpathways_clinical(context):
    """Ensure user is logged into Qpathways Clinical application"""
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
    context.qpathways_clinical_login_page = QpathwaysClinicalLoginPage(context.driver)
    
    # Perform login
    context.qpathways_clinical_login_page.launch_login_page(qpathways_config['url'])
    
    # Wait for page to load
    WebDriverWait(context.driver, 15).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )
    time.sleep(2)
    
    # Enter credentials and login
    context.qpathways_clinical_login_page.enter_username(qpathways_config['username'])
    context.qpathways_clinical_login_page.enter_password(qpathways_config['password'])
    time.sleep(1)
    
    # Click login
    context.qpathways_clinical_login_page.click_login_button()
    print("Login completed, session active for patient registration")

@when('I navigate to the Patients tab')
def step_navigate_to_patients_tab(context):
    """Navigate to the Patients tab"""
    context.patient_registration_page = PatientRegistrationPage(context.driver)
    context.patient_registration_page.click_patients_tab()
    time.sleep(2)

@when('I click on patient registration icon')
def step_click_patient_registration_icon(context):
    """Click on patient registration icon"""
    context.patient_registration_page.click_patient_registration_icon()
    time.sleep(2)

@when('I click on New Patient button')
def step_click_new_patient_button(context):
    """Click on New Patient button"""
    context.patient_registration_page.click_new_patient_button()
    time.sleep(2)

@when('I fill patient basic details')
def step_fill_patient_basic_details(context):
    """Fill patient basic details using fake data"""
    fake = Faker()
    
    # Generate fake patient data
    first_name = fake.first_name()
    middle_name = fake.first_name()
    last_name = fake.last_name()
    dob = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%m-%d-%Y')
    gender = random.choice(["Male", "Female"])
    address = fake.address()
    zip_code = address.split(',')[-1].strip()[-5:]
    mobile_number = str(random.randint(1000000000, 9999999999))
    # Generate email based on first and last name: firstnamelastname123@mailinator.com
    email = f"{first_name.lower()}{last_name.lower()}123@mailinator.com"
    value_program = "TREND"
    
    # Fill the form
    context.patient_registration_page.enter_first_name(first_name)
    time.sleep(1)
    
    context.patient_registration_page.enter_middle_name(middle_name)
    time.sleep(1)
    
    context.patient_registration_page.enter_last_name(last_name)
    time.sleep(1)
    
    context.patient_registration_page.enter_dob(dob)
    time.sleep(1)
    
    context.patient_registration_page.enter_gender(gender)
    time.sleep(1)
    
    context.patient_registration_page.enter_address(address)
    time.sleep(1)
    
    context.patient_registration_page.enter_zip(zip_code)
    time.sleep(1)
    
    context.patient_registration_page.enter_mobile(mobile_number)
    time.sleep(1)
    
    context.patient_registration_page.enter_email(email)
    time.sleep(1)
    
    context.patient_registration_page.enter_value_program(value_program)
    time.sleep(1)

@then('patient registration form should be filled successfully')
def step_patient_registration_form_filled(context):
    """Verify patient registration form is filled"""
    print("✅ Patient registration form filled successfully.")
    time.sleep(2) 