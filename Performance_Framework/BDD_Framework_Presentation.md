# Separated API Performance Testing Framework
## Comprehensive Architecture and Implementation Guide

---

## Slide 1: Title Slide
Separated API Performance Testing Framework
Comprehensive Architecture and Implementation Guide

Independent Frameworks for Ambient and QInsight APIs
- Locust-Based Performance Testing
- Separated Configuration Management
- Enhanced Automated Report Generation
- Multi-Environment Support
- Professional Test Orchestration

Presented by: Performance Engineering Team
Date: January 2025

---

## Slide 2: Framework Overview
Separated Framework Architecture Overview

Core Objectives
- API Separation: Independent frameworks for Ambient and QInsight APIs
- Load Testing: Comprehensive testing with Locust for both APIs
- Multi-Environment: Support for Dev, QA, Staging, Production
- Enhanced Reporting: Professional HTML reports with comprehensive metrics
- Configuration Management: API-specific YAML-based configuration
- System Monitoring: Built-in CPU and memory monitoring

Technology Stack
- Python 3.8+: Core framework language
- Locust: Performance testing engine (BDD removed)
- YAML: Configuration management
- HTML: Professional enhanced reporting
- psutil: System resource monitoring
- Separated Architecture: Independent Ambient and QInsight systems

---

## Slide 3: Project Structure
Separated Project Structure

```
BDD_Framework/
├── config/
│   ├── ambient_config.yaml              # Ambient API configuration
│   └── qinsight_config.yaml             # QInsight API configuration
├── tests/
│   ├── ambient_api_locust.py            # Ambient API Locust tests
│   └── qinsight_api_locust.py           # QInsight API Locust tests
├── utils/
│   └── config_loader.py                 # Shared configuration utility
├── reports/                             # Generated reports (HTML/PDF)
├── logs/                                # Test execution logs
├── ambient_run_performance_test.py      # Ambient API test runner
├── qinsight_run_performance_test.py     # QInsight API test runner
├── README_SEPARATED_FRAMEWORK.md        # Separated framework documentation
└── requirements.txt                     # Dependencies (behave removed)
```

Key Changes from Previous Architecture:
- ❌ BDD framework completely removed
- ✅ Separated API-specific configurations
- ✅ Independent test runners for each API
- ✅ Enhanced comprehensive HTML reporting
- ✅ Streamlined Locust-only architecture

---

## Slide 4: Configuration Management - Ambient API
Ambient API Configuration: ambient_config.yaml

Multi-Environment Support
```yaml
environments:
  dev:
    base_url: "https://innovationz-dev.myqone.com"
    timeout: 30
    verify_ssl: true
    description: "Dev Environment for Ambient API testing"
  
  qa:
    base_url: "https://innovationz-qa.myqone.com"
    timeout: 30
    verify_ssl: true
    description: "QA Environment for Ambient API testing"
  
  production:
    base_url: "https://innovationz.myqone.com"
    timeout: 30
    verify_ssl: true
    description: "Production Environment - use with caution"
```

Load Test Configurations
```yaml
load_configurations:
  light_load:
    users: 20
    spawn_rate: 5
    duration: "90s"
    description: "Light load testing - baseline validation"
    expected_rps: 1.0
    max_response_time: 20000
    max_error_rate: 5.0
    
  medium_load:
    users: 30
    spawn_rate: 5
    duration: "90s"
    description: "Medium load testing - standard validation"
    
  heavy_load:
    users: 40
    spawn_rate: 5
    duration: "90s"
    description: "Heavy load testing - stress testing"
```

API Configurations
```yaml
api_configurations:
  original:
    name: "Original Ambient API"
    description: "Original Ambient API endpoint"
    method: "POST"
    endpoint: "/Ambient/generate_summary_html"
    headers:
      Content-Type: "application/json"
      User-Agent: "Ambient-Performance-Testing-Framework/1.0"
    
  v1:
    name: "Ambient API V1"
    description: "Version 1 of Ambient API"
    method: "POST"
    endpoint: "/Ambient/generate_summary_html_v1"
    headers:
      Content-Type: "application/json"
      User-Agent: "Ambient-Performance-Testing-Framework/1.0"
```

---

## Slide 5: Configuration Management - QInsight API
QInsight API Configuration: qinsight_config.yaml

Multi-Environment Support
```yaml
environments:
  dev:
    base_url: "https://qinsight-dev.myqone.com"
    timeout: 45
    verify_ssl: true
    description: "QInsight Dev Environment for analytics testing"
  
  qa:
    base_url: "https://qinsight-qa.myqone.com"
    timeout: 45
    verify_ssl: true
    description: "QInsight QA Environment for analytics testing"
```

API Configuration with Authentication
```yaml
api_configurations:
  charges_analysis:
    name: "QInsight Charges Analysis API"
    description: "API for analyzing charges by CPT codes and practice metrics"
    method: "POST"
    endpoint: "/restservicefmetrics/ChargesAnalysisByCPT"
    headers:
      Content-Type: "application/json"
      User-Agent: "QInsight-Performance-Testing-Framework/1.0"
      Accept: "application/json"
      Authorization: "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
    timeout: 45
    retry_attempts: 3
    retry_delay: 2
    payload:
      clientkey: "QinsightQAData"
      practicelist:
        - "GCPBQDEMO4"
        - "GCPBQDEMO1"
```

Performance Thresholds (Analytics-Specific)
```yaml
thresholds:
  response_time:
    excellent: 15000     # ms - Analytics workload expectations
    good: 25000         # ms - Acceptable for complex analytics
    acceptable: 40000   # ms - Warning threshold for analytics
    critical: 60000     # ms - Critical threshold
    timeout: 90000      # ms - Extended timeout for analytics
  
  throughput:
    minimum: 0.3        # req/sec - Minimum for analytics
    good: 0.8          # req/sec - Good for analytics workload
    excellent: 1.2     # req/sec - Excellent for analytics
```

---

## Slide 6: Test Runner Architecture
Independent Test Runner Architecture

Ambient API Runner: ambient_run_performance_test.py
```python
class AmbientPerformanceTestRunner:
    """Ambient API Performance Test Runner - Locust-based load testing"""
    
    def __init__(self, config_file=None, environment=None):
        # Load ambient_config.yaml specifically
        config_file = config_file or self.config_dir / "ambient_config.yaml"
        self.config_loader = ConfigLoader(config_file)
        self.environment = environment or "qa"
        
    def run_locust_test(self, test_config_name="light_load"):
        """Run Locust performance test for Ambient API"""
        # Get Ambient-specific configuration
        # Execute Locust with ambient_api_locust.py
        # Generate Ambient-branded reports
```

QInsight API Runner: qinsight_run_performance_test.py
```python
class QInsightPerformanceTestRunner:
    """QInsight API Performance Test Runner - Locust-based load testing"""
    
    def __init__(self, config_file=None, environment=None):
        # Load qinsight_config.yaml specifically
        config_file = config_file or self.config_dir / "qinsight_config.yaml"
        self.config_loader = ConfigLoader(config_file)
        self.environment = environment or "qa"
        
    def run_locust_test(self, test_config_name="light_load"):
        """Run Locust performance test for QInsight API"""
        # Get QInsight-specific configuration
        # Execute Locust with qinsight_api_locust.py
        # Generate QInsight-branded reports
```

Key Benefits of Separation:
- ✅ Independent configurations prevent cross-API conflicts
- ✅ API-specific optimizations and thresholds
- ✅ Separate development and maintenance cycles
- ✅ Specialized reporting for each API type
- ✅ Independent scaling and resource management

---

## Slide 7: Locust Implementation - Ambient API
Ambient API Locust Implementation: ambient_api_locust.py

