"""
Enhanced Ambient API Locust Performance Test
Professional-grade performance testing with comprehensive metrics and reporting
"""

from locust import HttpUser, task, between, events
import requests
import psutil
import time
import json
import os
from datetime import datetime
from statistics import mean, median
from pathlib import Path

# Add project root to path for configuration imports
project_root = Path(__file__).parent.parent
import sys
sys.path.append(str(project_root))

# Import configuration loader
from utils.config_loader import get_config_loader

# Global variables to store comprehensive metrics
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
        self.endpoint_name = "unknown"
        self.endpoint_path = "/Ambient/generate_summary_html"

# Global metrics instance
metrics = PerformanceMetrics()

def monitor_system_resources():
    """Enhanced system resource monitoring"""
    try:
        cpu_percent = psutil.cpu_percent(interval=0.1)
        memory = psutil.virtual_memory()
        
        metrics.cpu_usage.append(cpu_percent)
        metrics.memory_usage.append(memory.percent)
        
    except Exception as e:
        print(f"⚠️ Error monitoring system resources: {e}")

@events.request.add_listener
def on_request(request_type, name, response_time, response_length, exception, context, **kwargs):
    """Enhanced request metrics capture with detailed error tracking"""
    metrics.total_requests += 1
    metrics.response_times.append(response_time)
    metrics.request_timestamps.append(time.time())
    
    if exception:
        metrics.error_count += 1
        metrics.failed_requests += 1
        
        # Capture detailed error information
        error_info = {
            'timestamp': datetime.now().isoformat(),
            'request_type': request_type,
            'name': name,
            'response_time': response_time,
            'exception': str(exception),
            'response_length': response_length
        }
        metrics.error_details.append(error_info)
        
        print(f"❌ Request failed: {name} - {exception} ({response_time:.0f}ms)")
    else:
        metrics.successful_requests += 1
        print(f"✅ Request successful: {name} - {response_time:.0f}ms")

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    """Initialize comprehensive metrics at test start"""
    global metrics
    metrics = PerformanceMetrics()
    metrics.start_time = datetime.now()
    metrics.user_count = environment.parsed_options.num_users
    
    # Get endpoint information from environment variables
    metrics.endpoint_name = os.environ.get('LOCUST_ENDPOINT_NAME', 'unknown')
    metrics.endpoint_path = os.environ.get('LOCUST_API_ENDPOINT', '/Ambient/generate_summary_html')
    current_env = os.environ.get('LOCUST_ENVIRONMENT', 'unknown')
    
    print("🚀 Ambient API Performance Test Started")
    print("="*60)
    print(f"📊 Target: {environment.host}{metrics.endpoint_path}")
    print(f"🔗 Endpoint: {metrics.endpoint_name} ({metrics.endpoint_path})")
    print(f"🌐 Environment: {current_env}")
    print(f"👥 Concurrent Users: {metrics.user_count}")
    print(f"⏰ Start Time: {metrics.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    """Generate comprehensive performance report at test end"""
    global metrics
    metrics.end_time = datetime.now()
    
    # Calculate comprehensive performance metrics
    if metrics.response_times:
        avg_response_time = mean(metrics.response_times)
        median_response_time = median(metrics.response_times)
        min_response_time = min(metrics.response_times)
        max_response_time = max(metrics.response_times)
        
        # Calculate percentiles
        sorted_times = sorted(metrics.response_times)
        p50 = sorted_times[int(0.50 * len(sorted_times))] if sorted_times else 0
        p75 = sorted_times[int(0.75 * len(sorted_times))] if sorted_times else 0
        p90 = sorted_times[int(0.90 * len(sorted_times))] if sorted_times else 0
        p95 = sorted_times[int(0.95 * len(sorted_times))] if sorted_times else 0
        p99 = sorted_times[int(0.99 * len(sorted_times))] if sorted_times else 0
    else:
        avg_response_time = median_response_time = min_response_time = max_response_time = 0
        p50 = p75 = p90 = p95 = p99 = 0
    
    # System resource metrics
    if metrics.cpu_usage:
        avg_cpu = mean(metrics.cpu_usage)
        max_cpu = max(metrics.cpu_usage)
        min_cpu = min(metrics.cpu_usage)
    else:
        avg_cpu = max_cpu = min_cpu = 0
        
    if metrics.memory_usage:
        avg_memory = mean(metrics.memory_usage)
        max_memory = max(metrics.memory_usage)
        min_memory = min(metrics.memory_usage)
    else:
        avg_memory = max_memory = min_memory = 0
    
    # Calculate test duration and throughput
    test_duration = (metrics.end_time - metrics.start_time).total_seconds()
    throughput = metrics.total_requests / test_duration if test_duration > 0 else 0
    
    # Calculate rates
    error_rate = (metrics.error_count / metrics.total_requests * 100) if metrics.total_requests > 0 else 0
    success_rate = (metrics.successful_requests / metrics.total_requests * 100) if metrics.total_requests > 0 else 0
    
    # Get configuration for enhanced report
    try:
        config_loader = get_config_loader()
        current_env = os.environ.get('LOCUST_ENVIRONMENT') or config_loader.current_environment or "unknown"
        
        # Try to get endpoint configuration if available
        try:
            endpoint_name = os.environ.get('LOCUST_ENDPOINT_NAME')
            if endpoint_name:
                endpoint_config = config_loader.get_endpoint_config(endpoint_name)
                endpoint_description = endpoint_config.get('description', 'No description available')
            else:
                endpoint_description = 'Default endpoint'
        except Exception:
            endpoint_description = 'Endpoint configuration not available'
        
        base_url = config_loader.get_base_url() if config_loader.current_environment else (environment.host if hasattr(environment, 'host') else "Unknown")
        endpoint_path = metrics.endpoint_path
        full_api_url = f"{base_url}{endpoint_path}"
        
    except Exception as e:
        print(f"⚠️ Error getting configuration for enhanced report: {e}")
        base_url = environment.host if hasattr(environment, 'host') else "Unknown"
        endpoint_path = metrics.endpoint_path
        full_api_url = f"{base_url}{endpoint_path}"
        current_env = os.environ.get('LOCUST_ENVIRONMENT', "unknown")
        endpoint_description = "Configuration not available"
    
    # Generate enhanced HTML report
    generate_enhanced_html_report(
        avg_response_time, median_response_time, min_response_time, max_response_time,
        p50, p75, p90, p95, p99, avg_cpu, max_cpu, min_cpu,
        avg_memory, max_memory, min_memory, throughput, test_duration,
        error_rate, success_rate, base_url, endpoint_path, current_env, endpoint_description
    )
    
    # Print comprehensive summary
    print_comprehensive_summary(
        avg_response_time, median_response_time, p95, p99,
        throughput, error_rate, success_rate, avg_cpu, avg_memory, test_duration
    )

# NOT REQUIRED FOR RUNNING SCRIPT - This function can be commented out
# It's only used for generating HTML reports, not essential for test execution
def generate_enhanced_html_report(avg_response_time, median_response_time, min_response_time, max_response_time,
                                p50, p75, p90, p95, p99, avg_cpu, max_cpu, min_cpu,
                                avg_memory, max_memory, min_memory, throughput, test_duration,
                                error_rate, success_rate, base_url, endpoint_path, current_env, endpoint_description):
    """Generate enhanced HTML performance report with professional styling"""
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Determine performance status
    if error_rate < 1 and avg_response_time < 10000:
        overall_status = "🌟 EXCELLENT"
        status_color = "#27ae60"
    elif error_rate < 5 and avg_response_time < 20000:
        overall_status = "✅ GOOD"
        status_color = "#2980b9"
    elif error_rate < 15 and avg_response_time < 30000:
        overall_status = "⚠️ NEEDS IMPROVEMENT"
        status_color = "#f39c12"
    else:
        overall_status = "❌ CRITICAL ISSUES"
        status_color = "#e74c3c"

    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ambient API Performance Report - {metrics.user_count} Users ({metrics.endpoint_name})</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{ 
            font-family: 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'sans-serif'; 
            line-height: 1.6;
            color: #2c3e50;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{ 
            max-width: 1400px; 
            margin: 0 auto; 
            background: white; 
            border-radius: 15px; 
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3); 
            overflow: hidden;
        }}
        
        .header {{ 
            background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        .header h1 {{ 
            font-size: 2.8em; 
            margin-bottom: 10px; 
            font-weight: 300;
        }}
        
        .header h2 {{ 
            font-size: 1.6em; 
            opacity: 0.9; 
            font-weight: 300;
        }}
        
        .header .timestamp {{ 
            margin-top: 20px; 
            font-size: 1.1em; 
            opacity: 0.8;
        }}
        
        .status-banner {{ 
            background: {status_color}; 
            color: white; 
            padding: 20px; 
            text-align: center; 
            font-size: 1.4em; 
            font-weight: bold;
        }}
        
        .content {{ padding: 40px; }}
        
        .metrics-grid {{ 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
            gap: 30px; 
            margin-bottom: 50px; 
        }}
        
        .metric-card {{ 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            color: white; 
            padding: 30px; 
            border-radius: 15px; 
            text-align: center; 
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2); 
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        
        .metric-card:hover {{ 
            transform: translateY(-10px); 
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }}
        
        .metric-title {{ 
            font-size: 14px; 
            font-weight: 600; 
            margin-bottom: 15px; 
            opacity: 0.9; 
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .metric-value {{ 
            font-size: 2.5em; 
            font-weight: 700; 
            margin-bottom: 10px; 
            line-height: 1;
        }}
        
        .metric-unit {{ 
            font-size: 13px; 
            opacity: 0.8; 
            font-weight: 300;
        }}
        
        .section {{ 
            margin: 50px 0; 
            background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
            border-radius: 15px; 
            padding: 40px; 
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }}
        
        .section h3 {{ 
            color: #2c3e50; 
            font-size: 1.8em; 
            margin-bottom: 25px; 
            padding-bottom: 15px; 
            border-bottom: 3px solid #3498db; 
            font-weight: 300;
        }}
        
        .table-container {{ 
            overflow-x: auto; 
            border-radius: 10px; 
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }}
        
        table {{ 
            width: 100%; 
            border-collapse: collapse; 
            background: white;
        }}
        
        th, td {{ 
            padding: 18px; 
            text-align: left; 
            border-bottom: 1px solid #e8e8e8; 
        }}
        
        th {{ 
            background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
            color: white; 
            font-weight: 600; 
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-size: 13px;
        }}
        
        tbody tr:nth-child(even) {{ 
            background-color: #f8f9fa; 
        }}
        
        tbody tr:hover {{ 
            background-color: #e3f2fd; 
            transition: background-color 0.3s ease;
        }}
        
        .status-excellent {{ color: #27ae60; font-weight: bold; }}
        .status-good {{ color: #2980b9; font-weight: bold; }}
        .status-warning {{ color: #f39c12; font-weight: bold; }}
        .status-critical {{ color: #e74c3c; font-weight: bold; }}
        
        .test-config {{ 
            background: linear-gradient(135deg, #ecf0f1 0%, #bdc3c7 100%);
            padding: 30px; 
            border-radius: 12px; 
            margin: 30px 0; 
            border-left: 5px solid #3498db; 
        }}
        
        .payload-box {{ 
            background: #2c3e50; 
            color: #ecf0f1; 
            padding: 25px; 
            border-radius: 10px; 
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace; 
            font-size: 13px;
            line-height: 1.5;
            overflow-x: auto; 
            margin: 20px 0;
        }}
        
        .error-section {{
            background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
            border-left: 5px solid #e74c3c;
            padding: 30px;
            border-radius: 10px;
            margin: 30px 0;
            display: {'block' if metrics.failed_requests > 0 else 'none'};
        }}
        
        .recommendations {{
            background: linear-gradient(135deg, #e8f5e8 0%, #c8e6c9 100%);
            border-left: 5px solid #27ae60;
            padding: 30px;
            border-radius: 10px;
            margin: 30px 0;
        }}
        
        .chart-placeholder {{
            background: linear-gradient(135deg, #f1f2f6 0%, #dfe4ea 100%);
            height: 250px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #57606f;
            font-style: italic;
            margin: 30px 0;
            font-size: 1.1em;
        }}
        
        .footer {{
            background: #2c3e50;
            color: white;
            padding: 30px;
            text-align: center;
            font-size: 14px;
        }}
        
        .grid-2 {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin: 30px 0;
        }}
        
        @media (max-width: 768px) {{
            .container {{ margin: 10px; }}
            .content {{ padding: 20px; }}
            .metrics-grid {{ grid-template-columns: 1fr; }}
            .grid-2 {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 Ambient API Performance Report</h1>
            <h2>Load Test with {metrics.user_count} Concurrent Users</h2>
            <h3>Environment: {current_env} | Endpoint: {metrics.endpoint_name}</h3>
            <div class="timestamp">Generated: {current_time}</div>
        </div>
        
        <div class="status-banner">
            Overall Performance Status: {overall_status}
        </div>
        
        <div class="content">
            <div class="test-config">
                <h3>📋 API Test Details</h3>
                <div class="grid-2">
                    <div>
                        <p><strong>Environment:</strong> {current_env}</p>
                        <p><strong>Base URL:</strong> {base_url}</p>
                        <p><strong>Endpoint:</strong> {endpoint_path}</p>
                        <p><strong>Endpoint Name:</strong> {metrics.endpoint_name}</p>
                        <p><strong>Method:</strong> POST</p>
                        <p><strong>Concurrent Users:</strong> {metrics.user_count}</p>
                        <p><strong>Test Duration:</strong> {test_duration:.1f} seconds</p>
                    </div>
                    <div>
                        <p><strong>Total Requests:</strong> {metrics.total_requests}</p>
                        <p><strong>Start Time:</strong> {metrics.start_time.strftime('%H:%M:%S')}</p>
                        <p><strong>End Time:</strong> {metrics.end_time.strftime('%H:%M:%S')}</p>
                        <p><strong>Test Type:</strong> Load Testing</p>
                        <p><strong>Endpoint Description:</strong> {endpoint_description}</p>
                    </div>
                </div>
                
                <h4>📨 Request Payload Sample:</h4>
                <div class="payload-box">{{
    "conversation": "Dave. I've heard your knee is hurting you. Yes, my right knee. Okay. And you had no injuries, correct? No, it's just I believe it's being caused by the fact that my wife and I walk typically three to four times a week, and we walk anywhere from three to four miles during the exercise. Got it. So let me just take a look at your knee..."
}}</div>
            </div>

            <div class="metrics-grid">
                <div class="metric-card">
                    <div class="metric-title">Average Response Time</div>
                    <div class="metric-value">{avg_response_time:.0f}</div>
                    <div class="metric-unit">milliseconds</div>
                </div>
                
                <div class="metric-card">
                    <div class="metric-title">Throughput</div>
                    <div class="metric-value">{throughput:.2f}</div>
                    <div class="metric-unit">requests/second</div>
                </div>
                
                <div class="metric-card">
                    <div class="metric-title">Success Rate</div>
                    <div class="metric-value">{success_rate:.1f}%</div>
                    <div class="metric-unit">successful requests</div>
                </div>
                
                <div class="metric-card">
                    <div class="metric-title">Error Rate</div>
                    <div class="metric-value">{error_rate:.1f}%</div>
                    <div class="metric-unit">failed requests</div>
                </div>
                
                <div class="metric-card">
                    <div class="metric-title">CPU Utilization</div>
                    <div class="metric-value">{avg_cpu:.1f}%</div>
                    <div class="metric-unit">average usage</div>
                </div>
                
                <div class="metric-card">
                    <div class="metric-title">Memory Usage</div>
                    <div class="metric-value">{avg_memory:.1f}%</div>
                    <div class="metric-unit">average usage</div>
                </div>
            </div>

            <div class="section">
                <h3>📊 Detailed Performance Metrics - {metrics.endpoint_name} Endpoint</h3>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Metric</th>
                                <th>Value</th>
                                <th>Status</th>
                                <th>Industry Standard</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Average Response Time</td>
                                <td>{avg_response_time:.0f} ms</td>
                                <td class="{'status-excellent' if avg_response_time < 2000 else 'status-good' if avg_response_time < 5000 else 'status-warning' if avg_response_time < 10000 else 'status-critical'}">
                                    {'🌟 EXCELLENT' if avg_response_time < 2000 else '✅ GOOD' if avg_response_time < 5000 else '⚠️ ACCEPTABLE' if avg_response_time < 10000 else '❌ POOR'}
                                </td>
                                <td>&lt; 2000 ms</td>
                            </tr>
                            <tr>
                                <td>Median Response Time</td>
                                <td>{median_response_time:.0f} ms</td>
                                <td class="{'status-excellent' if median_response_time < 1500 else 'status-good' if median_response_time < 3000 else 'status-warning' if median_response_time < 8000 else 'status-critical'}">
                                    {'🌟 EXCELLENT' if median_response_time < 1500 else '✅ GOOD' if median_response_time < 3000 else '⚠️ ACCEPTABLE' if median_response_time < 8000 else '❌ POOR'}
                                </td>
                                <td>&lt; 1500 ms</td>
                            </tr>
                            <tr>
                                <td>95th Percentile</td>
                                <td>{p95:.0f} ms</td>
                                <td class="{'status-excellent' if p95 < 3000 else 'status-good' if p95 < 6000 else 'status-warning' if p95 < 12000 else 'status-critical'}">
                                    {'🌟 EXCELLENT' if p95 < 3000 else '✅ GOOD' if p95 < 6000 else '⚠️ ACCEPTABLE' if p95 < 12000 else '❌ POOR'}
                                </td>
                                <td>&lt; 3000 ms</td>
                            </tr>
                            <tr>
                                <td>99th Percentile</td>
                                <td>{p99:.0f} ms</td>
                                <td class="{'status-excellent' if p99 < 5000 else 'status-good' if p99 < 10000 else 'status-warning' if p99 < 20000 else 'status-critical'}">
                                    {'🌟 EXCELLENT' if p99 < 5000 else '✅ GOOD' if p99 < 10000 else '⚠️ ACCEPTABLE' if p99 < 20000 else '❌ POOR'}
                                </td>
                                <td>&lt; 5000 ms</td>
                            </tr>
                            <tr>
                                <td>Min Response Time</td>
                                <td>{min_response_time:.0f} ms</td>
                                <td class="status-excellent">📊 INFO</td>
                                <td>N/A</td>
                            </tr>
                            <tr>
                                <td>Max Response Time</td>
                                <td>{max_response_time:.0f} ms</td>
                                <td class="{'status-excellent' if max_response_time < 10000 else 'status-good' if max_response_time < 20000 else 'status-warning' if max_response_time < 30000 else 'status-critical'}">
                                    {'✅ ACCEPTABLE' if max_response_time < 10000 else '⚠️ HIGH' if max_response_time < 20000 else '❌ CRITICAL' if max_response_time < 30000 else '🚨 EXTREME'}
                                </td>
                                <td>&lt; 10000 ms</td>
                            </tr>
                            <tr>
                                <td>Throughput</td>
                                <td>{throughput:.2f} req/sec</td>
                                <td class="{'status-excellent' if throughput > 50 else 'status-good' if throughput > 10 else 'status-warning' if throughput > 1 else 'status-critical'}">
                                    {'🌟 EXCELLENT' if throughput > 50 else '✅ GOOD' if throughput > 10 else '⚠️ LOW' if throughput > 1 else '❌ VERY LOW'}
                                </td>
                                <td>&gt; 10 req/sec</td>
                            </tr>
                            <tr>
                                <td>Error Rate</td>
                                <td>{error_rate:.2f}%</td>
                                <td class="{'status-excellent' if error_rate < 1 else 'status-good' if error_rate < 5 else 'status-warning' if error_rate < 15 else 'status-critical'}">
                                    {'🌟 EXCELLENT' if error_rate < 1 else '✅ GOOD' if error_rate < 5 else '⚠️ HIGH' if error_rate < 15 else '❌ CRITICAL'}
                                </td>
                                <td>&lt; 1%</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="section">
                <h3>🖥️ System Resource Analysis</h3>
                <div class="grid-2">
                    <div class="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>Resource</th>
                                    <th>Average</th>
                                    <th>Peak</th>
                                    <th>Status</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>CPU Usage</td>
                                    <td>{avg_cpu:.1f}%</td>
                                    <td>{max_cpu:.1f}%</td>
                                    <td class="{'status-excellent' if avg_cpu < 50 else 'status-good' if avg_cpu < 70 else 'status-warning' if avg_cpu < 85 else 'status-critical'}">
                                        {'✅ OPTIMAL' if avg_cpu < 50 else '✅ NORMAL' if avg_cpu < 70 else '⚠️ HIGH' if avg_cpu < 85 else '❌ CRITICAL'}
                                    </td>
                                </tr>
                                <tr>
                                    <td>Memory Usage</td>
                                    <td>{avg_memory:.1f}%</td>
                                    <td>{max_memory:.1f}%</td>
                                    <td class="{'status-excellent' if avg_memory < 60 else 'status-good' if avg_memory < 75 else 'status-warning' if avg_memory < 85 else 'status-critical'}">
                                        {'✅ OPTIMAL' if avg_memory < 60 else '✅ NORMAL' if avg_memory < 75 else '⚠️ HIGH' if avg_memory < 85 else '❌ CRITICAL'}
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="chart-placeholder">
                        📈 Resource Utilization Trends<br/>
                        <small>(Chart visualization would be implemented here)</small>
                    </div>
                </div>
            </div>

            <div class="section">
                <h3>📈 Request Distribution</h3>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Request Type</th>
                                <th>Count</th>
                                <th>Percentage</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>✅ Successful Requests</td>
                                <td>{metrics.successful_requests}</td>
                                <td>{success_rate:.2f}%</td>
                                <td class="status-excellent">SUCCESS</td>
                            </tr>
                            <tr>
                                <td>❌ Failed Requests</td>
                                <td>{metrics.failed_requests}</td>
                                <td>{error_rate:.2f}%</td>
                                <td class="{'status-excellent' if error_rate == 0 else 'status-good' if error_rate < 5 else 'status-warning' if error_rate < 15 else 'status-critical'}">
                                    {'NONE' if error_rate == 0 else 'LOW' if error_rate < 5 else 'MODERATE' if error_rate < 15 else 'HIGH'}
                                </td>
                            </tr>
                            <tr>
                                <td>📊 Total Requests</td>
                                <td>{metrics.total_requests}</td>
                                <td>100.00%</td>
                                <td class="status-excellent">COMPLETE</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="error-section">
                <h3>❌ Error Analysis</h3>
                <p><strong>Total Errors:</strong> {metrics.failed_requests}</p>
                <p><strong>Error Rate:</strong> {error_rate:.2f}%</p>
                <div class="payload-box">
                    <strong>Recent Error Details:</strong><br/>
                    {chr(10).join([f"• {error['timestamp']}: {error['exception']}" for error in metrics.error_details[-5:]]) if metrics.error_details else "No errors recorded"}
                </div>
            </div>

            <div class="recommendations">
                <h3>💡 Performance Recommendations</h3>
                <div class="grid-2">
                    <div>
                        <h4>🎯 Priority Actions:</h4>
                        <ul>
                            {f'<li>🔧 Optimize response times for {metrics.endpoint_name} endpoint (currently {avg_response_time:.0f}ms)</li>' if avg_response_time > 5000 else f'<li>✅ Response times for {metrics.endpoint_name} endpoint are within acceptable limits</li>'}
                            {f'<li>📈 Improve throughput (currently {throughput:.1f} req/sec)</li>' if throughput < 5 else '<li>✅ Throughput is adequate for current load</li>'}
                            {f'<li>🚨 Address error rate (currently {error_rate:.1f}%)</li>' if error_rate > 5 else '<li>✅ Error rate is within acceptable limits</li>'}
                        </ul>
                    </div>
                    <div>
                        <h4>📊 Monitoring:</h4>
                        <ul>
                            <li>🔄 Implement continuous performance monitoring for {metrics.endpoint_name}</li>
                            <li>📈 Set up automated alerting for performance degradation</li>
                            <li>🎯 Establish performance baselines for {metrics.endpoint_name} endpoint</li>
                            <li>📋 Regular performance regression testing across all endpoints</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="section">
                <h3>🏁 Executive Summary</h3>
                <p><strong>Overall Performance Grade:</strong> 
                    <span style="color: {status_color}; font-weight: bold;">{overall_status}</span>
                </p>
                
                <p><strong>Key Findings:</strong></p>
                <ul>
                    <li>System processed {metrics.total_requests} requests over {test_duration:.1f} seconds using {metrics.endpoint_name} endpoint</li>
                    <li>Average response time: {avg_response_time:.0f}ms ({'within' if avg_response_time < 10000 else 'exceeding'} acceptable limits)</li>
                    <li>System reliability: {success_rate:.1f}% success rate</li>
                    <li>Throughput: {throughput:.2f} requests per second</li>
                    <li>Resource utilization: CPU {avg_cpu:.1f}%, Memory {avg_memory:.1f}%</li>
                    <li>Endpoint tested: {metrics.endpoint_name} ({endpoint_path})</li>
                </ul>
                
                <p><strong>Recommendation:</strong> 
                    {'System is ready for production deployment with monitoring.' if error_rate < 5 and avg_response_time < 10000 else 'System requires optimization before production deployment.' if error_rate < 20 else 'System has critical issues requiring immediate attention.'}
                </p>
            </div>
        </div>
        
        <div class="footer">
            Generated by BDD Performance Testing Framework | {current_time}<br/>
            Test ID: {timestamp} | Environment: {current_env} | Endpoint: {metrics.endpoint_name}
        </div>
    </div>
</body>
</html>
    """
    
    # Save the enhanced HTML report
    reports_dir = Path(__file__).parent.parent / "reports"
    reports_dir.mkdir(exist_ok=True)
    
    endpoint_suffix = f"_{metrics.endpoint_name}" if metrics.endpoint_name != "unknown" else ""
    report_filename = f"ambient_api_performance_report_{current_env}_{metrics.user_count}users{endpoint_suffix}_{timestamp}.html"
    report_path = reports_dir / report_filename
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"📄 Enhanced HTML Report saved: {report_path}")
    return str(report_path)

