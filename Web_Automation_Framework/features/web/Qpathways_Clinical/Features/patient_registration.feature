@qpathways @clinical @patient_registration
Feature: Patient Registration in Qpathways Clinical

  Background:
    Given I am logged into Qpathways Clinical application

  Scenario: Register a new patient with basic details
    When I navigate to the Patients tab
    And I click on patient registration icon
    And I click on New Patient button
    And I fill patient basic details
    Then patient registration form should be filled successfully 