Enhanced Metrics Collection Platform
```python
class PerformanceMetrics:
    def __init__(self):
        self.cpu_usage = []
        self.memory_usage = []
        self.response_times = []
        self.error_count = 0
        self.total_requests = 0
        self.successful_requests = 0
        self.failed_requests = 0
        self.request_timestamps = []
        self.error_details = []
        self.start_time = None
        self.end_time = None
        self.user_count = 0
        self.endpoint_name = "original"
        self.endpoint_path = "/Ambient/generate_summary_html"

# Global metrics instance
metrics = PerformanceMetrics()

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    """Initialize comprehensive metrics at test start"""
    global metrics
    metrics = PerformanceMetrics()
    metrics.start_time = datetime.now()
    metrics.user_count = environment.parsed_options.num_users
    
@events.request.add_listener
def on_request(request_type, name, response_time, response_length, exception, **kwargs):
    """Enhanced request metrics capture with detailed error tracking"""
    metrics.total_requests += 1
    metrics.response_times.append(response_time)
    
    if exception:
        metrics.error_count += 1
        metrics.failed_requests += 1
        # Capture detailed error information
        error_info = {
            'timestamp': datetime.now().isoformat(),
            'request_type': request_type,
            'name': name,
            'response_time': response_time,
            'exception': str(exception)
        }
        metrics.error_details.append(error_info)
    else:
        metrics.successful_requests += 1

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    """Generate comprehensive Ambient performance report at test end"""
    # Calculate comprehensive performance metrics
    # Generate enhanced HTML report with Ambient branding
    # Print comprehensive summary
    generate_enhanced_html_report(...)
    print_comprehensive_summary(...)
```

---

## Slide 8: Locust Implementation - QInsight API
QInsight API Locust Implementation: qinsight_api_locust.py

QInsight-Specific User Behavior
```python
class QInsightAPIUser(HttpUser):
    """Enhanced QInsight API User with realistic behavior patterns"""
    wait_time = between(1, 3)
    
    def __init__(self, *args, **kwargs):
        """Initialize user with QInsight configuration"""
        super().__init__(*args, **kwargs)
        self.load_configuration()
        
        # QInsight-specific setup
        self.api_endpoint = os.environ.get('LOCUST_API_ENDPOINT', 
                                         '/restservicefmetrics/ChargesAnalysisByCPT')
        self.environment_name = os.environ.get('LOCUST_ENVIRONMENT', 'qa')
        self.endpoint_name = os.environ.get('LOCUST_ENDPOINT_NAME', 'charges_analysis')
    
    def load_configuration(self):
        """Load QInsight configuration from qinsight_config.yaml"""
        if ConfigLoader:
            try:
                config_path = project_root / "config" / "qinsight_config.yaml"
                config_loader = ConfigLoader(config_path)
                
                # Get API configuration for charges_analysis
                api_configs = config_loader.config.get('api_configurations', {})
                charges_config = api_configs.get('charges_analysis', {})
                
                self.headers = charges_config.get('headers', {})
                self.payload = charges_config.get('payload', {})
                self.timeout = charges_config.get('timeout', 45)
                self.method = charges_config.get('method', 'POST').upper()
            except Exception as e:
                print(f"⚠️ Error loading configuration: {e}")
                # Fallback configuration
    
    @task(1)
    def charges_analysis_request(self):
        """Main task: Submit charges analysis request to QInsight API"""
        monitor_system_resources()
        
        # Get payload for this request
        payload = self.get_test_payload()
        
        try:
            with self.client.post(
                self.api_endpoint,
                json=payload,
                headers=self.headers,
                timeout=self.timeout,
                name=f"POST {self.api_endpoint}",
                catch_response=True
            ) as response:
                success = self.validate_response(response)
                if success:
                    response.success()
                else:
                    response.failure(f"Response validation failed")
        except Exception as e:
            print(f"❌ Request failed with exception: {e}")
```

---

## Slide 9: Enhanced Reporting System
Professional Enhanced HTML Reporting

Ambient API Reports
```python
def generate_enhanced_html_report(...):
    """Generate enhanced HTML performance report for Ambient API"""
    
    # Ambient-specific performance assessment
    if error_rate < 1 and avg_response_time < 10000:
        overall_status = "🌟 EXCELLENT"
        status_color = "#27ae60"
    elif error_rate < 5 and avg_response_time < 20000:
        overall_status = "✅ GOOD"
        status_color = "#2980b9"
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>🚀 Ambient API Performance Report - {user_count} Users</title>
        <style>
            /* Professional CSS styling with Ambient branding */
            .header {{ background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%); }}
            .metric-card {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🚀 Ambient API Performance Report</h1>
                <h2>Load Test with {user_count} Concurrent Users</h2>
            </div>
            <!-- Comprehensive Ambient-specific metrics and analysis -->
        </div>
    </body>
    </html>
    """
```

QInsight API Reports
```python
def generate_enhanced_qinsight_html_report(...):
    """Generate enhanced HTML performance report for QInsight with analytics focus"""
    
    # QInsight-specific performance assessment (analytics workload)
    if error_rate < 1 and avg_response_time < 15000:
        overall_status = "🌟 EXCELLENT"
        status_color = "#27ae60"
    elif error_rate < 5 and avg_response_time < 25000:
        overall_status = "✅ GOOD"
        status_color = "#2980b9"
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>🔍 QInsight API Performance Report - {user_count} Users</title>
        <!-- QInsight-specific styling and branding -->
    </head>
    <body>
        <!-- QInsight analytics-focused reporting -->
        <div class="test-config">
            <h3>📋 QInsight API Test Details</h3>
            <p><strong>Endpoint:</strong> {endpoint_path}</p>
            <p><strong>Method:</strong> POST</p>
            <p><strong>Test Type:</strong> Analytics Load Testing</p>
            
            <h4>📨 Request Payload Sample:</h4>
            <div class="payload-box">{{
                "clientkey": "QinsightQAData",
                "practicelist": [
                    "GCPBQDEMO4",
                    "GCPBQDEMO1"
                ]
            }}</div>
        </div>
        <!-- Analytics-specific performance metrics and thresholds -->
    </body>
    </html>
    """
```

---

## Slide 10: Configuration Integration
Unified Configuration Management with API Separation

Configuration Loader Integration
```python
class ConfigLoader:
    """Unified configuration loader supporting both APIs"""
    
    def __init__(self, config_file):
        """Initialize with API-specific configuration file"""
        self.config_file = config_file  # ambient_config.yaml or qinsight_config.yaml
        self.config = None
        self.current_environment = None
        self.load_config()
    
    def get_api_configurations(self):
        """Get API-specific configurations"""
        return self.config.get('api_configurations', {})
    
    def get_endpoint_config(self, endpoint_name):
        """Get specific endpoint configuration"""
        api_configs = self.get_api_configurations()
        return api_configs.get(endpoint_name, {})
    
    def get_load_configuration(self, config_name):
        """Get load test configuration"""
        load_configs = self.config.get('load_configurations', {})
        return load_configs.get(config_name, {})
```

Environment-Specific Usage
```python
# Ambient API Usage
ambient_runner = AmbientPerformanceTestRunner()
ambient_runner.run_locust_test('light_load', 'qa')
# → Uses ambient_config.yaml
# → Executes ambient_api_locust.py
# → Generates Ambient-branded reports

# QInsight API Usage
qinsight_runner = QInsightPerformanceTestRunner()
qinsight_runner.run_locust_test('light_load', 'qa')
# → Uses qinsight_config.yaml
# → Executes qinsight_api_locust.py
# → Generates QInsight-branded reports
```

---

## Slide 11: Command Line Interface
Independent Command Line Interfaces

Ambient API CLI
```bash
# Basic Ambient API testing
python ambient_run_performance_test.py --test light_load --environment qa

# Custom Ambient API configuration
python ambient_run_performance_test.py --test medium_load --environment qa --users 25 --duration 120s

# List available Ambient configurations
python ambient_run_performance_test.py --list
```

