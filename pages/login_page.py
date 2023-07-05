import time

import pytest

from .base_page import BasePage
from .locators import LoginPageLocators, RegForm


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Url is correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form exists"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form exists"

    def register_new_user(self, email, password):
        self.go_to_login_page()
        input_1 = self.browser.find_element(*RegForm.LOGIN_FIELD)
        input_1.send_keys(email)
        input_2 = self.browser.find_element(*RegForm.PASS_FIELD_1)
        input_2.send_keys(password)
        input_3 = self.browser.find_element(*RegForm.PASS_FIELD_2)
        input_3.send_keys(password)
        button = self.browser.find_element(*RegForm.REG_BUTTON)
        button.click()
