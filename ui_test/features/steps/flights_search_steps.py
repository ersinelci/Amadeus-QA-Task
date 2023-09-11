from behave import when, then
from selenium.webdriver.common.keys import Keys
from ui_test.pages.search_page import SearchPage


@when("I enter '{from_value}' for start location")
def step_when_i_enter_start_location(context, from_value):
    page = SearchPage(context)
    page.from_input().send_keys(from_value)

@when("I enter '{to_value}' for end location")
def step_when_i_enter_end_location(context, to_value):
    page = SearchPage(context)
    page.to_input().send_keys(to_value)

@then("I checked the '{possible_flights}' are listed")
def step_then_i_check_possible_flights(context, possible_flights):
    page = SearchPage(context)
    print(page, possible_flights)
    pass



@when('I enter the same value "{value}" in the From and To input fields')
def step_when_enter_same_value_in_fields(context, value):
    page = SearchPage(context)
    page.from_input().send_keys(value)
    page.to_input().send_keys(value)

@then('I should see an error message indicating that the same values are not allowed')
def step_then_see_error_message(context):
    page = SearchPage(context)
    error_message = page.error_message().text

    assert "Same values are not allowed" in error_message