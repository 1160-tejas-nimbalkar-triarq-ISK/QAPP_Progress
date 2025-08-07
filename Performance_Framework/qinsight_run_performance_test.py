#!/usr/bin/env python3
"""
QInsight Performance Testing Framework
A Locust-based performance testing framework for QInsight APIs

This script provides a simplified interface for running performance tests
against QInsight APIs using Locust load testing tool.

Usage:
    python qinsight_run_performance_test.py --test light_load --environment qa
    python qinsight_run_performance_test.py --test heavy_load --environment qa --users 50 --duration 120s
"""

import os
import sys
import argparse
import subprocess
import time
from pathlib import Path
from datetime import datetime

# Add the project root to the Python path for imports
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

# Import configuration loader
from utils.config_loader import ConfigLoader

class QInsightPerformanceTestRunner:
    """QInsight Performance Test Runner - Locust-based load testing"""
    
    def __init__(self, config_file=None, environment=None):
        """Initialize the QInsight performance test runner"""
        
        # Set up paths
        self.current_dir = Path(__file__).parent
        self.config_dir = self.current_dir / "config"
        self.reports_dir = self.current_dir / "reports"
        self.tests_dir = self.current_dir / "tests"
        
        # Ensure directories exist
        self.reports_dir.mkdir(exist_ok=True)
        self.tests_dir.mkdir(exist_ok=True)
        
        # Initialize configuration
        config_file = config_file or self.config_dir / "qinsight_config.yaml"
        self.config_loader = ConfigLoader(config_file)
        
        # Set environment
        self.environment = environment or "qa"
        self.config_loader.set_environment(self.environment)
        
        print(f"🚀 QInsight Performance Testing Framework Initialized")
        print(f"📁 Config: {config_file}")
        print(f"🌐 Environment: {self.environment}")
        print("=" * 60)

    def list_available_tests(self):
        """List all available test configurations"""
        print("\n🔍 Available QInsight Test Configurations:")
        print("=" * 50)
        
        # List load configurations
        load_configs = self.config_loader.config.get('load_configurations', {})
        print("\n📊 Load Configurations:")
        for name, config in load_configs.items():
            print(f"  • {name:15} - {config.get('description', 'No description')}")
            print(f"    {'':17} Users: {config.get('users')}, Duration: {config.get('duration')}")
        
        # List load tests (combinations)
        load_tests = self.config_loader.config.get('load_tests', {})
        print("\n🎯 Combined Test Scenarios:")
        for name, config in load_tests.items():
            print(f"  • {name:20} - {config.get('description', 'No description')}")
        
        # List environments
        environments = self.config_loader.config.get('environments', {})
        print("\n🌐 Available Environments:")
        for name, config in environments.items():
            print(f"  • {name:10} - {config.get('base_url')} ({config.get('description')})")
    
    def run_locust_test(self, test_config_name="light_load", environment=None, custom_config=None):
        """Run Locust performance test using configuration loader"""
        print(f"🦗 Running QInsight Locust Performance Test: {test_config_name}")
        
        # Use current settings if none specified
        if not environment:
            environment = self.environment or "qa"
        
        # Get test configuration
        if custom_config:
            config = custom_config
        else:
            try:
                # Check if this is a load_tests configuration
                load_tests = self.config_loader.config.get('load_tests', {})
                if test_config_name in load_tests:
                    load_test_config = load_tests[test_config_name]
                    load_config_name = load_test_config['load_config']
                    endpoint_name = load_test_config['endpoint']
                    
                    # Get the actual load configuration
                    load_config = self.config_loader.get_load_configuration(load_config_name)
                    endpoint_config = self.config_loader.get_endpoint_config(endpoint_name)
                    
                    config = load_config.copy()
                    config['endpoint'] = endpoint_config['path']
                    config['endpoint_name'] = endpoint_name
                    config['endpoint_description'] = endpoint_config.get('description', '')
                    
                    print(f"📋 Using load test configuration: {test_config_name}")
                    print(f"📋 Load config: {load_config_name}, Endpoint: {endpoint_name}")
                    
                else:
                    # Try to get load configuration directly
                    config = self.config_loader.get_load_configuration(test_config_name)
                    config['endpoint'] = '/restservicefmetrics/ChargesAnalysisByCPT'
                    config['endpoint_name'] = 'charges_analysis'
                    config['endpoint_description'] = 'QInsight Charges Analysis API'
                    print(f"📋 Using load configuration: {test_config_name}")
                    
            except Exception as e:
                print(f"❌ Error loading test configuration '{test_config_name}': {e}")
                return False, None
        
        # Get environment configuration
        try:
            base_url = self.config_loader.get_base_url(environment)
            env_description = self.config_loader.get_environment_description(environment)
            
            # Get endpoint information
            endpoint_path = config.get('endpoint', '/restservicefmetrics/ChargesAnalysisByCPT')
            endpoint_name = config.get('endpoint_name', 'charges_analysis')
            endpoint_description = config.get('endpoint_description', 'QInsight Charges Analysis API')
            
            full_api_url = f"{base_url}{endpoint_path}"
            
        except Exception as e:
            print(f"❌ Error getting environment configuration: {e}")
            return False, None
        
        # Generate report filename with timestamp and endpoint info
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        endpoint_suffix = f"_{endpoint_name}" if endpoint_name != "charges_analysis" else ""
        html_report = f"qinsight_performance_report_{environment}_{config['users']}users{endpoint_suffix}_{timestamp}.html"
        report_path = self.reports_dir / html_report
        
        # Locust file path
        locust_file = self.tests_dir / "qinsight_api_locust.py"
        
        # Check if locust file exists
        if not locust_file.exists():
            print(f"❌ Locust file not found: {locust_file}")
            print("💡 Creating QInsight locust file...")
            return False, None
        
        # Build locust command
        cmd = [
            'locust',
            '-f', str(locust_file),
            '--host', base_url,
            '--users', str(config['users']),
            '--spawn-rate', str(config['spawn_rate']),
            '--run-time', config['duration'],
            '--headless',
            '--html', str(report_path)
        ]
        
        print(f"🌐 Environment: {environment} - {env_description}")
        print(f"🎯 Target: {full_api_url}")
        print(f"🔗 Endpoint: {endpoint_name} ({endpoint_path})")
        print(f"📝 Endpoint Description: {endpoint_description}")
        print(f"👥 Users: {config['users']}")
        print(f"📈 Spawn Rate: {config['spawn_rate']}/sec")
        print(f"⏱️  Duration: {config['duration']}")
        print(f"📄 Report: {report_path}")
        print(f"📊 Description: {config['description']}")
        
        try:
            print(f"🚀 Executing: {' '.join(cmd)}")
            start_time = time.time()
            
            # Set environment variables for locust to use
            env_vars = os.environ.copy()
            env_vars['LOCUST_API_ENDPOINT'] = endpoint_path
            env_vars['LOCUST_ENVIRONMENT'] = environment
            env_vars['LOCUST_ENDPOINT_NAME'] = endpoint_name
            
            # Execute Locust test
            result = subprocess.run(cmd, cwd=current_dir, env=env_vars)
            
            end_time = time.time()
            duration = end_time - start_time
            
            if result.returncode == 0:
                print(f"✅ Locust test completed successfully in {duration:.1f} seconds")
                
                # Generate PDF report if HTML was created
                if report_path.exists():
                    print(f"📄 HTML report generated: {report_path}")
                    
                    # Try to generate PDF report
                    try:
                        self.generate_pdf_report(report_path, environment, config)
                    except Exception as pdf_error:
                        print(f"⚠️  PDF generation failed: {pdf_error}")
                
                return True, report_path
            else:
                print(f"❌ Locust test failed with return code: {result.returncode}")
                return False, None
                
        except FileNotFoundError:
            print("❌ Locust not found. Please install locust:")
            print("   pip install locust")
            return False, None
        except Exception as e:
            print(f"❌ Error running Locust test: {e}")
            return False, None
    
    def generate_pdf_report(self, html_report_path, environment, config):
        """Generate PDF report from HTML report"""
        try:
            # Import PDF generator
            pdf_generator_dir = self.current_dir / "reports" / "pdf_generator"
            
            if not pdf_generator_dir.exists():
                print("⚠️  PDF generator directory not found, skipping PDF generation")
                return
            
            # Add to path temporarily
            sys.path.insert(0, str(pdf_generator_dir))
            
            # Try to import and use PDF generator
            from generate_pdf_report import generate_pdf_from_html
            
            pdf_path = generate_pdf_from_html(
                html_report_path, 
                environment, 
                config['users'],
                config.get('description', 'QInsight Performance Test')
            )
            
            if pdf_path and Path(pdf_path).exists():
                print(f"📑 PDF report generated: {pdf_path}")
            else:
                print("⚠️  PDF generation completed but file not found")
                
        except ImportError:
            print("⚠️  PDF generator not available, skipping PDF generation")
        except Exception as e:
            print(f"⚠️  PDF generation error: {e}")
        finally:
            # Remove from path
            if str(pdf_generator_dir) in sys.path:
                sys.path.remove(str(pdf_generator_dir))

