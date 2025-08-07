import os
from dotenv import load_dotenv

class Config:
    """Configuration class to manage environment variables and settings"""
    
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        
        # Web Configuration
        self.web_base_url = os.getenv('WEB_BASE_URL', 'https://qprime-qa.myqone.com/')
        self.web_username = os.getenv('WEB_USERNAME', 'tejas.automation@triarqhealth.com')
        self.web_password = os.getenv('WEB_PASSWORD', 'P@ssword1')
        
        # Qpathways Value Configuration
        self.qpathways_base_url = os.getenv('QPATHWAYS_BASE_URL', 'https://qprime-qa.myqone.com/')
        self.qpathways_username = os.getenv('QPATHWAYS_USERNAME', 'tejas.automation@triarqhealth.com')
        self.qpathways_password = os.getenv('QPATHWAYS_PASSWORD', 'P@ssword1')
        self.qpathways_dashboard_url = os.getenv('QPATHWAYS_DASHBOARD_URL', 'https://qprime-qa.myqone.com/#/app/home')
        
        # Qpathways 2WT Configuration
        self.qpathways_2wt_base_url = os.getenv('QPATHWAYS_2WT_BASE_URL', 'https://qprime-qa.myqone.com/')
        self.qpathways_2wt_username = os.getenv('QPATHWAYS_2WT_USERNAME', 'tejas.automation@triarqhealth.com')
        self.qpathways_2wt_password = os.getenv('QPATHWAYS_2WT_PASSWORD', 'P@ssword1')
        self.qpathways_2wt_dashboard_url = os.getenv('QPATHWAYS_2WT_DASHBOARD_URL', 'https://qprime-qa.myqone.com/#/app/home')
        
        # API Configuration
        self.api_base_url = os.getenv('API_BASE_URL', 'https://reqres.in/api')
        self.api_key = os.getenv('API_KEY', '')
        self.api_token = os.getenv('API_TOKEN', '')
        
        # Browser Configuration
        self.browser = os.getenv('BROWSER', 'chrome')
        self.headless = os.getenv('HEADLESS', 'false').lower() == 'true'
        self.timeout = int(os.getenv('TIMEOUT', '10'))
        
        # Test Data Configuration
        self.test_data_path = os.getenv('TEST_DATA_PATH', 'test_data/')
        
        # Reporting Configuration
        self.report_path = os.getenv('REPORT_PATH', 'reports/')
        self.screenshot_path = os.getenv('SCREENSHOT_PATH', 'screenshots/')
        
    def get_web_base_url(self):
        """Get web base URL"""
        return self.web_base_url
        
    def get_api_base_url(self):
        """Get API base URL"""
        return self.api_base_url
        
    def get_web_credentials(self):
        """Get web testing credentials"""
        return {
            'username': self.web_username,
            'password': self.web_password
        }
        
    def get_qpathways_credentials(self):
        """Get Qpathways Value testing credentials"""
        return {
            'username': self.qpathways_username,
            'password': self.qpathways_password,
            'url': self.qpathways_base_url,
            'dashboard_url': self.qpathways_dashboard_url
        }
        
    def get_qpathways_2wt_credentials(self):
        """Get Qpathways 2WT testing credentials"""
        return {
            'username': self.qpathways_2wt_username,
            'password': self.qpathways_2wt_password,
            'url': self.qpathways_2wt_base_url,
            'dashboard_url': self.qpathways_2wt_dashboard_url
        }
        
    def get_api_headers(self):
        """Get default API headers"""
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        if self.api_key:
            headers['X-API-Key'] = self.api_key
            
        if self.api_token:
            headers['Authorization'] = f'Bearer {self.api_token}'
            
        return headers
        
    def get_browser_config(self):
        """Get browser configuration"""
        return {
            'browser': self.browser,
            'headless': self.headless,
            'timeout': self.timeout
        }
        
    def get_reporting_config(self):
        """Get reporting configuration"""
        return {
            'report_path': self.report_path,
            'screenshot_path': self.screenshot_path
        }
        
    def create_directories(self):
        """Create necessary directories if they don't exist"""
        directories = [
            self.test_data_path,
            self.report_path,
            self.screenshot_path
        ]
        
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory) 