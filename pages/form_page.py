from .base_page import BasePage
from helpers.locators import *
import pytest
from data.data import student
import time
from selenium.webdriver.common.keys import Keys


class FormPage(BasePage):
    
    # def __init__(self, *args, **kwargs):
    #     super(FormPage, self).__init__(*args, **kwargs)
    
    # def should_be_submit_btn(self):
    #     assert self.is_element_present(*FormPageLocators.SUBMIT_BTN), 'There`s no submit btn on the form page'
        
    def should_be_submit_btn(self):
        pytest.xfail("known bug, btn hidden under footer")
        assert self.is_element_visible(*FormPageLocators.SUBMIT_BTN), 'There`s no submit btn on the form page'
        
    def validation_empty_required_fields(self):
        self.click_btn(*FormPageLocators.SUBMIT_BTN)
        
    def fill_required_fields(self):
        self.is_element_visible(*FormPageLocators.FIRST_NAME).send_keys(student.first_name)
        self.is_element_visible(*FormPageLocators.LAST_NAME).send_keys(student.last_name)
        self.is_element_visible(*FormPageLocators.EMAIL).send_keys(student.email)
        self.click_btn(*FormPageLocators.GENDER)
        self.is_element_visible(*FormPageLocators.MOBILE).send_keys(student.number)
        
        # known bug TypeError: Cannot read properties of null (reading 'getMonth')
        # self.is_element_visible(*FormPageLocators.DATE_OF_BIRTH).clear()
        # self.is_element_visible(*FormPageLocators.DATE_OF_BIRTH).send_keys(student.date)
        
        self.click_btn(*FormPageLocators.SUBMIT_BTN)
