# Separated Performance Testing Framework

This framework has been restructured to provide independent performance testing capabilities for **Ambient APIs** and **QInsight APIs**. Each API system now has its own dedicated configuration, test files, and runner scripts.

## 🏗️ Framework Structure

### Directory Layout
```
BDD_Framework/
├── config/
│   ├── ambient_config.yaml     # Ambient API configurations
│   ├── qinsight_config.yaml    # QInsight API configurations
│   └── test_config.yaml        # Legacy (can be removed)
├── tests/
│   ├── ambient_api_locust.py   # Ambient Locust test file
│   └── qinsight_api_locust.py  # QInsight Locust test file
├── utils/
│   └── config_loader.py        # Configuration loading utility
├── reports/                    # Generated test reports
├── ambient_run_performance_test.py    # Ambient test runner
├── qinsight_run_performance_test.py   # QInsight test runner
├── run_performance_test.py     # Legacy (can be removed)
└── requirements.txt            # Dependencies (Locust only)
```

## 🚀 Quick Start

### Prerequisites
```bash
# Install dependencies
pip install -r requirements.txt

# Or install individual packages
pip install locust pyyaml reportlab beautifulsoup4 requests psutil
```

### Running Ambient API Tests
```bash
# Basic test
python ambient_run_performance_test.py --test light_load --environment qa

# Custom parameters
python ambient_run_performance_test.py --test heavy_load --environment qa --users 50 --duration 120s

# List available tests
python ambient_run_performance_test.py --list
```

### Running QInsight API Tests
```bash
# Basic test
python qinsight_run_performance_test.py --test light_load --environment qa

# Custom parameters
python qinsight_run_performance_test.py --test heavy_load --environment qa --users 50 --duration 120s

# List available tests
python qinsight_run_performance_test.py --list
```

## 📋 Configuration Files

### Ambient Configuration (`config/ambient_config.yaml`)

**Environments:**
- `dev`, `qa`, `staging`, `production` - Ambient API environments

**API Endpoints:**
- `original` - `/Ambient/generate_summary_html`
- `v1` - `/Ambient/generate_summary_html_v1`

**Load Tests:**
- `light_load`, `medium_load`, `heavy_load` - Basic load scenarios
- `light_load_v1`, `medium_load_v1`, `heavy_load_v1` - V1 API scenarios
- `stress_test`, `endurance_test`, `spike_test` - Advanced scenarios

### QInsight Configuration (`config/qinsight_config.yaml`)

**Environments:**
- `dev`, `qa`, `staging`, `production` - QInsight API environments

**API Endpoints:**
- `charges_analysis` - `/restservicefmetrics/ChargesAnalysisByCPT`

**Load Tests:**
- `light_load`, `medium_load`, `heavy_load` - Basic load scenarios
- `stress_test`, `endurance_test`, `spike_test` - Advanced scenarios

## 🎯 Available Test Scenarios

### Load Configurations
| Scenario | Users | Spawn Rate | Duration | Description |
|----------|-------|------------|----------|-------------|
| `light_load` | 20 | 5/sec | 90s | Baseline performance validation |
| `medium_load` | 30 | 5/sec | 90s | Moderate stress testing |
| `heavy_load` | 40 | 8/sec | 120s | Heavy stress testing |
| `extreme_stress` | 50 | 10/sec | 180s | Push system to limits |
| `endurance_test` | 25 | 3/sec | 600s | Extended duration testing |
| `spike_test` | 35 | 10/sec | 180s | Rapid load increase testing |

### Test Environments
| Environment | Ambient URL | QInsight URL |
|-------------|-------------|--------------|
| `dev` | innovationz-dev.myqone.com | qinsight-dev.myqone.com |
| `qa` | innovationz-qa.myqone.com | qinsight-qa.myqone.com |
| `staging` | innovationz-staging.myqone.com | qinsight-staging.myqone.com |
| `production` | innovationz.myqone.com | qinsight.myqone.com |

## 🔧 Command Line Options

### Common Options (Both Frameworks)
```bash
--test, -t          Test configuration (light_load, medium_load, etc.)
--environment, -e   Target environment (dev, qa, staging, production)
--users, -u         Number of concurrent users (overrides config)
--spawn-rate, -r    User spawn rate per second (overrides config)
--duration, -d      Test duration (e.g., 60s, 5m) (overrides config)
--config, -c        Custom config file path
--list, -l          List available tests and environments
```

### Example Commands
```bash
# Run light load test against QA environment
python qinsight_run_performance_test.py --test light_load --environment qa

# Run custom test with 25 users for 2 minutes
python ambient_run_performance_test.py --test medium_load --users 25 --duration 120s

# Run stress test against staging environment
python qinsight_run_performance_test.py --test stress_test --environment staging

# List all available test configurations
python ambient_run_performance_test.py --list
```

## 📊 Test Reports

Both frameworks generate comprehensive HTML and PDF reports:

