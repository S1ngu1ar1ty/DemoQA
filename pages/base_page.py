from selenium.common.exceptions import *


class BasePage:
    
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(10)
        
        
    def open(self):
        self.driver.get(self.url)
        
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True