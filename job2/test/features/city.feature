
Feature: comparing speed

Scenario: distance on speed
    Given The size "20", location ["0", "200"]
    When comparing the driving speed and downloading speed
    Then It should give "320" and "3601600.0"
