import time
import os
import pytest
from Pages.Note_Page import NotesPage
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


@pytest.mark.run(order=53)
@pytest.mark.sanity
def test_click_on_Notes_plus_button(setup):
    driver = setup
    Notes_Page = NotesPage(driver)
    Notes_Page.click_on_Notes_plus_button()
    capture_screenshot(driver, "test_click_on_Notes_plus_button", 53)


@pytest.mark.run(order=54)
@pytest.mark.sanity
def test_Add_Normal_Notes(setup):
    driver = setup
    Notes_Page = NotesPage(driver)
    Notes_Page.Add_Normal_Notes()
    capture_screenshot(driver, "test_Add_Normal_Notes", 54)


'''
@pytest.mark.run(order=57)
@pytest.mark.sanity
def test_Open_Newly_Added_Notes_On_EV(setup):
    driver = setup
    Notes_Page = NotesPage(driver)
    Notes_Page.Open_Newly_Added_Notes_On_EV()
    capture_screenshot(driver, "Test_Open_Newly_Added_Notes_On_EV", 63)


@pytest.mark.run(order=58)
@pytest.mark.sanity
def test_Verify_Date_On_Right_Panel(setup):
    driver = setup
    Notes_Page = NotesPage(driver)
    Notes_Page.Verify_Date_On_Right_Panel()
    capture_screenshot(driver,"Test_Verify_Date_On_Right_Panel", 64)
'''
