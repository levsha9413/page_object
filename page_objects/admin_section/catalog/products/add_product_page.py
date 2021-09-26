from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

INPUT_PRODUCT_NAME = (By.XPATH, "//input[@id='input-name1']")
ELEM = (By.XPATH, "")
ELEM = (By.XPATH, "")
ELEM = (By.XPATH, "")
ELEM = (By.XPATH, "")
ELEM = (By.XPATH, "")

class ProductPage(BasePage):
    def enter_product_name(self, product_name):
        #найти
        #почистить
        #ввести пшн
        pass