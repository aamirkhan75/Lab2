Feature: Network Research Calculator

Scenario: distance on x
    Given I have size "10", location ["0", "100"] for route
    When I compare driving speed and downloading speed for route
    Then It should give us "32.0" and "27800.0" for route