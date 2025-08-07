Feature: User API Management
    As a system
    I want to manage users via API
    So that I can perform CRUD operations

    Background:
        Given the API is available

    Scenario: Create a new user successfully
        When I send a POST request to create a user with:
            | name     | John Doe              |
            | email    | john.doe@example.com  |
            | job      | Software Engineer     |
        Then the response status code should be 201
        And the response should contain user id
        And the response should contain "name" as "John Doe"
        And the response should contain "email" as "john.doe@example.com"

    Scenario: Get user details
        Given a user exists with id 2
        When I send a GET request to retrieve user with id 2
        Then the response status code should be 200
        And the response should contain user data
        And the response should have "data" field

    Scenario: Update user information
        Given a user exists with id 2
        When I send a PUT request to update user with id 2:
            | name     | Jane Smith            |
            | job      | Product Manager       |
        Then the response status code should be 200
        And the response should contain "name" as "Jane Smith"
        And the response should contain "job" as "Product Manager"

    Scenario: Delete user
        Given a user exists with id 2
        When I send a DELETE request to delete user with id 2
        Then the response status code should be 204

    Scenario: Get non-existent user
        When I send a GET request to retrieve user with id 999
        Then the response status code should be 404
        And the response should contain error message

    Scenario: Create user with invalid data
        When I send a POST request to create a user with:
            | name     |                      |
            | email    | invalid-email        |
        Then the response status code should be 400
        And the response should contain error message 