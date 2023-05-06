from .pages.registration_page import RegistrationPage, url_registration_page
import pytest


@pytest.mark.registration_page

class TestBodyFromRegistrationPage():
    def test_must_be_register_link(self, browser):
        main_page = RegistrationPage(browser, url_registration_page)
        main_page.open()
        main_page.must_be_register_link()
    def test_must_be_field_first_name_correctness(self, browser):
        main_page = RegistrationPage(browser, url_registration_page)
        main_page.open()
        main_page.field_first_name_must_be_correctness()
    def test_must_be_field_last_name_correctness(self, browser):
        main_page = RegistrationPage(browser, url_registration_page)
        main_page.open()
        main_page.field_last_name_must_be_correctness()
    def test_should_be_field_address_correctness(self, browser):
        main_page = RegistrationPage(browser, url_registration_page)
        main_page.open()
        main_page.should_be_field_address_correctness()
    def test_must_be_region_list(self, browser):
        main_page = RegistrationPage(browser, url_registration_page)
        main_page.open()
        main_page.must_be_region_list()
    def test_must_be_password_field_correctness(self, browser):
        main_page = RegistrationPage(browser, url_registration_page)
        main_page.open()
        main_page.must_be_password_field_correctness()

      # -m pytest -v --(your_driver) --driver-path <your_driver_directory>/your_driver.exe test_registration_page.py

    def test_must_be_password_confirm_field_correctness(browser):
        main_page = RegistrationPage(browser, url_registration_page)
        main_page.open()
        main_page.password_confirm_field_must_be_correctness()
