#!/usr/bin/env python3
"""
Simple HTML Report Generator for gloEMR BDD Test Results
"""

import json
import os
from datetime import datetime


def create_html_report():
    """Create HTML report from JSON results"""
    
    # Read JSON results
    json_file = "reports/glo_emr_test_results.json"
    if not os.path.exists(json_file):
        print(f"Error: {json_file} not found")
        return
    
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Calculate stats
    total_scenarios = 0
    passed_scenarios = 0
    total_steps = 0
    passed_steps = 0
    total_duration = 0
    
    feature_data = data[0] if data else {}
    
    for element in feature_data.get('elements', []):
        if element.get('type') == 'scenario':
            total_scenarios += 1
            if element.get('status') == 'passed':
                passed_scenarios += 1
            
            for step in element.get('steps', []):
                total_steps += 1
                if step.get('result', {}).get('status') == 'passed':
                    passed_steps += 1
                total_duration += step.get('result', {}).get('duration', 0)
    
    # Generate HTML
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>gloEMR BDD Test Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }}
        .container {{ max-width: 1000px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        .header {{ background: #2c3e50; color: white; padding: 20px; text-align: center; border-radius: 8px; margin-bottom: 20px; }}
        .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 20px 0; }}
        .stat-card {{ background: #3498db; color: white; padding: 20px; border-radius: 8px; text-align: center; }}
        .stat-card.passed {{ background: #27ae60; }}
        .stat-card.time {{ background: #e67e22; }}
        .stat-number {{ font-size: 2em; font-weight: bold; }}
        .feature {{ margin: 20px 0; border: 1px solid #ddd; border-radius: 8px; }}
        .feature-header {{ background: #34495e; color: white; padding: 15px; font-size: 1.2em; }}
        .scenario {{ margin: 10px 0; }}
        .scenario-header {{ background: #2ecc71; color: white; padding: 10px; font-weight: bold; }}
        .steps {{ background: #f8f9fa; padding: 15px; }}
        .step {{ padding: 8px 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; }}
        .step-passed {{ color: #27ae60; }}
        .step-failed {{ color: #e74c3c; }}
        .timestamp {{ text-align: center; color: #7f8c8d; margin-top: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏥 gloEMR BDD Test Report</h1>
            <p>Desktop Application Automation Results</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">{total_scenarios}</div>
                <div>Scenarios</div>
            </div>
            <div class="stat-card passed">
                <div class="stat-number">{passed_steps}</div>
                <div>Steps Passed</div>
            </div>
            <div class="stat-card time">
                <div class="stat-number">{total_duration:.1f}s</div>
                <div>Total Time</div>
            </div>
        </div>
        
        <div class="feature">
            <div class="feature-header">
                Feature: {feature_data.get('name', 'Unknown')}
            </div>
"""
    
    # Add scenarios
    for element in feature_data.get('elements', []):
        if element.get('type') == 'scenario':
            scenario_name = element.get('name', 'Unknown')
            scenario_status = element.get('status', 'unknown')
            tags = ', '.join([tag.replace('@', '') for tag in element.get('tags', [])])
            
            html_content += f"""
            <div class="scenario">
                <div class="scenario-header">
                    📝 Scenario: {scenario_name}
                    <small style="float: right;">Tags: {tags}</small>
                </div>
                <div class="steps">
"""
            
            # Add steps
            for step in element.get('steps', []):
                step_name = step.get('name', '')
                step_keyword = step.get('keyword', '')
                step_status = step.get('result', {}).get('status', 'unknown')
                step_duration = step.get('result', {}).get('duration', 0)
                
                status_class = 'step-passed' if step_status == 'passed' else 'step-failed'
                status_icon = '✅' if step_status == 'passed' else '❌'
                
                html_content += f"""
                    <div class="step {status_class}">
                        <span>{status_icon} {step_keyword}{step_name}</span>
                        <span>{step_duration:.3f}s</span>
                    </div>
"""
            
            html_content += """
                </div>
            </div>
"""
    
    html_content += f"""
        </div>
        
        <div class="timestamp">
            <p><strong>Report Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p><strong>Test Framework:</strong> Behave (BDD) | <strong>Automation:</strong> pywinauto</p>
        </div>
    </div>
</body>
</html>
"""
    
    # Save report
    output_file = "reports/glo_emr_test_report.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ HTML report generated: {output_file}")
    return output_file


if __name__ == "__main__":
    create_html_report() 