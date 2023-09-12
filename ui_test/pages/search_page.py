from ui_test.pages.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, context):
        super().__init__(context.browser)

    def from_input(self):
        return self.find_element_by_id("headlessui-combobox-input-:Rq9lla:")
    
    def to_input(self):
        return self.find_element_by_id("headlessui-combobox-input-:Rqhlla:")
    
    def dropdown_option(self, text):
        return self.find_element_by_text("span", text)
    
    def search_result(self):
        return self.find_element_by_text("p", "Found")
    
    # I added mock error message element for test
    def error_message(self):
        return self.find_element_by_id('error-message')
    

    