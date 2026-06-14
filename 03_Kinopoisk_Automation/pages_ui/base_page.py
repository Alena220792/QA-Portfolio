from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """
    Базовый класс для всех UI страниц.
    """
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация драйвера и стандартного ожидания.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
