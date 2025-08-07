import time
import pytest
from selenium.webdriver.common.by import By
from Pages.Episodes_Worksheet import EpisodesWorksheetPage
from Pages.Orders_Page import OrderPage
from Screenshots.Screenshots_Module import screenshot_path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


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


@pytest.mark.run(order=71)
@pytest.mark.sanity
def test_Open_Episodes_Worksheet(setup):
    driver = setup
    Worksheet_Page = EpisodesWorksheetPage(driver)
    Worksheet_Page.Open_Episodes_Worksheet()
    capture_screenshot(driver, "test_Open_Episodes_Worksheet", 71)


@pytest.mark.run(order=72)
@pytest.mark.sanity
def test_Open_Filters_Screen(setup):
    driver = setup
    Worksheet_Page = EpisodesWorksheetPage(driver)
    Worksheet_Page.Open_Filters_Screen()
    capture_screenshot(driver, "test_Open_Filters_Screen", 72)


@pytest.mark.run(order=73)
@pytest.mark.sanity
def test_ActiveStatus_Filter(setup):
    driver = setup
    Worksheet_Page = EpisodesWorksheetPage(driver)
    Worksheet_Page.ActiveStatus_Filter()
    capture_screenshot(driver, "test_Active_Status_Filter", 73)


@pytest.mark.run(order=74)
@pytest.mark.sanity
def test_Finished_Status_Filter(setup):
    driver = setup
    Worksheet_Page = EpisodesWorksheetPage(driver)
    Worksheet_Page.Finished_Status_Filter()
    capture_screenshot(driver, "test_Finished_Status_Filter", 74)


@pytest.mark.run(order=75)
@pytest.mark.sanity
def test_New_Status_Filter(setup):
    driver = setup
    Worksheet_Page = EpisodesWorksheetPage(driver)
    Worksheet_Page.New_Status_Filter()
    capture_screenshot(driver, "test_New_Status_Filter", 75)


@pytest.mark.run(order=76)
@pytest.mark.sanity
def test_physician_Filter(setup):
    driver = setup
    Worksheet_Page = EpisodesWorksheetPage(driver)
    Worksheet_Page.physician_filter()
    capture_screenshot(driver, "test_physician_Filter", 76)


@pytest.mark.run(order=77)
@pytest.mark.sanity
def test_PGP_Filter(setup):
    driver = setup
    Worksheet_Page = EpisodesWorksheetPage(driver)
    Worksheet_Page.PGP_filter()
    capture_screenshot(driver, "test_PGP_Filter", 77)


@pytest.mark.run(order=78)
@pytest.mark.sanity
def test_Facility_Filter(setup):
    driver = setup
    Worksheet_Page = EpisodesWorksheetPage(driver)
    Worksheet_Page.Facility_filter()
    capture_screenshot(driver, "test_Facility_Filter", 78)


@pytest.mark.run(order=79)
@pytest.mark.sanity
def test_facility_and_pgp_filter(setup):
    driver = setup
    Worksheet_Page = EpisodesWorksheetPage(driver)
    Worksheet_Page.facility_and_pgp_filter()
    capture_screenshot(driver, "test_facility_and_pgp_filter", 79)


'''
@pytest.mark.run(order=80)
@pytest.mark.sanity
def test_DateRange_Filter(setup):
    driver = setup
    Worksheet_Page = EpisodesWorksheetPage(driver)
    Worksheet_Page.DateRange_filter()
    capture_screenshot(driver, "test_DateRange_Filter", 80)

'''
