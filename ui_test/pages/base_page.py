from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def __init__(self, browser:WebDriver):
        self.browser = browser

    def find_element_by_id(self, element_id):
        return self.browser.find_element(By.ID, element_id)