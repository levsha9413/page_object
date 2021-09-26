from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

POSTFIX_URL = '/admin'

USERNAME_INPUT = (By.ID, "input-username")
PASSWORD_INPUT = (By.NAME, "password")
LOGO = (By.XPATH, '''//img[@alt="OpenCart"]'''),
LOGIN_BUTTON = (By.XPATH, '''//button[text()=" Login"]''')
PANEL_TITLE = (By.XPATH, '''//h1[text()=" Please enter your login details."]''')
FORGOTTEN_PASSWORD_LINK = (
    By.XPATH, '''//a[text()="Forgotten Password" and contains (@href, "admin/index.php?route=common/forgotten")]''')


class LoginPage(BasePage):

    def open_page(self, _url):
        self.browser.get(_url + POSTFIX_URL)

    def entering_login(self, login):
        username_input = self.find_element_with_wait(*USERNAME_INPUT)
        username_input.clear()
        username_input.send_keys(login)

    def entering_password(self, password):
        password_input = self.find_element_with_wait(*PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def login_button_click(self):
        button = self.find_element_with_wait(*LOGIN_BUTTON)
        button.click()

    def sign_in(self, login, password):
        '''
        вынес наиболее частый сценарий в отдельный метод
        '''
        self.entering_login(login)
        self.entering_login(password)
        self.login_button_click()

    def forgotten_password_link_click(self):
        link = self.find_element_with_wait(*FORGOTTEN_PASSWORD_LINK)
        link.click()
