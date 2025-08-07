import os
import json
import time
from datetime import datetime
from jinja2 import Template

class ReportGenerator:
    def __init__(self):
        self.reports_dir = "reports"
        self.screenshots_dir = "screenshots"
        self.test_results = {
            'start_time': None,
            'end_time': None,
            'total_scenarios': 0,
            'passed_scenarios': 0,
            'failed_scenarios': 0,
            'skipped_scenarios': 0,
            'features': [],
            'screenshots': [],
            'errors': []
        }
        
        # Create directories if they don't exist
        if not os.path.exists(self.reports_dir):
            os.makedirs(self.reports_dir)
        if not os.path.exists(self.screenshots_dir):
            os.makedirs(self.screenshots_dir)

    def start_test_run(self):
        """Start tracking test run"""
        self.test_results['start_time'] = datetime.now()
        print(f"📊 Test run started at: {self.test_results['start_time']}")

    def end_test_run(self):
        """End test run and generate report"""
        self.test_results['end_time'] = datetime.now()
        duration = self.test_results['end_time'] - self.test_results['start_time']
        self.test_results['duration'] = str(duration)
        
        print(f"📊 Test run completed at: {self.test_results['end_time']}")
        print(f"📊 Total duration: {duration}")
        
        # Generate report
        self.generate_html_report()
        self.generate_json_report()
        self.generate_summary_report()

    def add_feature_result(self, feature):
        """Add feature result to tracking"""
        feature_result = {
            'name': feature.name,
            'filename': feature.filename,
            'scenarios': [],
            'total_scenarios': len(feature.scenarios),
            'passed_scenarios': 0,
            'failed_scenarios': 0,
            'skipped_scenarios': 0
        }
        
        for scenario in feature.scenarios:
            scenario_result = {
                'name': scenario.name,
                'status': scenario.status,
                'duration': getattr(scenario, 'duration', 'N/A'),
                'error_message': getattr(scenario, 'error_message', ''),
                'steps': []
            }
            
            for step in scenario.steps:
                step_result = {
                    'name': step.name,
                    'status': step.status,
                    'duration': getattr(step, 'duration', 'N/A'),
                    'error_message': getattr(step, 'error_message', '')
                }
                scenario_result['steps'].append(step_result)
            
            feature_result['scenarios'].append(scenario_result)
            
            # Update counters
            if scenario.status == 'passed':
                feature_result['passed_scenarios'] += 1
                self.test_results['passed_scenarios'] += 1
            elif scenario.status == 'failed':
                feature_result['failed_scenarios'] += 1
                self.test_results['failed_scenarios'] += 1
            else:
                feature_result['skipped_scenarios'] += 1
                self.test_results['skipped_scenarios'] += 1
            
            self.test_results['total_scenarios'] += 1
        
        self.test_results['features'].append(feature_result)

    def add_screenshot(self, screenshot_path, scenario_name, status):
        """Add screenshot to report"""
        if os.path.exists(screenshot_path):
            self.test_results['screenshots'].append({
                'path': screenshot_path,
                'scenario': scenario_name,
                'status': status,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

    def add_error(self, error_message, scenario_name, step_name=""):
        """Add error to report"""
        self.test_results['errors'].append({
            'message': error_message,
            'scenario': scenario_name,
            'step': step_name,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def generate_html_report(self):
        """Generate comprehensive HTML report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"test_report_{timestamp}.html"
        report_path = os.path.join(self.reports_dir, report_filename)
        
        # Calculate statistics
        total_scenarios = self.test_results['total_scenarios']
        passed_scenarios = self.test_results['passed_scenarios']
        failed_scenarios = self.test_results['failed_scenarios']
        skipped_scenarios = self.test_results['skipped_scenarios']
        
        if total_scenarios > 0:
            pass_rate = (passed_scenarios / total_scenarios) * 100
            fail_rate = (failed_scenarios / total_scenarios) * 100
        else:
            pass_rate = fail_rate = 0
        
        # HTML Template
        html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Execution Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
        .stats { display: flex; justify-content: space-around; margin: 20px 0; }
        .stat-card { background: white; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .stat-number { font-size: 2em; font-weight: bold; }
        .passed { color: #28a745; }
        .failed { color: #dc3545; }
        .skipped { color: #ffc107; }
        .feature { background: white; margin: 10px 0; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .feature-header { background: #f8f9fa; padding: 15px; border-radius: 10px 10px 0 0; font-weight: bold; }
        .scenario { margin: 10px; padding: 10px; border-left: 4px solid #dee2e6; }
        .scenario.passed { border-left-color: #28a745; }
        .scenario.failed { border-left-color: #dc3545; }
        .scenario.skipped { border-left-color: #ffc107; }
        .step { margin: 5px 0; padding: 5px; font-size: 0.9em; }
        .step.passed { color: #28a745; }
        .step.failed { color: #dc3545; }
        .screenshots { margin: 20px 0; }
        .screenshot { margin: 10px 0; }
        .screenshot img { max-width: 100%; border: 1px solid #ddd; border-radius: 5px; }
        .errors { background: #fff3cd; border: 1px solid #ffeaa7; border-radius: 10px; padding: 15px; margin: 20px 0; }
        .error { background: #f8d7da; border: 1px solid #f5c6cb; border-radius: 5px; padding: 10px; margin: 5px 0; }
        .timestamp { color: #6c757d; font-size: 0.8em; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🚀 Test Execution Report</h1>
        <p>Generated on: {{ timestamp }}</p>
        <p>Duration: {{ duration }}</p>
    </div>
    
    <div class="stats">
        <div class="stat-card">
            <div class="stat-number passed">{{ passed_scenarios }}</div>
            <div>Passed</div>
        </div>
        <div class="stat-card">
            <div class="stat-number failed">{{ failed_scenarios }}</div>
            <div>Failed</div>
        </div>
        <div class="stat-card">
            <div class="stat-number skipped">{{ skipped_scenarios }}</div>
            <div>Skipped</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{{ total_scenarios }}</div>
            <div>Total</div>
        </div>
        <div class="stat-card">
            <div class="stat-number passed">{{ "%.1f"|format(pass_rate) }}%</div>
            <div>Pass Rate</div>
        </div>
    </div>
    
    <h2>📋 Test Results</h2>
    {% for feature in features %}
    <div class="feature">
        <div class="feature-header">
            📁 {{ feature.name }}
            <span class="timestamp">({{ feature.passed_scenarios }}/{{ feature.total_scenarios }} passed)</span>
        </div>
        {% for scenario in feature.scenarios %}
        <div class="scenario {{ scenario.status }}">
            <h4>🔄 {{ scenario.name }}</h4>
            <p><strong>Status:</strong> <span class="{{ scenario.status }}">{{ scenario.status.upper() }}</span></p>
            {% if scenario.duration != 'N/A' %}
            <p><strong>Duration:</strong> {{ scenario.duration }}</p>
            {% endif %}
            {% if scenario.error_message %}
            <p><strong>Error:</strong> {{ scenario.error_message }}</p>
            {% endif %}
            <details>
                <summary>Steps ({{ scenario.steps|length }})</summary>
                {% for step in scenario.steps %}
                <div class="step {{ step.status }}">
                    <span class="{{ step.status }}">{{ "✅" if step.status == "passed" else "❌" if step.status == "failed" else "⏭️" }}</span>
                    {{ step.name }}
                    {% if step.error_message %}
                    <br><small class="error">{{ step.error_message }}</small>
                    {% endif %}
                </div>
                {% endfor %}
            </details>
        </div>
        {% endfor %}
    </div>
    {% endfor %}
    
    {% if screenshots %}
    <h2>📸 Screenshots</h2>
    <div class="screenshots">
        {% for screenshot in screenshots %}
        <div class="screenshot">
            <h4>{{ screenshot.scenario }} ({{ screenshot.status }})</h4>
            <p class="timestamp">{{ screenshot.timestamp }}</p>
            <img src="../{{ screenshot.path }}" alt="Screenshot for {{ screenshot.scenario }}">
        </div>
        {% endfor %}
    </div>
    {% endif %}
    
    {% if errors %}
    <h2>❌ Errors</h2>
    <div class="errors">
        {% for error in errors %}
        <div class="error">
            <strong>{{ error.scenario }}</strong>
            {% if error.step %}<br><em>Step: {{ error.step }}</em>{% endif %}
            <br>{{ error.message }}
            <br><small class="timestamp">{{ error.timestamp }}</small>
        </div>
        {% endfor %}
    </div>
    {% endif %}
</body>
</html>
        """
        
        template = Template(html_template)
        html_content = template.render(
            timestamp=self.test_results['start_time'].strftime("%Y-%m-%d %H:%M:%S"),
            duration=self.test_results.get('duration', 'N/A'),
            total_scenarios=total_scenarios,
            passed_scenarios=passed_scenarios,
            failed_scenarios=failed_scenarios,
            skipped_scenarios=skipped_scenarios,
            pass_rate=pass_rate,
            fail_rate=fail_rate,
            features=self.test_results['features'],
            screenshots=self.test_results['screenshots'],
            errors=self.test_results['errors']
        )
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"📊 HTML Report generated: {report_path}")
        return report_path

    def generate_json_report(self):
        """Generate JSON report for programmatic access"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"test_report_{timestamp}.json"
        report_path = os.path.join(self.reports_dir, report_filename)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(self.test_results, f, indent=2, default=str)
        
        print(f"📊 JSON Report generated: {report_path}")
        return report_path

    def generate_summary_report(self):
        """Generate simple summary report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"test_summary_{timestamp}.txt"
        report_path = os.path.join(self.reports_dir, report_filename)
        
        summary = f"""
Test Execution Summary
=====================

Execution Time: {self.test_results['start_time']} to {self.test_results['end_time']}
Duration: {self.test_results.get('duration', 'N/A')}

Results:
- Total Scenarios: {self.test_results['total_scenarios']}
- Passed: {self.test_results['passed_scenarios']}
- Failed: {self.test_results['failed_scenarios']}
- Skipped: {self.test_results['skipped_scenarios']}

Features Tested:
"""
        
        for feature in self.test_results['features']:
            summary += f"- {feature['name']}: {feature['passed_scenarios']}/{feature['total_scenarios']} passed\n"
        
        if self.test_results['errors']:
            summary += "\nErrors:\n"
            for error in self.test_results['errors']:
                summary += f"- {error['scenario']}: {error['message']}\n"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(summary)
        
        print(f"📊 Summary Report generated: {report_path}")
        return report_path

# Global instance
report_generator = ReportGenerator() 