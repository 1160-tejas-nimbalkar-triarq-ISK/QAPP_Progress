import time
import pytest
from selenium.webdriver.common.by import By

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


'''
@pytest.mark.run(order=55)
@pytest.mark.sanity
def test_Click_Episode_Tab(setup):
    driver = setup
    Order_page = OrderPage(driver)
    Order_page.click_Episode_tab()
    capture_screenshot(driver, "test_Click_Episode_Tab", 55)



@pytest.mark.run(order=56)
@pytest.mark.sanity
def test_Apply_Planed_Filter(setup):
    driver = setup
    Order_page = OrderPage(driver)
    Order_page.Apply_Planed_Filter()
    capture_screenshot(driver, "test_Apply_Planed_Filter", 56)


@pytest.mark.run(order=57)
@pytest.mark.sanity
def test_select_First_index(setup):
    driver = setup
    Order_page = OrderPage(driver)
    Order_page.select_First_index()
    capture_screenshot(driver, "test_select_First_index", 57)

'''


@pytest.mark.run(order=58)
@pytest.mark.sanity
def test_click_On_Plus_Button(setup):
    driver = setup
    Order_page = OrderPage(driver)
    Order_page.click_On_Plus_Button()
    capture_screenshot(driver, "test_click_On_Plus_Button", 58)


@pytest.mark.run(order=59)
@pytest.mark.sanity
def test_open_Add_Order_Screen_for_HHA(setup):
    driver = setup
    Order_page = OrderPage(driver)
    Order_page.open_Add_Order_Screen_for_HHA()
    capture_screenshot(driver, "test_open_Add_Order_Screen_for_HHA", 59)


@pytest.mark.run(order=60)
@pytest.mark.sanity
def test_Add_HHA_Order(setup):
    driver = setup
    Order_page = OrderPage(driver)
    Order_page.Add_HHA_Order()
    time.sleep(5)
    capture_screenshot(driver, "test_Add_HHA_Order", 60)


@pytest.mark.run(order=61)
@pytest.mark.sanity
def test_open_Add_Order_Screen_for_PT(setup):
    driver = setup
    Order_page = OrderPage(driver)
    Order_page.open_Add_Order_Screen_for_PT()
    capture_screenshot(driver, "test_open_Add_Order_Screen_for_PT", 61)


@pytest.mark.run(order=62)
@pytest.mark.sanity
def test_Add_PT_Order(setup):
    driver = setup
    Order_page = OrderPage(driver)
    Order_page.Add_PT_Order()
    capture_screenshot(driver, "test_Add_PT_Order", 62)


@pytest.mark.run(order=63)
@pytest.mark.sanity
def test_open_Add_Order_Screen_for_SNF(setup):
    driver = setup
    Order_page = OrderPage(driver)
    Order_page.open_Add_Order_Screen_for_SNF()
    capture_screenshot(driver, "test_open_Add_Order_Screen_for_SNF", 63)


@pytest.mark.run(order=64)
@pytest.mark.sanity
def test_Add_SNF_Order(setup):
    driver = setup
    Order_page = OrderPage(driver)
    Order_page.Add_SNF_Order()
    time.sleep(5)
    capture_screenshot(driver, "test_Add_SNF_Order", 64)


'''
@pytest.mark.run(order=65)
@pytest.mark.sanity
def test_order_search_Order(setup):
    driver = setup
    Order_page = OrderPage(driver)
    Order_page.order_search_Order()
    time.sleep(5)
    capture_screenshot(driver, "test_order_search_Order", 65)


@pytest.mark.run(order=66)
@pytest.mark.sanity
def test_Verify_Description_Field_on_Right_Panel(setup):
    driver = setup
    Order_page = OrderPage(driver)
    Order_page.Verify_Description_Field_on_Right_Panel()
    capture_screenshot(driver, "test_Verify_Description_Field_on_Right_Panel", 66)


@pytest.mark.run(order=67)
@pytest.mark.sanity
def test_Verify_utilization_type_on_Right_Panel(setup):
    driver = setup
    Order_page = OrderPage(driver)
    Order_page.Verify_utilization_type_on_Right_Panel()
    capture_screenshot(driver, "test_Verify_utilization_type_on_Right_Panel", 67)


@pytest.mark.run(order=68)
@pytest.mark.sanity
def test_Verify_Orders_Facility_Field_on_Right_Panel(setup):
    driver = setup
    Order_page = OrderPage(driver)
    Order_page.Verify_Orders_Facility_Field_on_Right_Panel()
    capture_screenshot(driver, "test_Verify_Orders_Facility_Field_on_Right_Panel", 68)


@pytest.mark.run(order=69)
@pytest.mark.sanity
def test_Verify_Fees_Field_On_Orders_Right_Panel(setup):
    driver = setup
    Order_page = OrderPage(driver)
    Order_page.Verify_Fees_Field_On_Orders_Right_Panel()
    time.sleep(5)
    capture_screenshot(driver, "test_Verify_Fees_Field_On_Orders_Right_Panel", 69)

'''
