from page_objects.login_page import LoginPage
import time


def test_a(browser, url):
    page = LoginPage(browser)
    page.open_page(url)
    page.sign_in("demo", "demo")
    assert \
        page.browser.current_url == f"{url}/admin/index.php?route=common/dashboard&user_token=HJMo1IsWFpvWgnGTpmybtZqyMG1wo6jK"
    time.sleep(2)
