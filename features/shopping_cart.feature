Feature: Shopping Cart Management
  As a logged-in user
  I want to manage items in my shopping cart
  So that I can control what I intend to purchase

  Background:
    Given I am logged in as a standard user

  Scenario: Add a single item to the cart
    When I add "Sauce Labs Backpack" to the cart
    Then the cart count should be "1"

  Scenario: Add multiple items to the cart
    When I add "Sauce Labs Backpack" to the cart
    And I add "Sauce Labs Bike Light" to the cart
    Then the cart count should be "2"

  Scenario: Remove an item from the cart
    When I add "Sauce Labs Backpack" to the cart
    And I remove "Sauce Labs Backpack" from the cart
    Then the cart count should be "0"

  Scenario: Cart persists added items
    When I add "Sauce Labs Fleece Jacket" to the cart
    And I navigate to the cart page
    Then I should see "Sauce Labs Fleece Jacket" in the cart
