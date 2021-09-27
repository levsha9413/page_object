from selenium.webdriver.common.by import By

POSTFIX_URL = '/index.php?route=product/category&path=20'

DESKTOPS = (By.XPATH, '//*[text()="Desktops (13)"]')
APPLE_CINEMA = (By.XPATH, '''//a[text()='Apple Cinema 30"']''')
CANON = (By.XPATH, '''//a[text()='Canon EOS 5D']''')
HP = (By.XPATH, '''//a[text()='HP LP3065']''')
HTC = (By.XPATH, '''//a[text()='HTC Touch HD']''')
IPHONE = (By.XPATH, '''//a[text()='iPhone']''')
IPOD = (By.XPATH, '''//a[text()='iPod Classic']''')
MACBOOK = (By.XPATH, '''//a[text()='MacBook']''')
MACBOOK_AIR = (By.XPATH, '''//a[text()='MacBook Air']''')
PELM_TREO_PRO = (By.XPATH, '''//a[text()='Palm Treo Pro']''')
TEST_PRODUCT = (By.XPATH, '''//a[text()='Product 8']''')
SAMSUNG = (By.XPATH, '''//a[text()='Samsung SyncMaster 941BW']''')
SONY_VAIO = (By.XPATH, '''//a[text()='Sony VAIO']''')
LAPTOPS = (By.XPATH, '''//*[text()='Laptops & Notebooks (5)']''')
COMPONENTS = (By.XPATH, '''//*[text()='Components (2)']''')
TABLETS = (By.XPATH, '''//*[text()='Tablets (1)']''')
SOFTWARE = (By.XPATH, '''//*[text()='Software (0)']''')
PHONES = (By.XPATH, '''//*[text()='Phones & PDAs (3)']''')
CAMERAS = (By.XPATH, '''//*[text()='Cameras (2)']''')
MP3 = (By.XPATH, '''//*[text()='MP3 Players (4)']''')


class CatalogPage:

    pass