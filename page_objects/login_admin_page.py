from selenium.webdriver.common.by import By

POSTFIX_URL = '/admin'

USERNAME_INPUT = (By.ID, "input-username")
PASSWORD_INPUT = (By.NAME, "password")
LOGO = (By.XPATH, '''//img[@alt="OpenCart"]'''),
LOGIN_BUTTON = (By.XPATH, '''//button[text()=" Login"]''')
PANEL_TITLE = (By.XPATH, '''//h1[text()=" Please enter your login details."]''')
FORGOTTEN_PASSWORD_LINK = (
    By.XPATH, '''//a[text()="Forgotten Password" and contains (@href, "admin/index.php?route=common/forgotten")]''')


class LoginAdminPage:
    def __init__(self, browser):
        self.browser = browser

    def open_page(self, _url):
        self.browser.get(_url + POSTFIX_URL)

    def entering_login(self, login):
        username_input = find_element_with_wait(*USERNAME_INPUT)
        username_input.clear()
        username_input.send_keys(login)

    def entering_password(self, password):
        password_input = self.browser.find_element(*)
