from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, RecoveryPageLocators, RegistrationPageLocators, PasswordRecoveryPageLocators
from selenium.webdriver.common.by import By
import pytest

class RecoveryPage():


    def must_be_recovery_form(self):
        recovery_form = self.find_element(RecoveryPageLocators.RECOVERY_FORM)
        result = recovery_form.text
        assert result == "Форма"

    def number_of_characters_must_be_correctness(self):
        input_phone = self.find_element(RecoveryPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("+7375-29-123-  ")
        button_to_come_in = self.find_element(RecoveryPageLocators.BUTTON_CONTINUE)
        button_to_come_in.click()
        result = input_phone.number
        assert result == "Неверный формат номера"

    def password_recovery_must_be_check_registered_number(self):
        input_phone = self.find_element(RecoveryPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("+375-29-376-09-99")
        input_capcha = self.find_element(RecoveryPageLocators.INPUT_CAPCHA)
        input_capcha.clear()
        input_capcha.send_keys("CBwd3HEI")
        button_to_come_in = self.find_element(RecoveryPageLocators.BUTTON_CONTINUE)
        button_to_come_in.click()
        self.browser.current_url = result
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?session_code=RpQteafuCWnxWZkmsk_5CKEUoyfAR2x2PUPtFFEtfsQ&execution=1b1825d2-f76f-4706-8e25-4c71c1f7f120&client_id=account_b2c&tab_id=B8z6Ht7_4rs'


    def password_recovery_must_be_check_registered_mail(self, browser):
        input_mail = self.find_element(RecoveryPageLocators.INPUT_MAIL)
        input_mail.clear()
        input_mail.send_keys('katya.chupris@mail.ru')
        input_capcha = self.find_element(RecoveryPageLocators.INPUT_CAPCHA)
        input_capcha.clear()
        input_capcha.send_keys("2FS4q21")
        button_continue = self.find_element(RecoveryPageLocators.BUTTON_CONTINUE)
        button_continue.click()
        self.browser.current_url = result
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?execution=7ca0b6f9-7c84-472b-94e2-a57c35eb6b08&client_id=account_b2c&tab_id=4JvtA2huco0'


    def must_be_button_comeback(self):
        link_comeback = self.find_element(RecoveryPageLocators.BUTTON_COMEBACK)
        link_comeback.click()
        self.browser.current_url = result
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?execution=1b1825d2-f76f-4706-8e25-4c71c1f7f120&client_id=account_b2c&tab_id=mHPSKFbKvLQ'


    def must_be_button_continue(self):
        input_mail = self.find_element(RecoveryPageLocators.INPUT_MAIL)
        input_mail.clear()
        input_mail.send_keys('katya.chupris@mail.ru')
        input_capcha = self.find_element(RecoveryPageLocators.INPUT_CAPCHA)
        input_capcha.clear()
        input_capcha.send_keys("c4PAl3v")
        button_continue = self.find_element(RecoveryPageLocators.BUTTON_CONTINUE)
        button_continue.click()
        self.browser.current_url = result
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?execution=7ca0b6f9-7c84-472b-94e2-a57c35eb6b08&client_id=account_b2c&tab_id=4JvtA2huco0'


    def must_be_button_comeback_main_page(self):
        button_comeback = self.find_element(RecoveryPageLocators.BUTTON_COMEBACK)
        button_comeback.click()
        self.browser.current_url = result
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?session_code=Y0VJ5ZrIyarhrjbmUPmjkjmFdYC9D6gD-rASQlwayCI&execution=1b1825d2-f76f-4706-8e25-4c71c1f7f120&client_id=account_b2c&tab_id=mHPSKFbKvLQ'

    
    def mail_field_must_be_correctness(self):
       input_mail = self.find_element(RecoveryPageLocators.INPUT_MAIL)
       input_mail.clear()
       input_mail.send_keys('привет@mail.ru')
       button_continue = self.find_element(RecoveryPageLocators.BUTTON_CONTINUE)
       button_continue.click()
       tab.login = self.find_element(RecoveryPageLocators.TAB_LOGIN)
       result = tab_login.click()
       assert result == "Неверный логин или текст с картинки"
