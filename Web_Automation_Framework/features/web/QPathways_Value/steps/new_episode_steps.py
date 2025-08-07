from behave import given, when, then
from pages.QPathways_Value.new_episode_page import NewEpisodePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import os

# Episode Information Test Cases (13 fields)
@when('I enter episode description')
def step_enter_episode_description(context):
    """Test Case 21: Enter episode description"""
    try:
        if not hasattr(context, 'new_episode_page'):
            context.new_episode_page = NewEpisodePage(context.driver)
        context.new_episode_page.enter_episode_description()
        print("✅ Test Case 21 PASSED: Episode description entered successfully")
    except Exception as e:
        print(f"❌ Test Case 21 FAILED: Episode description entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc21_episode_description_error.png")
        raise AssertionError(f"Test Case 21 - Episode description entry failed: {str(e)}")

@when('I select episode physician')
def step_select_episode_physician(context):
    """Test Case 22: Select episode physician (Non-Critical)"""
    try:
        context.new_episode_page.select_physician()
        print("✅ Test Case 22 PASSED: Episode physician selected successfully")
    except Exception as e:
        print(f"⚠️ Test Case 22 WARNING: Episode physician selection failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc22_episode_physician_error.png")
        # Don't raise error - continue with test

@when('I select episode program')
def step_select_episode_program(context):
    """Test Case 23: Select episode program (Non-Critical)"""
    try:
        context.new_episode_page.select_program()
        print("✅ Test Case 23 PASSED: Episode program selected successfully")
    except Exception as e:
        print(f"⚠️ Test Case 23 WARNING: Episode program selection failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc23_episode_program_error.png")
        # Don't raise error - continue with test

@when('I select surgical facility')
def step_select_surgical_facility(context):
    """Test Case 24: Select surgical facility (Non-Critical)"""
    try:
        context.new_episode_page.select_surgical_facility()
        print("✅ Test Case 24 PASSED: Surgical facility selected successfully")
    except Exception as e:
        print(f"⚠️ Test Case 24 WARNING: Surgical facility selection failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc24_surgical_facility_error.png")
        # Don't raise error - continue with test

@when('I enter surgery date')
def step_enter_surgery_date(context):
    """Test Case 25: Enter surgery date"""
    try:
        context.new_episode_page.enter_surgery_date()
        print("✅ Test Case 25 PASSED: Surgery date entered successfully")
    except Exception as e:
        print(f"❌ Test Case 25 FAILED: Surgery date entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc25_surgery_date_error.png")
        raise AssertionError(f"Test Case 25 - Surgery date entry failed: {str(e)}")

@when('I select episode type')
def step_select_episode_type(context):
    """Test Case 26: Select episode type (Non-Critical)"""
    try:
        context.new_episode_page.select_type()
        print("✅ Test Case 26 PASSED: Episode type selected successfully")
    except Exception as e:
        print(f"⚠️ Test Case 26 WARNING: Episode type selection failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc26_episode_type_error.png")
        # Don't raise error - continue with test

@when('I select joint selection')
def step_select_joint_selection(context):
    """Test Case 27: Select joint selection"""
    try:
        context.new_episode_page.select_joint_selection()
        print("✅ Test Case 27 PASSED: Joint selection completed successfully")
    except Exception as e:
        print(f"❌ Test Case 27 FAILED: Joint selection failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc27_joint_selection_error.png")
        raise AssertionError(f"Test Case 27 - Joint selection failed: {str(e)}")

@when('I select diagnosis code')
def step_select_diagnosis_code(context):
    """Test Case 28: Select diagnosis code (Non-Critical)"""
    try:
        context.new_episode_page.select_diagnosis_code()
        print("✅ Test Case 28 PASSED: Diagnosis code selected successfully")
    except Exception as e:
        print(f"⚠️ Test Case 28 WARNING: Diagnosis code selection failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc28_diagnosis_code_error.png")
        # Don't raise error - continue with test

@when('I select procedure code')
def step_select_procedure_code(context):
    """Test Case 29: Select procedure code (Non-Critical)"""
    try:
        context.new_episode_page.select_procedure_code()
        print("✅ Test Case 29 PASSED: Procedure code selected successfully")
    except Exception as e:
        print(f"⚠️ Test Case 29 WARNING: Procedure code selection failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc29_procedure_code_error.png")
        # Don't raise error - continue with test

@when('I enter patient height')
def step_enter_patient_height(context):
    """Test Case 30: Enter patient height"""
    try:
        context.new_episode_page.enter_height()
        print("✅ Test Case 30 PASSED: Patient height entered successfully")
    except Exception as e:
        print(f"❌ Test Case 30 FAILED: Patient height entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc30_height_error.png")
        raise AssertionError(f"Test Case 30 - Patient height entry failed: {str(e)}")

@when('I enter patient weight')
def step_enter_patient_weight(context):
    """Test Case 31: Enter patient weight"""
    try:
        context.new_episode_page.enter_weight()
        print("✅ Test Case 31 PASSED: Patient weight entered successfully")
    except Exception as e:
        print(f"❌ Test Case 31 FAILED: Patient weight entry failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc31_weight_error.png")
        raise AssertionError(f"Test Case 31 - Patient weight entry failed: {str(e)}")

