from page_objects.login_page import LoginPage
from page_objects.admin_section.elements.navigation_panel import NavigationPanel, Sections
from page_objects.admin_section.elements.title_panel import TitlePanel
from page_objects.admin_section.sections.catalog.products.add_product_page import AddProductPageGeneral, \
    AddProductPageData
from page_objects.admin_section.elements.alert import Alert
from page_objects.admin_section.sections.catalog.products.products_page import ProductsPage
from page_objects.browser_alert import BrowserAlert
from page_objects.customer_section.elements.upper_user_panel import UpperUserPanel, Currencies
from page_objects.customer_section.pages.home_page import HomePage
from page_objects.customer_section.pages.register_page import RegisterPage

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
    login_page.sign_in("user", "bitnami")
    menu.open_section(Sections.CATALOG_SECTION)
    menu.open_subsection(Sections.PRODUCTS_SUBSECTION)
    title_panel.add_button_click()
    add_product_page = AddProductPageGeneral(browser)
    add_product_page.enter_all_fields()
    add_product_page = AddProductPageData(browser)
    add_product_page.switch_to_data_tab()
    add_product_page.enter_model()
    add_product_page.click_save_button() #добавить кнопки в отдельный класс модуля add_product_page
    browser.stop_client()
    browser.save_screenshot('2.png')
    assert alert.text() == "Warning: You do not have permission to modify products!\n×"


def test_delete_product(browser, url):
    '''
    Удаление товара из списка в разделе администартора.
    '''
    login_page = LoginPage(browser)
    menu = NavigationPanel(browser)
    local_alert = Alert(browser)
    browser_alert = BrowserAlert(browser)
    title_panel = TitlePanel(browser)
    login_page.open_page(url)
    login_page.sign_in("demo", "demo")
    menu.open_section(Sections.CATALOG_SECTION)
    menu.open_subsection(Sections.PRODUCTS_SUBSECTION)
    products_page = ProductsPage(browser)
    products_page.checkbox_click("Apple")
    title_panel.delete_button_click()
    browser_alert.accept_alert()
    assert local_alert.text() == "Warning: You do not have permission to modify products!\n×"


def test_new_customer_registration(browser, url):
    '''
    Регистрация нового пользователя в магазине опенкарта.
    '''
    page = HomePage(browser)
    panel = UpperUserPanel(browser)
    page.open_page(url)
    panel.go_to_register()
    register_page = RegisterPage(browser)
    register_page.enter_all_user_fields()
    register_page.click_privacy_policy_checkbox()
    register_page.click_continue()
    register_page.check_successfuly_created()


def test_switching_currency(browser, url):
    '''
    Переключение валют из верхнего меню опенкарта.
    '''
    page = HomePage(browser)
    panel = UpperUserPanel(browser)
    page.open_page(url)
    panel.switch_currency(Currencies.USD)
    panel.check_current_currency(Currencies.USD)
    panel.switch_currency(Currencies.EURO)
    panel.check_current_currency(Currencies.EURO)
    panel.switch_currency(Currencies.POUND_STERLING)
    panel.check_current_currency(Currencies.POUND_STERLING)

    browser.save_screenshot("2.png")
    time.sleep(2)
