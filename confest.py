from selenium import webdriver
import pytest

# Фикстура финализатор

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome("C:\Users\GrickevichK\Skillfactory\chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()
