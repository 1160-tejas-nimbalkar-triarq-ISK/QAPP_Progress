#!/usr/bin/env python3
"""
HTML Report Generator for gloEMR BDD Test Results
Generates a detailed HTML report from Behave JSON output
"""

import json
import os
from datetime import datetime
from pathlib import Path


def generate_html_report():
    """Generate HTML report from JSON test results"""
    
    # Read JSON test results
    json_file = "reports/glo_emr_test_results.json"
    if not os.path.exists(json_file):
        print(f"Error: JSON results file not found: {json_file}")
        return
    
    with open(json_file, 'r') as f:
        test_data = json.load(f)
    
    # Generate HTML content
    html_content = generate_html_content(test_data)
    
    # Save HTML report
    output_file = "reports/glo_emr_test_report.html"
    with open(output_file, 'w') as f:
        f.write(html_content)
    
    print(f"✅ HTML report generated: {output_file}")
    return output_file


def generate_html_content(test_data):
    """Generate the HTML content from test data"""
    
    # Extract test statistics
    stats = calculate_test_stats(test_data)
    
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>gloEMR BDD Test Report</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #2c3e50, #34495e);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .header .subtitle {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border-left: 4px solid;
        }}
        
        .stat-card.passed {{ border-left-color: #27ae60; }}
        .stat-card.failed {{ border-left-color: #e74c3c; }}
        .stat-card.time {{ border-left-color: #3498db; }}
        .stat-card.scenarios {{ border-left-color: #9b59b6; }}
        
        .stat-number {{
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        
        .stat-card.passed .stat-number {{ color: #27ae60; }}
        .stat-card.failed .stat-number {{ color: #e74c3c; }}
        .stat-card.time .stat-number {{ color: #3498db; }}
        .stat-card.scenarios .stat-number {{ color: #9b59b6; }}
        
        .stat-label {{
            font-size: 1.1em;
            color: #7f8c8d;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .content {{
            padding: 30px;
        }}
        
        .feature-section {{
            margin-bottom: 30px;
            border: 1px solid #ddd;
            border-radius: 8px;
            overflow: hidden;
        }}
        
        .feature-header {{
            background: #34495e;
            color: white;
            padding: 20px;
            font-size: 1.3em;
        }}
        
        .feature-description {{
            padding: 15px 20px;
            background: #ecf0f1;
            font-style: italic;
            color: #7f8c8d;
        }}
        
        .scenario {{
            border-top: 1px solid #ddd;
            margin: 0;
        }}
        
        .scenario-header {{
            background: #2ecc71;
            color: white;
            padding: 15px 20px;
            font-weight: bold;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .scenario-header.failed {{
            background: #e74c3c;
        }}
        
        .scenario-tags {{
            background: rgba(255,255,255,0.2);
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 0.9em;
        }}
        
        .steps-container {{
            padding: 20px;
        }}
        
        .step {{
            display: flex;
            align-items: center;
            padding: 12px 0;
            border-bottom: 1px solid #eee;
        }}
        
        .step:last-child {{
            border-bottom: none;
        }}
        
        .step-status {{
            width: 20px;
            height: 20px;
            border-radius: 50%;
            margin-right: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            font-size: 12px;
        }}
        
        .step-status.passed {{
            background: #27ae60;
        }}
        
        .step-status.failed {{
            background: #e74c3c;
        }}
        
        .step-text {{
            flex: 1;
            font-size: 1.1em;
        }}
        
        .step-duration {{
            color: #7f8c8d;
            font-size: 0.9em;
        }}
        
        .keyword {{
            font-weight: bold;
            color: #2c3e50;
        }}
        
        .test-info {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin-top: 30px;
        }}
        
        .test-info h3 {{
            color: #2c3e50;
            margin-bottom: 15px;
        }}
        
        .test-info p {{
            margin-bottom: 10px;
            color: #7f8c8d;
        }}
        
        .footer {{
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 20px;
            margin-top: 30px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏥 gloEMR BDD Test Report</h1>
            <div class="subtitle">Desktop Application Automation Test Results</div>
        </div>
        
        <div class="stats-grid">
            <div class="stat-card scenarios">
                <div class="stat-number">{stats['total_scenarios']}</div>
                <div class="stat-label">Scenarios</div>
            </div>
            <div class="stat-card passed">
                <div class="stat-number">{stats['passed_steps']}</div>
                <div class="stat-label">Steps Passed</div>
            </div>
            <div class="stat-card failed">
                <div class="stat-number">{stats['failed_steps']}</div>
                <div class="stat-label">Steps Failed</div>
            </div>
            <div class="stat-card time">
                <div class="stat-number">{stats['total_duration']:.1f}s</div>
                <div class="stat-label">Total Time</div>
            </div>
        </div>
        
        <div class="content">
"""
    
    # Add feature details
    for feature in test_data:
        html += generate_feature_html(feature)
    
    html += f"""
        </div>
        
        <div class="test-info">
            <h3>📋 Test Execution Details</h3>
            <p><strong>Report Generated:</strong> {timestamp}</p>
            <p><strong>Test Framework:</strong> Behave (BDD)</p>
            <p><strong>Automation Tool:</strong> pywinauto</p>
            <p><strong>Target Application:</strong> gloEMR Desktop Application</p>
            <p><strong>Test Environment:</strong> Windows Desktop</p>
        </div>
        
        <div class="footer">
            <p>Generated by BDD Automation Framework | © 2024</p>
        </div>
    </div>
</body>
</html>
"""
    
    return html


def generate_feature_html(feature):
    """Generate HTML for a feature"""
    # Handle description which can be a list or string
    description = feature.get('description', [])
    if isinstance(description, list):
        description_text = '<br>'.join(description)
    else:
        description_text = description.strip() if description else ''
    
    html = f"""
        <div class="feature-section">
            <div class="feature-header">
                🎯 Feature: {feature['name']}
            </div>
            <div class="feature-description">
                {description_text}
            </div>
"""
    
    # Add scenarios
    for element in feature['elements']:
        if element['type'] == 'scenario':
            html += generate_scenario_html(element)
    
    html += "</div>"
    return html


def generate_scenario_html(scenario):
    """Generate HTML for a scenario"""
    status = 'passed' if scenario['status'] == 'passed' else 'failed'
    
    # Get tags
    tags = ', '.join([tag.replace('@', '') for tag in scenario.get('tags', [])])
    
    html = f"""
        <div class="scenario">
            <div class="scenario-header {status}">
                <span>📝 Scenario: {scenario['name']}</span>
                <span class="scenario-tags">{tags}</span>
            </div>
            <div class="steps-container">
"""
    
    # Add steps
    for step in scenario['steps']:
        html += generate_step_html(step)
    
    html += """
            </div>
        </div>
"""
    
    return html


def generate_step_html(step):
    """Generate HTML for a step"""
    status = step['result']['status']
    duration = step['result'].get('duration', 0)
    
    status_icon = '✓' if status == 'passed' else '✗'
    
    html = f"""
        <div class="step">
            <div class="step-status {status}">{status_icon}</div>
            <div class="step-text">
                <span class="keyword">{step['keyword']}</span>{step['name']}
            </div>
            <div class="step-duration">{duration:.3f}s</div>
        </div>
"""
    
    return html


def calculate_test_stats(test_data):
    """Calculate test statistics"""
    stats = {
        'total_scenarios': 0,
        'passed_scenarios': 0,
        'failed_scenarios': 0,
        'total_steps': 0,
        'passed_steps': 0,
        'failed_steps': 0,
        'total_duration': 0
    }
    
    for feature in test_data:
        for element in feature['elements']:
            if element['type'] == 'scenario':
                stats['total_scenarios'] += 1
                
                if element['status'] == 'passed':
                    stats['passed_scenarios'] += 1
                else:
                    stats['failed_scenarios'] += 1
                
                for step in element['steps']:
                    stats['total_steps'] += 1
                    if step['result']['status'] == 'passed':
                        stats['passed_steps'] += 1
                    else:
                        stats['failed_steps'] += 1
                    
                    stats['total_duration'] += step['result'].get('duration', 0)
    
    return stats


if __name__ == "__main__":
    generate_html_report() 