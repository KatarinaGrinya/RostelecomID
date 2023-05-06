from .pages.main_page import MainPage, url_main_page
import pytest

def test_must_be_menu_autorization(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.menu_autorization_must_be()

def test_must_be_form_autorization(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.form_autorization_must_be()

    
@pytest.mark.main_page
class TestBodyFromMainPage():
    def test_must_be_product_slogan(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.product_slogan_must_be()
    def test_must_be_tab_click_phone(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.tab_click_phone_must_be()
    def test_must_be_tab_click_telefon(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.tab_click_telefon_must_be()
    def test_must_be_mobile_number_field_correctness(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.mobile_number_field_must_be_correctness()
    def test_must_be_field_correctness_phone_and_password(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.field_must_be_correctness_phone_and_password()

    # -m pytest -v --(your_driver) --driver-path <your_driver_directory>/your_driver.exe test_main_page.py

    def test_must_be_correctness_number_of_characters(browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.must_be_correctness_number()

    def test_must_be_autorization_by_a_registraited_usera(browser):
       main_page = MainPage(browser, url_main_page)
       main_page.open()
       main_page.must_be_autorization_by_a_registraited_user()

    def test_must_be_autorization_by_a_registraited_user(browser):
       main_page = MainPage(browser, url_main_page)
       main_page.open()
       main_page.must_be_autorization_by_a_registraited_user()

    def test_must_be_tab_click_mail(browser):
       main_page = MainPage(browser, url_main_page)
       main_page.open()
       main_page.must_be_tab_click_mail()

    def test_must_be_mail_field_correctness(browser):
       main_page = MainPage(browser, url_main_page)
       main_page.open()
       main_page.mail_field_must_be_correctness()
