from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

INPUT_PRODUCT_NAME = (By.XPATH, "//input[@id='input-name1']")
INPUT_DESCRIPTION = (By.XPATH, "")
INPUT_META_TEG_TITLE = (By.XPATH, "")
INPUT_META_TEG_KEYWORDS = (By.XPATH, "")
INPUT_PRODUCT_TEG = (By.XPATH, "")


class ProductPage(BasePage):
    def enter_product_name(self, locator, selector, product_name):
        self.enter_input(locator, selector, product_name)

    def enter_description(self, locator, selector, description):
        self.enter_input(locator, selector, description)

    def enter_meta_teg_title(self, locator, selector, tag):
        self.enter_input(locator, selector, tag)

    def enter_meta_teg_keywords(self, locator, selector, keywords):
        self.enter_input(locator, selector, keywords)

    def enter_product_teg(self, locator, selector, teg):
        self.enter_input(locator, selector, teg)