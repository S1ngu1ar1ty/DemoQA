from .base_page import BasePage
from helpers.locators import *


class FormPage(BasePage):
    
    # def __init__(self, *args, **kwargs):
    #     super(FormPage, self).__init__(*args, **kwargs)
    
    # def should_be_submit_btn(self):
    #     assert self.is_element_present(*FormPageLocators.SUBMIT_BTN), 'There`s no submit btn on the form page'
        
    def should_be_submit_btn(self):
        assert self.is_element_visible(*FormPageLocators.SUBMIT_BTN), 'There`s no submit btn on the form page'    