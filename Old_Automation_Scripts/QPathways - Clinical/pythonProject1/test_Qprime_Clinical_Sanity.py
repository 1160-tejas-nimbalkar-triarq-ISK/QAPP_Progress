import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#
class Locators:
    USERNAME_FIELD = "//input[@name='username']"
    PASSWORD_FIELD = "//input[@type='password']"
    LOGIN_BUTTON = "//ion-button[contains(.,'Login')]"
    CALENDAR_TAB = "//ion-label[contains(.,'calendar')]"
    APPOINTMENT_9_O_CLOCK = "(//div[@class='line-15'])[1]"
    PATIENT_NAME_XPATH = "//ion-text[@class='ion-text-wrap custom18 demographic-patient-name capitalize ion-color ion-color-black md hydrated']//span[@class='custom18-bold'][normalize-space()='philip,']"

@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_open_url(driver):
    url = "https://qprime-qa.myqone.com"
    driver.get(url)
    driver.maximize_window()

def test_login_qpathways(driver):
    driver.find_element(By.XPATH, Locators.USERNAME_FIELD).send_keys("somraj.navale@triarqhealth.com")
    time.sleep(5)
    driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys("P@ssword1")
    time.sleep(5)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
    time.sleep(30)

def test_open_calendar(driver):
    driver.find_element(By.XPATH, Locators.CALENDAR_TAB).click()
    time.sleep(8)

def test_click_on_9_clock_appointment(driver):
    driver.find_element(By.XPATH, Locators.APPOINTMENT_9_O_CLOCK).click()
    time.sleep(8)

def test_print_patient_name_from_excel():
    file_path = r"C:\Users\SomrajNavale\Desktop\Testdata1.xlsx"
    df = pd.read_excel(file_path)

    # Extract patient name from the Excel file
    global patient_name_from_excel
    patient_name_from_excel = df.iloc[0, 1]
    
    print("Patient Name (Excel):", patient_name_from_excel)

def test_compare_patient_name(driver):
    # Retrieve patient name from the web
    patient_name_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, Locators.PATIENT_NAME_XPATH))
    )
    patient_first_name = patient_name_element.text

    # Compare with Excel data
    assert patient_first_name == patient_name_from_excel, f"Patient name mismatch! Expected: {patient_name_from_excel}, Got: {patient_first_name}"
    print(f"Patient name matches: {patient_first_name}")
