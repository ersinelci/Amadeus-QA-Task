Feature: Flights List

Scenario Outline: List a flight 
When I enter '<from_value>' for departure location
And I enter '<to_value>' for arriving location
And I get possible flights count
Then I checked possible flights count is the same as the number of flights listed
Examples:
    | from_value | to_value    |
    | Istanbul   | Los Angeles |
    | Istanbul   | Paris       |


Scenario Outline: Check listed flights information
When I enter '<from_value>' for departure location
And I enter '<to_value>' for arriving location
Then I checked departure location on card is '<from_value_card>'
And I checked arriving location on card is '<to_value_card>'
Examples:
    | from_value | to_value    | from_value_card | to_value_card |
    | Istanbul   | Los Angeles | IST             | LAX           |
    | Paris      | Dubai       | CDG             | DXB           |