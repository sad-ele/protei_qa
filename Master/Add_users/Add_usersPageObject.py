from BaseApp import BasePage
from selenium.webdriver.common.by import By


class Locators:
    email = (By.ID, "dataEmail")
    password = (By.ID, "dataPassword")
    name = (By.ID, "dataName")
    button = (By.ID, "dataSend")
    modal = (By.CLASS_NAME, "uk-modal-body")
    warning = (By.ID, "blankNameError")
    warning_text = (By.CSS_SELECTOR, "#blankNameError p")
    email_error = (By.ID, "emailFormatError")
    email_error_text = (By.CSS_SELECTOR, "#emailFormatError p")


class SearchHelper(BasePage):

    def enter_email(self, word):
        field = self.find_element(Locators.email, time=5)
        field.click()
        field.send_keys(word)
        return field

    def enter_password(self, word):
        field = self.find_element(Locators.password, time=5)
        field.click()
        field.send_keys(word)
        return field

    def enter_name(self, word):
        field = self.find_element(Locators.name, time=5)
        field.click()
        field.send_keys(word)
        return field

    def add_user(self):
        return self.find_element(Locators.button).click()

    def check_window(self):
        window = self.find_element(Locators.modal, time=5)
        return window

    def check_warning(self):
        warning_frame = self.find_element(Locators.warning, time=5)
        return warning_frame

    def check_warning_text(self):
        warning_text = self.find_element(Locators.warning_text, time=5)
        return warning_text

    def check_email_error(self):
        error_frame = self.find_element(Locators.email_error, time=5)
        return error_frame

    def check_error_text(self):
        error_text = self.find_element(Locators.email_error_text, time=5)
        return error_text

