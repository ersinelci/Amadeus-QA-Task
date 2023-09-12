from selenium.webdriver.common.by import By
from ui_test.pages.base_page import BasePage


class ListPage(BasePage):
    def __init__(self, context):
        super().__init__(context.browser)


    def card_list(self):
        return self.find_elements_by_class("li", "overflow-hidden rounded-xl border border-gray-200")


    def card_header(self):
        return self.find_elements_by_class("div", "flex flex-row border-b border-gray-900/5 bg-gray-50 p-6")


    def card_from_and_to_locations(self, card_element):
        return card_element.find_elements(By.XPATH, ".//div")