QInsight API CLI
```bash
# Basic QInsight API testing
python qinsight_run_performance_test.py --test light_load --environment qa

# Custom QInsight API configuration
python qinsight_run_performance_test.py --test heavy_load --environment qa --users 30 --duration 180s

# List available QInsight configurations
python qinsight_run_performance_test.py --list
```

Parallel Testing Capability
```bash
# Run both APIs simultaneously in different terminals
Terminal 1: python ambient_run_performance_test.py --test light_load --environment qa
Terminal 2: python qinsight_run_performance_test.py --test light_load --environment qa

# Independent execution with no conflicts
# Separate reports generated for each API
# Independent resource monitoring and analysis
```

---

## Slide 12: Architecture Benefits
Separated Framework Architecture Benefits

API Isolation Benefits
- **Independent Development**: Each API can evolve independently without affecting the other
- **Specialized Optimization**: API-specific performance thresholds and configurations
- **Reduced Complexity**: Simpler configuration management without API mixing
- **Clear Responsibility**: Each team can own their API's performance testing

Technical Benefits
- **No Cross-API Conflicts**: Separate configurations prevent configuration interference
- **Optimized Resource Usage**: Each framework optimized for its specific API requirements
- **Simplified Debugging**: Issues isolated to specific API without cross-contamination
- **Enhanced Maintainability**: Smaller, focused codebases easier to maintain

Performance Benefits
- **API-Specific Thresholds**: Ambient (web UI) vs QInsight (analytics) have different performance expectations
- **Specialized Monitoring**: Each API monitored with appropriate metrics and validation
- **Independent Scaling**: Each API can be scaled and optimized independently
- **Targeted Optimization**: Performance improvements focused on specific API characteristics

Business Benefits
- **Faster Development**: Independent teams can work without coordination overhead
- **Risk Reduction**: Issues in one API don't impact testing of the other
- **Specialized Expertise**: Teams can develop deep expertise in their specific API
- **Clear Ownership**: Clear accountability for performance testing results

Operational Benefits
- **Independent Deployment**: Each framework can be deployed and updated independently
- **Separate Reporting**: Stakeholders get focused reports relevant to their API
- **Flexible Scheduling**: Tests can be scheduled independently based on API requirements
- **Resource Optimization**: Testing resources allocated based on API-specific needs

---

## Slide 13: Usage Examples & Best Practices
Practical Usage Examples

Ambient API Testing Workflow
```bash
# 1. Baseline Performance Validation
python ambient_run_performance_test.py --test light_load --environment qa

# 2. Progressive Load Testing
python ambient_run_performance_test.py --test medium_load --environment qa
python ambient_run_performance_test.py --test heavy_load --environment qa

# 3. Custom Load Testing
python ambient_run_performance_test.py --users 35 --spawn-rate 7 --duration 180s --environment qa

# 4. Production Validation (with caution)
python ambient_run_performance_test.py --test light_load --environment production
```

QInsight API Testing Workflow
```bash
# 1. Analytics Baseline Validation
python qinsight_run_performance_test.py --test light_load --environment qa

# 2. Analytics Load Progression
python qinsight_run_performance_test.py --test medium_load --environment qa
python qinsight_run_performance_test.py --test heavy_load --environment qa

# 3. Extended Analytics Testing
python qinsight_run_performance_test.py --users 20 --duration 300s --environment qa

# 4. QInsight Staging Validation
python qinsight_run_performance_test.py --test light_load --environment staging
```

Best Practices

Configuration Management
- Maintain separate configurations for each API to prevent conflicts
- Use environment-specific settings appropriate for each API type
- Regular configuration reviews to ensure optimal thresholds
- Version control all configuration changes with clear documentation

Test Strategy
- Start with light load tests for baseline establishment
- Progress through load levels systematically
- Use appropriate environments for each testing phase
- Consider API-specific characteristics (Ambient: UI response, QInsight: Analytics processing)

Report Analysis
- Review HTML reports for detailed technical metrics
- Focus on API-appropriate performance thresholds
- Track performance trends over time for each API
- Share reports with appropriate stakeholders

---

## Slide 14: Migration from BDD Framework
Migration Guide from Previous BDD Framework

What Was Removed
- ❌ **BDD Framework (Behave)**: All Gherkin scenarios and step definitions
- ❌ **Feature Files**: Business-readable test scenarios
- ❌ **Step Definitions**: BDD implementation bridge
- ❌ **Unified Configuration**: Single test_config.yaml file
- ❌ **Mixed API Testing**: Combined Ambient/QInsight in single framework
- ❌ **BDD Dependencies**: behave package and related dependencies

What Was Added
- ✅ **Separated APIs**: Independent Ambient and QInsight frameworks
- ✅ **API-Specific Configurations**: ambient_config.yaml and qinsight_config.yaml
- ✅ **Independent Runners**: Dedicated test runners for each API
- ✅ **Enhanced Reporting**: Comprehensive HTML reports with advanced metrics
- ✅ **API-Specific Optimizations**: Tailored thresholds and monitoring
- ✅ **Streamlined Architecture**: Pure Locust-based testing

Migration Process
1. **Configuration Migration**: Split existing test_config.yaml into API-specific files
2. **Test Runner Updates**: Replace unified runner with API-specific runners
3. **Dependencies Update**: Remove behave, add pathlib2 for enhanced functionality
4. **Report Updates**: Leverage new enhanced HTML reporting capabilities
5. **Team Training**: Update team procedures for separated framework usage

Benefits of Migration
- **Simplified Architecture**: Removed complexity of BDD integration
- **Focused Testing**: Each API gets specialized attention and optimization
- **Enhanced Performance**: Pure Locust implementation with advanced metrics
- **Better Separation**: Clear boundaries between different API testing
- **Improved Maintainability**: Smaller, focused codebases

---

## Slide 15: Enhanced Reporting Features
Advanced Reporting Capabilities

Comprehensive Metrics Collection
- **Response Time Analysis**: Min, Max, Average, Median, Percentiles (50th, 75th, 90th, 95th, 99th)
- **Throughput Metrics**: Requests per second, concurrent user handling
- **Error Analysis**: Error rates, error categorization, detailed error tracking
- **System Resources**: CPU usage, memory utilization, system health monitoring
- **Performance Trends**: Historical comparison and trend analysis

Professional Report Features
- **Executive Summaries**: High-level performance assessment and recommendations
- **Technical Deep-Dives**: Detailed metrics analysis for development teams
- **Visual Design**: Professional styling with API-specific branding
- **Interactive Elements**: Responsive design suitable for different devices
- **Performance Grading**: Automated performance assessment (Excellent, Good, Needs Improvement, Critical)

API-Specific Reporting
- **Ambient Reports**: Focus on web UI performance characteristics
- **QInsight Reports**: Emphasis on analytics workload performance
- **Specialized Thresholds**: API-appropriate performance expectations
- **Contextual Recommendations**: API-specific optimization suggestions

Report Generation Pipeline
1. **Real-Time Metrics Collection**: During test execution
2. **Comprehensive Analysis**: Statistical analysis and performance calculation
3. **Professional Formatting**: HTML generation with professional styling
4. **Automated Assessment**: Performance grading and recommendation generation
5. **Report Storage**: Organized file naming and report archival

---

## Slide 16: Future Enhancements & Roadmap
Framework Evolution and Enhancement Plans

Planned Enhancements

CI/CD Integration
```yaml
# GitHub Actions Integration
name: Ambient API Performance Testing
on:
  push:
    branches: [main]
jobs:
  performance-test:
    runs-on: ubuntu-latest
    steps:
      - name: Run Ambient Performance Tests
        run: python ambient_run_performance_test.py --test light_load --environment staging
      - name: Run QInsight Performance Tests
        run: python qinsight_run_performance_test.py --test light_load --environment staging
```

