@qpathways @2wt @sanity
Feature: Qpathways 2WT End-to-End Sanity Testing

  Background:
    Given I am logged into Qpathways 2WT

  Scenario: Complete Sanity Testing Workflow
    # Navigate to Patients
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