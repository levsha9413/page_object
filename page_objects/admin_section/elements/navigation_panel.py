from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

CATALOG_BUTTON = (By.XPATH, "")
E = (By.XPATH, "")
ELEM = (By.XPATH, "")
ELEM = (By.XPATH, "")
ELEM = (By.XPATH, "")
ELEM = (By.XPATH, "")


class MenuPanel(BasePage):
    def open_section(self, locator, selector):
        self.click_button(locator, selector)

    def enter_in_subsection(self, locator, selector):
        self.click_button(locator, selector)