Advanced Analytics
- **Machine Learning Integration**: Predictive performance analysis
- **Anomaly Detection**: Automated identification of performance anomalies
- **Performance Forecasting**: Predictive capacity planning and scaling recommendations
- **Intelligent Alerting**: Smart alerts based on performance trends and patterns

Framework Extensions
- **Additional APIs**: Easy framework extension for new APIs
- **Custom Metrics**: Extensible metrics collection framework
- **Plugin Architecture**: Support for custom plugins and extensions
- **Integration APIs**: Programmatic access to framework capabilities

Monitoring Integration
```yaml
integrations:
  grafana:
    enabled: true
    dashboard_url: "https://grafana.company.com/performance"
  
  datadog:
    enabled: true
    api_key: "performance-monitoring-key"
  
  slack:
    enabled: true
    webhook_url: "https://hooks.slack.com/performance-alerts"
    channel: "#performance-engineering"
```

Enhanced Features
- **Real-Time Monitoring**: Live performance dashboards during test execution
- **Automated Baseline Management**: Dynamic performance baseline establishment
- **Multi-Region Testing**: Support for testing across different geographical regions
- **Performance Budgets**: Automated performance budget enforcement

---

## Slide 17: Team Adoption Guide
Framework Adoption and Team Integration

Team Roles and Responsibilities

Performance Engineers
- **Framework Maintenance**: Configuration updates and framework enhancements
- **Threshold Management**: Performance criteria definition and updates
- **Report Analysis**: Deep-dive performance analysis and optimization recommendations
- **Training**: Team education and best practices development

Development Teams
- **API-Specific Testing**: Regular performance validation for their APIs
- **Performance Integration**: Integration of performance testing into development workflows
- **Issue Resolution**: Performance issue identification and resolution
- **Optimization**: Performance optimization based on testing insights

QA Teams
- **Test Execution**: Regular performance test execution across environments
- **Validation**: Performance criteria validation and regression testing
- **Documentation**: Test results documentation and trend tracking
- **Quality Gates**: Performance quality gate implementation and enforcement

DevOps Teams
- **Infrastructure**: Framework infrastructure management and optimization
- **CI/CD Integration**: Automated testing pipeline integration
- **Monitoring**: Performance monitoring and alerting setup
- **Environment Management**: Test environment provisioning and management

Adoption Process
1. **Team Training**: Framework capabilities and usage training
2. **Environment Setup**: Framework installation and configuration
3. **Initial Baselines**: Establish performance baselines for each API
4. **Integration Planning**: CI/CD and workflow integration planning
5. **Gradual Rollout**: Phased adoption with support and feedback

Success Metrics
- **Test Coverage**: Percentage of APIs covered by performance testing
- **Issue Detection**: Number of performance issues identified before production
- **Response Time**: Time from issue detection to resolution
- **Team Adoption**: Framework usage across different teams

---

## Slide 18: Framework Summary & Quick Start
Framework Summary & Getting Started

Architecture Summary
Independent API Frameworks
- **Ambient Framework**: Web UI performance testing with appropriate thresholds
- **QInsight Framework**: Analytics performance testing with extended timeouts
- **Shared Utilities**: Common configuration management and reporting capabilities
- **Enhanced Reporting**: Professional HTML reports with comprehensive metrics
- **Flexible Configuration**: API-specific configurations with environment support

Integration Flow
```
API-Specific Config → Test Runner → Locust Execution → Enhanced Reports
        ↑                ↑               ↑                ↑
ambient_config.yaml → ambient_runner → ambient_locust → Ambient HTML
qinsight_config.yaml → qinsight_runner → qinsight_locust → QInsight HTML
```

Key Success Factors
Comprehensive Coverage
- Multi-environment support (Dev, QA, Staging, Production)
- Multiple test types (Light, Medium, Heavy, Stress, Custom)
- Professional reporting with actionable insights
- Real-time system monitoring and resource tracking

Developer Experience
- Single command execution for each API
- Clear, separated configuration management
- Detailed error handling and comprehensive logging
- Flexible test customization and parameter overrides

Business Value
- API-specific performance validation and optimization
- Professional reports suitable for stakeholder communication
- Automated performance validation and regression detection
- Proactive performance monitoring and capacity planning

Quick Start Guide
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run your first Ambient test
python ambient_run_performance_test.py --test light_load --environment qa

# 3. Run your first QInsight test
python qinsight_run_performance_test.py --test light_load --environment qa

# 4. Review generated reports
# Check reports/ directory for API-specific HTML outputs

# 5. Scale up testing
python ambient_run_performance_test.py --test heavy_load --environment qa
python qinsight_run_performance_test.py --test heavy_load --environment qa
```

---

## Slide 19: Q&A and Contact Information
Questions & Contact Information

Thank You!
Questions & Discussion

Framework Repository: BDD_Framework/ (now Separated API Framework)
Documentation: README_SEPARATED_FRAMEWORK.md
Configurations: 
- config/ambient_config.yaml
- config/qinsight_config.yaml

Key Contacts
- Performance Engineering Team
- DevOps Team  
- Ambient API Development Team
- QInsight API Development Team

Resources
- Framework Documentation: Complete in README_SEPARATED_FRAMEWORK.md
- Configuration Reference: API-specific YAML files
- Best Practices Guide: Included in framework documentation
- Troubleshooting Guide: Available in documentation

Next Steps
1. **Hands-on Workshop**: Schedule practical framework training for separated architecture
2. **Implementation Planning**: Discuss integration with existing API development workflows
3. **Customization Requirements**: Identify API-specific organizational needs
4. **Performance Baselines**: Establish initial performance benchmarks for both APIs
5. **Team Assignment**: Define team responsibilities for each API framework

Contact Information
- Framework Support: performance-engineering@company.com
- Ambient API Testing: ambient-team@company.com  
- QInsight API Testing: qinsight-team@company.com
- Technical Support: framework-support@company.com

---

End of Presentation 

---

# Appendix: Detailed File Descriptions

## Python Files - Comprehensive Analysis

### 1. ambient_run_performance_test.py
**Primary Purpose:** Main orchestrator and entry point for Ambient API performance testing

**Detailed Description:**
This file serves as the central command and control system for all Ambient API performance testing operations. It provides a professional CLI interface and orchestrates the complete testing lifecycle from configuration loading through test execution to report generation.

**Key Classes:**
```python
class AmbientPerformanceTestRunner:
    """Ambient Performance Test Runner - Locust-based load testing"""
    
    def __init__(self, config_file=None, environment=None):
        # Initialize with ambient_config.yaml
        # Set up directory structure
        # Configure environment settings
        
    def list_available_tests(self):
        # Display available test configurations
        # Show load configurations and environments
        
    def run_locust_test(self, test_config_name="light_load", environment=None, custom_config=None):
        # Main test execution method
        # Build and execute Locust commands
        # Coordinate report generation
        
    def generate_pdf_report(self, html_report_path, environment, config):
        # PDF report generation coordination
        # Call PDF generation utilities
