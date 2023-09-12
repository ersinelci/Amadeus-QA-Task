from behave import then
from ui_test.pages.search_page import SearchPage
from selenium.common.exceptions import NoSuchElementException

@then("I checked the '{possible_flights}' are listed")
def step_then_i_check_possible_flights(context, possible_flights):
    page = SearchPage(context)
    try:
        result_element = page.search_result()
    except NoSuchElementException:
        if int(possible_flights) == 0:
            assert True, f"No flights found, as expected."
            return
        else:
            assert False
    assert f"Found {possible_flights} items" in result_element.text

@then("I should see an error message as '{expected_error_message}'")
def step_then_see_error_message(context, expected_error_message):
    page = SearchPage(context)
    error_message = page.error_message().text
    assert expected_error_message == error_message