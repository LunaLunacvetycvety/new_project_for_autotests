import allure
import pytest
from locators.auth_page_locators import AuthPageLocators as locators
from locators.test_data import TestData as data
from pages.auth_page import LoginAccount

 # Во всех тестах отсутствует ввод otp кода
class TestAuth:
    # Тест для успешного входа в аккунт без параметров, так как есть единственный логин и пароль для корректного входа
    @allure.title('Проверяем успешный вход в аккаунт')
    @allure.description('Последовательное выполнение действий для проверки входа в аккаунт')
    def test_success_test(self, driver):
        login_page = LoginAccount(driver)
        login_page.clear_field(locators.username_input)
        login_page.input_username(data.login)
        login_page.clear_field(locators.password_input)
        login_page.input_password(data.password)
        login_page.click_login_button()
        login_page.click_confirm_button()


        assert login_page.get_current_url() == data.welcome_url

    # Добавила негативные тесты, чтобы была параметризация для задач
    # Вход считается неудачным, когда мы с некорректными кредами подтвердили otp - ошибка будет "Неверный код", так как до этого логин и пароль не проверяются
    @allure.title('Проверяем вход в аккаунт с некорректными кредами')
    @allure.description('Последовательное выполнение действий для проверки входа в аккаунт')
    @pytest.mark.parametrize("login, password", [
        (data.invalid_login, data.invalid_password),
        (data.invalid_login, data.password),
        (data.login, data.invalid_password),
    ])
    def test_get_error(self, driver, login, password):
        login_page = LoginAccount(driver)
        login_page.clear_field(locators.username_input)
        login_page.input_username(login)
        login_page.clear_field(locators.password_input)
        login_page.input_password(password)
        login_page.click_login_button()
        login_page.click_confirm_button()
        error_text = login_page.get_error_text(locators.login_error)

        assert "Неверный код" == error_text


