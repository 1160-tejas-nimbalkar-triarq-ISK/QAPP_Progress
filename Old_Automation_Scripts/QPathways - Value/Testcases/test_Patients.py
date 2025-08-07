from Pages.Patient_Page import PatientPage
import time
import os
import pytest
from Screenshots.Screenshots_Module import screenshot_path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def capture_screenshot(driver, test_name, order):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body")))
    screenshot_file = f"{screenshot_path}/{order}.{test_name}.png"
    if os.path.exists(screenshot_file):
        count = 1
        while os.path.exists(f"{screenshot_file}_{count}.png"):
            count += 1
        screenshot_file = f"{screenshot_file}_{count}.png"
    driver.save_screenshot(screenshot_file)


@pytest.mark.run(order=2)
@pytest.mark.sanity
def test_view_patients_list(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.click_patients_tab()
    capture_screenshot(driver, "test_view_patients_list", 2)


@pytest.mark.run(order=3)
@pytest.mark.sanity
def test_click_reg_patient_icon(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.click_patient_registration_icon()
    capture_screenshot(driver, "test_click_reg_patient_icon", 3)


@pytest.mark.run(order=4)
@pytest.mark.sanity
def test_open_new_patient_form(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.open_new_patient_form()
    capture_screenshot(driver, "test_open_new_patient_form", 4)


@pytest.mark.run(order=5)
@pytest.mark.sanity
def test_select_PGP_dropdown(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.select_PGP_dropdown()
    capture_screenshot(driver, "test_select_PGP_dropdown", 5)


@pytest.mark.run(order=6)
@pytest.mark.sanity
def test_enter_first_name(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_first_name()
    capture_screenshot(driver, "test_enter_first_name", 6)


@pytest.mark.run(order=7)
@pytest.mark.sanity
def test_enter_middle_name(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_middle_name()
    capture_screenshot(driver, "test_enter_middle_name", 7)


@pytest.mark.run(order=8)
@pytest.mark.sanity
def test_enter_last_name(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_last_name()
    capture_screenshot(driver, "test_enter_last_name", 8)


@pytest.mark.run(order=9)
@pytest.mark.sanity
def test_enter_dob(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_dob()
    capture_screenshot(driver, "test_enter_dob", 9)


@pytest.mark.run(order=10)
@pytest.mark.sanity
def test_enter_gender(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_gender()
    capture_screenshot(driver, "test_enter_gender", 10)


@pytest.mark.run(order=11)
@pytest.mark.sanity
def test_enter_address(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_address()
    capture_screenshot(driver, "test_enter_address", 11)


@pytest.mark.run(order=12)
@pytest.mark.sanity
def test_enter_zip(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_zip()
    capture_screenshot(driver, "test_enter_zip", 12)


@pytest.mark.run(order=13)
@pytest.mark.sanity
def test_enter_Mo_No(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_Mobile_No()
    capture_screenshot(driver, "test_enter_Mo_No", 13)


@pytest.mark.run(order=14)
@pytest.mark.sanity
def test_enter_home_no(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_home_no()
    capture_screenshot(driver, "test_enter_home_no", 14)


@pytest.mark.run(order=15)
def test_see_office_number_option(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.see_office_number_option()
    capture_screenshot(driver, "test_see_office_number_option", 15)


@pytest.mark.run(order=16)
def test_enter_office_number(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_office_number()
    capture_screenshot(driver, "test_enter_office_number", 16)


@pytest.mark.run(order=17)
def test_see_fax_number_option(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.see_fax_number_option()
    capture_screenshot(driver, "test_see_fax_number_option", 17)


@pytest.mark.run(order=18)
def test_enter_fax_number(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_fax_number()
    capture_screenshot(driver, "test_enter_fax_number", 18)


@pytest.mark.run(order=19)
@pytest.mark.sanity
def test_enter_email(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_email()
    capture_screenshot(driver, "test_enter_email", 19)


@pytest.mark.run(order=20)
@pytest.mark.sanity
def test_select_physician(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.select_physician()
    capture_screenshot(driver, "test_select_physician", 20)


@pytest.mark.run(order=21)
@pytest.mark.sanity
def test_select_insurance(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.select_insurance()
    capture_screenshot(driver, "test_select_insurance", 21)


@pytest.mark.run(order=22)
@pytest.mark.sanity
def test_enter_insurance_id(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_Insurance_ID()
    capture_screenshot(driver, "test_enter_insurance_id", 22)


@pytest.mark.run(order=23)
def test_enter_group_id(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_Group_ID()
    capture_screenshot(driver, "test_enter_group_id", 23)


@pytest.mark.run(order=24)
def test_enter_Patient_Note(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.enter_Patient_Note()
    capture_screenshot(driver, "test_enter_Patient_Note", 24)


@pytest.mark.run(order=25)
def test_check_exclude_Report_ceckbox(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.check_exclude_Report_ceckbox()
    capture_screenshot(driver, "test_check_exclude_Report_ceckbox", 25)


@pytest.mark.run(order=26)
def test_see_save_button(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.see_save_button()
    capture_screenshot(driver, "test_see_save_button", 26)


@pytest.mark.run(order=27)
def test_see_save_and_initiate_button(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.see_save_and_initiate_button()
    capture_screenshot(driver, "test_see_save_and_initiate_button", 27)


@pytest.mark.run(order=28)
def test_open_new_Episode_Screen(setup):
    driver = setup
    patient_page = PatientPage(driver)
    patient_page.open_New_Episode_Screen()
    capture_screenshot(driver, "test_open_new_Episode_Screen", 28)
