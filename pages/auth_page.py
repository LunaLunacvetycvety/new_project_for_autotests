import allure
from locators.auth_page_locators import AuthPageLocators as locators
from element.base_page import BasePage

class AuthPage(BasePage):

    @allure.step('Вводим username')
    def input_username(self, username):
        self.input_value(locators.username_input, username)

    @allure.step('Вводим пароль')
    def input_password(self, password):
        self.input_value(locators.password_input, password)

    @allure.step('Нажимаем Войти')
    def click_login_button(self):
        self.click_on_element(locators.login_button)

    @allure.step('Нажимаем Подтвердить')
    def click_confirm_button(self):
        self.click_on_element(locators.confirm_button)

    @allure.step('Очищаем username')
    def clear_username(self):
        self.clear_field(locators.username_input)

    @allure.step('Очищаем password')
    def clear_password(self):
        self.clear_field(locators.password_input)

    @allure.step('Получаем текущую ссылку')
    def get_current_url(self):
        return self.driver.current_url

