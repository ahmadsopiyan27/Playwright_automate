import pytest
import allure
from pages.login import Login


@allure.title('Login Negatif')
@allure.description('Login menggunakan credential yang tidak valid')
@allure.severity(allure.severity_level.NORMAL)

@pytest.mark.parametrize(
    "username, password, error_message",
    [
        pytest.param('standard_user', 'salah',
                     'Epic sadface: Username and password do not match any user in this service',
                     id="wrong_password"),

        pytest.param('salah_user', 'secret_sauce',
                     'Epic sadface: Username and password do not match any user in this service',
                     id="wrong_username"),

        pytest.param('', 'secret_sauce',
                     'Epic sadface: Username is required',
                     id="empty_username"),

        pytest.param('standard_user', '',
                     'Epic sadface: Password is required',
                     id="empty_password"),

        pytest.param('', '',
                     'Epic sadface: Username is required',
                     id="empty_all"),
    ]
)
def test_login_negatif(setup, username, password, error_message):

    login = Login(setup)

    login.input_username(username)
    login.input_password(password)
    login.click_login_button()

    login.verify_error_message(error_message)