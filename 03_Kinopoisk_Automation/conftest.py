import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver
from config import Config


@pytest.fixture(scope="class")
def driver() -> WebDriver:
    """
    Инициализация браузера Chrome с настройками обхода защиты.
    :return: Экземпляр WebDriver для работы с UI.
    """
    with allure.step("Запуск браузера Chrome с защитой от"
                    "распознавания ботов"):
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)
        browser.maximize_window()

    yield browser

    with allure.step("Закрытие сессии браузера"):
        browser.quit()


@pytest.fixture
def auth_driver(driver: WebDriver) -> WebDriver:
    """
    Авторизация пользователя через подкладывание куки сессии.
    :param driver: Базовая фикстура WebDriver.
    :return: Авторизованный экземпляр драйвера.
    """
    with allure.step("Переход на главную страницу для установки кук"):
        driver.get(Config.BASE_URL_UI)

    with allure.step("Установка авторизационной куки 'sessionid2'"):
        driver.add_cookie({
            "name": "sessionid2",
            "value": Config.AUTH_COOKIE,
            "domain": ".kinopoisk.ru"
        })

    with allure.step(f"Установка куки логина для пользователя {Config.LOGIN_NAME}"):
        driver.add_cookie({
            "name": "l",
            "value": Config.LOGIN_NAME,
            "domain": ".kinopoisk.ru"
        })

    with allure.step("Обновление страницы для применения авторизации"):
        driver.refresh()

    return driver
