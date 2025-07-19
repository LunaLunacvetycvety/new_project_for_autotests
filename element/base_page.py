from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # для поиска элемента
    def find_element(self, locator, time=25):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    # для получения текста
    def get_text(self, locator):
        return self.find_element(locator).text

    # для клика по элементу
    def click_on_element(self, locator):
        self.find_element(locator).click()

    # для получения текущей ссылки
    def get_current_url(self):
        return self.driver.current_url

    # для ввода данных в поле
    def input_value(self, locator, text):
        self.find_element(locator).send_keys(text)

    # для очистки поля
    def clear_field(self, locator):
        self.find_element(locator).clear()



