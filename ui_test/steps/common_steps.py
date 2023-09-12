from behave import when
from ui_test.pages.search_page import SearchPage


@when("I enter '{from_value}' for departure location")
@when('I enter "{from_value}" for departure location')
def step_when_i_enter_start_location(context, from_value):
    page = SearchPage(context)
    page.from_input().send_keys(from_value)
    page.dropdown_option(from_value).click()


@when("I enter '{to_value}' for arriving location")
@when('I enter "{to_value}" for arriving location')
def step_when_i_enter_end_location(context, to_value):
    page = SearchPage(context)
    page.to_input().send_keys(to_value)
    page.dropdown_option(to_value).click()