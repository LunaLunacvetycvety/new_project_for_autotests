import allure
import pytest
from locators.auth_page_locators import AuthPageLocators as locators
from locators.test_data import TestData as data
from pages.auth_page import AuthPage
from time import sleep

 # Во всех тестах отсутствует проверка ввода otp кода
class TestAuth:
    # Тест для успешного входа в аккунт без параметров, так как есть единственный логин и пароль для корректного входа
    @allure.title('Проверяем успешный вход в аккаунт')
    @allure.description('Последовательное выполнение действий для проверки входа в аккаунт')
    def test_success_auth(self, driver):
        auth_page = AuthPage(driver)
        auth_page.clear_username()
        auth_page.input_username(data.login)
        auth_page.clear_password()
        auth_page.input_password(data.password)
        auth_page.click_login_button()
        auth_page.click_confirm_button()
        assert auth_page.get_current_url() == data.welcome_url

    # Добавила негативные тесты, чтобы была параметризация для задач
    # Вход считается неудачным, когда мы с некорректными кредами подтвердили otp - ошибка будет "Неверный код", так как до этого логин и пароль не проверяются
    @allure.title('Проверяем вход в аккаунт с некорректными кредами')
    @allure.description('Последовательное выполнение действий для проверки входа в аккаунт')
    @pytest.mark.parametrize("login, password", [
        (data.invalid_login, data.invalid_password),
        (data.invalid_login, data.password),
        (data.login, data.invalid_password),
    ])
    def test_fail_auth(self, driver, login, password):
        auth_page = AuthPage(driver)
        auth_page.clear_username()
        auth_page.input_username(login)
        auth_page.clear_password()
        auth_page.input_password(password)
        auth_page.click_login_button()
        auth_page.click_confirm_button()
        error_text = auth_page.get_text(locators.login_error)

        assert "Неверный код" == error_text


