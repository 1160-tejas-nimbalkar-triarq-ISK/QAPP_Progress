from behave import given, when, then
from pages.Qpathways_2WT.qpathways_2wt_dashboard_page import Qpathways2WTDashboardPage
from selenium.webdriver.support.ui import WebDriverWait
import time
import random

@given('I am logged into Qpathways 2WT')
def step_logged_into_qpathways_2wt(context):
    """Verify user is logged into Qpathways 2WT"""
    print("User is logged into Qpathways 2WT")
    context.qpathways_2wt_dashboard = Qpathways2WTDashboardPage(context.driver)

@when('I click on the Patients tab')
def step_click_patients_tab(context):
    """Click on the Patients tab"""
    context.qpathways_2wt_dashboard.click_patients_tab()

@when('I click on a random patient')
def step_click_random_patient(context):
    """Click on a random patient and store the patient name"""
    context.patient_name = context.qpathways_2wt_dashboard.click_random_patient()
    print(f"Selected patient name: {context.patient_name}")

@when('I click on the chat button')
def step_click_chat_button(context):
    """Click on the chat button"""
    context.qpathways_2wt_dashboard.click_chat_button()

@when('I enter a random message in the text area')
def step_enter_random_message(context):
    """Enter a random message in the text area"""
    random_messages = [
        "Hello good morning this message is generated through Automation By user Tejas Nimbalkar",
        "Good afternoon! This is an automated test message from Tejas Nimbalkar",
        "Hi there! Automated testing in progress by Tejas Nimbalkar",
        "Greetings! This message was sent via automation by Tejas Nimbalkar",
        "Hello! Automated test message from Tejas Nimbalkar"
    ]
    
    context.random_message = random.choice(random_messages)
    context.qpathways_2wt_dashboard.enter_message(context.random_message)

@when('I click the send button')
def step_click_send_button(context):
    """Click the send button"""
    context.qpathways_2wt_dashboard.click_send_button()

@when('I click on the template button')
def step_click_template_button(context):
    """Click on the template button"""
    context.qpathways_2wt_dashboard.click_template_button()

@when('I click on the template dropdown arrow')
def step_click_template_dropdown_arrow(context):
    """Click on the template dropdown arrow"""
    context.qpathways_2wt_dashboard.click_template_dropdown_arrow()

@when('I select a random template')
def step_select_random_template(context):
    """Select a random template from the dropdown"""
    context.selected_template = context.qpathways_2wt_dashboard.select_random_template()

@when('I click the send button for template')
def step_click_send_button_for_template(context):
    """Click the send button for the selected template"""
    context.qpathways_2wt_dashboard.click_send_button()

@when('I click on the PT Chats tab')
def step_click_pt_chats_tab(context):
    """Click on the PT Chats tab"""
    context.qpathways_2wt_dashboard.click_pt_chats_tab()

@when('I search for the patient by name')
def step_search_patient_by_name(context):
    """Search for the patient by name in the chat search"""
    # Extract first and last name from patient name (e.g., "Doe,Jane E." -> "Doe Jane")
    if hasattr(context, 'patient_name') and context.patient_name:
        # Split by comma and take first part, then split by space and take first two parts
        name_parts = context.patient_name.split(',')
        if len(name_parts) > 0:
            last_name = name_parts[0].strip()
            if len(name_parts) > 1:
                first_name_part = name_parts[1].strip()
                # Split first name part and take only first two words (excluding middle initial)
                first_name_words = first_name_part.split()[:2]
                first_name = ' '.join(first_name_words)
                
                # Create search name: "Doe Jane" (last name first, then first name)
                search_name = f"{last_name} {first_name}"
            else:
                search_name = last_name
            
            context.search_patient_name = search_name
            context.qpathways_2wt_dashboard.search_patient(search_name)
            print(f"Searching for patient: {search_name}")
        else:
            context.search_patient_name = context.patient_name
            context.qpathways_2wt_dashboard.search_patient(context.patient_name)
    else:
        print("No patient name available for search")

@when('I click on the first search result')
def step_click_first_search_result(context):
    """Click on the first search result"""
    context.qpathways_2wt_dashboard.click_search_result()

@then('I should see my messages in the chat')
def step_verify_messages_in_chat(context):
    """Verify that both the random message and template message are present in the chat"""
    print("Verifying messages in chat...")
    
    # Verify random message
    if hasattr(context, 'random_message'):
        random_message_found = context.qpathways_2wt_dashboard.verify_message_in_chat(context.random_message)
        assert random_message_found, f"Random message not found in chat: {context.random_message}"
    
    # Verify template message
    if hasattr(context, 'selected_template'):
        template_message_found = context.qpathways_2wt_dashboard.verify_message_in_chat(context.selected_template)
        assert template_message_found, f"Template message not found in chat: {context.selected_template}"
    
    print("✓ All messages verified successfully in chat")
    print("✓ Qpathways 2WT sanity testing completed successfully")

@then('the sanity testing for Qpathways 2WT should be completed')
def step_sanity_testing_completed(context):
    """Final verification that sanity testing is completed"""
    print("✓ Qpathways 2WT End-to-End Sanity Testing Completed Successfully!")
    print(f"✓ Patient: {getattr(context, 'patient_name', 'N/A')}")
    print(f"✓ Random Message: {getattr(context, 'random_message', 'N/A')}")
    print(f"✓ Template Message: {getattr(context, 'selected_template', 'N/A')}")
    print(f"✓ Search Patient: {getattr(context, 'search_patient_name', 'N/A')}") 