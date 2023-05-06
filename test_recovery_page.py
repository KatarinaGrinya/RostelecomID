from .pages.recovery_page import RecoveryPage, url_recovery_page
import pytest


@pytest.mark.recovery_page
class TestBodyFromRecoveryPage():
    def test_must_be_recovery_form(self, browser):
        main_page = RecoveryPage(browser, url_recovery_page)
        main_page.open()
        main_page.must_be_recovery_form()
    def test_must_be_correctness_number_of_characters(self, browser):
        main_page = RecoveryPage(browser, url_recovery_page)
        main_page.open()
        main_page.number_of_characters_must_be_correctness()
    def test_must_be_password_recovery_check_registered_number(self, browser):
        main_page = RecoveryPage(browser, url_recovery_page)
        main_page.open()
        main_page.password_recovery_must_be_check_registered_number()
    def test_must_be_password_recovery_check_registered_mail(self, browser):
        main_page = RecoveryPage(browser, url_recovery_page)
        main_page.open()
        main_page.password_recovery_must_be_check_registered_mail()
    def test_must_be_button_comeback(self, browser):
        main_page = RecoveryPage(browser, url_recovery_page)
        main_page.open()
        main_page.must_be_button_comeback()

        # -m pytest -v --(your_driver) --driver-path <your_driver_directory>/your_driver.exe test_recovery_page.py

    def test_must_be_button_continue(browser):
        main_page = RecoveryPage(browser, url_recovery_page)
        main_page.open()
        main_page.must_be_button_continues()

    def test_must_be_button_comeback_main_page(browser):
       main_page = RecoveryPage(browser, url_recovery_page)
       main_page.open()
       main_page.must_be_button_comeback_main_page()

    def test_must_be_mail_field_correctness(browser):
       main_page = RecoveryPage(browser, url_recovery_page)
       main_page.open()
       main_page.mail_field_must_be_correctness()
