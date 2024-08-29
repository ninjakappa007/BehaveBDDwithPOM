Feature: Login Functionality

  @implemented
  Scenario: Login with valid credentials
    Given I navigated to Login page
    When I enter valid email and valid password into the fields
    And I click login button
    Then I should get logged in

  Scenario: Login with invalid email and valid password
    Given I navigated to Login page
    When I enter invalid email and valid password into the fields
    And I click login button
    Then I should get proper error message

  Scenario: Login with valid email and invalid password
    Given I navigated to Login page
    When I enter valid email and invalid password into the fields
    And I click login button
    Then I should get proper error message

  Scenario: Login with invalid email and invalid password
    Given I navigated to Login page
    When I enter invalid email and invalid password into the fields
    And I click login button
    Then I should get proper error message

  Scenario: Login without entering any credentials
    Given I navigated to Login page
    When I enter nothing into email and password field
    And I click login button
    Then I should get proper error message