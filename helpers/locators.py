from selenium.webdriver.common.by import By
from random import randint

class FormPageLocators:
    
    SUBMIT_BTN = (By.CSS_SELECTOR, '#submit')
    FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME = (By.CSS_SELECTOR, '#lastName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    GENDER = (By.CSS_SELECTOR, f'lable[for="gender-radio-{randint(1,3)}"]')
    MOBILE = (By.CSS_SELECTOR, '#userNumber')
    SUBJECTS = (By.CSS_SELECTOR, '.css-1hwfws3')
    HOBBIES = (By.CSS_SELECTOR, f'lable[for="hobbies-checkbox-{randint(1,3)}"]')
    ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    CHOOSE_FILE_BTN = (By.CSS_SELECTOR, '#uploadPicture')
    STATE = (By.CSS_SELECTOR, '#state')
    CITY = (By.CSS_SELECTOR, '#city')