```

**Dependencies:**
- **File Dependencies:**
  - `config/ambient_config.yaml` → Primary configuration source
  - `tests/ambient_api_locust.py` → Test execution target
  - `utils/config_loader.py` → Configuration management
  - `reports/` directory → Report output location
- **Python Dependencies:**
  - `subprocess` → Execute Locust commands
  - `argparse` → Command line interface
  - `pathlib` → File path management
  - `datetime` → Timestamp generation

**Execution Flow:**
1. **Initialization (0-2 seconds):**
   - Load ambient_config.yaml via ConfigLoader
   - Validate environment configuration
   - Set up directory structure (reports/, tests/)
   - Initialize CLI argument parser

2. **Configuration Phase (2-5 seconds):**
   - Parse command line arguments
   - Load test configuration (light_load, medium_load, etc.)
   - Resolve environment settings (dev, qa, staging, production)
   - Build custom configuration overrides if provided

3. **Pre-execution Validation (5-7 seconds):**
   - Validate Locust file exists (ambient_api_locust.py)
   - Check environment connectivity
   - Validate configuration completeness
   - Generate report file names with timestamps

4. **Test Execution Orchestration (7 seconds - test completion):**
   - Build Locust command with parameters
   - Set environment variables for Locust consumption
   - Execute subprocess with comprehensive error handling
   - Monitor test execution progress

5. **Post-execution Processing (test completion + 5-30 seconds):**
   - Validate HTML report generation
   - Trigger PDF report generation if available
   - Print execution summary
   - Return execution status and report paths

**Usage Scenarios:**
```bash
# Basic execution
python ambient_run_performance_test.py --test light_load --environment qa

# Custom configuration
python ambient_run_performance_test.py --users 25 --spawn-rate 5 --duration 120s

# List available options
python ambient_run_performance_test.py --list

# Environment-specific testing
python ambient_run_performance_test.py --test heavy_load --environment staging
```

**Framework Integration:**
- **Entry Point:** First file executed by users or CI/CD systems
- **Orchestration Role:** Coordinates all other framework components
- **Configuration Hub:** Loads and distributes configuration to other components
- **Report Coordinator:** Manages report generation pipeline

**Business Value:**
- Provides single command execution for complex testing workflows
- Abstracts technical complexity from users
- Enables CI/CD integration with proper exit codes
- Supports both interactive and automated execution

---

### 2. qinsight_run_performance_test.py
**Primary Purpose:** Main orchestrator and entry point for QInsight API performance testing

**Detailed Description:**
Dedicated orchestrator for QInsight API performance testing, specifically designed for analytics workloads with extended timeouts and QInsight-specific configurations. Mirrors the ambient runner but with QInsight optimizations.

**Key Classes:**
```python
class QInsightPerformanceTestRunner:
    """QInsight API Performance Test Runner - Analytics-focused load testing"""
    
    def __init__(self, config_file=None, environment=None):
        # Initialize with qinsight_config.yaml
        # Configure analytics-appropriate timeouts
        # Set up QInsight-specific environment
        
    def run_locust_test(self, test_config_name="light_load", environment=None, custom_config=None):
        # QInsight-specific test execution
        # Handle JWT authentication
        # Analytics workload optimization
```

**Dependencies:**
- **File Dependencies:**
  - `config/qinsight_config.yaml` → QInsight configuration source
  - `tests/qinsight_api_locust.py` → QInsight test execution target
  - `utils/config_loader.py` → Shared configuration management
  - `reports/` directory → QInsight report output
- **Python Dependencies:**
  - Same as ambient runner but with QInsight-specific optimizations

**Execution Flow:**
1. **Initialization (0-3 seconds):**
   - Load qinsight_config.yaml with analytics configurations
   - Set up JWT authentication handling
   - Configure extended timeouts for analytics workload
   - Initialize QInsight-specific CLI options

2. **QInsight Configuration Phase (3-6 seconds):**
   - Load QInsight API configurations (charges_analysis endpoint)
   - Configure JWT token validation
   - Set up analytics-appropriate timeouts (45s vs 30s for Ambient)
   - Resolve QInsight environment settings

3. **Analytics Pre-execution (6-8 seconds):**
   - Validate QInsight API connectivity
   - Check JWT token validity
   - Validate qinsight_api_locust.py exists
   - Set up analytics payload configuration

4. **Analytics Test Execution (8 seconds - test completion):**
   - Execute Locust with QInsight-specific parameters
   - Monitor analytics request processing
   - Handle extended response times for complex analytics
   - Track QInsight-specific metrics

5. **QInsight Post-execution (test end - test end + 10-45 seconds):**
   - Generate QInsight-branded HTML reports
   - Include analytics-specific performance analysis
   - Create QInsight PDF reports with executive summaries
   - Analytics performance assessment and recommendations

**Usage Scenarios:**
```bash
# QInsight analytics testing
python qinsight_run_performance_test.py --test light_load --environment qa

# Extended analytics testing
python qinsight_run_performance_test.py --users 15 --duration 300s --environment qa

# QInsight configuration listing
python qinsight_run_performance_test.py --list

# Production analytics validation
python qinsight_run_performance_test.py --test light_load --environment production
```

**QInsight-Specific Features:**
- JWT authentication management
- Analytics-appropriate timeout handling (45s vs 30s)
- Complex payload structure for analytics
- Extended monitoring for long-running analytics processes
- QInsight-branded reporting with analytics focus

---

### 3. tests/ambient_api_locust.py
**Primary Purpose:** Enhanced Locust implementation for Ambient API with comprehensive metrics and professional reporting

**Detailed Description:**
This is the core performance testing engine for Ambient API, implementing sophisticated load testing with real-time metrics collection, system monitoring, and professional report generation. It simulates realistic user behavior patterns while capturing comprehensive performance data.

**Key Classes and Functions:**

```python
class PerformanceMetrics:
    """Comprehensive performance metrics collection system"""
    def __init__(self):
        self.cpu_usage = []              # Real-time CPU monitoring
        self.memory_usage = []           # System memory tracking
        self.response_times = []         # All request response times
        self.error_count = 0             # Failed request counter
        self.total_requests = 0          # Total request counter
        self.successful_requests = 0     # Success counter
        self.failed_requests = 0         # Failure counter
        self.request_timestamps = []     # Throughput calculation data
        self.error_details = []          # Detailed error information
        self.start_time = None           # Test start timestamp
        self.end_time = None            # Test completion timestamp
        self.user_count = 0             # Concurrent user count
        self.endpoint_name = "original"  # Endpoint identifier
        self.endpoint_path = "/Ambient/generate_summary_html"

class AmbientAPIUser(HttpUser):
    """Enhanced Ambient API User with realistic behavior patterns"""
    wait_time = between(1, 3)  # Realistic think time
    
    def __init__(self, *args, **kwargs):
        # Dynamic configuration loading
        # Environment-specific setup
        # API endpoint configuration
        
    @task(1)
    def generate_summary_html(self):
        # Main Ambient API request task
        # Response validation and error handling
        # Performance metrics collection
```

**Event Listeners (Execution Timing):**
```python
@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    """Executed at test initiation (0 seconds)"""
    # Initialize metrics collection
    # Set up monitoring systems
    # Configure environment-specific settings

@events.request.add_listener  
def on_request(request_type, name, response_time, response_length, exception, **kwargs):
    """Executed after each request (throughout test)"""
    # Capture request metrics in real-time
    # Track errors and performance data
    # Monitor system resources

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    """Executed at test completion"""
    # Calculate comprehensive performance metrics
    # Generate enhanced HTML reports
    # Print detailed performance summaries
