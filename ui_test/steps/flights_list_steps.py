from behave import when, then
from ui_test.pages.search_page import SearchPage
from ui_test.pages.list_page import ListPage
from selenium.common.exceptions import NoSuchElementException
import re


@when("I get possible flights count")
def step_then_i_check_listed_flights(context):
    page = SearchPage(context)
    try:
        result_element = page.search_result().text
    except NoSuchElementException:
        context.possible_flights = 0
        return
    context.possible_flights = int(re.search(r'\d+', result_element).group())


@then("I checked possible flights count is the same as the number of flights listed")
def step_then_i_check_listed_flight_cards_count(context):
    page = ListPage(context)
    card_count = len(page.card_list())
    assert card_count == context.possible_flights


@then ("I checked departure location on card is '{from_value_card}'")
def step_then_i_check_listed_flight_cards_information(context, from_value_card):
    page = ListPage(context)
    for card_element in page.card_header():
        from_location_elements = page.card_from_and_to_locations(card_element)
        for i in range(0, len(from_location_elements), 2):
            assert from_value_card == from_location_elements[i].text


@then ("I checked arriving location on card is '{to_value_card}'")
def step_then_i_check_listed_flight_cards_information(context, to_value_card):
    page = ListPage(context)
    for card_element in page.card_header():
        from_location_elements = page.card_from_and_to_locations(card_element)
        for i in range(1, len(from_location_elements), 2):
            assert to_value_card == from_location_elements[i].text