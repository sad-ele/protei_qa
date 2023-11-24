from BaseApp import BasePage
from selenium.webdriver.common.by import By


class AuthLocators:
    login_field = (By.ID, "loginEmail")
    password_field = (By.ID, "loginPassword")
    enter_button = (By.ID, "authButton")
    title = (By.TAG_NAME, "h3")
    fast_warning = (By.ID, "KEKEKEKEKEKKEKE")
    p_text = (By.CSS_SELECTOR, "#KEKEKEKEKEKKEKE p")
    usual_warning = (By.CSS_SELECTOR, ".uk-alert.uk-alert-danger")
    p_text_us = (By.CSS_SELECTOR, "#emailFormatError > p")
    email_warning = (By.ID, "emailFormatError")


class SearchHelper(BasePage):

    def enter_login(self, word):
        field = self.find_element(AuthLocators.login_field)
        field.click()
        field.send_keys(word)
        return field

    def enter_password(self, word):
        field = self.find_element(AuthLocators.password_field)
        field.click()
        field.send_keys(word)
        return field

    def click_button(self):
        return self.find_element(AuthLocators.enter_button,time=1).click()

    def check_title(self):
        main_title = self.find_element(AuthLocators.title, time=5)
        return main_title

    def check_fast_warning(self):
        warning = self.find_element(AuthLocators.fast_warning, time=5)
        return warning

    def read_text_fast(self):
        text_warning = self.find_element(AuthLocators.p_text, time=5)
        return text_warning

    def check_warning(self):
        warning = self.find_element(AuthLocators.usual_warning, time=5)
        return warning

    def read_text_usual(self):
        text_warning = self.find_element(AuthLocators.p_text_us, time=5)
        return text_warning

    def check_email_warning(self):
        warning = self.find_element(AuthLocators.email_warning, time=5)
        return warning