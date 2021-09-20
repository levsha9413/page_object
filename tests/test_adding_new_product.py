from page_objects.login_admin_page import LoginAdminPage
import time


def test_a(browser, url):
    page = LoginAdminPage(browser)
    page.open_page(url)
    page.entering_login("Login")
    time.sleep(3)
