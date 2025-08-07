@qpathways @2wt
Feature: Qpathways 2WT Login Testing

  Scenario: Successful Login with Valid Credentials
    Given I launch the Qpathways 2WT login page "<QPATHWAYS_2WT_BASE_URL>"
    When I enter the username "<QPATHWAYS_2WT_USERNAME>"
    And I enter the password "<QPATHWAYS_2WT_PASSWORD>"
    And I click the login button
    Then I should be successfully logged in 