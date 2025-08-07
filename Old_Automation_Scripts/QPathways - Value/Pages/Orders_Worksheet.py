import time
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Qprime_Locators
import random
from datetime import datetime, timedelta

locators = Qprime_Locators.Orders_Worksheet_Locators


class OrdersWorksheetPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Open_Orders_Worksheet(self):
        Orders_Tab = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orders_Tab)))
        Orders_Tab.click()
        WorkSheet_button = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Worksheet_Button)))
        WorkSheet_button.click()

    def Open_Filters_Screen(self):
        Filter_button = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Filter_button)))
        Filter_button.click()
        time.sleep(3)

    # --------------------------------------------------Orders Filter------------------------------------------------------------------#
    def Filter_by_Facility(self, Facility_name, max_pages=2):
        Facility_Box = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Facility_text_Box)))
        Facility_Box.click()
        time.sleep(2)
        Facility_Box.send_keys(Facility_name)
        Facility_Box.send_keys(Keys.ENTER)

        Apply_Button = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Apply_Button)))
        Apply_Button.click()
        time.sleep(3)

        page = 1
        while page <= max_pages:
            print(f"Checking page {page} for status '{Facility_name}'")
            row_index = 1
            while True:
                try:
                    xpath = f"(//td[@data-kendo-grid-column-index='2'])[{row_index}]"
                    element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                    element_text = element.text
                    print(f"Row {row_index} on page {page}: {element_text}")
                    assert element_text == Facility_name, f"Row {row_index} does not contain '{Facility_name}'. Found: {element_text}"
                    row_index += 1
                except TimeoutException:
                    break

            try:
                next_button = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//span[contains(@aria-label,'Go to the next page')]")))
                next_button.click()
                time.sleep(1)
                page += 1
            except TimeoutException:
                break

            if page > max_pages:
                break

    def Facility_filter(self):
        self.Filter_by_Facility("ACTIVE PHYSICAL THERAPY PLC")

    # --------------------------------------------------Orders Filter------------------------------------------------------------------#
    def Filter_by_Provider(self, Provider_name, max_pages=2):
        Provider_Box = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Provider_Textbox)))
        Provider_Box.click()
        time.sleep(2)
        Provider_Box.send_keys(Provider_name)
        Provider_Box.send_keys(Keys.ENTER)

        Apply_Button = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Apply_Button)))
        Apply_Button.click()
        time.sleep(3)

        errors = []

        page = 1
        while page <= max_pages:
            print(f"Checking page {page} for provider '{Provider_name}'")
            row_index = 1
            while True:
                try:
                    xpath = f"(//td[@data-kendo-grid-column-index='3'])[{row_index}]"
                    element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                    element_text = element.text
                    print(f"Row {row_index} on page {page}: {element_text}")
                    if element_text != Provider_name:
                        errors.append(f"Row {row_index} on page {page}: expected '{Provider_name}', but found '{element_text}'")
                    row_index += 1
                except TimeoutException:
                    break

            try:
                next_button = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//span[contains(@aria-label,'Go to the next page')]")))
                next_button.click()
                time.sleep(1)
                page += 1
            except TimeoutException:
                break

        if errors:
            raise AssertionError("\n".join(errors))

    def Provider_filter(self):
        self.Open_Filters_Screen()
        self.Filter_by_Provider("YOGITA PATIL")
