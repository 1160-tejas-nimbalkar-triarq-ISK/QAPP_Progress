import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class locators:
    User_Name = "//input[@name='username']"
    Password = "//input[@name='password']"
    Login_Button = "//ion-button[contains(.,'Login')]"
    Calendar_Label = "//ion-label[contains(.,'calendar')]"
    Search_Provider_Box = "//input[@placeholder='Search Providers']"
    Provider_Label = "(//label[contains(.,'Wayne w Best')])[2]"
    Appointment_Label = "//ion-text[@color='gray100'][contains(.,'ZUKERBERG, Mark')]"
    Show_History_Button = "//ion-text[contains(.,'Show history')]"
    Checkout_Time = "/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-patients/div/div/div/patient-content/calendar-schedular/div[1]/div[3]/calendar-schedular-right-panel/div/div/patients-appointments-details/div/div/ion-list/div[1]/ion-card/div[3]/div[1]/div/div/ion-text[1]"
    Checkin_Time = "/html/body/app-root/ion-app/ion-router-outlet/app-main/div/app-patients/div/div/div/patient-content/calendar-schedular/div[1]/div[3]/calendar-schedular-right-panel/div/div/patients-appointments-details/div/div/ion-list/div[1]/ion-card/div[3]/div[3]/div/div/ion-text[1]"

    Patient_Tab = "//ion-tab-button[contains(.,'Patients')]"
    Patient_Reg_Icon = "//ion-button[@data-ion-popover-trigger='true']"
    New_Patient_Button = "//ion-text[@color='gray80'][contains(.,'New Patient')]"
    PGP_Dropdown_Arrow = "(//span[@class='k-button-icon k-icon k-i-caret-alt-down'])[9]"
    PGP_BOX = "(//input[@placeholder='*Physician Group'])[1]"
    FIRST_NAME_BOX = "//input[@placeholder='*First Name']"
    MIDDLE_NAME_BOX = "//input[@placeholder='Middle Name']"
    LAST_NAME_BOX = "//input[contains(@placeholder,'*Last Name')]"
    BIRTHDATE_FIELD = "//input[@id='datepicker-1']"
    GENDER_BOX = "//input[@placeholder='*Gender']"
    ADDRESS_FIELD = "//input[contains(@placeholder,'Address 1')]"
    ZIP_CODE_BOX = "//input[@placeholder='Zip']"
    MOBILE_NUMBER_FIELD = "(//input[contains(@type,'text')])[1]"
    HOME_NUMBER_FIELD = "(//input[contains(@type,'text')])[2]"
    EMAIL_BOX = "//input[contains(@placeholder,'Email')]"
    INSURANCE_ID_BOX = "//input[contains(@placeholder,'*ID')]"
    PHYSICIAN_DROPDOWN = "//input[@placeholder='*Physician']"
    Physician_Dropdown_Arrow = "//kendo-combobox[@placeholder='*Physician']//span[@class='k-button-icon k-icon k-i-caret-alt-down']"
    Insurance_Dropdown_Arrow = "//kendo-combobox[@placeholder='*Primary Insurance']//span[@class='k-button-icon k-icon k-i-caret-alt-down']"
    INSURANCE1_DROPDOWN = "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[13]"
    SAVE_INITIATE_EPISODE_BUTTON = "//ion-text[contains(.,'Save & initiate Episode')]"
    Save_Patient_button = "//ion-text[contains(.,'save & close')]"
    Plus_Button_Office = "//div[@class='mb-5'][1]"
    Plus_Button_Fax = "//body/modal-container[1]/div[2]/div[1]/patient-registration[1]/div[1]/kendo-dialog[1]/div[2]/div[1]/div[1]/episodic-patient-registration[1]/div[1]/div[1]/ngx-simplebar[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/ion-button[1]"
    Office_No_Option = "//ion-text[contains(.,'Office')]"
    Fax_Number_Option = "//ion-text[contains(.,'Fax')]"
    Office_Number_Box = "/html/body/modal-container/div[2]/div/patient-registration/div/kendo-dialog/div[2]/div/div/episodic-patient-registration/div/div/ngx-simplebar/div[1]/div[2]/div/div/div/div/form/div/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/kendo-formfield/div/kendo-maskedtextbox/input"
    Fax_No_Box = "/html/body/modal-container/div[2]/div/patient-registration/div/kendo-dialog/div[2]/div/div/episodic-patient-registration/div/div/ngx-simplebar/div[1]/div[2]/div/div/div/div/form/div/div[3]/div[2]/div[1]/div[4]/div/div[1]/kendo-formfield/div/kendo-maskedtextbox/input"
    Group_ID_Box = "//input[@placeholder=' Group ID']"
    Note_Box = "//textarea[@placeholder='Notes']"
    Exclude_Report_Box = "//input[@type='checkbox']"
    Pin_Icon = "(//ion-button[@fill='clear'])[5]"


