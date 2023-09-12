import allure
from selenium import webdriver
from ui_test.pages.base_page import BasePage
import sys
import os

config_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(config_folder_path)

import config

project_url = config.config.get("uiProjectUrl", "")

def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.get(project_url)
    context.base_page = BasePage(context.browser)

    # Initialize Allure for the scenario
    scenario_title = scenario.name if scenario.name else scenario.filename
    allure.dynamic.feature(scenario.feature.name)
    allure.dynamic.story(scenario.feature.name)
    allure.dynamic.title(scenario_title)

def after_scenario(context, scenario):
    if scenario.status == "failed":
        # Attach screenshot or additional information for failed scenarios
        allure.attach(
            context.browser.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG,
        )

    context.browser.quit()
