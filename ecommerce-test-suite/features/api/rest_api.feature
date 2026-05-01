Feature: REST API Validation
  As a QA engineer
  I want to validate the JSONPlaceholder REST API
  So that I can ensure endpoints behave as specified

  Scenario: GET all posts returns 200 and a non-empty list
    When I send a GET request to "/posts"
    Then the response status code should be 200
    And the response should be a non-empty list

  Scenario: GET a single post returns correct data
    When I send a GET request to "/posts/1"
    Then the response status code should be 200
    And the response body field "id" should equal "1"
    And the response body field "userId" should equal "1"

  Scenario: POST creates a new resource
    When I send a POST request to "/posts" with JSON body:
      """
      {"title": "QA Test Post", "body": "Automated test content", "userId": 1}
      """
    Then the response status code should be 201
    And the response body field "title" should equal "QA Test Post"

  Scenario: GET a non-existent post returns 404
    When I send a GET request to "/posts/99999"
    Then the response status code should be 404

  Scenario: GET all comments for a post returns 200
    When I send a GET request to "/posts/1/comments"
    Then the response status code should be 200
    And the response should be a non-empty list

  Scenario: Response headers contain JSON content type
    When I send a GET request to "/posts/1"
    Then the response status code should be 200
    And the response content type should contain "application/json"