@pytest.fixture(scope='session')
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_launch_url(setup):
    driver = setup
    driver.get("https://qprime-qa.myqone.com/")


def test_Login(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    user_name_field = wait.until(EC.presence_of_element_located((By.XPATH, locators.User_Name)))
    user_name_field.send_keys("rachana.chichghare@triarqhealth.com")

    password_field = driver.find_element(By.XPATH, locators.Password)
    password_field.send_keys("P@ssword1")

    login_button = driver.find_element(By.XPATH, locators.Login_Button)
    login_button.click()


def test_click_patients_tab(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    Patients_Tab = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Patient_Tab)))
    Patients_Tab.click()


def test_click_patient_registration_icon(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    Patient_Reg_icon = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Patient_Reg_Icon)))
    Patient_Reg_icon.click()


def test_open_new_patient_form(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    New_Patient_Button = wait.until(EC.element_to_be_clickable((By.XPATH, locators.New_Patient_Button)))
    New_Patient_Button.click()


'''
def select_PGP_dropdown(self):
        PGP_Box = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.PGP_BOX)))
        PGP_Box.click()
        PGP_Box.send_keys(Patient_data.PGP)

def enter_first_name(self):
        First_Name = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.FIRST_NAME_BOX)))
        First_Name.send_keys(Patient_data.first_name)
        assert isinstance(Patient_data.first_name, str), "First name should be a string."

def enter_middle_name(self):
        Middle_Name = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.MIDDLE_NAME_BOX)))
        Middle_Name.send_keys(Patient_data.middle_name)
        assert isinstance(Patient_data.middle_name, str), "Middle name should be a string."
def enter_last_name(self):
        Last_Name = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.LAST_NAME_BOX)))
        Last_Name.send_keys(Patient_data.last_name)
        assert isinstance(Patient_data.last_name, str), "Last name should be a string."

def enter_dob(self):
        DOB = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.BIRTHDATE_FIELD)))
        DOB.click()
        DOB.send_keys(Patient_data.dob)
        assert re.match(r'^\d{2}-\d{2}-\d{4}$', Patient_data.dob), "Invalid date format. Please use MM-DD-YYYY format."
def enter_gender(self):
        Gender = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.GENDER_BOX)))
        Gender.send_keys(Patient_data.gender)
        assert Patient_data.gender in ["Male", "Female"], "Invalid gender specified."

def enter_address(self):
        Address = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.ADDRESS_FIELD)))
        Address.send_keys(Patient_data.address)

def enter_zip(self):
        Zip = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.ZIP_CODE_BOX)))
        Zip.send_keys(Patient_data.zip_code)
        Zip.submit()  # Press Enter key after entering the ZIP code

def enter_Mobile_No(self):
        Mobile_No = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.MOBILE_NUMBER_FIELD)))
        Mobile_No.clear()
        Mobile_No.click()
        Mobile_No.send_keys(Patient_data.mobile_number)

def enter_home_no(self):
        Home_No = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.HOME_NUMBER_FIELD)))
        Home_No.clear()
        Home_No.click()
        Home_No.send_keys(Patient_data.Home_Number)

def see_office_number_option(self):
        Plus_Button = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Plus_Button_Office)))
        Plus_Button.click()

def enter_office_number(self):
        Office_No_Option = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Office_No_Option)))
        Office_No_Option.click()
        Office_No = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Office_Number_Box)))
        Office_No.clear()
        Office_No.click()
        Office_No.send_keys(Patient_data.office_number)

def see_fax_number_option(self):
        Plus_Button = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Plus_Button_Fax)))
        Plus_Button.click()

def enter_fax_number(self):
        Fax_No_Option = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Fax_Number_Option)))
        Fax_No_Option.click()
        Fax_No = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Fax_No_Box)))
        Fax_No.clear()
        Fax_No.click()
        Fax_No.send_keys(Patient_data.fax_number)

def enter_email(self):
        Email = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.EMAIL_BOX)))
        Email.send_keys(Patient_data.email)
        assert re.match(r'^[\w\.-]+@[\w\.-]+$', Patient_data.email), "Invalid email format."
        time.sleep(5)

def select_physician(self):
        dropdown_arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Physician_Dropdown_Arrow)))
        ActionChains(self.driver).move_to_element(dropdown_arrow).click(dropdown_arrow).perform()
        time.sleep(1)
        options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@role='option']")))
        total_options = len(options)
        print(f"Total options available: {total_options}")
        random_index = 1
        random_option = options[random_index - 1]
        random_option.click()

def select_insurance(self):
        dropdown_arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Insurance_Dropdown_Arrow)))
        ActionChains(self.driver).move_to_element(dropdown_arrow).click(dropdown_arrow).perform()
        time.sleep(1)
        options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@role='option']")))
        total_options = len(options)
        print(f"Total options available: {total_options}")
        random_index = 1
        random_option = options[random_index - 1]
        random_option.click()

def enter_Insurance_ID(self):
        Insurance_ID = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.INSURANCE_ID_BOX)))
        Insurance_ID.send_keys(Patient_data.insurance_id)
        assert re.match(r'^[A-Za-z0-9]+$', Patient_data.insurance_id), "Insurance ID should be alphanumeric."

def enter_Group_ID(self):
        Group_ID = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Group_ID_Box)))
        Group_ID.send_keys(Patient_data.Group_id)
        assert re.match(r'^[A-Za-z0-9]+$', Patient_data.Group_id), "Group ID should be alphanumeric."

def enter_Patient_Note(self):
        Patient_Note = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Note_Box)))
        Patient_Note.send_keys(Patient_data.Patient_Note)

def check_exclude_Report_ceckbox(self):
        Exclude_patient_Checkbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Exclude_Report_Box)))
        Exclude_patient_Checkbox.click()
def see_save_button(self):
        Save_and_Close_Button = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Save_Patient_button)))
        assert Save_and_Close_Button.is_enabled()

'''


def test_Open_Calender_Tab(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    calendar_label = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Calendar_Label)))
    calendar_label.click()


def test_Select_Provider(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    search_provider_box = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Search_Provider_Box)))
    search_provider_box.click()

    provider_label = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Provider_Label)))
    provider_label.click()


def test_click_on_appointment(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    appointment_label = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Appointment_Label)))
    appointment_label.click()


def test_Click_On_Show_History_Button(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    show_history_button = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Show_History_Button)))
    show_history_button.click()


def test_Checkin_Checkout_Time(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)
    checkout_time_element = wait.until(EC.presence_of_element_located((By.XPATH, locators.Checkout_Time)))
    checkin_time_element = wait.until(EC.presence_of_element_located((By.XPATH, locators.Checkin_Time)))

    checkout_time = checkout_time_element.text
    checkin_time = checkin_time_element.text

    # Define the expected times
    expected_checkout_time = "11:18 PM"
    expected_checkin_time = "11:10 PM"

    # Assert the values
    assert checkout_time == expected_checkout_time, f"Expected checkout time to be {expected_checkout_time}, but got {checkout_time}"
    assert checkin_time == expected_checkin_time, f"Expected check-in time to be {expected_checkin_time}, but got {checkin_time}"

    # Print success message if assertions pass
    print("Both checkout and check-in times are as expected.")