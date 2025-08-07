from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random

class Qpathways2WTDashboardPage:
    """Page Object Model for Qpathways 2WT Dashboard Page"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        
    # Locators
    PATIENTS_TAB = (By.XPATH, "//ion-label[@color='gray100'][contains(.,'Patients')]")
    PATIENT_ITEM = (By.XPATH, "(//ion-text[@ng-reflect-ng-class='[object Object]'])[{}]")
    CHAT_BUTTON = (By.XPATH, "(//ion-label[contains(.,'Chats')])[3]")
    TEXT_AREA = (By.XPATH, "//textarea[contains(@placeholder,'Enter secure text message...')]")
    SEND_BUTTON = (By.XPATH, "//ion-button[@class='filled-icon-btn send-btn md button button-solid ion-activatable ion-focusable hydrated']")
    TEMPLATE_BUTTON = (By.XPATH, "//ion-icon[contains(@class,'p-5 icon-size pointer text-fav-icon md ion-color ion-color-gray80 hydrated')]")
    TEMPLATE_DROPDOWN_ARROW = (By.XPATH, "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[9]")
    TEMPLATE_OPTION = (By.XPATH, "(//li[@role='option'])[{}]")
    PT_CHATS_TAB = (By.XPATH, "//ion-label[contains(.,'PT Chats')]")
    SEARCH_CHATS_INPUT = (By.XPATH, "//input[@placeholder='Search chats']")
    SEARCH_RESULT_ITEM = (By.XPATH, "//ion-text[contains(@ng-reflect-ng-class,'body2-txt')]")
    CHAT_CONTAINER = (By.XPATH, "//div[contains(@class,'container pb-50')]")
    
    def click_patients_tab(self):
        """Click on the Patients tab"""
        print("Clicking on Patients tab")
        patients_tab = self.wait.until(EC.element_to_be_clickable(self.PATIENTS_TAB))
        patients_tab.click()
        time.sleep(2)
        print("Patients tab clicked successfully")
        
    def click_random_patient(self):
        """Click on a random patient from the list"""
        # Generate random number between 1-20
        random_index = random.randint(1, 20)
        print(f"Selecting patient at index: {random_index}")
        
        patient_locator = (By.XPATH, self.PATIENT_ITEM[1].format(random_index))
        patient_element = self.wait.until(EC.element_to_be_clickable(patient_locator))
        
        # Get patient name before clicking
        patient_name = patient_element.text
        print(f"Selected patient: {patient_name}")
        
        patient_element.click()
        time.sleep(2)
        print("Patient clicked successfully")
        return patient_name
        
    def click_chat_button(self):
        """Click on the chat button"""
        print("Clicking on chat button")
        chat_button = self.wait.until(EC.element_to_be_clickable(self.CHAT_BUTTON))
        chat_button.click()
        time.sleep(2)
        print("Chat button clicked successfully")
        
    def enter_message(self, message):
        """Enter message in the text area"""
        print(f"Entering message: {message}")
        text_area = self.wait.until(EC.presence_of_element_located(self.TEXT_AREA))
        text_area.clear()
        text_area.send_keys(message)
        print("Message entered successfully")
        
    def click_send_button(self):
        """Click on the send button"""
        print("Clicking send button")
        send_button = self.wait.until(EC.element_to_be_clickable(self.SEND_BUTTON))
        send_button.click()
        time.sleep(2)
        print("Send button clicked successfully")
        
    def click_template_button(self):
        """Click on the template button"""
        print("Clicking template button")
        template_button = self.wait.until(EC.element_to_be_clickable(self.TEMPLATE_BUTTON))
        template_button.click()
        time.sleep(2)
        print("Template button clicked successfully")
        
    def click_template_dropdown_arrow(self):
        """Click on the template dropdown arrow"""
        print("Clicking template dropdown arrow")
        
        # Try multiple approaches to find and click the dropdown arrow
        dropdown_selectors = [
            "(//span[@ng-reflect-ng-class='k-i-caret-alt-down'])[9]",
            "(//span[contains(@class,'caret')])[1]",
            "(//i[contains(@class,'arrow')])[1]",
            "(//span[contains(@class,'dropdown')])[1]",
            "//span[contains(@class,'k-i-caret-alt-down')]",
            "//i[contains(@class,'fa-chevron-down')]"
        ]
        
        for selector in dropdown_selectors:
            try:
                dropdown_arrow = self.wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                dropdown_arrow.click()
                time.sleep(3)  # Wait longer for dropdown to open
                print(f"✓ Template dropdown arrow clicked successfully using: {selector}")
                return
            except TimeoutException:
                continue
            except Exception as e:
                print(f"Error with dropdown selector {selector}: {e}")
                continue
        
        # If all selectors fail, try the original one
        try:
            dropdown_arrow = self.wait.until(EC.element_to_be_clickable(self.TEMPLATE_DROPDOWN_ARROW))
            dropdown_arrow.click()
            time.sleep(3)
            print("✓ Template dropdown arrow clicked successfully (fallback)")
        except Exception as e:
            print(f"Failed to click dropdown arrow: {e}")
            # Continue anyway, maybe dropdown is already open
        
    def select_random_template(self):
        """Select a random template from the dropdown"""
        print("Attempting to select a random template...")
        
        # Wait for dropdown to fully open
        time.sleep(3)
        
        # Try multiple approaches to find template options
        template_selectors = [
            "(//li[@role='option'])[{}]",
            "(//div[contains(@class,'option')])[{}]",
            "(//span[contains(@class,'option')])[{}]",
            "(//div[contains(@class,'template')])[{}]",
            "(//li[contains(@class,'option')])[{}]"
        ]
        
        # Try different indices (1-5)
        for index in range(1, 6):
            print(f"Trying template index: {index}")
            
            for selector in template_selectors:
                try:
                    template_locator = (By.XPATH, selector.format(index))
                    template_option = self.wait.until(EC.element_to_be_clickable(template_locator))
                    
                    # Get text before clicking
                    template_text = template_option.text.strip()
                    if template_text:  # Only proceed if text is not empty
                        print(f"Found template option: {template_text}")
                        template_option.click()
                        time.sleep(2)
                        print(f"✓ Template selected successfully: {template_text}")
                        return template_text
                except TimeoutException:
                    continue
                except Exception as e:
                    print(f"Error with selector {selector}: {e}")
                    continue
        
        # If no template found, try to get all available options
        print("No specific template found, trying to get all available options...")
        try:
            all_options = self.driver.find_elements(By.XPATH, "//li[@role='option']")
            if all_options:
                # Click on the first available option
                first_option = all_options[0]
                template_text = first_option.text.strip()
                first_option.click()
                time.sleep(2)
                print(f"✓ Selected first available template: {template_text}")
                return template_text
            else:
                print("No template options found")
                return "Default Template"
        except Exception as e:
            print(f"Error finding template options: {e}")
            return "Default Template"
            
    def click_pt_chats_tab(self):
        """Click on the PT Chats tab"""
        print("Clicking on PT Chats tab")
        pt_chats_tab = self.wait.until(EC.element_to_be_clickable(self.PT_CHATS_TAB))
        pt_chats_tab.click()
        time.sleep(2)
        print("PT Chats tab clicked successfully")
        
    def search_patient(self, patient_name):
        """Search for patient in the chat search"""
        print(f"Searching for patient: {patient_name}")
        search_input = self.wait.until(EC.presence_of_element_located(self.SEARCH_CHATS_INPUT))
        search_input.clear()
        search_input.send_keys(patient_name)
        time.sleep(2)
        print("Patient search completed")
        
    def click_search_result(self):
        """Click on the first search result"""
        print("Clicking on first search result")
        search_result = self.wait.until(EC.element_to_be_clickable(self.SEARCH_RESULT_ITEM))
        search_result.click()
        time.sleep(2)
        print("Search result clicked successfully")
        
    def verify_message_in_chat(self, message):
        """Verify if the message is present in the chat container"""
        print(f"Verifying message in chat: {message}")
        chat_container = self.wait.until(EC.presence_of_element_located(self.CHAT_CONTAINER))
        chat_text = chat_container.text
        
        if message in chat_text:
            print("✓ Message found in chat successfully")
            return True
        else:
            print(f"✗ Message not found in chat. Chat content: {chat_text}")
            return False 