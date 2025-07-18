from dataclasses import field
from dbm.sqlite3 import error

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.auth_page_locators import AuthPageLocators as locators
from element.base_page import BasePage
from locators.test_data import TestData as data

class LoginAccount(BasePage):

    @allure.step('Вводим username')
    def input_username(self, name):
        self.input_value(locators.username_input, name)

    @allure.step('Вводим пароль')
    def input_password(self, surname):
        self.input_value(locators.password_input, surname)

    @allure.step('Нажимаем Войти')
    def click_login_button(self):
        self.click_on_element(locators.login_button)

    @allure.step('Нажимаем Подтвердить')
    def click_confirm_button(self):
        self.click_on_element(locators.confirm_button)

    @allure.step('Очищаем поле')
    def clear_field(self, locator):
        element = self.find_element(locator)
        element.clear()

    @allure.step('Получаем текущую ссылку')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получаем текст ошибки")
    def get_error_text(self, locator):
        error_text=self.find_element(locator)
        return error_text.text



