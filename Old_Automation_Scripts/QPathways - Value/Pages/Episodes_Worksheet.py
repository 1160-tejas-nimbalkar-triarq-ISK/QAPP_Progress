import time
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Qprime_Locators
import random
from datetime import datetime, timedelta

locators = Qprime_Locators.Episodes_Worksheet_Locators


class EpisodesWorksheetPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Open_Episodes_Worksheet(self):
        Episodes_Tab = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Episodes_Tab)))
        Episodes_Tab.click()
        WorkSheet_button = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Worksheet_Button)))
        WorkSheet_button.click()

    def Open_Filters_Screen(self):
        Filter_button = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Filter_button)))
        Filter_button.click()
        time.sleep(3)

    # --------------------------------------------------Status Filter------------------------------------------------------------------#
    def Filter_by_Status(self, status_name, max_pages=1):
        Reset_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//ion-text[contains(.,'Reset')]")))
        Reset_button.click()

        Status_Arrow = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[10]")))
        Status_Arrow.click()
        time.sleep(1)
        Status_Element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, f"//li[contains(.,'{status_name}')]")))
        Status_Element.click()
        Apply_Button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//ion-text[@class='body2-txt md hydrated'][contains(.,'Apply')]")))
        Apply_Button.click()
        time.sleep(2)

        page = 1
        while page <= max_pages:
            print(f"Checking page {page} for status '{status_name}'")
            row_index = 1
            while True:
                try:

                    xpath = f"(//td[@data-kendo-grid-column-index='8'])[{row_index}]"
                    element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                    element_text = element.text
                    print(f"Row {row_index} on page {page}: {element_text}")
                    assert element_text == status_name, f"Row {row_index} does not contain '{status_name}'. Found: {element_text}"
                    row_index += 1
                except TimeoutException:

                    break

            try:
                next_button = self.wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//span[contains(@aria-label,'Go to the next page')]")))
                next_button.click()
                time.sleep(2)
                page += 1
            except TimeoutException:

                break
            if page > max_pages:
                break

    def ActiveStatus_Filter(self):

        self.Filter_by_Status("Active")

    def Finished_Status_Filter(self):
        self.Open_Filters_Screen()
        self.Filter_by_Status("Finished")

    def New_Status_Filter(self):
        self.Open_Filters_Screen()
        self.Filter_by_Status("New")

    # --------------------------------------------------Physician Filter------------------------------------------------------------------#
    def Filter_by_Physician(self, physician_name, max_pages=1):
        Reset_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//ion-text[contains(.,'Reset')]")))
        Reset_button.click()
        Physician_Arrow = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[11]")))
        Physician_Arrow.click()
        time.sleep(2)
        physician_Element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, f"//li[contains(.,'{physician_name}')]")))
        physician_Element.click()
        Apply_Button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//ion-text[@class='body2-txt md hydrated'][contains(.,'Apply')]")))
        Apply_Button.click()
        time.sleep(5)

        page = 1
        while page <= max_pages:
            print(f"Checking page {page} for status '{physician_name}'")
            row_index = 1
            while True:
                try:

                    xpath = f"(//td[@data-kendo-grid-column-index='3'])[{row_index}]"
                    element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                    element_text = element.text
                    print(f"Row {row_index} on page {page}: {element_text}")
                    assert element_text == physician_name, f"Row {row_index} does not contain '{physician_name}'. Found: {element_text}"
                    row_index += 1
                except TimeoutException:

                    break

            try:
                next_button = self.wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//span[contains(@aria-label,'Go to the next page')]")))
                next_button.click()
                time.sleep(1)
                page += 1
            except TimeoutException:

                break
            if page > max_pages:
                break

    def physician_filter(self):
        self.Open_Filters_Screen()
        self.Filter_by_Physician("Tejas Nimbalkar")

    # --------------------------------------------------PGP Filter------------------------------------------------------------------#
    def Filter_by_PGP(self, PGP_name, max_pages=1):
        Reset_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//ion-text[contains(.,'Reset')]")))
        Reset_button.click()
        Physician_Arrow = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[12]")))
        Physician_Arrow.click()
        time.sleep(2)
        physician_Element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, f"//li[contains(.,'{PGP_name}')]")))
        physician_Element.click()
        Apply_Button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//ion-text[@class='body2-txt md hydrated'][contains(.,'Apply')]")))
        Apply_Button.click()
        time.sleep(5)

        page = 1
        while page <= max_pages:
            print(f"Checking page {page} for status '{PGP_name}'")
            row_index = 1
            while True:
                try:

                    xpath = f"(//td[@data-kendo-grid-column-index='4'])[{row_index}]"
                    element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                    element_text = element.text
                    print(f"Row {row_index} on page {page}: {element_text}")
                    assert element_text == PGP_name, f"Row {row_index} does not contain '{PGP_name}'. Found: {element_text}"
                    row_index += 1
                except TimeoutException:

                    break

            try:
                next_button = self.wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//span[contains(@aria-label,'Go to the next page')]")))
                next_button.click()
                time.sleep(1)
                page += 1
            except TimeoutException:

                break
            if page > max_pages:
                break

    def PGP_filter(self):
        self.Open_Filters_Screen()
        self.Filter_by_PGP("AWESOME THOUGHTS")

    # --------------------------------------------------Facility Filter------------------------------------------------------------------#

    def Filter_by_Facility(self, Facility_name, max_pages=1):
        Facility_Arrow = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[14]")))
        Facility_Arrow.click()
        time.sleep(2)
        Facility_Element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, f"//li[contains(.,'{Facility_name}')]")))
        Facility_Element.click()
        Apply_Button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//ion-text[@class='body2-txt md hydrated'][contains(.,'Apply')]")))
        Apply_Button.click()
        time.sleep(5)

        page = 1
        while page <= max_pages:
            print(f"Checking page {page} for status '{Facility_name}'")
            row_index = 1
            while True:
                try:
                    xpath = f"(//td[@data-kendo-grid-column-index='6'])[{row_index}]"
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
        self.Open_Filters_Screen()
        self.Filter_by_Facility("ACTIVE PHYSICAL THERAPY PLC")

    # --------------------------------------------------Date Range Filter------------------------------------------------------------------#
    def Filter_by_Date_Range(self, from_date, to_date, max_pages=2):
        from_date_box = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='From']")))
        from_date_box.click()
        from_date_box.send_keys(from_date)

        to_date_box = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='To']")))
        to_date_box.click()
        to_date_box.send_keys(to_date)

        apply_button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//ion-text[@class='body2-txt md hydrated'][contains(.,'Apply')]")))
        apply_button.click()
        time.sleep(5)

        page = 1
        while page <= max_pages:
            print(f"Checking page {page} for status")
            row_index = 1
            while True:
                try:
                    xpath = f"(//td[@ng-reflect-col-index='5'])[{row_index}]"
                    surgery_date_element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                    surgery_date = surgery_date_element.text
                    print(f"Row {row_index} on page {page}: {surgery_date}")
                    surgery_date_obj = datetime.strptime(surgery_date, '%d/%m/%Y')
                    assert from_date <= surgery_date_obj <= to_date, f"Surgery date {surgery_date} is not within the specified range."
                    row_index += 1
                except TimeoutException:

                    break

            try:
                next_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@aria-label,'Go to the next page')]")))
                next_button.click()
                time.sleep(1)
                page += 1
            except TimeoutException:

                break
            if page > max_pages:
                break

    def DateRange_filter(self):
        # Get the current date
        today = datetime.now()

        # Calculate the start date (2-3 months ago)
        start_date = today - timedelta(days=random.randint(60, 90))

        # Generate a random date between the start and end dates
        from_date = start_date + timedelta(seconds=int((today - start_date).total_seconds() * random.random()))
        from_date_str = from_date.strftime('%d/%m/%Y')

        # Generate a random date between the from_date and today
        to_date = from_date + timedelta(seconds=int((today - from_date).total_seconds() * random.random()))
        to_date_str = to_date.strftime('%d/%m/%Y')

        print(f"From date: {from_date_str}")
        print(f"To date: {to_date_str}")

        self.Open_Filters_Screen()
        self.Filter_by_Date_Range(from_date_str, to_date_str)

    def filter_by_facility_and_pgp(self, facility_name, pgp_name, max_pages=1):
        reset_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//ion-text[contains(.,'Reset')]")))
        reset_button.click()

        facility_arrow = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[14]")))
        facility_arrow.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, f"//li[contains(.,'{facility_name}')]"))).click()

        pgp_arrow = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[12]")))
        pgp_arrow.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, f"//li[contains(.,'{pgp_name}')]"))).click()

        apply_button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//ion-text[@class='body2-txt md hydrated'][contains(.,'Apply')]")))
        apply_button.click()

        page = 1
        while page <= max_pages:
            print(f"Checking page {page} for facility '{facility_name}' and PGP '{pgp_name}'")
            row_index = 1
            while True:
                try:
                    facility_xpath = f"(//td[@data-kendo-grid-column-index='6'])[{row_index}]"
                    facility_text = self.wait.until(EC.presence_of_element_located((By.XPATH, facility_xpath))).text
                    print(f"Row {row_index} on page {page} (Facility): {facility_text}")
                    assert facility_text == facility_name, f"Row {row_index} does not contain '{facility_name}'. Found: {facility_text}"

                    pgp_xpath = f"(//td[@data-kendo-grid-column-index='4'])[{row_index}]"
                    pgp_text = self.wait.until(EC.presence_of_element_located((By.XPATH, pgp_xpath))).text
                    print(f"Row {row_index} on page {page} (PGP): {pgp_text}")
                    assert pgp_text == pgp_name, f"Row {row_index} does not contain '{pgp_name}'. Found: {pgp_text}"

                    row_index += 1
                except TimeoutException:
                    break

            try:
                next_button = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//span[contains(@aria-label,'Go to the next page')]")))
                next_button.click()
                self.wait.until(EC.staleness_of(next_button))
                page += 1
            except TimeoutException:
                break

    def facility_and_pgp_filter(self):
        self.Open_Filters_Screen()
        self.filter_by_facility_and_pgp("ACTIVE PHYSICAL THERAPY PLC", "AWESOME THOUGHTS")
