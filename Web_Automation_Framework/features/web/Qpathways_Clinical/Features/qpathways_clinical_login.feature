@qpathways @clinical @login
Feature: Qpathways Clinical Login

  Scenario: Login to Qpathways Clinical with valid credentials
    Given I launch the Qpathways Clinical login page "<QPATHWAYS_BASE_URL>"
    When I enter the username "<QPATHWAYS_USERNAME>"
    And I enter the password "<QPATHWAYS_PASSWORD>"
    And I click the login button 