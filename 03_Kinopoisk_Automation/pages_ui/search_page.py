import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages_ui.base_page import BasePage


class SearchPage(BasePage):
    """
    Класс для работы с поисковой строкой.
    """
    @allure.step("UI: Поиск фильма '{name}' с очисткой поля")
    def find_movie(self, name: str) -> None:
        """
        Очищает поле и выполняет поиск.
        """
        field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "kp_query")))
        field.clear()
        field.send_keys(name + Keys.ENTER)

    @allure.step("UI: Проверка наличия ссылки '{text}'")
    def is_result_present(self, text: str) -> bool:
        """
        Проверяет наличие ссылки в результатах поиска.
        """
        return self.wait.until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, text))).is_displayed()