```

**Dependencies:**
- **File Dependencies:**
  - `config/ambient_config.yaml` → Via config_loader for dynamic configuration
  - `utils/config_loader.py` → Configuration management and environment setup
- **Python Dependencies:**
  - `locust` → Core performance testing framework
  - `psutil` → System resource monitoring (CPU, memory)
  - `datetime` → Timestamp management and duration calculation
  - `statistics` → Performance calculations (mean, median, percentiles)
  - `json` → Response data parsing and validation
  - `requests` → HTTP client functionality

**Execution Timeline:**
1. **Test Initialization (0-5 seconds):**
   - Load Ambient configuration via ConfigLoader
   - Initialize PerformanceMetrics global instance
   - Set up system resource monitoring
   - Configure API endpoints and headers
   - Establish baseline system metrics

2. **User Spawn Phase (5-25 seconds depending on spawn rate):**
   - Spawn concurrent users based on configuration
   - Each user loads Ambient-specific configuration
   - Initialize individual user sessions
   - Begin realistic user behavior simulation

3. **Load Testing Phase (25 seconds - test duration end):**
   - Execute generate_summary_html tasks continuously
   - Monitor system resources every request
   - Collect detailed performance metrics
   - Track errors and response validation
   - Maintain realistic user behavior patterns

4. **Test Completion Phase (test end - test end + 30 seconds):**
   - Stop all user activity
   - Calculate comprehensive performance statistics
   - Generate professional HTML report with Ambient branding
   - Print detailed console performance summary
   - Save performance data for historical analysis

**Key Functions Execution Order:**
1. `on_test_start()` → Initialize metrics and monitoring
2. `AmbientAPIUser.__init__()` → Configure each user instance
3. `generate_summary_html()` → Execute throughout test duration
4. `monitor_system_resources()` → Called during each request
5. `on_request()` → Process each request's metrics
6. `on_test_stop()` → Final processing and reporting

**Report Generation Features:**
- **Executive Summary:** High-level performance assessment
- **Detailed Metrics:** Response times, throughput, error analysis
- **System Resources:** CPU and memory utilization trends
- **Performance Grading:** Automated assessment (Excellent/Good/Needs Improvement/Critical)
- **Recommendations:** Actionable optimization suggestions
- **Visual Design:** Professional HTML styling with responsive design

---

### 4. tests/qinsight_api_locust.py
**Primary Purpose:** Enhanced Locust implementation for QInsight API with analytics-focused testing and comprehensive reporting

**Detailed Description:**
Specialized performance testing engine for QInsight analytics API, designed to handle complex analytics workloads with extended timeouts, JWT authentication, and analytics-specific performance validation. Generates QInsight-branded reports with analytics-appropriate metrics.

**Key Classes and Functions:**

```python
class QInsightAPIUser(HttpUser):
    """Enhanced QInsight API User with analytics behavior patterns"""
    wait_time = between(1, 3)
    
    def __init__(self, *args, **kwargs):
        # QInsight configuration loading
        # JWT authentication setup
        # Analytics payload configuration
        
    def load_configuration(self):
        # Load qinsight_config.yaml specifically
        # Configure JWT authentication headers
        # Set up analytics payload structure
        
    @task(1)
    def charges_analysis_request(self):
        # Main QInsight analytics request
        # Handle complex analytics payload
        # Extended timeout for analytics processing
        
    def validate_response(self, response):
        # QInsight-specific response validation
        # Analytics data format verification
        # JSON structure validation for analytics results
```

**QInsight-Specific Features:**
```python
def get_test_payload(self):
    """Generate analytics test payload with variations"""
    # Base analytics payload structure
    # Practice list variations for load testing
    # Client key configuration for QInsight environment
    
def generate_enhanced_qinsight_html_report(...):
    """Generate QInsight-branded HTML report with analytics focus"""
    # Analytics-appropriate performance thresholds
    # QInsight visual branding and styling
    # Analytics workload recommendations
    # Executive summary for analytics performance
```

**Dependencies:**
- **File Dependencies:**
  - `config/qinsight_config.yaml` → QInsight-specific configuration
  - `utils/config_loader.py` → Shared configuration management
- **Python Dependencies:**
  - Same as ambient_api_locust.py plus QInsight-specific modules
  - Enhanced JSON handling for complex analytics responses
  - JWT token management utilities

**Execution Timeline:**
1. **QInsight Initialization (0-8 seconds):**
   - Load qinsight_config.yaml with analytics configurations
   - Validate JWT authentication tokens
   - Configure extended timeouts (45s vs 30s for Ambient)
   - Set up analytics payload structures
   - Initialize QInsight-specific metrics collection

2. **Analytics User Spawn (8-35 seconds):**
   - Spawn users with QInsight-specific configuration
   - Configure JWT authentication for each user
   - Set up analytics request patterns
   - Initialize QInsight API connectivity

3. **Analytics Load Testing (35 seconds - test duration end):**
   - Execute charges_analysis_request tasks
   - Handle extended response times for complex analytics
   - Monitor JWT token validity throughout test
   - Collect analytics-specific performance metrics
   - Validate complex JSON analytics responses

4. **QInsight Completion (test end - test end + 45 seconds):**
   - Generate QInsight-branded HTML reports
   - Include analytics-specific performance analysis
   - Provide analytics workload recommendations
   - Create executive summaries for analytics performance

**Analytics-Specific Validations:**
- JWT token expiration handling
- Complex JSON response structure validation
- Analytics data integrity verification
- Extended timeout management for long-running analytics
- Practice list and client key validation

---

### 5. utils/config_loader.py
**Primary Purpose:** Shared configuration management utility supporting both Ambient and QInsight APIs

**Detailed Description:**
Sophisticated configuration management system that provides a unified interface for accessing API-specific configurations. Implements flexible initialization to support both Ambient and QInsight configurations while maintaining type safety and comprehensive error handling.

**Key Classes:**

```python
class EnvironmentConfigLoader:
    """Utility class to load and manage API-specific configurations"""
    
    def __init__(self, config_path: Optional[str] = None):
        # Flexible config file initialization
        # Support for both ambient_config.yaml and qinsight_config.yaml
        # Automatic configuration validation
        
    def set_environment(self, environment: str) -> bool:
        # Environment validation and switching
        # Support for dev, qa, staging, production
        
    def get_base_url(self, environment: Optional[str] = None) -> str:
        # Environment-specific URL resolution
        # Ambient vs QInsight URL handling
        
    def get_load_configuration(self, config_name: str) -> Dict[str, Any]:
        # Load test configuration retrieval
        # API-specific threshold management
        
    def get_api_configurations(self) -> Dict[str, Any]:
        # API endpoint configurations
        # Authentication and header management
        
    def get_endpoint_config(self, endpoint_name: str) -> Dict[str, Any]:
        # Specific endpoint configuration
        # Support for Ambient (original, v1) and QInsight (charges_analysis)

# Alias for backward compatibility
ConfigLoader = EnvironmentConfigLoader
```

**Dependencies:**
- **File Dependencies:**
  - `config/ambient_config.yaml` OR `config/qinsight_config.yaml` → Based on initialization
- **Python Dependencies:**
  - `yaml` → YAML configuration file parsing
  - `pathlib` → File path management and validation
  - `typing` → Type hints for robust interface

**Execution Context:**
This utility is imported and used by all other Python files but doesn't execute independently. It's instantiated during framework initialization and used throughout the test lifecycle.

**Initialization Timing:**
1. **Framework Startup (0-2 seconds):**
   - Imported by test runners during startup
   - Configuration file loaded and parsed
   - Environment validation performed
   - Default environment set if available

2. **During Test Execution (throughout test):**
   - Configuration values accessed via getter methods
   - Environment-specific settings retrieved
   - API configurations provided to Locust tests
   - No file re-reading (cached configuration)

**Usage Patterns:**
```python
# Ambient usage
config_loader = ConfigLoader("config/ambient_config.yaml")
config_loader.set_environment("qa")
base_url = config_loader.get_base_url()

# QInsight usage  
config_loader = ConfigLoader("config/qinsight_config.yaml")
config_loader.set_environment("qa")
api_configs = config_loader.get_api_configurations()
```

---

## YAML Configuration Files - Comprehensive Analysis

### 1. config/ambient_config.yaml
**Primary Purpose:** Centralized configuration hub for Ambient API performance testing

**Detailed Structure:**

```yaml
# Ambient API Performance Testing Framework Configuration

environments:
  dev:
    base_url: "https://innovationz-dev.myqone.com"
    timeout: 30
    verify_ssl: true
    description: "Dev Environment for Ambient API testing"
  qa:
    base_url: "https://innovationz-qa.myqone.com"
    timeout: 30
    verify_ssl: true
    description: "QA Environment for Ambient API testing"
  staging:
    base_url: "https://innovationz-staging.myqone.com"
    timeout: 30
    verify_ssl: true
    description: "Staging Environment for pre-production testing"
  production:
    base_url: "https://innovationz.myqone.com"
    timeout: 30
    verify_ssl: true
    description: "Production Environment - use with caution"

