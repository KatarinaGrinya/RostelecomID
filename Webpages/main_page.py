from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, RecoveryPageLocators, RegistrationPageLocators
from selenium.webdriver.common.by import By
import pytest

# создаем конструктор, который принимает browser — экземпляр webdriver.
# Указываем url, который будет использоваться для открытия страницы.
class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # команда для неявного ожидания со значением по умолчанию в 10c:
        self.browser.implicitly_wait(timeout)

    # создаем метод find_element (ищет элемент и возвращает его)
    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    # создаем метод find_elements (ищет множество элементов и возвращает их списком)
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    # метод open должен открывать нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)

    # метод is_element_except перехватывает исключение.
    # будет использоваться для проверки нахождения элемента на странице
    # В него будем передавать два аргумента: как искать, что искать.
    def is_element_except(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # метод is_element_not_except будет использоваться для проверки отсутствия элемента на странице
    def is_element_not_except(self, how, what):
        try:
            WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((how, what)))
        except (TimeoutException):
            return True
        return False


    # Общие методы проверок для всех страниц #
    
    def menu_autorization_must_be(self):
        menu_autorization = self.find_element(MainPageLocators.PAGE_RIGHT)
        result = menu_autorization.text
        assert result == "Авторизация"

    def form_autorization_must_be(self):
        form_autorization = self.find_element(MainPageLocators.FORM_AUTORIZATION)
        result = form_autorization.text
        assert result == "ФОРМА"

    def product_slogan_must_be(self):
        product_slogan = self.find_element(MainPageLocators.PAGE_LEFT)
        result = product_slogan.text
        assert result == "Личный кабинет"

    def tab_click_telefon_must_be(self):
        tab = self.find_element(MainPageLocators.TAB_PHONE, TAB_MAIL, TAB_LOGIN, TAB_LS)
        tab.click()
        result = tab.text
        assert "Телефон" == result

    def tab_click_telefon_must_be(self):
        tab = self.find_element(MainPageLocators.TAB_PHONE)
        tab.click()
        result = tab.text
        assert "Телефон" == result

    def mobile_number_field_must_be_correctness(self):
        input_phone = self.find_element(MainPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys(input_phone)
        button_to_come_in = self.find_element(MainPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()
        result = input_phone.number
        assert result == "Неверный логин или пароль"

    def field_must_be_correctness_phone_and_password(self):
        input_phone = self.find_element(MainPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("+375-29-123-45-67")
        input_password = self.find_element(MainPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("Grinya12")
        button_to_come_in = self.find_element(MainPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()
        result = input_phone.number, input_password.text
        assert result == "Неверный логин или пароль"

    def must_be_correctness_number(self):
        input_phone = self.find_element(MainPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("+375-29-123-  ")
        button_to_come_in = self.find_element(MainPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()
        result = input_phone.number
        assert result == "Неверный формат телефона"

    def must_be_autorization_by_a_registraited_user(self):
        input_phone = self.find_element(MainPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("+375-29-376-09-99")
        input_password = self.find_element(MainPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("Margosha11112020")
        button_to_come_in = self.find_element(MainPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()
        self.browser.current_url = result
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/account_b2c/page?state=e3d65269-e827-4107-9841-1e66b63201b5&client_id=account_b2c#/'

    def must_be_tab_click_mail(self):
        tab = self.find_element(MainPageLocators.TAB_MAIL)
        tab.click()
        result = tab.text
        assert "Почта" == result

    def mail_field_must_be_correctness(self):
        input_mail = self.find_element(MainPageLocators.INPUT_MAIL)
        input_mail.clear()
        input_mail.send_keys('привет@mail.ru')
        button_to_come_in = self.find_element(MainPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()
        result = input_mail.text
        assert result == "Неверный логин или пароль"

    def must_be_autorization_by_mail_a_unregistraited_user(self):
        input_mail = self.find_element(MainPageLocators.INPUT_MAIL)
        input_mail.clear()
        input_mail.send_keys("katya.cupris@mail.ru")
        input_password = self.find_element(MainPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("Grinya12")
        button_to_come_in = self.find_element(MainPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()
        result = input_mail.text, input_password.text
        assert result == "Неверный логин или пароль"

    def must_be_tab_click_login(self):
        tab = self.find_element(MainPageLocators.TAB_LOGIN)
        tab.click()
        result = tab.text
        assert "Логин" == result

    def login_field_must_be_correctness(self):
        input_login = self.find_element(MainPageLocators.INPUT_LOGIN)
        input_login.clear()
        input_login.send_keys('Логин')
        button_to_come_in = self.find_element(MainPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()
        result = input_login.text
        assert result == "Неверный логин или пароль"

    def must_be_login_field(self):
        input_login = self.find_element(MainPageLocators.INPUT_LOGIN)
        input_login.clear()
        field input_login.click()
        result = input_login.text
        assert result == "Укажите логин, указанный при регистрации"

    def field_login_and_password_must_be_correctness(self):
        input_login = self.find_element(MainPageLocators.INPUT_LOGIN)
        input_login.clear()
        input_login.send_keys('KatarinaGrinya')
        input_password = self.find_element(MainPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("Grinya12")
        button_to_come_in = self.find_element(MainPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()
        result = input_login.text, input_password.text
        assert result == "Неверный логин или пароль"

    def personal_account_field_must_be_correctness(self):
        input_ls = self.find_element(MainPageLocators.INPUT_LS)
        input_ls.clear()
        input_ls.send_keys('98765____')
        result = input_ls.text
        assert result == "Проверьте, пожалуйста, номер лицевого счета"

    def personal_account_must_be_field(self):
        input_ls = self.find_element(MainPageLocators.INPUT_LOGIN)
        input_ls.clear()
        field input_ls.click()
        result = input_ls.text
        assert result == "Проверьте, пожалуйста, номер лицевого счета"
