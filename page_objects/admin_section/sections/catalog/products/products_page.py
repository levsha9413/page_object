from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

'''
селектор product_checkbox находится в методе checkbox_click,
т.к. он зависит от передаваемого в метод параметра
'''


class ProductsPage(BasePage):

    def checkbox_click(self, product_name: str = 'Test product name'):
        '''
        выставляет чекбокс у товара, в название которого входит строка product_name
        '''
        product_checkbox = (By.XPATH, f'//tbody/tr[./td[contains(text(), "{product_name}")]]//input')
        self.click_button(*product_checkbox)
