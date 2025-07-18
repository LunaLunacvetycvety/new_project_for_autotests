import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-cache')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-notifications')
    options.add_argument('--window-size=1980,1080')

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    driver.get("https://idemo.bspb.ru/")

    yield driver
    driver.quit()

