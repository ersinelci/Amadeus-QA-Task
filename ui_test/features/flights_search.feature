Feature: Flights Search

Scenario Outline: Search a flight 
When I enter '<from_value>' for start location
And I enter '<to_value>' for end location
Then I checked the '<possible_flights>' are listed
Examples:
    | from_value | to_value    | possible_flights |
    | Istanbul   | Los Angeles | 2                |
    | IST        | LAX         | 2                |
    | Istanbul   | Paris       | 0                |
    | IST        | CDG         | 0                |


  
Scenario: From and To input fields should not allow the same value
  When I enter the same value "New York" in the From and To input fields
  Then I should see an error message indicating that the same values are not allowed
