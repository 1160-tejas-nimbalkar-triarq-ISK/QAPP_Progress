# Testcases/conftest.py
import pytest
from selenium import webdriver
from Config import Contents


# @pytest.fixture(params=["Chrome","Firefox", "Edge"], scope="session")
@pytest.fixture(params=["Chrome"], scope="session")
def setup(request):
    browser = request.param
    if browser == "Chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "Firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--disable-notifications")
        driver = webdriver.Firefox(options=firefox_options)
    elif browser == "Edge":
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument("--disable-notifications")
        driver = webdriver.Edge(options=edge_options)
    else:
        raise ValueError("Unsupported browser specified in configuration.")

    # Use the environment URL from Contents
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
