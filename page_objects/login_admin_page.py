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
    pass
