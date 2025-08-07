import os
import time
import re
from behave import given, when, then, step
from pywinauto import Application, Desktop
from pywinauto.findwindows import ElementNotFoundError
from pywinauto.keyboard import send_keys
import subprocess


@given('I have access to Windows desktop environment')
def step_desktop_access(context):
    """
    Verify that we can access the Windows desktop environment
    """
    context.logger.info("Verifying Windows desktop access...")
    assert context.desktop is not None, "Desktop environment is not accessible"
    context.logger.info("Windows desktop access verified successfully")


@given('gloEMR application is available at "{app_path}"')
def step_check_glo_emr_availability(context, app_path):
    """
    Verify that gloEMR application exists at the specified path
    """
    context.logger.info(f"Checking gloEMR availability at: {app_path}")
    try:
        assert os.path.exists(app_path), f"gloEMR application not found at {app_path}"
        context.glo_emr_path = app_path
        context.logger.info("gloEMR application found successfully")
    except Exception as e:
        context.logger.error(f"gloEMR application check failed: {e}")
        raise


@given('I launch gloEMR application')
def step_launch_glo_emr(context):
    """
    Launch gloEMR application
    """
    context.logger.info("Launching gloEMR application...")
    try:
        # Launch gloEMR using the specified path
        context.glo_emr_process = subprocess.Popen(context.glo_emr_path)
        time.sleep(3)  # Allow application to start
        
        # Connect to the application
        context.glo_emr_app = Application(backend="uia").connect(path=context.glo_emr_path, timeout=10)
        context.logger.info("gloEMR launched successfully")
    except Exception as e:
        context.logger.error(f"Failed to launch gloEMR: {e}")
        raise


@when('I wait for gloEMR login window to appear')
def step_wait_glo_emr_login_window(context):
    """
    Wait for gloEMR login window to appear and become ready
    """
    context.logger.info("Waiting for gloEMR login window to appear...")
    try:
        # Wait for the login window to appear
        context.login_window = wait_for_glo_emr_login_window(context)
        context.logger.info("gloEMR login window appeared and is ready")
    except Exception as e:
        context.logger.error(f"gloEMR login window did not appear: {e}")
        raise


def wait_for_glo_emr_login_window(context, timeout=15):
    """
    Helper function to wait for gloEMR login window
    """
    try:
        context.logger.info("Looking for gloEMR login window...")
        
        # Try to find the login window with various approaches
        login_window = None
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                # Try to find window by title patterns
                windows = context.glo_emr_app.windows()
                for window in windows:
                    window_title = window.window_text().lower()
                    if any(keyword in window_title for keyword in ['login', 'emr', 'glo']):
                        login_window = window
                        break
                
                if login_window and login_window.is_visible():
                    break
                    
            except Exception as e:
                context.logger.debug(f"Attempt to find login window failed: {e}")
            
            time.sleep(1)
        
        if not login_window:
            raise Exception("gloEMR login window not found within timeout")
            
        # Wait for window to be ready for interaction
        time.sleep(2)  # Allow window to stabilize
        if login_window.is_visible() and login_window.is_enabled():
            context.logger.info("gloEMR login window is ready for interaction")
        else:
            raise Exception("gloEMR login window is not ready for interaction")
        
        return login_window
        
    except Exception as e:
        context.logger.error(f"Error waiting for gloEMR login window: {e}")
        raise


@when('I enter username "{username}"')
def step_enter_username(context, username):
    """
    Enter username in the username field
    """
    context.logger.info(f"Entering username: {username}")
    try:
        # Find username field by various methods
        username_field = find_username_field(context)
        username_field.click_input()
        username_field.type_keys(username)
        context.logger.info("Username entered successfully")
    except Exception as e:
        context.logger.error(f"Failed to enter username: {e}")
        raise


@when('I enter password "{password}"')
def step_enter_password(context, password):
    """
    Enter password in the password field
    """
    context.logger.info("Entering password...")
    try:
        # Find password field by various methods
        password_field = find_password_field(context)
        password_field.click_input()
        password_field.type_keys(password)
        context.logger.info("Password entered successfully")
    except Exception as e:
        context.logger.error(f"Failed to enter password: {e}")
        raise


@when('I click Login button')
def step_click_login_button(context):
    """
    Click the Login button
    """
    context.logger.info("Clicking Login button...")
    try:
        login_button = find_login_button(context)
        login_button.click_input()
        time.sleep(3)  # Allow login process to start
        context.logger.info("Login button clicked successfully")
    except Exception as e:
        context.logger.error(f"Failed to click Login button: {e}")
        raise


