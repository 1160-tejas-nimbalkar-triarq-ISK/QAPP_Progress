from Pages.New_Episode_Page import EpisodePage
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


@pytest.mark.run(order=29)
@pytest.mark.sanity
def test_enter_Episode_Description(setup):
    driver = setup
    episode_page = EpisodePage(driver)
    episode_page.enter_Episode_Description()
    capture_screenshot(driver, "test_enter_Episode_Description", 29)


'''
@pytest.mark.run(order=30)
@pytest.mark.sanity
def test_PGP_Box(setup):
    driver = setup
    episode_page = EpisodePage(driver)
    episode_page.select_PGP_dropdown()
'''


@pytest.mark.run(order=31)
@pytest.mark.sanity
def test_select_Physician(setup):
    driver = setup
    episode_page = EpisodePage(driver)
    episode_page.select_Physician()
    capture_screenshot(driver, "test_select_Physician", 31)


@pytest.mark.run(order=32)
@pytest.mark.sanity
def test_select_Program(setup):
    driver = setup
    episode_page = EpisodePage(driver)
    episode_page.select_Program()
    capture_screenshot(driver, "test_select_Program", 32)


@pytest.mark.run(order=33)
@pytest.mark.sanity
def test_select_Facility(setup):
    driver = setup
    episode_page = EpisodePage(driver)
    episode_page.select_Facility()
    capture_screenshot(driver, "test_select_Facility", 33)


@pytest.mark.run(order=34)
@pytest.mark.sanity
def test_select_surgery_Date(setup):
    driver = setup
    episode_page = EpisodePage(driver)
    episode_page.select_surgery_Date()
    capture_screenshot(driver, "test_select_surgery_Date", 34)


@pytest.mark.run(order=35)
@pytest.mark.sanity
def test_select_type(setup):
    driver = setup
    episode_page = EpisodePage(driver)
    episode_page.select_type()
    capture_screenshot(driver, "test_select_type", 35)


@pytest.mark.run(order=36)
@pytest.mark.sanity
def test_select_Surgery_For_Box(setup):
    driver = setup
    episode_page = EpisodePage(driver)
    episode_page.select_Surgery_For_Box()
    capture_screenshot(driver, "test_select_Surgery_For_Box", 36)


@pytest.mark.run(order=37)
@pytest.mark.sanity
def test_click_on_Save_button(setup):
    driver = setup
    episode_page = EpisodePage(driver)
    episode_page.click_on_Save_button()
    capture_screenshot(driver, "test_click_on_Save_button", 37)


@pytest.mark.run(order=38)
@pytest.mark.sanity
def test_select_Risk(setup):
    driver = setup
    episode_page = EpisodePage(driver)
    episode_page.select_risk()
    capture_screenshot(driver, "test_select_Risk", 38)


@pytest.mark.run(order=39)
@pytest.mark.sanity
def test_enter_target_Price(setup):
    driver = setup
    episode_page = EpisodePage(driver)
    episode_page.enter_target_Price()
    capture_screenshot(driver, "test_enter_target_Price", 39)


@pytest.mark.run(order=40)
@pytest.mark.sanity
def test_Enter_Episode_Note(setup):
    driver = setup
    episode_page = EpisodePage(driver)
    episode_page.enter_Episode_Note()
    capture_screenshot(driver, "test_Enter_Episode_Note", 40)


@pytest.mark.run(order=41)
@pytest.mark.sanity
def test_Select_Care_Plan(setup):
    driver = setup
    episode_page = EpisodePage(driver)
    episode_page.select_care_Plan()
    capture_screenshot(driver, "test_Select_Care_Plan", 41)


@pytest.mark.run(order=42)
@pytest.mark.sanity
def test_Click_On_Initiate_Button(setup):
    driver = setup
    episode_page = EpisodePage(driver)
    episode_page.Click_On_Initiate_Button()
    capture_screenshot(driver, "test_Click_On_Initiate_Button", 42)
