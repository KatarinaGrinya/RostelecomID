from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, RecoveryPageLocators, RegistrationPageLocators, PasswordRecoveryPageLocators
from selenium.webdriver.common.by import By
import pytest


class PasswordRecoveryPageLocators():


    def new_password_field_must_be_correctness(self):
       input_password_new = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_NEW)
       input_password_new.clear()
       input_password_new.send_keys('123')
       input_password_confirm = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_CONFIRM)
       input_password_confirm.click()
       result = input_newpassword.number
       assert result == "Длина пароля должна быть не менее 8 символов"

    def new_password_password_confirm_field_must_be_correctness(self):
        input_password_new = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_NEW)
        input_password_new.clear()
        input_password_new.sendkeys('KattyGrinya12')
        input_password_confirm = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_CONFIRM)
        input_password_confirm.clear()
        input_password_confirm.sendkeys('KattyGrinya11')
        button_save = self.find_element(PasswordRecoveryPageLocators.BUTTON_SAVE)
        button_save.click()
        result = input_password_new.text, input_password_confirm.text
        assert result == "Пароли не совпадают"


    def new_password_password_confirm_field_must_be_correctness(self):
        input_password_new = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_NEW)
        input_password_new.clear()
        input_password_new.sendkeys('kattygrinya12')
        input_password_confirm = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_CONFIRM)
        input_password_confirm.clear()
        input_password_confirm.sendkeys('kattygrinya12')
        button_save = self.find_element(PasswordRecoveryPageLocators.BUTTON_SAVE)
        button_save.click()
        result = input_password_new.text, input_password_confirm.text
        assert result == "Пароль должен содержать хотя бы одну заглавную букву"

    def smust_be_button_save(self):
        button_save = self.find_element(PasswordRecoveryPageLocators.BUTTON_SAVE)
        button_save.click()
        self.browser.current_url = result
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=P2FZFyPlzzE'