def main():
    """Main function to handle command line execution"""
    parser = argparse.ArgumentParser(
        description='QInsight Performance Testing Framework',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --test light_load --environment qa
  %(prog)s --test heavy_load --environment qa --users 50 --duration 120s
  %(prog)s --list
        """
    )
    
    parser.add_argument('--test', '-t',
                        choices=['light_load', 'medium_load', 'heavy_load', 'stress_test', 'endurance_test', 'spike_test'],
                        default='light_load',
                        help='Test configuration to run (default: light_load)')
    
    parser.add_argument('--environment', '-e',
                        choices=['dev', 'qa', 'staging', 'production'],
                        default='qa',
                        help='Environment to test against (default: qa)')
    
    parser.add_argument('--users', '-u',
                        type=int,
                        help='Number of concurrent users (overrides config)')
    
    parser.add_argument('--spawn-rate', '-r',
                        type=int,
                        help='User spawn rate per second (overrides config)')
    
    parser.add_argument('--duration', '-d',
                        help='Test duration (e.g., 60s, 5m) (overrides config)')
    
    parser.add_argument('--config', '-c',
                        help='Custom config file path')
    
    parser.add_argument('--list', '-l',
                        action='store_true',
                        help='List available tests and environments')
    
    args = parser.parse_args()
    
    try:
        # Initialize the test runner
        runner = QInsightPerformanceTestRunner(
            config_file=args.config,
            environment=args.environment
        )
        
        # Handle list command
        if args.list:
            runner.list_available_tests()
            return
        
        # Build custom configuration if overrides provided
        custom_config = None
        if any([args.users, args.spawn_rate, args.duration]):
            try:
                # Get base config first
                base_config = runner.config_loader.get_load_configuration(args.test)
                custom_config = base_config.copy()
                
                if args.users:
                    custom_config['users'] = args.users
                if args.spawn_rate:
                    custom_config['spawn_rate'] = args.spawn_rate
                if args.duration:
                    custom_config['duration'] = args.duration
                    
                print(f"🔧 Using custom configuration overrides")
                
            except Exception as e:
                print(f"❌ Error building custom configuration: {e}")
                return 1
        
        # Run the test
        print(f"🎯 Starting QInsight performance test...")
        success, report_path = runner.run_locust_test(
            test_config_name=args.test,
            environment=args.environment,
            custom_config=custom_config
        )
        
        if success:
            print(f"\n✅ Test completed successfully!")
            if report_path:
                print(f"📊 Report: {report_path}")
            return 0
        else:
            print(f"\n❌ Test failed!")
            return 1
            
    except KeyboardInterrupt:
        print(f"\n⚡ Test interrupted by user")
        return 130
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    exit(main()) 