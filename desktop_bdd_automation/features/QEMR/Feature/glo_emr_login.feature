@glo_emr @desktop_automation @login
Feature: gloEMR Desktop Application Login Automation
    As a healthcare professional
    I want to login to the gloEMR application
    So that I can access patient records and clinical functionality

    Background:
        Given I have access to Windows desktop environment
        And gloEMR application is available at "C:\Program Files (x86)\gloEMR\gloEMR.exe"

    @smoke @valid_login
    Scenario: Successful login with valid credentials
        Given I launch gloEMR application
        When I wait for gloEMR login window to appear
        And I enter username "admin"
        And I enter password "admin123"
        And I click Login button
        Then I should be successfully logged into gloEMR application
        When I click Log Out button
        And I close gloEMR application

    