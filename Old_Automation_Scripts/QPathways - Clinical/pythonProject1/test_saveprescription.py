import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


class Patient_data:
    excel_file_path = r'C:\Users\somraj.nawale\Qprime_Sanity_QF30_Automation\pythonProject1\Qpathways_Clinical_Data_Excel.xlsx'
    df = pd.read_excel(excel_file_path)

    for i in range(1, len(df)):
        patient_name = df.iloc[i, 0]
        drugs1 = df.iloc[i, 1]
        supply_days = df.iloc[i, 2]
        supply_refills = df.iloc[i, 3]
        # Print or use the variables as needed
        print(f"Row {i}:")
        print(f"  Patient Name: {patient_name}")
        print(f"  Drugs1: {drugs1}")
        print(f"  Supply Days: {supply_days}")
        print(f"  Supply Refills: {supply_refills}")


class locators:
    Patient_Tab = "//ion-tab-button[contains(.,'Patients')]"
    Patient_Search = "//input[@name='ion-searchbar-3']"
    Patient1_Index = "/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-patients/div/app-patient-queue/div/ion-list/ngx-simplebar/div[1]/div[2]/div/div/div/div/div/div/div/ion-item[1]/div/div[1]/ion-text"
    Medication_Plus_Button = "//ion-button[contains(@class,'small-ic-btn mr-10 plus-btn-new ion-color ion-color-gray100 md button button-clear ion-activatable ion-focusable hydrated')]"
    Search_Drugs_box = "//input[@placeholder='Search all drugs...']"
    Drugs1_Path = "/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-patients/div/div/div/patient-content/patient-facesheet/div[8]/kendo-dialog/div[2]/div/add-rxmx/div/form/div[1]/div/drug-list/div/ion-list/div[2]/div/div/div/div/div/div[1]/ion-text"
    Supply_Days_Box = "/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-patients/div/div/div/patient-content/patient-facesheet/div[8]/kendo-dialog/div[2]/div/add-rxmx/div/form/div[1]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/div/div[2]/div[4]/div/div[1]/div[1]/kendo-formfield/div/kendo-textbox/input"
    Supply_Refills_Box = "/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-patients/div/div/div/patient-content/patient-facesheet/div[8]/kendo-dialog/div[2]/div/add-rxmx/div/form/div[1]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/div/div[2]/div[4]/div/div[3]/div[1]/kendo-formfield/div/kendo-textbox/input"
    Medication_1_index = "/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-patients/div/div/div/patient-content/patient-facesheet/ngx-simplebar/div[1]/div[2]/div/div/div/div/ion-card[5]/ion-list/div[1]/ion-item/div/div[1]/ion-text[1]"
    Save_Button = "//ion-text[contains(.,'save')]"
    User_Name_Field = "//input[@name='username']"
    Password_Field = "//input[@type='password']"
    Login_Button = "//ion-button[contains(.,'Login')]"
    Three_Dot_Button="//ion-icon[@id='medication-popover-trigger-0']"
    Edit_Button="//ion-text[@color='gray80'][contains(.,'Edit')]"
    Dispense_Line = "/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-patients/div/div/div/patient-content/patient-facesheet/div[4]/kendo-dialog/div[2]/div/patients-medication-details/div/div[2]/ion-list/div[3]/div/ion-text[2]"


@pytest.fixture(scope='session')
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_launch_url(setup):
    driver = setup
    driver.get("https://qprime-qa.myqone.com/")

####
def test_Login(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    user_name_field = wait.until(EC.presence_of_element_located((By.XPATH, locators.User_Name_Field)))
    user_name_field.send_keys("somraj.navale@triarqhealth.com")

    password_field = driver.find_element(By.XPATH, locators.Password_Field)
    password_field.send_keys("P@ssword1")

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Login_Button)))
    login_button.click()

    time.sleep(10)


def test_Open_Patient_List(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    patient_Tab = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Patient_Tab)))
    patient_Tab.click()
    time.sleep(5)


def test_Search_Patient(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    patient_search_box = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Patient_Search)))
    patient_search_box.click()
    patient_search_box.send_keys(Patient_data.patient_name)
    time.sleep(2)
    patient_search_box.send_keys(Keys.RETURN)
    time.sleep(2)


def test_click_Patient_index1(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    patient_index1 = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Patient1_Index)))
    patient_index1.click()
    time.sleep(2)


def test_click_Medication_Plus_Button(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    Medication_Plus_Button = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Medication_Plus_Button)))
    Medication_Plus_Button.click()
    time.sleep(5)


def test_Search_Drugs_In_SearchBox(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    Search_Drug_Box = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Search_Drugs_box)))
    Search_Drug_Box.click()
    time.sleep(3)
    Search_Drug_Box.send_keys(Patient_data.drugs1)
    time.sleep(4)
    Drugs_List_index1 = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Drugs1_Path)))
    time.sleep(3)
    Drugs_List_index1.click()
    time.sleep(3)


def test_Provide_Supply_Details(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    Supply_Days_Box = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Supply_Days_Box)))
    Supply_Days_Box.click()
    time.sleep(3)
    Supply_Days_Box.send_keys(Patient_data.supply_days)
    time.sleep(3)

    Supply_Refills_Box = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Supply_Refills_Box)))
    Supply_Refills_Box.click()
    time.sleep(2)
    Supply_Refills_Box.clear()
    time.sleep(2)
    Supply_Refills_Box.send_keys(Patient_data.supply_refills)
    time.sleep(5)


def test_save_refills(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    Save_Box = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Save_Button)))
    Save_Box.click()
    time.sleep(5)


def test_open_Latest_Medication(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    Latest_Medication = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Medication_1_index)))
    Latest_Medication.click()
    time.sleep(2)


def test_verify_compared_prescription(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    Dispense_Line = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Dispense_Line)))
    dispense_line_text = Dispense_Line.text

    expected_supply_days = f"{Patient_data.supply_days} Days"
    expected_supply_refills = f"{Patient_data.supply_refills} refills"

    print(expected_supply_refills)
    print(expected_supply_days)

    assert expected_supply_days in dispense_line_text, f"Expected supply days not found: {expected_supply_days}"
    assert expected_supply_refills in dispense_line_text, f"Expected supply refills not found: {expected_supply_refills}"

    time.sleep(5)


def test_verify_Updated_prescription(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    Dispense_Line = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Dispense_Line)))
    dispense_line_text = Dispense_Line.text

    expected_supply_days = f"{Patient_data.supply_days} Days"
    expected_supply_refills = f"{Patient_data.supply_refills} refills"

    print(expected_supply_refills)
    print(expected_supply_days)

    assert expected_supply_days in dispense_line_text, f"Expected supply days not found: {expected_supply_days}"
    assert expected_supply_refills in dispense_line_text, f"Expected supply refills not found: {expected_supply_refills}"

    time.sleep(5)


def test_verify_Open_Edit_prescription_Screen(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    Three_Dot_Button = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Three_Dot_Button)))
    Three_Dot_Button.click()
    Edit_Button = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Edit_Button)))
    Edit_Button.click()
    time.sleep(5)