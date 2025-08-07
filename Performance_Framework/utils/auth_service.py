"""
Authentication Service for API Testing Framework
Provides dynamic token generation and authentication management
"""

import requests
import json
import time
from typing import Dict, Optional, Any
from datetime import datetime, timedelta
import os

class AuthService:
    """Authentication service for managing API tokens and authentication"""
    
    def __init__(self, config: Dict[str, Any] = None):
        """Initialize authentication service with configuration"""
        self.config = config or {}
        self.token_cache = {}
        self.token_expiry = {}
        
    def get_dynamic_token(self, environment: str = "qa") -> str:
        """Generate dynamic authorization token for the specified environment"""
        try:
            # Check if we have a cached valid token
            if self._is_token_valid(environment):
                return self.token_cache.get(environment, "")
            
            # Generate new token based on environment
            if environment == "qa":
                return self._generate_qa_token()
            elif environment == "dev":
                return self._generate_dev_token()
            elif environment == "staging":
                return self._generate_staging_token()
            elif environment == "production":
                return self._generate_production_token()
            else:
                # Fallback to QA token
                return self._generate_qa_token()
                
        except Exception as e:
            print(f"⚠️ Error generating dynamic token: {e}")
            return self._get_fallback_token()
    
    def _is_token_valid(self, environment: str) -> bool:
        """Check if cached token is still valid"""
        if environment not in self.token_cache:
            return False
            
        if environment not in self.token_expiry:
            return False
            
        # Check if token has expired (with 5 minute buffer)
        expiry_time = self.token_expiry[environment]
        current_time = datetime.now()
        
        return current_time < expiry_time - timedelta(minutes=5)
    
    def _generate_qa_token(self) -> str:
        """Generate QA environment token"""
        # This would typically call an authentication service
        # For now, return a static token with dynamic expiry
        token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NTM3Nzc1ODMsImV4cCI6MTc1NjM2OTU4MywiaXNzIjoiY2xvdWQtZW5kcG9pbnRzLXFhQHFwYXRod2F5cy1xYS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsImF1ZCI6Imh0dHBzOi8vcW9yZS1xYS5teXFvbmUuY29tIiwic3ViIjoiY2xvdWQtZW5kcG9pbnRzLXFhQHFwYXRod2F5cy1xYS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsImVtYWlsIjoic2FjaGluLnNhbmFwQHRyaWFycWhlYWx0aC5jb20iLCJ1c2VyaWQiOiI2MGUwODZkYS1lNzJiLTExZWMtODVhNS05MWEyZDNjZWJmZTEiLCJmaXJzdG5hbWUiOiJTYWNoaW4iLCJsYXN0bmFtZSI6IlNhbmFwIn0.PhMI-2dOmDyaHG5FOXeRfKYiaNCgZGIPeV9Mbq8sh7ihaJ4olsqLPj6tL7tnT7qKJztSHEqrzKtYoiiNa1XOSjZvTLmIlDHanX5iS2NGq8u6QUA_IVATw-rr904unMfgUEa3_fCb15mdmWNznmysWBHTBdBIh174X6oXlNKMi0FjJYIskUGSKbQjLBVu_IVfAeWl6PXWVhBfhvctxjTnBzKm8FoTxX-DhM_TOYuFIzoZaxPd9wlcCq6lEa-qozxYH0LRqW4ulTXyR_qdv92lLWNf0txLwwjGNr017SKCG5WmR8VzLAdXtQWZPkiX3XRNNzlB17O8vloFpr7S9hePPw"
        
        # Cache the token with expiry
        self.token_cache["qa"] = token
        self.token_expiry["qa"] = datetime.now() + timedelta(hours=24)
        
        return token
    
    def _generate_dev_token(self) -> str:
        """Generate DEV environment token"""
        # Similar to QA but with dev-specific configuration
        token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NTM3Nzc1ODMsImV4cCI6MTc1NjM2OTU4MywiaXNzIjoiY2xvdWQtZW5kcG9pbnRzLWRldkBxcGF0aHdheXMtZGV2LmlhbS5nc2VydmljZWFjY291bnQuY29tIiwiYXVkIjoiaHR0cHM6Ly9xb3JlLWRldi5teXFvbmUuY29tIiwic3ViIjoiY2xvdWQtZW5kcG9pbnRzLWRldkBxcGF0aHdheXMtZGV2LmlhbS5nc2VydmljZWFjY291bnQuY29tIiwiZW1haWwiOiJzYWNoaW4uc2FuYXBAdHJpYXJxaGVhbHRoLmNvbSIsInVzZXJpZCI6IjYwZTA4NmRhLWU3MmItMTFlYy04NWE1LTkxYTJkM2NlYmZlMSIsImZpcnN0bmFtZSI6IlNhY2hpbiIsImxhc3RuYW1lIjoiU2FuYXAifQ.DEV_TOKEN_PLACEHOLDER"
        
        self.token_cache["dev"] = token
        self.token_expiry["dev"] = datetime.now() + timedelta(hours=24)
        
        return token
    
    def _generate_staging_token(self) -> str:
        """Generate STAGING environment token"""
        token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NTM3Nzc1ODMsImV4cCI6MTc1NjM2OTU4MywiaXNzIjoiY2xvdWQtZW5kcG9pbnRzLXN0YWdpbmdAcXBhdGh3YXlzLXN0YWdpbmcuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJhdWQiOiJodHRwczovL3FvcmUtc3RhZ2luZy5teXFvbmUuY29tIiwic3ViIjoiY2xvdWQtZW5kcG9pbnRzLXN0YWdpbmdAcXBhdGh3YXlzLXN0YWdpbmcuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJlbWFpbCI6InNhY2hpbi5zYW5hcEB0cmlhcnFoZWFsdGguY29tIiwidXNlcmlkIjoiNjBlMDg2ZGEtZTcyYi0xMWVjLTg1YTUtOTFhMmQzY2ViZmUxIiwiZmlyc3RuYW1lIjoiU2FjaGluIiwibGFzdG5hbWUiOiJTYW5hcCJ9.STAGING_TOKEN_PLACEHOLDER"
        
        self.token_cache["staging"] = token
        self.token_expiry["staging"] = datetime.now() + timedelta(hours=24)
        
        return token
    
    def _generate_production_token(self) -> str:
        """Generate PRODUCTION environment token"""
        token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NTM3Nzc1ODMsImV4cCI6MTc1NjM2OTU4MywiaXNzIjoiY2xvdWQtZW5kcG9pbnRzLXByb2R1Y3Rpb25AcXBhdGh3YXlzLXByb2R1Y3Rpb24uaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJhdWQiOiJodHRwczovL3FvcmUtcHJvZHVjdGlvbi5teXFvbmUuY29tIiwic3ViIjoiY2xvdWQtZW5kcG9pbnRzLXByb2R1Y3Rpb25AcXBhdGh3YXlzLXByb2R1Y3Rpb24uaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJlbWFpbCI6InNhY2hpbi5zYW5hcEB0cmlhcnFoZWFsdGguY29tIiwidXNlcmlkIjoiNjBlMDg2ZGEtZTcyYi0xMWVjLTg1YTUtOTFhMmQzY2ViZmUxIiwiZmlyc3RuYW1lIjoiU2FjaGluIiwibGFzdG5hbWUiOiJTYW5hcCJ9.PRODUCTION_TOKEN_PLACEHOLDER"
        
        self.token_cache["production"] = token
        self.token_expiry["production"] = datetime.now() + timedelta(hours=24)
        
        return token
    
    def _get_fallback_token(self) -> str:
        """Get fallback token when dynamic generation fails"""
        return "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NTM3Nzc1ODMsImV4cCI6MTc1NjM2OTU4MywiaXNzIjoiY2xvdWQtZW5kcG9pbnRzLXFhQHFwYXRod2F5cy1xYS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsImF1ZCI6Imh0dHBzOi8vcW9yZS1xYS5teXFvbmUuY29tIiwic3ViIjoiY2xvdWQtZW5kcG9pbnRzLXFhQHFwYXRod2F5cy1xYS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsImVtYWlsIjoic2FjaGluLnNhbmFwQHRyaWFycWhlYWx0aC5jb20iLCJ1c2VyaWQiOiI2MGUwODZkYS1lNzJiLTExZWMtODVhNS05MWEyZDNjZWJmZTEiLCJmaXJzdG5hbWUiOiJTYWNoaW4iLCJsYXN0bmFtZSI6IlNhbmFwIn0.PhMI-2dOmDyaHG5FOXeRfKYiaNCgZGIPeV9Mbq8sh7ihaJ4olsqLPj6tL7tnT7qKJztSHEqrzKtYoiiNa1XOSjZvTLmIlDHanX5iS2NGq8u6QUA_IVATw-rr904unMfgUEa3_fCb15mdmWNznmysWBHTBdBIh174X6oXlNKMi0FjJYIskUGSKbQjLBVu_IVfAeWl6PXWVhBfhvctxjTnBzKm8FoTxX-DhM_TOYuFIzoZaxPd9wlcCq6lEa-qozxYH0LRqW4ulTXyR_qdv92lLWNf0txLwwjGNr017SKCG5WmR8VzLAdXtQWZPkiX3XRNNzlB17O8vloFpr7S9hePPw"
    
    def get_headers_with_auth(self, environment: str = "qa", additional_headers: Dict[str, str] = None) -> Dict[str, str]:
        """Get headers with dynamic authorization token"""
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Performance-Testing-Framework/1.0",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.get_dynamic_token(environment)}"
        }
        
        if additional_headers:
            headers.update(additional_headers)
            
        return headers
    
    def get_dynamic_headers_for_qa(self, headers: Dict[str, str]) -> Dict[str, str]:
        """Add dynamic authentication headers for QA environment"""
        # Get dynamic token for QA environment
        qa_token = self.get_dynamic_token("qa")
        
        # Update headers with dynamic authentication
        headers.update({
            "Authorization": f"Bearer {qa_token}",
            "X-Environment": "qa",
            "X-Dynamic-Auth": "true"
        })
        
        return headers
    
    def refresh_token(self, environment: str = "qa") -> str:
        """Force refresh of token for specified environment"""
        # Remove cached token to force regeneration
        if environment in self.token_cache:
            del self.token_cache[environment]
        if environment in self.token_expiry:
            del self.token_expiry[environment]
            
        return self.get_dynamic_token(environment)
    
    def validate_token(self, token: str) -> bool:
        """Validate if a token is properly formatted"""
        if not token:
            return False
            
        # Basic JWT token validation (check structure)
        parts = token.split('.')
        if len(parts) != 3:
            return False
            
        # Check if it starts with "Bearer "
        if token.startswith("Bearer "):
            token = token[7:]  # Remove "Bearer " prefix
            
        return True

# Global auth service instance
auth_service = AuthService()

def get_auth_service() -> AuthService:
    """Get the global authentication service instance"""
    return auth_service 