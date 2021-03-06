from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        
    def open(self):
        self.driver.get(self.url)
        
    def is_element_visible(self, how, what, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))
    
    def is_element_present(self, how, what, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        
    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        
    def click_btn(self, how, what):
        btn = self.driver.find_element(how, what)
        # handling problem with Submit btn covered by footer
        self.driver.execute_script("arguments[0].click();", btn)