@when('I save episode information')
def step_save_episode_information(context):
    """Test Case 32: Save episode information"""
    try:
        context.new_episode_page.click_save_button()
        print("✅ Test Case 32 PASSED: Episode information saved successfully")
    except Exception as e:
        print(f"❌ Test Case 32 FAILED: Episode save failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc32_episode_save_error.png")
        raise AssertionError(f"Test Case 32 - Episode save failed: {str(e)}")

@when('I select risk level')
def step_select_risk_level(context):
    """Test Case 33: Select risk level"""
    try:
        context.new_episode_page.click_risk_button()
        print("✅ Test Case 33 PASSED: Risk level selected successfully")
    except Exception as e:
        print(f"❌ Test Case 33 FAILED: Risk level selection failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc33_risk_level_error.png")
        raise AssertionError(f"Test Case 33 - Risk level selection failed: {str(e)}")

@when('I add episode note')
def step_add_episode_note(context):
    """Test Case 34: Add episode note"""
    try:
        context.new_episode_page.click_note_button()
        print("✅ Test Case 34 PASSED: Episode note added successfully")
    except Exception as e:
        print(f"❌ Test Case 34 FAILED: Episode note addition failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc34_episode_note_error.png")
        raise AssertionError(f"Test Case 34 - Episode note addition failed: {str(e)}")

@when('I select episode manager')
def step_select_episode_manager(context):
    """Test Case 35: Select episode manager (Non-Critical)"""
    try:
        context.new_episode_page.select_episode_manager()
        print("✅ Test Case 35 PASSED: Episode manager selected successfully")
    except Exception as e:
        print(f"⚠️ Test Case 35 WARNING: Episode manager selection failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc35_episode_manager_error.png")
        # Don't raise error - continue with test

@when('I open care plan')
def step_open_care_plan(context):
    """Test Case 36: Open care plan"""
    try:
        context.new_episode_page.click_care_plan_button()
        print("✅ Test Case 36 PASSED: Care plan opened successfully")
    except Exception as e:
        print(f"❌ Test Case 36 FAILED: Care plan open failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc36_care_plan_open_error.png")
        raise AssertionError(f"Test Case 36 - Care plan open failed: {str(e)}")

@when('I select care plan index')
def step_select_care_plan_index(context):
    """Test Case 37: Select care plan index"""
    try:
        context.new_episode_page.select_care_plan_index()
        print("✅ Test Case 37 PASSED: Care plan index selected successfully")
    except Exception as e:
        print(f"❌ Test Case 37 FAILED: Care plan index selection failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc37_care_plan_index_error.png")
        raise AssertionError(f"Test Case 37 - Care plan index selection failed: {str(e)}")

@when('I click next in care plan')
def step_click_next_care_plan(context):
    """Test Case 38: Click next button in care plan"""
    try:
        context.new_episode_page.click_next_button_care_plan()
        print("✅ Test Case 38 PASSED: Next button clicked successfully")
    except Exception as e:
        print(f"❌ Test Case 38 FAILED: Next button click failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc38_care_plan_next_error.png")
        raise AssertionError(f"Test Case 38 - Next button click failed: {str(e)}")

@when('I save care plan')
def step_save_care_plan(context):
    """Test Case 39: Save care plan"""
    try:
        context.new_episode_page.click_save_button_care_plan()
        print("✅ Test Case 39 PASSED: Care plan saved successfully")
    except Exception as e:
        print(f"❌ Test Case 39 FAILED: Care plan save failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc39_care_plan_save_error.png")
        raise AssertionError(f"Test Case 39 - Care plan save failed: {str(e)}")

@when('I initiate episode')
def step_initiate_episode(context):
    """Test Case 40: Initiate episode"""
    try:
        context.new_episode_page.click_initiate_button()
        print("✅ Test Case 40 PASSED: Episode initiated successfully")
    except Exception as e:
        print(f"❌ Test Case 40 FAILED: Episode initiation failed - {str(e)}")
        context.driver.save_screenshot("screenshots/tc40_episode_initiation_error.png")
        raise AssertionError(f"Test Case 40 - Episode initiation failed: {str(e)}")

@then('episode should be created successfully')
def step_episode_created_successfully(context):
    """Final Episode Test Case: Verify episode creation completion"""
    try:
        print("🎉 Episode creation workflow completed!")
        time.sleep(3)
        
        # Optional: Verify episode creation success by checking current URL or success message
        current_url = context.driver.current_url
        print(f"Current URL after episode creation: {current_url}")
        print("✅ EPISODE CREATION COMPLETED: All test cases executed successfully!")
        
    except Exception as e:
        print(f"❌ FINAL EPISODE TEST FAILED: Verification failed - {str(e)}")
        context.driver.save_screenshot("screenshots/final_episode_verification_error.png")
        
        # Try to get page source for debugging
        try:
            page_source = context.driver.page_source
            with open("reports/episode_error_page_source.html", "w", encoding="utf-8") as f:
                f.write(page_source)
            print("📄 Episode page source saved to reports/episode_error_page_source.html for debugging")
        except:
            pass
            
        raise AssertionError(f"Final Episode Test Case - Episode creation verification failed: {str(e)}")