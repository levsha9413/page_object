from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

POSTFIX_URL = '/index.php?route=product/product&path=20&product_id=42'

PAGE_TITLE = (By.XPATH, '''//head/title[text()='Apple Cinema 30']''')
PRODUCT_NAME = (By.XPATH, '''//h1[text()='Apple Cinema 30"']''')
TAB_DESCRIPTION = (By.XPATH, '''//a[@href="#tab-description"]''')
TAB_SPECIFICATION = (By.XPATH, '''//a[@href="#tab-specification"]''')
TAB_REVIEW = (By.XPATH, '''//a[@href="#tab-review"]''')
DESCRIPTION_CONTENT = (By.XPATH, '''//div[@class='tab-content']''')
CURRENT_PRICE = (By.XPATH, '''//h2[text()='$110.00']''')


class ProductPage(BasePage):
    pass