### HTML Reports
- Real-time statistics during test execution
- Response time percentiles (50th, 75th, 90th, 95th, 99th)
- Request rate and failure analysis
- Charts and graphs for visual analysis

### PDF Reports
- Executive summary
- Performance metrics
- Recommendations
- Stored in `reports/pdf_generator/`

### Report File Naming
```
# Ambient reports
ambient_performance_report_{environment}_{users}users_{endpoint}_{timestamp}.html

# QInsight reports
qinsight_performance_report_{environment}_{users}users_{endpoint}_{timestamp}.html
```

## 🔍 Test Data and Payloads

### Ambient API
- **Medical Conversations**: Realistic doctor-patient dialogue
- **Enhanced Processing**: Toggle for advanced features
- **Multiple Scenarios**: Various conversation types for load diversity

### QInsight API
- **Client Keys**: Environment-specific authentication
- **Practice Lists**: Various practice configurations (small, medium, large)
- **Payload Variations**: Different practice combinations for load testing

## 🚨 Authentication

### Ambient API
- Uses standard JSON headers
- No special authentication required for testing environments

### QInsight API
- Requires JWT Bearer token in Authorization header
- Token configured in `qinsight_config.yaml`
- Update token if tests fail with 401 errors

## 🔧 Customization

### Adding New Test Scenarios
1. **Edit Configuration**: Add to `load_configurations` in YAML
2. **Update Choices**: Add to `--test` choices in runner script
3. **Test**: Run with `--list` to verify

### Adding New Environments
1. **Edit Configuration**: Add to `environments` in YAML
2. **Update Choices**: Add to `--environment` choices in runner script
3. **Test**: Verify connectivity before load testing

### Custom Locust Scripts
- **Ambient**: Modify `tests/ambient_api_locust.py`
- **QInsight**: Modify `tests/qinsight_api_locust.py`
- Both scripts include fallback configurations for standalone usage

## 🛠️ Troubleshooting

### Common Issues

**1. Configuration Not Found**
```bash
❌ Configuration file not found: config/ambient_config.yaml
```
**Solution**: Ensure you're running from the BDD_Framework directory

**2. Locust Not Found**
```bash
❌ Locust not found. Please install locust
```
**Solution**: `pip install locust`

**3. JWT Token Expired (QInsight)**
```bash
❌ Authentication failed: 401 - Check JWT token
```
**Solution**: Update the Authorization header in `qinsight_config.yaml`

**4. Import Errors**
```bash
❌ Error: No module named 'utils.config_loader'
```
**Solution**: Run scripts from the BDD_Framework directory

### Debug Mode
Both frameworks provide verbose output including:
- Configuration loading status
- Environment details
- Request/response validation
- Performance metrics

## 🔄 Migration from Legacy Framework

### What Changed
1. **Removed BDD/Behave**: Framework now only supports Locust
2. **Separated Configurations**: Independent YAML files for each API
3. **Dedicated Runners**: Separate Python scripts for each system
4. **Simplified Dependencies**: Removed behave, kept only Locust essentials

### Migration Steps
1. **Use New Runners**: Replace old commands with new script names
2. **Update Configurations**: Use `ambient_config.yaml` or `qinsight_config.yaml`
3. **Remove Old Files**: Clean up legacy `test_config.yaml` and old runners

### Command Mapping
```bash
# OLD (Legacy)
python run_performance_test.py --mode locust --test light_load

# NEW (Ambient)
python ambient_run_performance_test.py --test light_load

# NEW (QInsight)
python qinsight_run_performance_test.py --test light_load
```

## 📈 Performance Thresholds

### Ambient API Expectations
- **Response Time**: < 20s for 95th percentile
- **Error Rate**: < 5% under normal load
- **Throughput**: > 1.0 requests/second

### QInsight API Expectations
- **Response Time**: < 25s for 95th percentile (analytics workload)
- **Error Rate**: < 5% under normal load
- **Throughput**: > 0.8 requests/second

## 🎯 Best Practices

### Test Planning
1. **Start Small**: Begin with `light_load` tests
2. **Gradual Increase**: Progress to `medium_load`, then `heavy_load`
3. **Environment Isolation**: Use `qa` for regular testing, `staging` for pre-production
4. **Documentation**: Record test results and observations

### Performance Analysis
1. **Monitor Trends**: Compare results across test runs
2. **Identify Bottlenecks**: Look for response time spikes
3. **Error Analysis**: Investigate any failures or timeouts
4. **Capacity Planning**: Use results to determine production capacity

### Security Considerations
1. **Token Management**: Regularly update JWT tokens for QInsight
2. **Environment Access**: Ensure proper permissions for target environments
3. **Data Privacy**: Use appropriate test data for each environment

---

## 🆘 Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify configuration files are properly formatted
3. Ensure all dependencies are installed
4. Review the verbose output for error details

**Framework Version**: 2.0 (Separated)  
**Last Updated**: January 2025 