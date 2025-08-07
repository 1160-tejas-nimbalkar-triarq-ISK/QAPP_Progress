import requests
import json
import logging
from utils.config import Config

class ApiHelper:
    """Helper class for API testing operations"""
    
    def __init__(self):
        self.config = Config()
        self.base_url = self.config.get_api_base_url()
        self.headers = self.config.get_api_headers()
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def get(self, endpoint, params=None):
        """Send GET request"""
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"GET request to: {url}")
        
        try:
            response = self.session.get(url, params=params)
            self.logger.info(f"GET response: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            self.logger.error(f"GET request failed: {e}")
            raise
    
    def post(self, endpoint, data=None, json_data=None):
        """Send POST request"""
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"POST request to: {url}")
        
        try:
            if json_data:
                response = self.session.post(url, json=json_data)
            else:
                response = self.session.post(url, data=data)
            
            self.logger.info(f"POST response: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            self.logger.error(f"POST request failed: {e}")
            raise
    
    def put(self, endpoint, data=None, json_data=None):
        """Send PUT request"""
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"PUT request to: {url}")
        
        try:
            if json_data:
                response = self.session.put(url, json=json_data)
            else:
                response = self.session.put(url, data=data)
            
            self.logger.info(f"PUT response: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            self.logger.error(f"PUT request failed: {e}")
            raise
    
    def delete(self, endpoint):
        """Send DELETE request"""
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"DELETE request to: {url}")
        
        try:
            response = self.session.delete(url)
            self.logger.info(f"DELETE response: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            self.logger.error(f"DELETE request failed: {e}")
            raise
    
    def patch(self, endpoint, data=None, json_data=None):
        """Send PATCH request"""
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"PATCH request to: {url}")
        
        try:
            if json_data:
                response = self.session.patch(url, json=json_data)
            else:
                response = self.session.patch(url, data=data)
            
            self.logger.info(f"PATCH response: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            self.logger.error(f"PATCH request failed: {e}")
            raise
    
    def validate_response_status(self, response, expected_status):
        """Validate response status code"""
        assert response.status_code == expected_status, \
            f"Expected status {expected_status}, got {response.status_code}. Response: {response.text}"
    
    def validate_response_contains(self, response, key, expected_value=None):
        """Validate response contains specific key or key-value pair"""
        try:
            response_data = response.json()
        except json.JSONDecodeError:
            raise AssertionError(f"Response is not valid JSON: {response.text}")
        
        assert key in response_data, f"Response should contain '{key}' key. Got: {response_data}"
        
        if expected_value is not None:
            actual_value = response_data[key]
            assert actual_value == expected_value, \
                f"Expected '{key}' to be '{expected_value}', got '{actual_value}'"
    
    def validate_response_schema(self, response, schema):
        """Validate response against JSON schema"""
        try:
            from jsonschema import validate
            response_data = response.json()
            validate(instance=response_data, schema=schema)
        except ImportError:
            self.logger.warning("jsonschema not installed, skipping schema validation")
        except json.JSONDecodeError:
            raise AssertionError(f"Response is not valid JSON: {response.text}")
    
    def get_response_value(self, response, key):
        """Get specific value from response"""
        try:
            response_data = response.json()
            return response_data.get(key)
        except json.JSONDecodeError:
            raise AssertionError(f"Response is not valid JSON: {response.text}")
    
    def set_auth_token(self, token):
        """Set authentication token for requests"""
        self.session.headers.update({'Authorization': f'Bearer {token}'})
    
    def remove_auth_token(self):
        """Remove authentication token"""
        if 'Authorization' in self.session.headers:
            del self.session.headers['Authorization'] 