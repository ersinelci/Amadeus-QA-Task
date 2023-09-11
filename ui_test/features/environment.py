
from selenium import webdriver
from ui_test.pages.base_page import BasePage

def before_all(context):
    context.browser = webdriver.Chrome()  
    context.browser.get('https://flights-app.pages.dev/') 
    context.base_page = BasePage(context.browser) 

def after_all(context):
    context.browser.quit() 
