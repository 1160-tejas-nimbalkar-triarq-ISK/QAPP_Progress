# Testcases/test_Login.py
from Pages.Login_Page import LoginPage
from Config.Contents import USERNAME, PASSWORD
import time
import os
import pytest
from Screenshots.Screenshots_Module import screenshot_path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#
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


@pytest.mark.run(order=1)
@pytest.mark.sanity
def test_valid_login(setup):
    # Setup
    driver = setup
    login_page = LoginPage(driver)
    login_page.Login_Qpathways()
    capture_screenshot(driver, "test_valid_login", 1)


if __name__ == "__main__":
    pytest.main()
