import allure
from locators.login import Loc  


class Login:
    def __init__(self, driver):
            self.driver = driver

    def input_usernamee(self, username):
         with allure.step('Input valid username'):
            self.driver.locator(Loc.input_username).fill(username)
    def input_password(self, password):
        with allure.step('Input valid password'):
            self.driver.locator(Loc.input_password).fill(password)
    def click_login_button(self):        
        with allure.step('Click login button'):
            self.driver.locator(Loc.click_login_button).click()