import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages_ui.base_page import BasePage


class MovieDetailsPage(BasePage):
    """
    Класс для работы с детальной страницей фильма.
    """

    @allure.step("UI: Получение текста главного заголовка страницы (h1)")
    def get_movie_title(self) -> str:
        """
        Находит заголовок h1 и возвращает его текст.
        :return: Текст заголовка (название фильма).
        """
        header = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h1")),
            message="Заголовок фильма (h1) не найден"
        )
        return header.text

    @allure.step("UI: Проверка наличия жанра '{genre_name}' в инфо-панели")
    def is_genre_present(self, genre_name: str) -> bool:
        """
        Проверяет, отображается ли конкретный жанр в списке жанров фильма.
        :param genre_name: Название жанра для поиска.
        :return: True, если жанр виден.
        """
        genre_element = self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, genre_name.lower())),
            message=f"Жанр '{genre_name}' не найден на странице"
        )
        return genre_element.is_displayed()
