Feature: User Authentication
  As a SauceDemo user
  I want to log in with my credentials
  So that I can access the product catalogue

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter username "standard_user" and password "secret_sauce"
    And I click the login button
    Then I should be redirected to the inventory page
    And the page title should be "Products"

  Scenario: Failed login with invalid credentials
    Given I am on the login page
    When I enter username "wrong_user" and password "wrong_pass"
    And I click the login button
    Then I should see a login error message

  Scenario: Locked out user cannot log in
    Given I am on the login page
    When I enter username "locked_out_user" and password "secret_sauce"
    And I click the login button
    Then I should see a login error message