load_configurations:
  light_load:
    users: 20
    spawn_rate: 5
    duration: "90s"
    description: "Light load testing - baseline validation"
    expected_rps: 1.0
    max_response_time: 20000
    max_error_rate: 5.0
  
  medium_load:
    users: 30
    spawn_rate: 5
    duration: "90s"
    description: "Medium load testing - standard validation"
    expected_rps: 1.5
    max_response_time: 25000
    max_error_rate: 8.0
  
  heavy_load:
    users: 40
    spawn_rate: 5
    duration: "90s"
    description: "Heavy load testing - stress testing"
    expected_rps: 2.0
    max_response_time: 30000
    max_error_rate: 10.0

api_configurations:
  original:
    name: "Original Ambient API"
    description: "Original Ambient API endpoint for medical conversation processing"
    method: "POST"
    endpoint: "/Ambient/generate_summary_html"
    headers:
      Content-Type: "application/json"
      User-Agent: "Ambient-Performance-Testing-Framework/1.0"
      Accept: "application/json"
    timeout: 30
    retry_attempts: 3
    retry_delay: 1
  
  v1:
    name: "Ambient API V1"
    description: "Version 1 of Ambient API with enhanced features"
    method: "POST"
    endpoint: "/Ambient/generate_summary_html_v1"
    headers:
      Content-Type: "application/json"
      User-Agent: "Ambient-Performance-Testing-Framework/1.0"
      Accept: "application/json"
    timeout: 30
    retry_attempts: 3
    retry_delay: 1

test_data:
  medical_conversation: |
    "Dave. I've heard your knee is hurting you. Yes, my right knee has been bothering me for about two weeks now. It started after I was doing some yard work, and I think I might have twisted it. The pain is mostly on the inside of my knee, and it's worse when I try to bend it or put weight on it. I've been taking some ibuprofen, which helps a little, but it's still pretty uncomfortable. I'm worried it might be something serious."
  
  alternative_conversations:
    - "Patient presents with chronic back pain lasting six months. Pain is localized to lower lumbar region, radiates to left leg. Worse with prolonged sitting or standing. Previously tried physical therapy with minimal improvement."
    - "Follow-up visit for diabetes management. Current A1C is 7.2%, improved from 8.1% three months ago. Patient reports better dietary compliance and regular blood glucose monitoring."
    - "Chief complaint of persistent headaches for past month. Described as bilateral, pressure-like sensation. No visual changes or neurological symptoms. Stress and lack of sleep identified as potential triggers."

thresholds:
  response_time:
    excellent: 5000      # ms - Web UI excellent performance
    good: 10000         # ms - Web UI acceptable performance  
    acceptable: 20000   # ms - Web UI warning threshold
    critical: 30000     # ms - Web UI critical threshold
    timeout: 45000      # ms - Request timeout
  
  error_rate:
    excellent: 1.0      # % - Excellent error rate
    good: 5.0          # % - Good error rate
    acceptable: 10.0   # % - Acceptable error rate
    critical: 20.0     # % - Critical error rate
    failure: 50.0      # % - System failure threshold
  
  throughput:
    minimum: 0.5        # req/sec - Minimum acceptable
    good: 1.0          # req/sec - Good throughput
    excellent: 2.0     # req/sec - Excellent throughput
    target: 3.0        # req/sec - Target for optimization

reports:
  output_directory: "reports"
  naming_convention: "ambient_api_performance_report_{environment}_{users}users_{endpoint}_{timestamp}"
  formats:
    html: true
    pdf: true
    
execution:
  default_environment: "qa"
  default_test: "light_load"
  recovery_time_between_tests: 60  # seconds
```

**Usage Timing:**
1. **Framework Startup (0-2 seconds):** Loaded by ConfigLoader when ambient_run_performance_test.py starts
2. **Configuration Phase (2-5 seconds):** Environment and test configurations resolved
3. **Test Execution (throughout test):** API configurations and thresholds referenced
4. **Report Generation (test completion):** Report configurations used for output formatting

**Dependencies:**
- **Used By:**
  - `ambient_run_performance_test.py` → Test orchestration and configuration
  - `tests/ambient_api_locust.py` → API endpoints, headers, and validation thresholds
  - `utils/config_loader.py` → Configuration parsing and validation

**Key Features:**
- **Environment Isolation:** Separate configurations for each environment prevent cross-environment issues
- **Web UI Optimized Thresholds:** Performance expectations appropriate for web user interface interactions
- **Multiple API Versions:** Support for both original and v1 Ambient API endpoints
- **Rich Test Data:** Realistic medical conversation data for authentic testing scenarios

---

### 2. config/qinsight_config.yaml
**Primary Purpose:** Centralized configuration hub for QInsight API analytics performance testing

**Detailed Structure:**

```yaml
# QInsight API Performance Testing Framework Configuration

environments:
  dev:
    base_url: "https://qinsight-dev.myqone.com"
    timeout: 45
    verify_ssl: true
    description: "QInsight Dev Environment for analytics and metrics testing"
  qa:
    base_url: "https://qinsight-qa.myqone.com"
    timeout: 45
    verify_ssl: true
    description: "QInsight QA Environment for analytics and metrics testing"
  staging:
    base_url: "https://qinsight-staging.myqone.com"
    timeout: 45
    verify_ssl: true
    description: "QInsight Staging Environment for pre-production analytics testing"
  production:
    base_url: "https://qinsight.myqone.com"
    timeout: 45
    verify_ssl: true
    description: "QInsight Production Environment - use with extreme caution"

load_configurations:
  light_load:
    users: 20
    spawn_rate: 5
    duration: "90s"
    description: "Light load testing - analytics baseline validation"
    expected_rps: 1.0
    max_response_time: 25000  # Extended for analytics processing
    max_error_rate: 5.0
  
  medium_load:
    users: 30
    spawn_rate: 5
    duration: "90s"
    description: "Medium load testing - standard analytics validation"
    expected_rps: 0.8         # Lower expectation for analytics
    max_response_time: 35000  # Extended timeout for complex analytics
    max_error_rate: 8.0
  
  heavy_load:
    users: 40
    spawn_rate: 5
    duration: "90s"
    description: "Heavy load testing - analytics stress testing"
    expected_rps: 0.6         # Realistic for heavy analytics processing
    max_response_time: 45000  # Maximum tolerance for analytics
    max_error_rate: 10.0

api_configurations:
  charges_analysis:
    name: "QInsight Charges Analysis API"
    description: "API for analyzing charges by CPT codes and practice metrics"
    method: "POST"
    endpoint: "/restservicefmetrics/ChargesAnalysisByCPT"
    headers:
      Content-Type: "application/json"
      User-Agent: "QInsight-Performance-Testing-Framework/1.0"
      Accept: "application/json"
      Authorization: "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NTM3Nzc1ODMsImV4cCI6MTc1NjM2OTU4MywiaXNzIjoiY2xvdWQtZW5kcG9pbnRzLXFhQHFwYXRod2F5cy1xYS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsImF1ZCI6Imh0dHBzOi8vcW9yZS1xYS5teXFvbmUuY29tIiwic3ViIjoiY2xvdWQtZW5kcG9pbnRzLXFhQHFwYXRod2F5cy1xYS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsImVtYWlsIjoic2FjaGluLnNhbmFwQHRyaWFycWhlYWx0aC5jb20iLCJ1c2VyaWQiOiI2MGUwODZkYS1lNzJiLTExZWMtODVhNS05MWEyZDNjZWJmZTEiLCJmaXJzdG5hbWUiOiJTYWNoaW4iLCJsYXN0bmFtZSI6IlNhbmFwIn0.PhMI-2dOmDyaHG5FOXeRfKYiaNCgZGIPeV9Mbq8sh7ihaJ4olsqLPj6tL7tnT7qKJztSHEqrzKtYoiiNa1XOSjZvTLmIlDHanX5iS2NGq8u6QUA_IVATw-rr904unMfgUEa3_fCb15mdmWNznmysWBHTBdBIh174X6oXlNKMi0FjJYIskUGSKbQjLBVu_IVfAeWl6PXWVhBfhvctxjTnBzKm8FoTxX-DhM_TOYuFIzoZaxPd9wlcCq6lEa-qozxYH0LRqW4ulTXyR_qdv92lLWNf0txLwwjGNr017SKCG5WmR8VzLAdXtQWZPkiX3XRNNzlB17O8vloFpr7S9hePPw"
    timeout: 45
    retry_attempts: 3
    retry_delay: 2
    payload:
      clientkey: "QinsightQAData"
      practicelist:
        - "GCPBQDEMO4"
        - "GCPBQDEMO1"

