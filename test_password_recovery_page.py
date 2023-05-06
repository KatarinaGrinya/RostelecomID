from .pages.passwordrecovery_page import PasswordRecoveryPage, url_passwordrecovery_page
import pytest


@pytest.mark.passwordrecovery_page
class TestBodyFromPasswordRecoveryPage():
    def test_must_be_new_password_field_correctness(self, browser):
        main_page = PasswordRecoveryPage(browser, url_passwordrecovery_page)
        main_page.open()
        main_page.new_password_field_must_be_correctness()
    def test_must_be_new_password_password_confirm_field_correctness(self, browser):
        main_page = PasswordRecoveryPage(browser, url_passwordrecovery_page)
        main_page.open()
        main_page.new_password_password_confirm_field_must_be_correctness()
    def test_must_be_new_password_password_confirm_field_correctness(self, browser):
        main_page = PasswordRecoveryPage(browser, url_passwordrecovery_page)
        main_page.open()
        main_page.new_password_password_confirm_field_must_be_correctness()
    def test_must_be_button_save(self, browser):
        main_page = PasswordRecoveryPage(browser, url_passwordrecovery_page)
        main_page.open()
        main_page.must_be_button_save()
