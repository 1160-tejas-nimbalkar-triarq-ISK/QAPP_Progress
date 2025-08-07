@qpathways @trend
Feature: QPathways TREND End-to-End Testing

  Scenario: Complete Patient Registration Workflow
    # Login Test Cases
    Given I am logged into QPathways TREND application
    
    # Patient Registration Test Cases
    When I navigate to the Patients tab
    And I click on patient registration icon
    And I click on New Patient button
    
    # Basic Information Test Cases (6 fields)
    And I enter patient first name
    And I enter patient middle name
    And I enter patient last name
    And I enter patient date of birth
    And I enter patient gender
    And I select patient trend program
    
    # Healthcare Providers Test Cases (3 fields)
    And I select patient primary care provider
    And I select patient PGP
    And I select patient provider
    
    # Primary Insurance Sequence (3 fields)
    And I select primary insurance
    And I enter primary insurance ID
    And I enter primary group ID
    
    # Secondary Insurance Sequence (3 fields)
    And I select secondary insurance
    And I enter secondary insurance ID
    And I enter secondary group ID
    
    # Contact Information Test Cases (6 fields)
    And I enter patient address
    And I enter patient address details
    And I enter patient mobile number
    And I enter patient phone number
    And I enter patient email
    And I enter patient notes
    
    # Save Patient Registration
    When patient registration form should be saved successfully
    Then patient should be registered successfully in TREND 