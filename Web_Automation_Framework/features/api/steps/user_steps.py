from behave import given, when, then
from utils.api_helpers import ApiHelper
import json

@given('the API is available')
def step_api_available(context):
    """Initialize API helper and verify API is available"""
    context.api_helper = ApiHelper()
    # Verify API is reachable
    response = context.api_helper.get('/users')
    assert response.status_code in [200, 404], f"API is not available. Status: {response.status_code}"

@given('a user exists with id {user_id:d}')
def step_user_exists(context, user_id):
    """Verify that a user exists with the given ID"""
    context.api_helper = ApiHelper()
    response = context.api_helper.get(f'/users/{user_id}')
    # If user doesn't exist, create one for testing
    if response.status_code == 404:
        user_data = {
            "name": "Test User",
            "email": f"test{user_id}@example.com",
            "job": "Tester"
        }
        create_response = context.api_helper.post('/users', user_data)
        assert create_response.status_code == 201, f"Failed to create test user: {create_response.status_code}"

@when('I send a POST request to create a user with')
def step_create_user_post(context):
    """Send POST request to create a user with given data"""
    context.api_helper = ApiHelper()
    user_data = {}
    for row in context.table:
        user_data[row[0]] = row[1]
    
    context.response = context.api_helper.post('/users', json_data=user_data)

@when('I send a GET request to retrieve user with id {user_id:d}')
def step_get_user(context, user_id):
    """Send GET request to retrieve user by ID"""
    context.api_helper = ApiHelper()
    context.response = context.api_helper.get(f'/users/{user_id}')

@when('I send a PUT request to update user with id {user_id:d}')
def step_update_user(context, user_id):
    """Send PUT request to update user with given data"""
    context.api_helper = ApiHelper()
    user_data = {}
    for row in context.table:
        user_data[row[0]] = row[1]
    context.response = context.api_helper.put(f'/users/{user_id}', json_data=user_data)

@when('I send a DELETE request to delete user with id {user_id:d}')
def step_delete_user(context, user_id):
    """Send DELETE request to delete user by ID"""
    context.api_helper = ApiHelper()
    context.response = context.api_helper.delete(f'/users/{user_id}')

@then('the response status code should be {status_code:d}')
def step_verify_status_code(context, status_code):
    """Verify the response status code"""
    assert context.response.status_code == status_code, \
        f"Expected status code {status_code}, got {context.response.status_code}. Response: {context.response.text}"

@then('the response should contain user id')
def step_verify_user_id(context):
    """Verify response contains user ID"""
    response_data = context.response.json()
    assert 'id' in response_data, f"Response should contain 'id' field. Got: {response_data}"

@then('the response should contain "{field}" as "{value}"')
def step_verify_field_value(context, field, value):
    """Verify response contains specific field with expected value"""
    response_data = context.response.json()
    assert field in response_data, f"Response should contain '{field}' field. Got: {response_data}"
    assert response_data[field] == value, f"Expected {field} to be '{value}', got '{response_data[field]}'"

@then('the response should contain user data')
def step_verify_user_data(context):
    """Verify response contains user data"""
    response_data = context.response.json()
    assert isinstance(response_data, dict), f"Response should be a dictionary. Got: {type(response_data)}"
    assert len(response_data) > 0, f"Response should not be empty. Got: {response_data}"

@then('the response should have "{field}" field')
def step_verify_field_exists(context, field):
    """Verify response has specific field"""
    response_data = context.response.json()
    assert field in response_data, f"Response should contain '{field}' field. Got: {response_data}"

@then('the response should contain error message')
def step_verify_error_message(context):
    """Verify response contains error message"""
    response_data = context.response.json()
    # Check for common error message fields
    error_fields = ['error', 'message', 'detail', 'errors']
    has_error = any(field in response_data for field in error_fields)
    assert has_error, f"Response should contain error message. Got: {response_data}" 