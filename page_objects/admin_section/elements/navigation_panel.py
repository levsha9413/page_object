from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

CATALOG_SECTION = (By.XPATH, "//a[@href='#collapse1']")
EXTENSIONS_SECTION = (By.XPATH, "//a[@href='#collapse14']")
DESIGN_SECTION = (By.XPATH, "//a[@href='#collapse20']")
SALES_SECTION = (By.XPATH, "//a[@href='#collapse26']")
CUSTOMERS_SECTION = (By.XPATH, "//a[@href='#collapse33']")
MARKETING_SECTION = (By.XPATH, "//a[@href='#collapse38']")
SYSTEM_SECTION = (By.XPATH, "//a[@href='#collapse42']")
REPORTS_SECTION = (By.XPATH, "//a[@href='#collapse61']")


class MenuPanel(BasePage):
    def open_section(self, locator, selector):
        self.click_button(locator, selector)

    def enter_in_subsection(self, locator, selector):
        self.click_button(locator, selector)
