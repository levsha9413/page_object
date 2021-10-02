import pytest
from page_objects.login_page import LoginPage
from page_objects.admin_section.elements.navigation_panel import NavigationPanel, Sections
from page_objects.admin_section.elements.title_panel import TitlePanel
from page_objects.admin_section.sections.catalog.products.add_product_page import AddProductPage
from page_objects.admin_section.elements.alert import Alert
import time


def test_add_new_product(browser, url):
    '''
    Добавление нового товара в разделе администратора.
    '''
    login_page = LoginPage(browser)
    menu = NavigationPanel(browser)
    alert = Alert(browser)
    title_panel = TitlePanel(browser)
    login_page.open_page(url)
    login_page.sign_in("demo", "demo")
    menu.open_section(Sections.CATALOG_SECTION)
    menu.open_subsection(Sections.PRODUCTS_SUBSECTION)
    title_panel.add_button_click()
    add_product_page = AddProductPage(browser)
    add_product_page.enter_all_fields()
    add_product_page.click_save_button()
    assert alert.text() == "Warning: You do not have permission to modify products!\n×"

def test_delete_product(browser, url):
    '''
    Удаление товара из списка в разделе администартора.
    '''
    login_page = LoginPage(browser)
    menu = NavigationPanel(browser)
    alert = Alert(browser)
    title_panel = TitlePanel(browser)
    login_page.open_page(url)
    login_page.sign_in("demo", "demo")
    menu.open_section(Sections.CATALOG_SECTION)
    menu.open_subsection(Sections.PRODUCTS_SUBSECTION)
    browser.save_screenshot("screen.png")
    time.sleep(1)
