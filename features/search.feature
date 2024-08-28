Feature: Search functionality

  @implemented
  Scenario: Search for a valid product
    Given  I navigated to home page
    When I enter valid product into the search box field
    And I click on search button
    Then Valid product should get displayed in search results

  Scenario: Search for a invalid product
    Given  I navigated to home page
    When I enter invalid product into the search box field
    And I click on search button
    Then Proper message should be displayed in search results

  Scenario: Search without entering product
    Given  I navigated to home page
    When I dont enter anything into the search box field
    And I click on search button
    Then Proper message should be displayed in search results