test_data:
  practice_lists:
    small_practice:
      - "GCPBQDEMO1"
    medium_practice:
      - "GCPBQDEMO1"
      - "GCPBQDEMO4"
    large_practice:
      - "GCPBQDEMO1"
      - "GCPBQDEMO4"
      - "GCPBQDEMO2"
      - "GCPBQDEMO3"
  
  client_keys:
    qa_data: "QinsightQAData"
    dev_data: "QinsightDevData"
    staging_data: "QinsightStagingData"

thresholds:
  response_time:
    excellent: 15000     # ms - Analytics excellent performance
    good: 25000         # ms - Analytics acceptable performance
    acceptable: 40000   # ms - Analytics warning threshold  
    critical: 60000     # ms - Analytics critical threshold
    timeout: 90000      # ms - Extended timeout for complex analytics
  
  error_rate:
    excellent: 1.0      # % - Excellent error rate for analytics
    good: 5.0          # % - Good error rate for analytics
    acceptable: 10.0   # % - Acceptable error rate for analytics
    critical: 20.0     # % - Critical error rate for analytics
    failure: 50.0      # % - System failure threshold
  
  throughput:
    minimum: 0.3        # req/sec - Minimum for analytics workload
    good: 0.8          # req/sec - Good for analytics workload
    excellent: 1.2     # req/sec - Excellent for analytics workload
    target: 1.5        # req/sec - Target for analytics optimization

reports:
  output_directory: "reports"
  naming_convention: "qinsight_api_performance_report_{environment}_{users}users_{endpoint}_{timestamp}"
  formats:
    html: true
    pdf: true
    
execution:
  default_environment: "qa"
  default_test: "light_load"
  recovery_time_between_tests: 90  # seconds - longer for analytics cleanup
```

**Usage Timing:**
1. **Framework Startup (0-3 seconds):** Loaded by ConfigLoader when qinsight_run_performance_test.py starts
2. **Authentication Setup (3-6 seconds):** JWT token validation and configuration
3. **Test Execution (throughout test):** API configurations, authentication, and analytics thresholds used
4. **Report Generation (test completion):** QInsight-specific report configurations applied

**Dependencies:**
- **Used By:**
  - `qinsight_run_performance_test.py` → QInsight test orchestration and configuration
  - `tests/qinsight_api_locust.py` → QInsight API endpoints, JWT auth, and analytics validation
  - `utils/config_loader.py` → QInsight configuration parsing and validation

**Key Features:**
- **Analytics-Optimized Thresholds:** Performance expectations appropriate for complex analytics processing
- **JWT Authentication:** Complete authentication configuration with Bearer tokens
- **Extended Timeouts:** Longer timeouts (45s vs 30s) for analytics processing
- **Analytics Payload Structure:** Complex payload structures for practice analytics
- **Environment-Specific Analytics:** Different client keys and practice lists for different environments

---

## Framework Integration and Execution Flow

### Complete Framework Execution Timeline

**Phase 1: Initialization (0-10 seconds)**
1. **User Command Execution (0s):**
   ```bash
   python ambient_run_performance_test.py --test light_load --environment qa
   # OR
   python qinsight_run_performance_test.py --test light_load --environment qa
   ```

2. **Runner Initialization (0-3s):**
   - Import required modules (subprocess, argparse, config_loader)
   - Initialize respective runner class (Ambient or QInsight)
   - Load API-specific configuration file (ambient_config.yaml or qinsight_config.yaml)

3. **Configuration Loading (3-6s):**
   - ConfigLoader parses YAML configuration
   - Environment validation (dev, qa, staging, production)
   - Load test configuration resolution (light_load, medium_load, heavy_load)
   - API configuration setup (endpoints, headers, authentication)

4. **Pre-execution Setup (6-10s):**
   - Validate Locust test file exists (ambient_api_locust.py or qinsight_api_locust.py)
   - Create reports directory if needed
   - Generate report filenames with timestamps
   - Set environment variables for Locust consumption

**Phase 2: Test Execution (10s - test completion)**
1. **Locust Command Execution (10s):**
   - Build Locust command with parameters from configuration
   - Execute subprocess with API-specific Locust file
   - Set environment variables (LOCUST_API_ENDPOINT, LOCUST_ENVIRONMENT, LOCUST_ENDPOINT_NAME)

2. **Locust Initialization (10-15s):**
   - Import and initialize respective Locust file
   - Load configuration via ConfigLoader
   - Initialize PerformanceMetrics global instance
   - Execute on_test_start event listener

3. **User Spawn Phase (15-30s depending on spawn rate):**
   - Spawn concurrent users based on configuration
   - Each user initializes with API-specific configuration
   - Load API endpoints, headers, and authentication
   - Begin user behavior simulation

4. **Load Testing Phase (30s - test duration end):**
   - Execute API-specific tasks (generate_summary_html or charges_analysis_request)
   - Monitor system resources (CPU, memory) in real-time
   - Collect comprehensive performance metrics
   - Validate responses and track errors
   - Maintain realistic user behavior patterns

**Phase 3: Completion and Reporting (test end - test end + 60s)**
1. **Test Stop Processing (test end):**
   - Execute on_test_stop event listener
   - Stop all user activity and resource monitoring
   - Calculate comprehensive performance statistics

2. **Report Generation (test end + 5-45s):**
   - Generate enhanced HTML report with API-specific branding
   - Calculate performance metrics and percentiles
   - Create performance assessment and recommendations
   - Save report with API-specific naming convention

3. **Post-processing (test end + 45-60s):**
   - Print comprehensive console summary
   - Generate PDF report if available
   - Return execution status to runner
   - Cleanup temporary resources

### Dependency Resolution Order

1. **Configuration Files** (loaded first):
   - `ambient_config.yaml` or `qinsight_config.yaml`
   - Parsed by `utils/config_loader.py`

2. **Test Runners** (entry points):
   - `ambient_run_performance_test.py` or `qinsight_run_performance_test.py`
   - Import and use ConfigLoader

3. **Locust Test Files** (executed by runners):
   - `tests/ambient_api_locust.py` or `tests/qinsight_api_locust.py`
   - Import and use ConfigLoader for dynamic configuration

4. **Report Generation** (triggered by Locust):
   - HTML reports generated by respective Locust files
   - PDF reports generated by runner if available

### Framework Communication Patterns

**Configuration Flow:**
```
YAML Config → ConfigLoader → Runner → Environment Variables → Locust File
```

**Execution Flow:**
```
User Command → Runner → Locust Subprocess → Test Execution → Report Generation
```

**Data Flow:**
```
Config Data → Test Parameters → Performance Metrics → Analysis → Reports
```

This comprehensive documentation provides complete details on all files, their dependencies, execution timing, and integration within the separated framework architecture. 