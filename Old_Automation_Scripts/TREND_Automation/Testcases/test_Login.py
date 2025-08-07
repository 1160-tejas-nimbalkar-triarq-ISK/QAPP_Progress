# Testcases/test_Login.py
from Pages.Login_Page import LoginPage
import time
import pytest
import os
import datetime

@pytest.mark.run(order=1)
@pytest.mark.sanity
def test_valid_login(setup):
    driver = setup
    lp = LoginPage(driver)
    lp.Login_Qpathways()
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    screenshot_dir = r"C:\Users\TejasNimbalkar\GlobalWorkspace\TREND_Automation\Screenshots"
    screenshot_filename = f"test_valid_Login_{timestamp}.png"
    screenshot_path = os.path.join(screenshot_dir, screenshot_filename)
    
    driver.save_screenshot(screenshot_path)
    
    time.sleep(20)

if __name__ == "__main__":
    pytest.main()
