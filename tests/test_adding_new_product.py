from page_objects.login_admin_page import LoginAdminPage
import time


def test_a(browser, url):
    page = LoginAdminPage(browser)
    page.open_page(url)
    page.sign_in("demo", "demo")
    assert \
        page.browser.current_url == f"{url}/admin/index.php?route=common/dashboard&user_token=HJMo1IsWFpvWgnGTpmybtZqyMG1wo6jK"
    time.sleep(2)
