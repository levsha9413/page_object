from page_objects.login_page import LoginPage
from page_objects.admin_section.elements.navigation_panel import NavigationPanel, Sections
from page_objects.admin_section.elements.title_panel import TitlePanel
from page_objects.admin_section.sections.catalog.products.add_product_page import AddProductPage
import time


def test_a(browser, url):
    '''
    Добавление нового товара в разделе администратора.
    :param browser:
    :param url:
    :return:
    '''
    page = LoginPage(browser)
    menu = NavigationPanel(browser)
    title_panel = TitlePanel(browser)
    page.open_page(url)
    page.sign_in("demo", "demo")
    menu.open_section(Sections.CATALOG_SECTION)
    menu.open_subsection(Sections.PRODUCTS_SUBSECTION)
    title_panel.add_button_click()
    page = AddProductPage(browser)
    page.enter_product_name()



    time.sleep(2)