# NOT REQUIRED FOR RUNNING SCRIPT - This function can be commented out
# It's only used for printing summary to console, not essential for test execution
def print_comprehensive_summary(avg_response_time, median_response_time, p95, p99,
                               throughput, error_rate, success_rate, avg_cpu, avg_memory, test_duration):
    """Print comprehensive test summary to console"""
    print("\n" + "="*80)
    print("🎉 AMBIENT API PERFORMANCE TEST COMPLETED")
    print("="*80)
    
    print(f"📊 EXECUTIVE SUMMARY:")
    print(f"   • Test Duration: {test_duration:.1f} seconds")
    print(f"   • Total Requests: {metrics.total_requests}")
    print(f"   • Successful: {metrics.successful_requests} ({success_rate:.1f}%)")
    print(f"   • Failed: {metrics.failed_requests} ({error_rate:.1f}%)")
    print(f"   • Endpoint: {metrics.endpoint_name} ({metrics.endpoint_path})")
    
    print(f"\n⏱️ RESPONSE TIME ANALYSIS:")
    print(f"   • Average: {avg_response_time:.0f} ms")
    print(f"   • Median: {median_response_time:.0f} ms")
    print(f"   • 95th Percentile: {p95:.0f} ms")
    print(f"   • 99th Percentile: {p99:.0f} ms")
    
    print(f"\n📈 PERFORMANCE METRICS:")
    print(f"   • Throughput: {throughput:.2f} req/sec")
    print(f"   • Average CPU: {avg_cpu:.1f}%")
    print(f"   • Average Memory: {avg_memory:.1f}%")
    
    # Performance assessment
    if error_rate < 1 and avg_response_time < 10000:
        assessment = "🌟 EXCELLENT - Ready for production"
    elif error_rate < 5 and avg_response_time < 20000:
        assessment = "✅ GOOD - Minor optimizations recommended"
    elif error_rate < 15 and avg_response_time < 30000:
        assessment = "⚠️ NEEDS IMPROVEMENT - Optimization required"
    else:
        assessment = "❌ CRITICAL ISSUES - Immediate attention required"
    
    print(f"\n🎯 PERFORMANCE ASSESSMENT: {assessment}")
    print("="*80)

