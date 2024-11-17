from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    """class to represent the base page that other pages can inherit from"""
    def __init__(self,driver:WebDriver):
        self.driver=driver
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    def click_element(self,locator):
        self.find_element(locator).click()
    def enter_text(self,locator,text):
        element=self.find_element(locator)
        element.clear()
        element.send_keys(text)