import time
import os
import pytest
from Pages.Activities_Page import ActivitiesPage
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


@pytest.mark.run(order=48)
@pytest.mark.sanity
def test_click_on_activities_plus_button(setup):
    driver = setup
    Activities_Page = ActivitiesPage(driver)
    Activities_Page.click_on_activities_plus_button()
    capture_screenshot(driver, "test_click_on_activities_plus_button", 48)


@pytest.mark.run(order=49)
@pytest.mark.sanity
def test_click_on_call_activity_option(setup):
    driver = setup
    Activities_Page = ActivitiesPage(driver)
    Activities_Page.click_on_call_activity_option()
    capture_screenshot(driver, "test_click_on_call_activity_option", 49)


@pytest.mark.run(order=50)
@pytest.mark.sanity
def test_add_CallActivity(setup):
    driver = setup
    Activities_Page = ActivitiesPage(driver)
    Activities_Page.add_CallActivity()
    capture_screenshot(driver, "test_add_CallActivity", 50)


@pytest.mark.run(order=51)
@pytest.mark.sanity
def test_click_on_form_activity_option(setup):
    driver = setup
    Activities_Page = ActivitiesPage(driver)
    Activities_Page.click_on_form_activity_option()
    capture_screenshot(driver, "test_click_on_form_activity_option", 51)


@pytest.mark.run(order=52)
@pytest.mark.sanity
def test_add_Form_Activity(setup):
    driver = setup
    Activities_Page = ActivitiesPage(driver)
    Activities_Page.add_Form_Activity()
    capture_screenshot(driver, "test_add_Form_Activity", 52)


'''
@pytest.mark.run(order=48)
@pytest.mark.sanity
def test_find_and_click_activity(setup):
    driver = setup
    Activities_Page = ActivitiesPage(driver)
    Activities_Page.find_and_click_activity()
    time.sleep(5)
    capture_screenshot(driver, "test_find_and_click_activity", 60)
'''