class AmbientAPIUser(HttpUser):
    """Enhanced Ambient API User with realistic behavior patterns and endpoint configuration"""
    wait_time = between(1, 3)
    
    def __init__(self, *args, **kwargs):
        """Initialize user with configuration"""
        super().__init__(*args, **kwargs)
        self.config_loader = get_config_loader()
        
        # Get API configuration
        try:
            # Check for environment from environment variable (set by test runner)
            env_environment = os.environ.get('LOCUST_ENVIRONMENT')
            if env_environment:
                self.config_loader.set_environment(env_environment)
                print(f"🌐 Using environment from runner: {env_environment}")
            
            # Try to get API configuration from api_configurations section first
            try:
                # Determine which API configuration to use based on endpoint
                api_name = os.environ.get('LOCUST_ENDPOINT_NAME', 'original')  # default to 'original'
                api_config = self.config_loader.get_environment_aware_api_configuration(api_name)
                
                # Use the resolved headers and configuration
                self.api_config = {
                    "timeout": api_config.get('timeout', 30),
                    "content_type": "application/json",
                    "headers": api_config.get('resolved_headers', api_config.get('headers', {}))
                }
                self.endpoint = api_config.get('endpoint', '/Ambient/generate_summary_html')
                self.endpoint_name = api_name
                print(f"✅ Using API configuration '{api_name}' with environment-aware headers")
                print(f"🔗 Endpoint: {self.endpoint}")
                print(f"📋 Headers: {len(self.api_config['headers'])} configured")
                
            except Exception as api_config_error:
                print(f"⚠️ Could not load from api_configurations: {api_config_error}")
                # Fallback to legacy API config method
                self.api_config = self.config_loader.get_api_config()
                
                # Check for endpoint from environment variable (set by test runner)
                env_endpoint = os.environ.get('LOCUST_API_ENDPOINT')
                env_endpoint_name = os.environ.get('LOCUST_ENDPOINT_NAME')
                
                if env_endpoint:
                    self.endpoint = env_endpoint
                    self.endpoint_name = env_endpoint_name or "custom"
                    print(f"🔗 Using endpoint from environment: {self.endpoint} ({self.endpoint_name})")
                else:
                    # Try to get default endpoint from configuration
                    try:
                        default_endpoint_name = self.config_loader.config.get('execution', {}).get('default_endpoint', 'v1')
                        endpoint_config = self.config_loader.get_endpoint_config(default_endpoint_name)
                        self.endpoint = endpoint_config['path']
                        self.endpoint_name = default_endpoint_name
                        print(f"🔗 Using default endpoint from config: {self.endpoint} ({self.endpoint_name})")
                    except Exception as e:
                        print(f"⚠️ Could not load endpoint from config: {e}")
                        self.endpoint = self.config_loader.get_api_endpoint()
                        self.endpoint_name = "original"
                        print(f"🔗 Using fallback endpoint: {self.endpoint}")
            
            self.test_data_config = self.config_loader.get_test_data()
                
        except Exception as e:
            print(f"⚠️ Error loading configuration: {e}")
            # Use fallback configuration
            self.api_config = {
                "timeout": 30,
                "content_type": "application/json",
                "headers": {
                    "User-Agent": "BDD-Performance-Testing-Framework/1.0",
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                }
            }
            self.endpoint = "/Ambient/generate_summary_html"
            self.endpoint_name = "fallback"
            self.test_data_config = {}
    
    def on_start(self):
        """Initialize user session"""
        monitor_system_resources()
        
        # Update global metrics with endpoint information
        metrics.endpoint_name = getattr(self, 'endpoint_name', 'unknown')
        metrics.endpoint_path = getattr(self, 'endpoint', '/Ambient/generate_summary_html')
        
        # Get current environment info
        try:
            current_env = self.config_loader.current_environment or os.environ.get('LOCUST_ENVIRONMENT', 'unknown')
            full_url = f"{self.host}{self.endpoint}"
            print(f"🔥 User started - Environment: {current_env}")
            print(f"🎯 Target: {full_url}")
        except Exception as e:
            print(f"🔥 User started - Target: {self.host}{self.endpoint}")
            print(f"⚠️ Configuration error: {e}")

    # NOT REQUIRED FOR RUNNING SCRIPT - This function can be commented out
    # It's only used for generating summary HTML, not essential for test execution
    @task(10)
    def generate_summary_html(self):
        """Main task - POST request to generate summary HTML with realistic medical data"""
        monitor_system_resources()
        
        # Get headers from configuration
        headers = self.api_config.get('headers', {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "BDD-Performance-Testing-Framework/1.0"
        })
        
        # Get conversation data from configuration
        conversation = self.test_data_config.get('medical_conversation', 
            """Dave. I've heard your knee is hurting you. Yes, my right knee. Okay. And you had no injuries, correct? No, it's just I believe it's being caused by the fact that my wife and I walk typically three to four times a week, and we walk anywhere from three to four miles during the exercise. Got it. So let me just take a look at your knee. I see you don't have any effusion in your knee. Is it tender along here? I'm pressing along your medial femoral condyle. Does that work? It's tender on the internal side of the knee, yes. Yeah. Okay. And I'm looking at your motion now. You're able to extend fully, and you're flexing 140 degrees, which is great. I'm doing this little test on you, a McMurray's test. Does that hurt where I'm pressing and twisting your ankle?"""
        )
        
        payload = {
            "conversation": conversation
        }
        
        try:
            with self.client.post(
                self.endpoint,
                json=payload,
                headers=headers,
                name=f"POST {self.endpoint}",
                catch_response=True
            ) as response:
                
                if response.status_code == 200:
                    # Validate response content
                    try:
                        content = response.text
                        if content and len(content) > 50:
                            # Additional validation for HTML content
                            if 'html' in content.lower() or len(content) > 100:
                                response.success()
                                print(f"✅ Request successful - {response.elapsed.total_seconds() * 1000:.0f}ms")
                            else:
                                response.failure("Response content validation failed - insufficient content")
                        else:
                            response.failure("Response content too short or empty")
                    except Exception as e:
                        response.failure(f"Response validation error: {str(e)}")
                        
                elif response.status_code in [502, 503, 504]:
                    response.failure(f"Server error {response.status_code} - Service unavailable")
                    
                elif response.status_code == 429:
                    response.failure("Rate limit exceeded - too many requests")
                    
                else:
                    response.failure(f"HTTP {response.status_code}: {response.text[:200]}")
                    
        except Exception as e:
            print(f"❌ Request exception: {str(e)}")

    def on_stop(self):
        """Cleanup when user stops"""
        print("🛑 User session ended")

# Custom Locust events for enhanced metrics collection
@events.init.add_listener
def on_locust_init(environment, **kwargs):
    """Initialize enhanced performance monitoring"""
    print("🔧 Initializing enhanced performance monitoring...")
    print("📊 Metrics collection enabled for comprehensive reporting")

if __name__ == "__main__":
    # This allows the file to be run directly with locust
    import subprocess
    import sys
    
    # Example usage
    print("🦗 Ambient API Locust Performance Test")
    print("Usage: locust -f ambient_api_locust.py --host=https://innovationz-dev.myqone.com")
    print("Example: locust -f ambient_api_locust.py --host=https://innovationz-dev.myqone.com --users=30 --spawn-rate=5 --run-time=90s --headless") 