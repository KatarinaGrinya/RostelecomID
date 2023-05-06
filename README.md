Дипломный проект: реальный кейс компании «Ростелеком Информационные Технологии» от онлайн-школы Skillfactory.

Автоматизированное тестирование UI сайта: https://b2c.passport.rt.ru/ с использованием Selenium и PyTest.

В папке Webpages:
  1. в файле main_page.py находится конструктор webdriver и общие для всех тестируемых страниц методы.
  2. в файлах main_page.py, password_recovery_page.py, recovery_page.py, registration_page.py находятся методы для соответствующих тестируемых страниц.
  3. в файле locators.py находятся все локаторы.

В корне проекта в файле conftest.py находится фикстура с функцией открытия и закрытия браузера. Для запуска тестов необходимо поменять путь до webdriver на Ваш.
Тесты находятся в корне проекта в файлах test_main_page.py, test_password_recovery_page.py, test_recovery_page.py, test_registration_page.py

