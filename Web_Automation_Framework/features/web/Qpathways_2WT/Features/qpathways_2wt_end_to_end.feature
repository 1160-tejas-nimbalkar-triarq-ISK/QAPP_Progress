@qpathways @2wt @e2e
Feature: Qpathways 2WT Complete End-to-End Testing

  Scenario: Login and Sanity Testing Workflow
    # Login Steps
    Given I launch the Qpathways 2WT login page "<QPATHWAYS_2WT_BASE_URL>"
    When I enter the username "<QPATHWAYS_2WT_USERNAME>"
    And I enter the password "<QPATHWAYS_2WT_PASSWORD>"
    And I click the login button
    Then I should be successfully logged in
    
    # Sanity Testing Steps
    When I click on the Patients tab
    And I click on a random patient
    
    # Send Custom Message
    And I click on the chat button
    And I enter a random message in the text area
    And I click the send button
    
    # Send Template Message
    And I click on the template button
    And I click on the template dropdown arrow
    And I select a random template
    And I click the send button for template
    
    # Navigate to PT Chats and Verify
    And I click on the PT Chats tab
    And I search for the patient by name
    And I click on the first search result
    
    # Verify Messages
    Then I should see my messages in the chat
    And the sanity testing for Qpathways 2WT should be completed 