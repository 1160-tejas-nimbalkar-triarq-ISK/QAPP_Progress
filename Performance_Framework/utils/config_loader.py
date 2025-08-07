"""
Environment Configuration Loader for BDD Performance Testing Framework
Centralizes configuration management and environment-specific settings
"""

import os
import yaml
from pathlib import Path
from typing import Dict, Any, Optional

# Import authentication service for dynamic token management
try:
    from .auth_service import auth_service
    DYNAMIC_AUTH_AVAILABLE = True
except ImportError:
    print("⚠️ Dynamic authentication service not available")
    auth_service = None
    DYNAMIC_AUTH_AVAILABLE = False

class EnvironmentConfigLoader:
    """Utility class to load and manage environment-specific configurations"""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the configuration loader
        
        Args:
            config_path: Path to the configuration file. If None, uses default location.
        """
        if config_path:
            self.config_path = Path(config_path)
        else:
            # Default path relative to the project root
            project_root = Path(__file__).parent.parent
            self.config_path = project_root / "config" / "test_config.yaml"
        
        self.config = None
        self.current_environment = None
        self.load_config()
        
        # Initialize authentication service with this config loader instance
        if DYNAMIC_AUTH_AVAILABLE and auth_service:
            auth_service.config_loader = self
    
    def load_config(self) -> bool:
        """
        Load configuration from YAML file
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not self.config_path.exists():
                raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
            
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = yaml.safe_load(f)
            
            print(f"✅ Configuration loaded from: {self.config_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error loading configuration: {e}")
            return False
    
    def set_environment(self, environment: str) -> bool:
        """
        Set the current environment for configuration
        
        Args:
            environment: Environment name (qa, staging, production, etc.)
            
        Returns:
            bool: True if environment exists, False otherwise
        """
        if not self.config:
            print("❌ Configuration not loaded")
            return False
        
        environments = self.config.get('environments', {})
        if environment not in environments:
            available_envs = list(environments.keys())
            print(f"❌ Environment '{environment}' not found. Available: {available_envs}")
            return False
        
        self.current_environment = environment
        print(f"🌐 Environment set to: {environment}")
        return True
    
    def get_base_url(self, environment: Optional[str] = None) -> str:
        """
        Get base URL for the specified or current environment
        
        Args:
            environment: Environment name. If None, uses current environment.
            
        Returns:
            str: Base URL for the environment
        """
        env = environment or self.current_environment
        
        if not env:
            raise ValueError("No environment specified and no current environment set")
        
        if not self.config:
            raise ValueError("Configuration not loaded")
        
        env_config = self.config.get('environments', {}).get(env, {})
        base_url = env_config.get('base_url', '')
        
        if not base_url:
            raise ValueError(f"Base URL not found for environment: {env}")
        
        return base_url
    
    def get_environment_config(self, environment: Optional[str] = None) -> Dict[str, Any]:
        """
        Get full configuration for the specified or current environment
        
        Args:
            environment: Environment name. If None, uses current environment.
            
        Returns:
            dict: Complete environment configuration
        """
        env = environment or self.current_environment
        
        if not env:
            raise ValueError("No environment specified and no current environment set")
        
        if not self.config:
            raise ValueError("Configuration not loaded")
        
        return self.config.get('environments', {}).get(env, {})
    
    def get_load_configuration(self, load_config_name: str) -> Dict[str, Any]:
        """
        Get load configuration template (users, spawn_rate, duration, etc.)
        
        Args:
            load_config_name: Load configuration name (light_load, medium_load, etc.)
            
        Returns:
            dict: Load configuration template
        """
        if not self.config:
            raise ValueError("Configuration not loaded")
        
        load_configs = self.config.get('load_configurations', {})
        if load_config_name not in load_configs:
            available_configs = list(load_configs.keys())
            raise ValueError(f"Load configuration '{load_config_name}' not found. Available: {available_configs}")
        
        return load_configs[load_config_name]
    
    def get_endpoint_config(self, endpoint_name: str) -> Dict[str, Any]:
        """
        Get API endpoint configuration
        
        Args:
            endpoint_name: Endpoint name (original, v1, v2, etc.)
            
        Returns:
            dict: Endpoint configuration with path, name, description
        """
        if not self.config:
            raise ValueError("Configuration not loaded")
        
        endpoints = self.config.get('api_endpoints', {})
        if endpoint_name not in endpoints:
            available_endpoints = list(endpoints.keys())
            raise ValueError(f"Endpoint '{endpoint_name}' not found. Available: {available_endpoints}")
        
        return endpoints[endpoint_name]
    
    def get_api_config(self) -> Dict[str, Any]:
        """
        Get API configuration settings
        
        Returns:
            dict: API configuration
        """
        if not self.config:
            raise ValueError("Configuration not loaded")
        
        return self.config.get('api', {})
    
    def get_api_endpoint(self, test_config: Optional[Dict[str, Any]] = None) -> str:
        """
        Get the API endpoint path, optionally from test configuration
        
        Args:
            test_config: Optional test configuration that may contain custom endpoint
            
        Returns:
            str: API endpoint path
        """
        # If test config has an endpoint, use it
        if test_config and 'endpoint' in test_config:
            return test_config['endpoint']
        
        # Otherwise use the global API endpoint
        api_config = self.get_api_config()
        return api_config.get('endpoint', '/Ambient/generate_summary_html')
    
    def get_full_api_url(self, environment: Optional[str] = None, test_config: Optional[Dict[str, Any]] = None) -> str:
        """
        Get the complete API URL (base_url + endpoint) for the environment
        
        Args:
            environment: Environment name. If None, uses current environment.
            test_config: Optional test configuration that may contain custom endpoint
            
        Returns:
            str: Complete API URL
        """
        base_url = self.get_base_url(environment)
        endpoint = self.get_api_endpoint(test_config)
        return f"{base_url}{endpoint}"
    
    def get_common_headers(self) -> Dict[str, Dict[str, str]]:
        """
        Get common headers configuration
        
        Returns:
            dict: Common headers configuration with all header templates
        """
        if not self.config:
            raise ValueError("Configuration not loaded")
        
        return self.config.get('common_headers', {})
    
    def get_headers_from_template(self, template_name: str) -> Dict[str, str]:
        """
        Get headers from a specific template with dynamic authentication support
        
        Args:
            template_name: Name of the header template (e.g., 'basic', 'ambient_standard')
            
        Returns:
            dict: Headers from the specified template (with dynamic auth for QA if enabled)
            
        Raises:
            ValueError: If template is not found
        """
        if not self.config:
            raise ValueError("Configuration not loaded")
        
        common_headers = self.get_common_headers()
        
        if template_name not in common_headers:
            available_templates = list(common_headers.keys())
            raise ValueError(f"Header template '{template_name}' not found. Available templates: {available_templates}")
        
        headers = common_headers[template_name].copy()
        
        # Apply dynamic authentication for QA environment templates
        if (DYNAMIC_AUTH_AVAILABLE and auth_service and 
            template_name in ['qinsight_qa', 'qinsight_analytics_qa'] and 
            self.current_environment == 'qa'):
            
            print(f"🔐 Applying dynamic authentication for template: {template_name}")
            headers = auth_service.get_dynamic_headers_for_qa(headers)
        
        return headers
    
    def resolve_api_headers(self, api_config: Dict[str, Any]) -> Dict[str, str]:
        """
        Resolve headers for an API configuration by merging template headers with custom headers
        
        Args:
            api_config: API configuration dictionary that may contain headers_template and custom_headers
            
        Returns:
            dict: Resolved headers combining template and custom headers
        """
        if not self.config:
            raise ValueError("Configuration not loaded")
        
        headers = {}
        
        # Get headers from template if specified
        headers_template = api_config.get('headers_template')
        if headers_template:
            try:
                # Try environment-specific template first
                env_specific_template = self.get_environment_specific_template(headers_template)
                if env_specific_template:
                    template_headers = self.get_headers_from_template(env_specific_template)
                    headers.update(template_headers)
                    print(f"✅ Loaded environment-specific headers from template: {env_specific_template}")
                else:
                    # Fall back to original template
                    template_headers = self.get_headers_from_template(headers_template)
                    headers.update(template_headers)
                    print(f"✅ Loaded headers from template: {headers_template}")
                    
            except ValueError as e:
                print(f"⚠️ Warning: {e}")
                # Fall back to default template if available
                try:
                    default_headers = self.get_headers_from_template('basic_no_auth')
                    headers.update(default_headers)
                    print(f"✅ Loaded headers from fallback template: basic_no_auth")
                except ValueError:
                    print(f"⚠️ No fallback header template available")
        
        # Merge custom headers if specified
        custom_headers = api_config.get('custom_headers', {})
        if custom_headers:
            headers.update(custom_headers)
            print(f"✅ Merged custom headers: {list(custom_headers.keys())}")
        
        # Legacy support: if neither template nor custom headers, try legacy headers field
        if not headers and 'headers' in api_config:
            headers = api_config['headers'].copy()
            print(f"✅ Using legacy headers configuration")
        
        return headers
    
    def get_environment_specific_template(self, base_template: str) -> Optional[str]:
        """
        Get environment-specific header template name based on current environment
        
        Args:
            base_template: Base template name (e.g., 'qinsight_qa', 'ambient_v1_qa')
            
        Returns:
            str: Environment-specific template name or None if not found
        """
        if not self.current_environment:
            return None
        
        common_headers = self.get_common_headers()
        
        # Check if the base template already includes environment
        if base_template in common_headers:
            # If template already has environment suffix, check if it matches current env
            if base_template.endswith(f"_{self.current_environment}"):
                return base_template
            
            # If template has different environment suffix, try to find matching one
            for env in ['qa', 'dev', 'staging', 'production']:
                if base_template.endswith(f"_{env}"):
                    # Replace the environment suffix
                    base_name = base_template[:-len(f"_{env}")]
                    env_specific = f"{base_name}_{self.current_environment}"
                    if env_specific in common_headers:
                        return env_specific
                    break
        
        # Try to construct environment-specific template name
        possible_templates = [
            f"{base_template}_{self.current_environment}",
            base_template,  # Original template as fallback
        ]
        
        # For templates that don't have environment suffix, try to add it
        if not any(base_template.endswith(f"_{env}") for env in ['qa', 'dev', 'staging', 'production']):
            # Check if there's an environment-specific variant
            env_template = f"{base_template}_{self.current_environment}"
            if env_template in common_headers:
                return env_template
        
        # Return the template that exists
        for template in possible_templates:
            if template in common_headers:
                return template
        
        return None
    
    def get_environment_aware_api_configuration(self, api_name: str) -> Dict[str, Any]:
        """
        Get a specific API configuration with environment-aware header resolution
        
        Args:
            api_name: Name of the API configuration
            
        Returns:
            dict: API configuration with environment-specific resolved headers
        """
        api_config = self.get_api_configuration(api_name)
        
        # The headers are already resolved in get_api_configuration, 
        # but let's ensure they're environment-specific
        if self.current_environment:
            headers_template = api_config.get('headers_template')
            if headers_template:
                env_specific_template = self.get_environment_specific_template(headers_template)
                if env_specific_template and env_specific_template != headers_template:
                    # Re-resolve with environment-specific template
                    resolved_headers = self.resolve_api_headers(api_config)
                    api_config['resolved_headers'] = resolved_headers
                    print(f"🌐 Using environment-specific headers for {self.current_environment}")
        
        return api_config
    
    def get_api_configurations(self) -> Dict[str, Dict[str, Any]]:
        """
        Get API configurations with resolved headers
        
        Returns:
            dict: API configurations with headers resolved from templates
        """
        if not self.config:
            raise ValueError("Configuration not loaded")
        
        api_configs = self.config.get('api_configurations', {}).copy()
        
        # Resolve headers for each API configuration
        for api_name, api_config in api_configs.items():
            resolved_headers = self.resolve_api_headers(api_config)
            if resolved_headers:
                api_configs[api_name]['resolved_headers'] = resolved_headers
        
        return api_configs
    
    def get_api_configuration(self, api_name: str) -> Dict[str, Any]:
        """
        Get a specific API configuration with resolved headers
        
        Args:
            api_name: Name of the API configuration (e.g., 'original', 'v1', 'charges_analysis')
            
        Returns:
            dict: API configuration with resolved headers
            
        Raises:
            ValueError: If API configuration is not found
        """
        if not self.config:
            raise ValueError("Configuration not loaded")
        
        api_configs = self.config.get('api_configurations', {})
        
        if api_name not in api_configs:
            available_apis = list(api_configs.keys())
            raise ValueError(f"API configuration '{api_name}' not found. Available APIs: {available_apis}")
        
        api_config = api_configs[api_name].copy()
        
        # Resolve headers for this specific API
        resolved_headers = self.resolve_api_headers(api_config)
        if resolved_headers:
            api_config['resolved_headers'] = resolved_headers
        
        return api_config
    
    def get_environment_description(self, environment: Optional[str] = None) -> str:
        """
        Get description for the specified or current environment
        
        Args:
            environment: Environment name. If None, uses current environment.
            
        Returns:
            str: Environment description
        """
        env_config = self.get_environment_config(environment)
        return env_config.get('description', f'Environment: {environment or self.current_environment}')


# Global configuration loader instance
_config_loader = None

def get_config_loader() -> EnvironmentConfigLoader:
    """
    Get the global configuration loader instance (singleton pattern)
    
    Returns:
        EnvironmentConfigLoader: Global configuration loader instance
    """
    global _config_loader
    if _config_loader is None:
        _config_loader = EnvironmentConfigLoader()
        # Set default environment if available
        available_envs = _config_loader.list_environments()
        if available_envs:
            default_env = _config_loader.config.get('execution', {}).get('default_environment', available_envs[0])
            _config_loader.set_environment(default_env)
    
    return _config_loader

# Alias for backward compatibility
ConfigLoader = EnvironmentConfigLoader 