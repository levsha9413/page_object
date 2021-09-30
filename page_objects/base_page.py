from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_element_with_wait(self, locator, selector, timeout=5):
        # кастомный поиск элемента с ожидаением по существованию элемента

        try:
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((locator, selector)))
        except TimeoutException:
            raise AssertionError("Не найден элемент с селектором: {}".format(selector))
        return element

    def find_element_with_wait_clickable(self, locator, selector, timeout=5):
        # кастомный поиск элемента с ожидаением по существованию элемента

        try:
            element = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((locator, selector)))
        except TimeoutException:
            raise AssertionError("Не найден элемент с селектором: {}".format(selector))
        return element

    def enter_input(self, locator, selector, data):

        input_field = self.find_element_with_wait(locator, selector)
        input_field.clear()
        input_field.send_keys(data)

    def click_button(self, locator, selector):
        button = self.find_element_with_wait(locator, selector)
        button.click()
