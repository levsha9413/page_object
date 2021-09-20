from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_element_with_wait(self, locator, selector, _browser,  timeout=5):
        # кастомный поиск элемента с ожидаением по существованию элемента
        try:
            WebDriverWait(_browser, timeout).until(EC.presence_of_element_located((locator, selector)))
        except TimeoutException:
            raise AssertionError("Не найден элемент с селектором: {}".format(selector))