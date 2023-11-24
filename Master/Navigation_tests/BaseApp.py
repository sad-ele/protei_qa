from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        #self.base_url = "http://149.255.118.78:7080/main"
        #self.base_url = "http://149.255.118.78:7080/more"
        self.base_url = "http://149.255.118.78:7080/users"
        #self.base_url = "http://149.255.118.78:7080/add_user"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def action(self):
        return ActionChains(self.driver)