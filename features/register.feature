Feature: Register Account Functionality

  Scenario: Register with mandatory fields
    Given I navigated to Register page
    When I enter mandatory fields
    And I click on Continue button
    Then Account should get created

  Scenario: Register with a duplicate email address
    Given I navigated to Register page
    When I enter all fields except email fields
    And I enter existing accounts email into email field
    And I click on Continue button
    Then Proper message should be displayed about using duplicate email

  Scenario: Register without providing any details
    Given I navigated to Register page
    When I dont enter anything into the fields
    And I click on Continue button
    Then Proper message should be displayed about mandatory fields