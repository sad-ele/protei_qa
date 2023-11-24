from BaseApp import BasePage
from selenium.webdriver.common.by import By


class Locators:
    auth_link = (By.ID, "menuAuth")
    main_link = (By.ID, "menuMain")
    users_link = (By.ID, "menuUsersOpener")
    more_link = (By.ID, "menuMore")

    auth_page = (By.TAG_NAME, "legend")
    main_page = (By.TAG_NAME, "h3")
    users_page = (By.ID, "dataTable")
    more_page = (By.TAG_NAME, "h3")
    add_page = (By.TAG_NAME, "legend")

    users_page_dropdown = (By.ID, "menuUsers")
    add_dropdown = (By.ID, "menuUserAdd")

    add_user_button = (By.ID, "addUser")


class SearchHelper(BasePage):

    def go_to_auth(self):
        return self.find_element(Locators.auth_link).click()

    def go_to_main(self):
        return self.find_element(Locators.main_link).click()

    def go_to_users(self):
        link = self.find_element(Locators.users_link, time=5)
        action = self.action()
        return action.double_click(on_element=link).perform()

    def go_to_users_dropdown(self):
        self.find_element(Locators.users_link, time=5).click()
        return self.find_element(Locators.users_page_dropdown, time=5).click()

    def go_to_add_dropdown(self):
        self.find_element(Locators.users_link, time=5).click()
        return self.find_element(Locators.add_dropdown, time=5).click()

    def go_to_variants(self):
        return self.find_element(Locators.more_link, time=5).click()

    def check_auth(self):
        main_title = self.find_element(Locators.auth_page, time=5)
        return main_title

    def check_main(self):
        main_title = self.find_element(Locators.main_page, time=5)
        return main_title

    def check_users(self):
        table = self.find_element(Locators.users_page, time=5)
        return table

    def check_add(self):
        title = self.find_element(Locators.add_page, time=5)
        return title

    def check_variants(self):
        main_title = self.find_element(Locators.more_page, time=5)
        return main_title

    def add_button(self):
        return self.find_element(Locators.add_user_button, time=5).click()
