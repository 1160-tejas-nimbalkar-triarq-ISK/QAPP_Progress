import time
import re
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Input_Excel.Patient_Details_Faker import Orders_Data
from Locators import Qprime_Locators
from Pages import Orders_Worksheet

locators = Qprime_Locators.Order_Locators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_Episode_tab(self):
        Episode_Tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Episodes_Tab)))
        Episode_Tab.click()

    def Apply_Planed_Filter(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Status_Filter))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Planed_Filter))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Apply_Button))).click()

    def select_First_index(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Searched_Episode_Index))).click()

    def click_On_Plus_Button(self):
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "k-i-loading")))
        plus_button_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locators.Plus_Button_Order)))
        self.driver.execute_script("arguments[0].scrollIntoView();", plus_button_element)
        plus_button_element.click()

    def open_Add_Order_Screen_for_HHA(self):
        HHA = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Home_Health_Tab)))
        HHA.click()

    def Add_HHA_Order(self):
        Description = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Description_Box)))
        Description.send_keys(Orders_Data.HHA_Order_Description)
        Facility_Dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Facility_Dropdown)))
        Facility_Dropdown.click()
        Facility_Dropdown.send_keys(Orders_Data.Orders_Facility)
        Facility_Dropdown.send_keys(Keys.RETURN)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Range_Field))).send_keys(Orders_Data.Range)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Weeks_Field))).send_keys(Orders_Data.Weeks)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Add_range_buttton))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Fees_Field))).send_keys("10")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Save_Order_Button))).click()

    def open_Add_Order_Screen_for_PT(self):
        self.click_On_Plus_Button()
        PT_Option = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.PT_Options)))
        PT_Option.click()

    def Add_PT_Order(self):
        Description = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Description_Box)))
        Description.send_keys(Orders_Data.PT_Order_Description)
        Facility_Dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Facility_Dropdown)))
        Facility_Dropdown.click()
        Facility_Dropdown.send_keys(Orders_Data.Orders_Facility)
        Facility_Dropdown.send_keys(Keys.RETURN)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Range_Field))).send_keys(Orders_Data.Range)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Weeks_Field))).send_keys(Orders_Data.Weeks)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Add_range_buttton))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Fees_Field))).send_keys("10")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Save_Order_Button))).click()

    def open_Add_Order_Screen_for_SNF(self):
        self.click_On_Plus_Button()
        SNF_Option = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.SNF_Option)))
        SNF_Option.click()

    def Add_SNF_Order(self):
        time.sleep(5)
        Description = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Description_Box)))
        Description.send_keys(Orders_Data.SNF_Order_Description)
        Facility_Dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Facility_Dropdown)))
        Facility_Dropdown.click()
        Facility_Dropdown.send_keys(Orders_Data.Orders_Facility)
        Facility_Dropdown.send_keys(Keys.RETURN)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.SNF_Fees_Field))).send_keys("10")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Days_Field_SNF))).send_keys(Orders_Data.Range)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Save_Order_Button))).click()






