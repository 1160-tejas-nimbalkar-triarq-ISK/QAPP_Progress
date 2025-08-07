import time
import pytest
from selenium.webdriver.common.by import By

from Pages.Utilization_Page import UtilizationPage
from Screenshots.Screenshots_Module import screenshot_path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def capture_screenshot(driver, test_name, utilization):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body")))
    screenshot_file = f"{screenshot_path}/{utilization}.{test_name}.png"
    if os.path.exists(screenshot_file):
        count = 1
        while os.path.exists(f"{screenshot_file}_{count}.png"):
            count += 1
        screenshot_file = f"{screenshot_file}_{count}.png"
    driver.save_screenshot(screenshot_file)


@pytest.mark.run(order=43)
@pytest.mark.sanity
def test_click_On_Utilization_Plus_Button(setup):
    driver = setup
    Utilization_page = UtilizationPage(driver)
    Utilization_page.click_On_Utilization_Plus_Button()
    capture_screenshot(driver, "test_click_On_Utilization_Plus_Button", 43)


@pytest.mark.run(order=44)
@pytest.mark.sanity
def test_open_Add_Order_Screen_for_Inpatient(setup):
    driver = setup
    Utilization_page = UtilizationPage(driver)
    Utilization_page.open_Add_Utilization_Screen_for_Inpatient()
    capture_screenshot(driver, "test_open_Add_Utilization_Screen_for_Inpatient", 44)
    time.sleep(3)


@pytest.mark.run(order=45)
@pytest.mark.sanity
def test_Add_Inpatient_Utilization(setup):
    driver = setup
    Utilization_page = UtilizationPage(driver)
    Utilization_page.Add_Inpatient_Utilization()
    capture_screenshot(driver, "test Add_Inpatient_utilization", 45)
    time.sleep(3)


@pytest.mark.run(order=46)
@pytest.mark.sanity
def test_Add_Outpatient_Utilization(setup):
    driver = setup
    Utilization_page = UtilizationPage(driver)
    Utilization_page.click_On_Utilization_Plus_Button()
    Utilization_page.Add_Outpatient_Utilization()
    capture_screenshot(driver, "test Add_Outpatient_utilization", 46)
    time.sleep(3)


@pytest.mark.run(order=47)
@pytest.mark.sanity
def test_Add_SNF_Utilization(setup):
    driver = setup
    Utilization_page = UtilizationPage(driver)
    Utilization_page.click_On_Utilization_Plus_Button()
    Utilization_page.Add_SNF_Utilization()
    capture_screenshot(driver, "test Add_SNF_utilization", 47)
    time.sleep(3)


@pytest.mark.run(order=54)
@pytest.mark.sanity
def test_Add_Home_Health_Utilization(setup):
    driver = setup
    Utilization_page = UtilizationPage(driver)
    Utilization_page.click_On_Utilization_Plus_Button()
    Utilization_page.Add_Home_Health_Utilization()
    capture_screenshot(driver, "test Add_Home_Health_utilization", 70)
    time.sleep(3)
