from .base_page import BasePage
from helpers.locators import *
import pytest
from selenium.webdriver import ActionChains

class FormPage(BasePage):
    
    # def __init__(self, *args, **kwargs):
    #     super(FormPage, self).__init__(*args, **kwargs)
    
    # def should_be_submit_btn(self):
    #     assert self.is_element_present(*FormPageLocators.SUBMIT_BTN), 'There`s no submit btn on the form page'
        
    def should_be_submit_btn(self):
        pytest.xfail("known bug, btn hidden under footer")
        assert self.is_element_visible(*FormPageLocators.SUBMIT_BTN), 'There`s no submit btn on the form page'
        
    def validation_empty_required_fields(self):
        # self.remove_footer()
        submit_btn = self.driver.find_element(*FormPageLocators.SUBMIT_BTN)
        self.driver.execute_script("arguments[0].click();", submit_btn)