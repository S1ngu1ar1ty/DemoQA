from pages.form_page import FormPage
from selenium.webdriver.common.by import By



class TestFormPage:
    
    def test_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        # form_page.validation_empty_required_fields()
        # form_page.should_be_submit_btn()
        form_page.fill_required_fields()
