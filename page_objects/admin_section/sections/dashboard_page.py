from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

NAVIGATION_PANEL = (By.XPATH, "//*[id='column-left']")
DASHBOARDS_TITLE = (By.XPATH, "//h1[text()='Dashboard']")
CATALOG_BUTTON = (By.XPATH, "")
PRODUCT_BUTTON = (By.XPATH, "")
ADD_PRODUCT_BUTTON = (By.XPATH, "")
ELEM = (By.XPATH, "")
ELEM = (By.XPATH, "")
ELEM = (By.XPATH, "")
ELEM = (By.XPATH, "")
ELEM = (By.XPATH, "")


class AdminPage(BasePage):
    POSTFIX_URL = '/admin'
