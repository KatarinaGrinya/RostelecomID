from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, RecoveryPageLocators, RegistrationPageLocators, PasswordRecoveryPageLocators
from selenium.webdriver.common.by import By
import pytest

class RegistrationPageLocators():

    def must_be_register_link(self):
        link = self.find_element(MainPageLocators.LINK_REGISTER)
        result = link.text
        assert "Зарегистрироваться" == result

    def field_first_name_must_be_correctness(self):
        input_first_name = self.find_element(RegistrationPageLocators.INPUT_FIRST_NAME)
        input_first_name.clear()
        input_first_name.send_keys('Gr')
        button_register = self.find_element(RegistrationPageLocators.BUTTON_PAGE_REGISTER)
        button_register.click()
        result = input_first_name.text
        assert result == "Необходимо заполнить поле кириллицей. От 2 до 30 символов"

    def field_first_surname_must_be_correctness(self):
        input_first_name = self.find_element(RegistrationPageLocators.INPUT_FIRST_NAME)
        input_first_name.clear()
        input_first_name.send_keys('Grinya')
        button_register = self.find_element(RegistrationPageLocators.BUTTON_PAGE_REGISTER)
        button_register.click()
        result = input_first_name.text
        assert result == "Необходимо заполнить поле кириллицей. От 2 до 30 символов"
        
     def must_be_region_list(self):
        region_list = self.find_elements(RegistrationPageLocators.REGION_LIST)
        button region_list.click()
        result = region_list.text
        assert result == "Регион"

    def field_phone_must_be_correctness(self):
        input_address = self.find_element(RegistrationPageLocators.INPUT_ADDRESS)
        input_address.clear()
        input_address.send_keys("+375-29-123-  ")
        button_page_register = self.find_element(RegistrationPageLocators.BUTTON_PAGE_REGISTER)
        button_page_register.click()
        result = input_address.number
        assert result == "Сообщение введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

    def field_email_must_be_correctness(self):
        input_address = self.find_element(RegistrationPageLocators.INPUT_ADDRESS)
        input_address.clear()
        input_address.send_keys("katarinaGrinya@mailru")
        button_page_register = self.find_element(RegistrationPageLocators.BUTTON_PAGE_REGISTER)
        button_page_register.click()
        result = input_address.number
        assert result == "Сообщение введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

    def should_be_password_field_correctness(self):
       input_password = self.find_element(RegistrationPageLocator.INPUT_PASSWORD)
       input_password.clear()
       input_password.send_keys('13579')
       input_password.click()
       result = input_password.text
       assert result == "Длина пароля должна быть не менее 8 символов"

    def password_confirm_field_must_be_correctness(self):
       input_password_confirm = self.find_element(RegistrationPageLocators.INPUT_PASSWORD_CONFIRM)
       input_password_confirm.clear()
       input_password_confirm.send_keys('123456789')
       input_password_confirm.click()
       result = input_password_confirm.number
       assert result == "Пароль должен содержать хотя бы одну заглавную букву"


