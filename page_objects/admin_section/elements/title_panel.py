from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

ELEM = (By.XPATH, "")
ELEM = (By.XPATH, "")
ELEM = (By.XPATH, "")
ELEM = (By.XPATH, "")
ELEM = (By.XPATH, "")


class TitlePanel(BasePage):

    def get_title(self):
        # return title
        pass

    def add_new_button_click(self, locator, selector):
        self.click_button(locator, selector)

    def delete_button_click(self, locator, selector):
        self.click_button(locator, selector)

    def middle_button_click(self, locator, selector):
        self.click_button(locator, selector)