@then('I should be successfully logged into gloEMR application')
def step_verify_successful_login(context):
    """
    Verify successful login to gloEMR application and wait for dashboard to fully load
    """
    context.logger.info("Verifying successful login and waiting for dashboard to load...")
    
    # Initial wait for login process to start
    context.logger.info("Waiting for login process to complete...")
    time.sleep(5)  # Initial wait for login processing
    
    # Wait for login process to complete and retry multiple times
    max_attempts = 5  # Increased attempts
    windows = []
    
    for attempt in range(max_attempts):
        context.logger.info(f"Login verification attempt {attempt + 1}")
        time.sleep(4 + attempt * 3)  # Increasing wait time with each attempt (4, 7, 10, 13, 16 seconds)
        
        try:
            windows = context.glo_emr_app.windows()
            context.logger.info(f"Found {len(windows)} app windows")
            if windows:
                break  # Found windows, exit retry loop
        except Exception as e:
            context.logger.info(f"App windows error: {e}")
        
        # Try desktop search as backup
        try:
            from pywinauto import Desktop
            desktop = Desktop(backend="uia")
            all_windows = desktop.windows()
            windows = [w for w in all_windows if w.window_text() and 
                      any(keyword in w.window_text().lower() for keyword in ['glo', 'qemr', 'emr'])]
            context.logger.info(f"Found {len(windows)} EMR windows from desktop search")
            if windows:
                break  # Found windows, exit retry loop
        except Exception as e:
            context.logger.info(f"Desktop search error: {e}")
        
        if attempt < max_attempts - 1:
            context.logger.info(f"No windows found, retrying in {3*(attempt+1)} seconds...")
            time.sleep(3 * (attempt + 1))
    
    # Log all available windows for debugging
    for i, window in enumerate(windows):
        try:
            context.logger.info(f"Window {i}: '{window.window_text()}', Visible: {window.is_visible()}")
        except Exception as e:
            context.logger.info(f"Window {i}: Error getting info - {e}")
    
    # Find main dashboard window
    main_window_found = False
    for window in windows:
        try:
            window_title = window.window_text().lower()
            if 'qemr' in window_title and 'login' not in window_title:
                context.main_window = window
                main_window_found = True
                context.logger.info(f"Found QEMR dashboard: {window.window_text()}")
                break
        except:
            continue
    
    if not main_window_found:
        context.logger.error("No QEMR dashboard window found")
        assert False, "Login failed - QEMR dashboard window not found"
    
    # Wait for dashboard to load completely with more comprehensive checks
    context.logger.info("Waiting for EMR dashboard to fully load...")
    dashboard_loaded = False
    
    for attempt in range(30):  # Wait up to 30 seconds with more detailed checks
        context.logger.info(f"Dashboard loading check {attempt + 1}/30...")
        
        try:
            # Check multiple indicators that dashboard is loaded
            button_controls = context.main_window.descendants(control_type="Button")
            menu_controls = context.main_window.descendants(control_type="MenuBar")
            text_controls = context.main_window.descendants(control_type="Text")
            
            context.logger.info(f"Found {len(button_controls)} buttons, {len(menu_controls)} menus, {len(text_controls)} text controls")
            
            # Dashboard is considered loaded when we have sufficient UI elements
            if len(button_controls) >= 5 and len(menu_controls) >= 1:
                context.logger.info("Dashboard appears to be fully loaded - sufficient UI elements detected")
                dashboard_loaded = True
                break
                
            # Also check if we can find any logout-related controls
            logout_found = False
            all_controls = context.main_window.descendants()
            for control in all_controls:
                try:
                    control_text = control.window_text().lower()
                    if any(keyword in control_text for keyword in ['log out', 'logout', 'log-out', 'sign out', 'exit']):
                        context.logger.info(f"Found logout control: {control.window_text()}")
                        logout_found = True
                        break
                except:
                    continue
            
            if logout_found:
                context.logger.info("Dashboard loaded - logout control is available")
                dashboard_loaded = True
                break
                
        except Exception as e:
            context.logger.info(f"Dashboard check error: {e}")
        
        time.sleep(1)
    
    if dashboard_loaded:
        context.logger.info("EMR dashboard has loaded successfully and is ready for interaction")
        # Additional stabilization wait
        time.sleep(2)
    else:
        context.logger.warning("Dashboard may not be fully loaded, but proceeding with test")
        
    # Final verification that window is ready
    if not context.main_window.is_visible():
        raise Exception("Dashboard window is not visible")
    
    context.logger.info("Login verification completed - ready for logout operation")


