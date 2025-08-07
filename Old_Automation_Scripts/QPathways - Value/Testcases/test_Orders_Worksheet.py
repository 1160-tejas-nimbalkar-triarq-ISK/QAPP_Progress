import time
import pytest
from selenium.webdriver.common.by import By
from Pages.Orders_Worksheet import OrdersWorksheetPage
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


@pytest.mark.run(order=81)
@pytest.mark.sanity
def test_Open_Orders_Worksheet(setup):
    driver = setup
    Worksheet_Page = OrdersWorksheetPage(driver)
    Worksheet_Page.Open_Orders_Worksheet()
    capture_screenshot(driver, "test_Open_Orders_Worksheet", 81)


@pytest.mark.run(order=82)
@pytest.mark.sanity
def test_Open_Filters_Screen(setup):
    driver = setup
    Worksheet_Page = OrdersWorksheetPage(driver)
    Worksheet_Page.Open_Filters_Screen()
    capture_screenshot(driver, "test_Open_Filters_Screen", 82)


@pytest.mark.run(order=83)
@pytest.mark.sanity
def test_Facility_Filter(setup):
    driver = setup
    Worksheet_Page = OrdersWorksheetPage(driver)
    Worksheet_Page.Facility_filter()
    capture_screenshot(driver, "test_Facility_Filter", 83)


@pytest.mark.run(order=84)
@pytest.mark.sanity
def test_Provider_filter(setup):
    driver = setup
    Worksheet_Page = OrdersWorksheetPage(driver)
    Worksheet_Page.Provider_filter()
    capture_screenshot(driver, "test_Provider_filter", 84)

