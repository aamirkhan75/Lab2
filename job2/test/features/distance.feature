Feature: Network Research Calculator

Scenario: distance on x
    Given I have points ["0", "0"] and ["0", "10"]
    When I calculate the distance between them
    Then it should equal "10"

Scenario: distance on y
    Given I have points ["0", "0"] and ["10", "0"]
    When I calculate the distance between them
    Then it should equal "10"

Scenario: distance on both x and y
    Given I have points ["0", "0"] and ["3", "4"]
    When I calculate the distance between them
    Then it should equal "5"