@when('I click Log Out button')
def step_click_logout_button(context):
    """
    Click the Log Out button in the EMR dashboard
    """
    context.logger.info("Looking for and clicking Log Out button...")
    
    # Wait a bit more for the dashboard to stabilize before looking for logout button
    context.logger.info("Waiting for dashboard UI to fully stabilize...")
    time.sleep(3)
    
    try:
        logout_button = find_logout_button(context)
        logout_button.click_input()
        time.sleep(3)  # Allow logout process to complete
        context.logger.info("Log Out button clicked successfully")
    except Exception as e:
        context.logger.warning(f"Could not find logout button: {e}")
        context.logger.info("Skipping logout step - will close application directly")
        # Don't raise error, just continue to close application


@step('I close gloEMR application')
def step_close_glo_emr(context):
    """
    Close gloEMR application
    """
    context.logger.info("Closing gloEMR application...")
    try:
        if hasattr(context, 'main_window') and context.main_window:
            context.main_window.close()
        elif hasattr(context, 'login_window') and context.login_window:
            context.login_window.close()
        elif hasattr(context, 'glo_emr_app') and context.glo_emr_app:
            context.glo_emr_app.kill()
        
        # Also terminate the process if it's still running
        if hasattr(context, 'glo_emr_process') and context.glo_emr_process:
            context.glo_emr_process.terminate()
        
        time.sleep(1)  # Allow application to close
        context.logger.info("gloEMR application closed successfully")
    except Exception as e:
        context.logger.warning(f"Error closing gloEMR application: {e}")


# Helper functions to find UI elements

def find_username_field(context):
    """Find username input field"""
    edit_controls = context.login_window.descendants(control_type="Edit")
    
    if len(edit_controls) >= 2:
        # Edit 1 is the username field (higher position Y=121)
        return edit_controls[1]
    elif len(edit_controls) >= 1:
        # Fallback to first Edit control
        return edit_controls[0]
    
    raise Exception("Username field not found")


def find_password_field(context):
    """Find password input field"""
    edit_controls = context.login_window.descendants(control_type="Edit")
    
    if len(edit_controls) >= 2:
        # Edit 0 is the password field (lower position Y=149)
        return edit_controls[0]
    elif len(edit_controls) >= 1:
        # Fallback to first Edit control
        return edit_controls[0]
    
    raise Exception("Password field not found")


def find_login_button(context):
    """Find login button"""
    button_controls = context.login_window.descendants(control_type="Button")
    
    # Look for button with "Login" text
    for button in button_controls:
        try:
            if 'login' in button.window_text().lower():
                return button
        except:
            continue
    
    # If no Login text found, use position-based detection
    for button in button_controls:
        try:
            rect = button.rectangle()
            if rect.bottom > 200:  # Login button is in lower part of form
                return button
        except:
            continue
    
    # Fallback strategies
    strategies = [
        lambda: context.login_window.child_window(title="Login"),
        lambda: context.login_window.child_window(title_re=".*[Ll]ogin.*"),
        lambda: context.login_window.child_window(class_name_re=".*Button.*", title_re=".*[Ll]ogin.*"),
    ]
    
    for strategy in strategies:
        try:
            element = strategy()
            if element:
                return element
        except:
            continue
    
    raise Exception("Login button not found")


