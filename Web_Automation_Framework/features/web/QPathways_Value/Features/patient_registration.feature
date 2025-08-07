@qpathways @value
Feature: QPathways Value End-to-End Testing

  Scenario: Complete Patient Registration and Episode Creation Workflow
    # Login Test Cases
    Given I launch the Qpathways Value login page "<QPATHWAYS_BASE_URL>"
    When I enter the username "<QPATHWAYS_USERNAME>"
    And I enter the password "<QPATHWAYS_PASSWORD>"
    And I click the login button
    Then I should be successfully logged in
    
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
    And I select patient value program
    
    # Healthcare Providers Test Cases (2 fields)
    And I select patient PGP
    And I select patient provider
    
    # Insurance Information Test Cases (6 fields)
    And I select primary insurance
    And I enter primary insurance ID
    And I enter primary group ID
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
    
    # Save Patient Registration - This triggers Episode Creation
    When patient registration form should be saved successfully
    
    # Episode Creation Test Cases (20 fields)
    And I enter episode description
    And I select episode physician
    And I select episode program
    And I select surgical facility
    And I enter surgery date
    And I select episode type
    And I select joint selection
    And I select diagnosis code
    And I select procedure code
    And I enter patient height
    And I enter patient weight
    And I save episode information
    And I select risk level
    And I add episode note
    And I select episode manager
    And I open care plan
    And I select care plan index
    And I click next in care plan
    And I save care plan
    And I initiate episode
    
    Then episode should be created successfully 