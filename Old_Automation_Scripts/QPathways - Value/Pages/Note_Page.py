# Pages/Patient_Page.py
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Input_Excel.Patient_Details_Faker import Notes_Data,Patient_data
from Locators import Qprime_Locators

locators = Qprime_Locators.Notes_Locators


class NotesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_on_Notes_plus_button(self):
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "k-i-loading")))
        Notes_plus_button_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, locators.Notes_Plus_Button)))
        Notes_plus_button_element.click()

    def Add_Normal_Notes(self):
        Category_Dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Notes_Category_Dropdown)))
        Category_Dropdown.click()
        Category_Dropdown.send_keys(Notes_Data.category)
        Category_Dropdown.send_keys(Keys.RETURN)
        Enter_Note_Box = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Enter_Note_Box)))
        Enter_Note_Box.click()
        Enter_Note_Box.send_keys(Notes_Data.Note)
        Save_Button = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Save_Button)))
        Save_Button.click()

    def Open_Newly_Added_Notes_On_EV(self):
        Notes_Card_Index1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Notes_Card_Index_1)))
        Notes_Card_Index1.click()

    def Verify_Date_On_Right_Panel(self):
        Date_On_Right_Panel = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Date_On_Right_Panel)))
        Date_Right_Panel=Date_On_Right_Panel.text
        print(Date_Right_Panel)
        Today_Date = Patient_data.todays_date
        print(Today_Date)
        print(Date_On_Right_Panel)