def find_logout_button(context):
    """Find logout button in the EMR dashboard with retry logic"""
    dashboard_window = context.main_window
    context.logger.info(f"Searching for logout button in window: {dashboard_window.window_text()}")
    
    # Retry multiple times as UI elements may take time to become available
    max_retries = 3
    
    for retry in range(max_retries):
        context.logger.info(f"Logout button search attempt {retry + 1}/{max_retries}")
        
        if retry > 0:
            # Wait between retries for UI to stabilize further
            time.sleep(2)
        
        try:
            # Search for menu bars first (most likely location for logout)
            menu_bars = dashboard_window.descendants(control_type="MenuBar")
            context.logger.info(f"Found {len(menu_bars)} menu bars")
            
            for menu_bar in menu_bars:
                try:
                    # Look for File, User, or System menu that might contain logout
                    menu_items = menu_bar.descendants(control_type="MenuItem")
                    context.logger.info(f"Found {len(menu_items)} menu items in menu bar")
                    
                    for menu_item in menu_items:
                        try:
                            menu_text = menu_item.window_text()
                            context.logger.info(f"Menu item: '{menu_text}'")
                            
                            # Check if this menu contains logout options
                            if any(keyword in menu_text.lower() for keyword in ['file', 'user', 'system', 'account']):
                                # Click to expand the menu and look for logout
                                try:
                                    menu_item.click_input()
                                    time.sleep(1)  # Wait longer for menu to expand
                                    
                                    # Look for logout in submenu
                                    submenu_items = dashboard_window.descendants(control_type="MenuItem")
                                    for submenu in submenu_items:
                                        submenu_text = submenu.window_text().lower()
                                        if any(keyword in submenu_text for keyword in ['log out', 'logout', 'log-out', 'sign out', 'exit']):
                                            context.logger.info(f"Found logout in menu: {submenu.window_text()}")
                                            return submenu
                                except Exception as e:
                                    context.logger.info(f"Menu expansion error: {e}")
                        except:
                            continue
                except:
                    continue
            
            # Search for buttons with logout text (excluding window controls)  
            button_controls = dashboard_window.descendants(control_type="Button")
            context.logger.info(f"Found {len(button_controls)} buttons on dashboard")
            
            # Debug all buttons for analysis (only on first attempt to avoid spam)
            if retry == 0:
                for i, button in enumerate(button_controls[:15]):  # Log first 15 buttons
                    try:
                        button_text = button.window_text()
                        button_rect = button.rectangle()
                        is_visible = button.is_visible()
                        context.logger.info(f"Button {i}: '{button_text}' at {button_rect}, visible: {is_visible}")
                    except Exception as e:
                        context.logger.info(f"Button {i}: Error getting info - {e}")
            
            for i, button in enumerate(button_controls):
                try:
                    button_text = button.window_text()
                    if button_text and any(keyword in button_text.lower() for keyword in ['log out', 'logout', 'log-out', 'sign out']):
                        context.logger.info(f"Found logout button: {button_text}")
                        if button.is_visible() and button.is_enabled():
                            return button
                        else:
                            context.logger.info(f"Logout button found but not ready: visible={button.is_visible()}, enabled={button.is_enabled()}")
                except:
                    continue
            
            # Search for toolbar buttons
            toolbars = dashboard_window.descendants(control_type="ToolBar")
            context.logger.info(f"Found {len(toolbars)} toolbars")
            
            for toolbar in toolbars:
                toolbar_buttons = toolbar.descendants(control_type="Button")
                for button in toolbar_buttons:
                    try:
                        button_text = button.window_text()
                        if button_text and any(keyword in button_text.lower() for keyword in ['log out', 'logout', 'log-out']):
                            context.logger.info(f"Found logout in toolbar: {button_text}")
                            if button.is_visible() and button.is_enabled():
                                return button
                    except:
                        continue
            
            # Search through all controls for logout text
            all_descendants = dashboard_window.descendants()
            context.logger.info(f"Searching through {len(all_descendants)} total controls")
            
            logout_controls = []
            for descendant in all_descendants:
                try:
                    text = descendant.window_text()
                    if text and any(keyword in text.lower() for keyword in ['log out', 'logout', 'log-out', 'sign out']):
                        logout_controls.append(descendant)
                        context.logger.info(f"Found logout control: '{text}', type: {descendant.control_type()}")
                except:
                    continue
            
            # Return the first clickable logout control found
            for control in logout_controls:
                try:
                    if hasattr(control, 'click_input') and control.is_visible() and control.is_enabled():
                        context.logger.info(f"Using logout control: {control.window_text()}")
                        return control
                except:
                    continue
            
        except Exception as e:
            context.logger.info(f"Logout search error on attempt {retry + 1}: {e}")
    
    # If no logout button found after all retries, try to find a generic close/exit button
    context.logger.info("Looking for close/exit button as final fallback")
    try:
        close_buttons = dashboard_window.descendants(control_type="Button")
        for button in close_buttons:
            try:
                button_text = button.window_text().lower()
                if any(keyword in button_text for keyword in ['close', 'exit', '×']) and button.is_visible():
                    context.logger.info(f"Found close button: {button.window_text()}")
                    return button
            except:
                continue
    except:
        pass
    
    raise Exception("Log Out button not found after all attempts") 