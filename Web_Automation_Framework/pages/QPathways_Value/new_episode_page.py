from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from test_data.episode_data_generator import Episode_data
import time
import random

class NewEpisodePage:
    """Page Object Model for New Episode Creation in QPathways Value"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Locators
    EPISODE_TYPE_INPUT = "//input[@placeholder='*Episode Type']"
    DESCRIPTION_BOX = "//input[@placeholder='Description (e.g. Right Knee Surgery)']"
    PGP_Box = "/html/body/modal-container/div[2]/div/episode-add-new-episode-popup/div/kendo-dialog/div[2]/div/div/ion-list/form/div/div[1]/div[1]/kendo-formfield[1]/div"
    
    Physician_Arrow = "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[11]"
    Program_Arrow = "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[12]"
    Surgical_Facility_Arrow = "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[13]"

    Surgery_Date_Box = "//input[@placeholder='*Surgery Date']"
    Type_Arrow = "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[14]"

    Join_Selection = "//ion-text[contains(.,'Hip') or contains(.,'Knee') or contains(.,'Ankle') or contains(.,'Shoulder')]"
    Diagnosis_Code_Arrow = "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[15]"
    Procedure_Code_Arrow = "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[16]"

    Height_Box = "//input[@placeholder='in']"
    Weight_BOx = "//input[@placeholder='lbs']"

    Save_Buttton = "//ion-text[@class='body2-txt md hydrated'][contains(.,'Save')]"

    Episode_Manager_Box = "//ion-text[contains(.,'Episode Manager')]"
    Episode_Manager_Arrow = "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[9]"

    Risk_Button = "//ion-text[contains(.,'Risk')]"
    Select_Risk = "//ion-text[@color='gray100'][contains(.,'Low') or contains(.,'Medium') or contains(.,'High')]"

    Note_BUtton = "//ion-text[contains(.,'+ Note')]"
    Note_Box = "//input[@placeholder='Add a note']"
    Tick_Button = "//ion-button[@ng-reflect-disabled='false']"

    Care_Plan_Button = "//ion-text[contains(.,'+ Care Plan')]"
    care_Plan_Index = "(//input[contains(@type,'checkbox')])[1]"
    NExt_Button_Care_Plan = "//ion-button[contains(.,'Next')]"
    Save_Button = "//ion-text[@class='body2-txt md hydrated'][contains(.,'Save')]"
    Initiate_Buitton = "//ion-text[contains(.,'Initiate')]"

    Episode_Tab = "//ion-tab-button[contains(.,'Episode')]"
    
    # Helper Locators
    DROPDOWN_OPTIONS = "//li[@role='option']"

    def enter_episode_description(self):
        """Enter episode description"""
        try:
            description_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.DESCRIPTION_BOX)))
            description_box.click()
            time.sleep(1)
            description_box.clear()
            description_box.send_keys(Episode_data.Description)
            time.sleep(2)
            print(f"✓ Entered episode description: {Episode_data.Description}")
        except Exception as e:
            print(f"✗ Error entering episode description: {str(e)}")
            raise Exception("Failed to enter episode description")

    def select_physician(self):
        """Select physician from dropdown"""
        try:
            arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Physician_Arrow)))
            arrow.click()
            time.sleep(2)
            
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.DROPDOWN_OPTIONS)))
            options = self.driver.find_elements(By.XPATH, self.DROPDOWN_OPTIONS)
            
            if not options:
                raise Exception("No Physician options found in dropdown")
                
            selected_option = random.choice(options)
            selected_option.click()
            time.sleep(2)
            print("✓ Selected physician from dropdown successfully")
            
        except Exception as e:
            print(f"✗ Error selecting physician: {str(e)}")
            raise Exception("Failed to select physician")

    def select_program(self):
        """Select program from dropdown"""
        try:
            arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Program_Arrow)))
            arrow.click()
            time.sleep(2)
            
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.DROPDOWN_OPTIONS)))
            options = self.driver.find_elements(By.XPATH, self.DROPDOWN_OPTIONS)
            
            if not options:
                raise Exception("No Program options found in dropdown")
                
            selected_option = random.choice(options)
            selected_option.click()
            time.sleep(1)
            print("✓ Selected program from dropdown successfully")
            
        except Exception as e:
            print(f"✗ Error selecting program: {str(e)}")
            raise Exception("Failed to select program")

    def select_surgical_facility(self):
        """Select surgical facility from dropdown"""
        try:
            arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Surgical_Facility_Arrow)))
            arrow.click()
            time.sleep(2)
            
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.DROPDOWN_OPTIONS)))
            options = self.driver.find_elements(By.XPATH, self.DROPDOWN_OPTIONS)
            
            if not options:
                raise Exception("No Surgical Facility options found in dropdown")
                
            selected_option = random.choice(options)
            selected_option.click()
            time.sleep(1)
            print("✓ Selected surgical facility from dropdown successfully")
            
        except Exception as e:
            print(f"✗ Error selecting surgical facility: {str(e)}")
            raise Exception("Failed to select surgical facility")

    def enter_surgery_date(self):
        """Enter surgery date"""
        try:
            surgery_date_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Surgery_Date_Box)))
            surgery_date_box.click()
            time.sleep(1)
            # Clear any existing content first
            surgery_date_box.send_keys(Keys.CONTROL + "a")
            time.sleep(1)
            surgery_date_box.send_keys(Keys.DELETE)
            time.sleep(1)
            surgery_date_box.send_keys(Episode_data.Surgery_Date)
            time.sleep(1)
            print(f"✓ Entered surgery date: {Episode_data.Surgery_Date}")
        except Exception as e:
            print(f"✗ Error entering surgery date: {str(e)}")
            raise Exception("Failed to enter surgery date")

    def select_type(self):
        """Select type from dropdown"""
        try:
            type_arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Type_Arrow)))
            type_arrow.click()
            time.sleep(2)
            
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.DROPDOWN_OPTIONS)))
            options = self.driver.find_elements(By.XPATH, self.DROPDOWN_OPTIONS)
            
            if not options:
                raise Exception("No Type options found in dropdown")
                
            selected_option = random.choice(options)
            selected_option.click()
            time.sleep(1)
            print("✓ Selected type from dropdown successfully")
            
        except Exception as e:
            print(f"✗ Error selecting type: {str(e)}")
            raise Exception("Failed to select type")

    def select_joint_selection(self):
        """Select joint selection"""
        try:
            join_selection = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Join_Selection)))
            join_selection.click()
            time.sleep(1)
            print("✓ Selected joint successfully")
        except Exception as e:
            print(f"✗ Error selecting joint: {str(e)}")
            raise Exception("Failed to select joint")

    def select_diagnosis_code(self):
        """Select diagnosis code from dropdown"""
        try:
            arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Diagnosis_Code_Arrow)))
            arrow.click()
            time.sleep(2)
            
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.DROPDOWN_OPTIONS)))
            options = self.driver.find_elements(By.XPATH, self.DROPDOWN_OPTIONS)
            
            if not options:
                raise Exception("No Diagnosis Code options found in dropdown")
                
            selected_option = random.choice(options)
            selected_option.click()
            time.sleep(1)
            print("✓ Selected diagnosis code from dropdown successfully")
            
        except Exception as e:
            print(f"✗ Error selecting diagnosis code: {str(e)}")
            raise Exception("Failed to select diagnosis code")

    def select_procedure_code(self):
        """Select procedure code from dropdown"""
        try:
            arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Procedure_Code_Arrow)))
            arrow.click()
            time.sleep(2)
            
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.DROPDOWN_OPTIONS)))
            options = self.driver.find_elements(By.XPATH, self.DROPDOWN_OPTIONS)
            
            if not options:
                raise Exception("No Procedure Code options found in dropdown")
                
            selected_option = random.choice(options)
            selected_option.click()
            time.sleep(1)
            print("✓ Selected procedure code from dropdown successfully")
            
        except Exception as e:
            print(f"✗ Error selecting procedure code: {str(e)}")
            raise Exception("Failed to select procedure code")

    def enter_height(self):
        """Enter patient height"""
        try:
            height_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Height_Box)))
            height_box.click()
            time.sleep(1)
            height_box.clear()
            height_box.send_keys(Episode_data.Height)
            time.sleep(1)
            print(f"✓ Entered height: {Episode_data.Height} inches")
        except Exception as e:
            print(f"✗ Error entering height: {str(e)}")
            raise Exception("Failed to enter height")

    def enter_weight(self):
        """Enter patient weight"""
        try:
            weight_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Weight_BOx)))
            weight_box.click()
            time.sleep(1)
            weight_box.clear()
            weight_box.send_keys(Episode_data.Weight)
            time.sleep(1)
            print(f"✓ Entered weight: {Episode_data.Weight} lbs")
        except Exception as e:
            print(f"✗ Error entering weight: {str(e)}")
            raise Exception("Failed to enter weight")

    def click_save_button(self):
        """Click save button"""
        try:
            button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Save_Buttton)))
            button.click()
            time.sleep(5)
            print("✓ Clicked save button successfully")
        except Exception as e:
            print(f"✗ Error clicking save button: {str(e)}")
            raise Exception("Failed to click save button")

    def click_risk_button(self):
        """Click risk button and select risk level"""
        try:
            risk_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Risk_Button)))
            risk_button.click()
            time.sleep(1)
            select_risk = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Select_Risk)))
            select_risk.click()
            time.sleep(1)
            print("✓ Selected risk level successfully")
        except Exception as e:
            print(f"✗ Error selecting risk: {str(e)}")
            raise Exception("Failed to select risk")

    def click_note_button(self):
        """Click note button and add note"""
        try:
            note_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Note_BUtton)))
            note_button.click()
            time.sleep(1)
            note_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Note_Box)))
            note_box.click()
            time.sleep(1)
            note_box.send_keys(Episode_data.Note)
            time.sleep(1)
            print(f"✓ Added note: {Episode_data.Note}")
            
            # Click the tick button to confirm the note
            tick_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Tick_Button)))
            tick_button.click()
            time.sleep(1)
            print("✓ Clicked tick button to confirm note")
        except Exception as e:
            print(f"✗ Error adding note: {str(e)}")
            raise Exception("Failed to add note")

    def select_episode_manager(self):
        """Select episode manager (optional)"""
        try:
            episode_manager_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Episode_Manager_Box)))
            episode_manager_box.click()
            print("✓ Clicked on Episode Manager box.")
            time.sleep(1)
            episode_manager_arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Episode_Manager_Arrow)))
            episode_manager_arrow.click()
            time.sleep(1)
            
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.DROPDOWN_OPTIONS)))
            options = self.driver.find_elements(By.XPATH, self.DROPDOWN_OPTIONS)
            random.choice(options).click()
            print("✓ Selected an Episode Manager.")
            time.sleep(5)
        except TimeoutException:
            print("⚠ Episode Manager is patched by default. Skipping Episode Manager selection.")
        except Exception as e:
            print(f"⚠ Warning: Episode Manager selection failed: {str(e)}")

    def click_care_plan_button(self):
        """Click care plan button"""
        try:
            care_plan_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Care_Plan_Button)))
            care_plan_button.click()
            time.sleep(1)
            print("✓ Clicked care plan button successfully")
        except Exception as e:
            print(f"✗ Error clicking care plan button: {str(e)}")
            raise Exception("Failed to click care plan button")

    def select_care_plan_index(self):
        """Select care plan index"""
        try:
            care_plan_index = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.care_Plan_Index)))
            care_plan_index.click()
            time.sleep(1)
            print("✓ Selected care plan index successfully")
        except Exception as e:
            print(f"✗ Error selecting care plan index: {str(e)}")
            raise Exception("Failed to select care plan index")

    def click_next_button_care_plan(self):
        """Click next button in care plan"""
        try:
            next_button_care_plan = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.NExt_Button_Care_Plan)))
            next_button_care_plan.click()
            time.sleep(1)
            print("✓ Clicked next button in care plan successfully")
        except Exception as e:
            print(f"✗ Error clicking next button: {str(e)}")
            raise Exception("Failed to click next button")

    def click_save_button_care_plan(self):
        """Click save button in care plan"""
        try:
            save_button_care_plan = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Save_Button)))
            save_button_care_plan.click()
            time.sleep(1)
            print("✓ Clicked save button in care plan successfully")
        except Exception as e:
            print(f"✗ Error clicking save button in care plan: {str(e)}")
            raise Exception("Failed to click save button in care plan")

    def click_initiate_button(self):
        """Click initiate button to complete episode creation"""
        try:
            initiate_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Initiate_Buitton)))
            initiate_button.click()
            time.sleep(1)
            print("✓ Clicked initiate button successfully - Episode created!")
        except Exception as e:
            print(f"✗ Error clicking initiate button: {str(e)}")
            raise Exception("Failed to click initiate button")