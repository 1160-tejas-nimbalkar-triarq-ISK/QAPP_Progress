# Testcases/conftest.py
import pytest
from selenium import webdriver
from Config import Contents

#
@pytest.fixture(scope='session')
def setup():
    if Contents.BROWSER == "Chrome":
        # Set Chrome options to disable notifications
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=chrome_options)

    elif Contents.BROWSER == "Firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--disable-notifications")
        driver = webdriver.Firefox(options=firefox_options)

    elif Contents.BROWSER == "IE":
        driver = webdriver.Ie()
    else:
        raise ValueError("Unsupported browser specified in configuration.")

    # Determine the URL based on the environment
    if Contents.ENVIRONMENT == "QA":
        website_url = "https://qprime-qa.myqone.com/"
    elif Contents.ENVIRONMENT == "Staging":
        website_url = "https://qprime-Staging.myqone.com/"
    elif Contents.ENVIRONMENT == "Dev":
        website_url = "https://qprime-dev.myqone.com/"
    else:
        raise ValueError("Unsupported environment specified in configuration.")

    driver.get(website_url)
    driver.maximize_window()
    yield driver
    driver.quit()
