from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, browser:WebDriver):
        self.browser = browser


    def find_element_by_id(self, element_id):
        return self.browser.find_element(By.ID, element_id)


    def find_element_by_text(self, element_type, text):
        return self.browser.find_element(By.XPATH, f"//{element_type}[contains(text(),'{text}')]")


    def find_elements_by_class(self, element_type, class_name):
        return self.browser.find_elements(By.XPATH, f"//{element_type}[@class='{class_name}']")