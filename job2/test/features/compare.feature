Feature: Network Research Calculator

Scenario: distance on x
    Given I have size "10", location ["0", "100"]
    When I compare driving speed and downloading speed
    Then It should give us "160" and "108800.0"




