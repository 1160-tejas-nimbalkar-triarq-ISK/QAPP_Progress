# Testcases/test_Patients.py
from Pages.Patient_Page import PatientPage
import time
import os
import pytest
import datetime

def capture_screenshot(driver, test_name, order_number):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    screenshot_dir = r"C:\Users\TejasNimbalkar\GlobalWorkspace\TREND_Automation\Screenshots\Latest_Screenshot"
    screenshot_filename = f"{test_name}_{order_number}_{timestamp}.png"
    screenshot_path = os.path.join(screenshot_dir, screenshot_filename)
    driver.save_screenshot(screenshot_path)


@pytest.mark.run(order=2)
@pytest.mark.sanity
def test_view_patients_list(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.click_patients_tab()
    capture_screenshot(driver, "test_view_patients_list", 2)
    time.sleep(5)


@pytest.mark.run(order=3)
@pytest.mark.sanity
def test_click_reg_patient_icon(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.click_patient_registration_icon()
    capture_screenshot(driver, "test_click_reg_patient_icon", 3)
    time.sleep(5)


@pytest.mark.run(order=4)
@pytest.mark.sanity
def test_open_new_patient_form(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.open_new_patient_form()
    capture_screenshot(driver, "test_open_new_patient_form", 4)
    time.sleep(5)


@pytest.mark.run(order=5)
@pytest.mark.sanity
def test_enter_first_name(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_first_name()
    capture_screenshot(driver, "test_enter_first_name", 5)
    time.sleep(2)


@pytest.mark.run(order=6)
@pytest.mark.sanity
def test_enter_middle_name(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_middle_name()
    capture_screenshot(driver, "test_enter_middle_name", 6)
    time.sleep(2)


@pytest.mark.run(order=7)
@pytest.mark.sanity
def test_enter_last_name(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_last_name()
    capture_screenshot(driver, "test_enter_last_name", 7)
    time.sleep(2)


@pytest.mark.run(order=8)
@pytest.mark.sanity
def test_enter_dob(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_dob()
    capture_screenshot(driver, "test_enter_dob", 8)
    time.sleep(2)


@pytest.mark.run(order=9)
@pytest.mark.sanity
def test_enter_gender(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_gender()
    capture_screenshot(driver, "test_enter_gender", 9)
    time.sleep(2)

@pytest.mark.run(order=10)  # Added test case for select_value_program
@pytest.mark.sanity
def test_select_value_program(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.select_value_program() # Use the PatientPage method
    capture_screenshot(driver, "test_select_value_program", 10)
    time.sleep(2)

@pytest.mark.run(order=11)  # Order 11 for PCP Group selection
@pytest.mark.sanity
def test_select_pcp_group(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.select_pcp_group()
    capture_screenshot(driver, "test_select_pcp_group", 11)
    time.sleep(2)

@pytest.mark.run(order=12) # Order 12 for PCP Provider selection
@pytest.mark.sanity
def test_select_pcp_provider(setup): # Added test case
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.select_pcp_provider()
    capture_screenshot(driver, "test_select_pcp_provider", 12)
    time.sleep(2)

@pytest.mark.run(order=13)  # Order 13 for PGP Group selection
@pytest.mark.sanity
def test_select_pgp_group(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.select_pgp_group()
    capture_screenshot(driver, "test_select_pgp_group", 13)
    time.sleep(2)

@pytest.mark.run(order=14)  # Order 14 for Provider (PGP Provider) selection
@pytest.mark.sanity
def test_select_provider(setup):  # This is assumed to be PGP Provider selection
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.select_provider()
    capture_screenshot(driver, "test_select_provider", 14)
    time.sleep(2)

@pytest.mark.run(order=15)  # Order 15 for Email
@pytest.mark.sanity
def test_enter_email(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_email()
    capture_screenshot(driver, "test_enter_email", 15)
    time.sleep(2)

