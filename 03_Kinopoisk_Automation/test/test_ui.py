import pytest
import allure
from config import Config
from pages_ui.search_page import SearchPage
from pages_ui.navigation_page import NavigationPage
from pages_ui.movie_details_page import MovieDetailsPage
from pages_ui.footer_page import FooterPage


@pytest.mark.ui
@allure.feature("UI тесты Кинопоиска")
@allure.story("Пользовательские сценарии")
class TestKinopoiskUI:
    """
    Класс с набором UI-тестов:
    1. Поиск фильма по названию
    2. Проверка жанра на странице фильма
    3. Переход в раздел Сериалы
    4. Прямой переход на страницу фильма
    5. Проверка соцсетей в футере
    """

    @allure.title("Поиск фильма по названию")
    @allure.description("Тест проверяет ввод названия фильма в поисковую"
                        "строку и наличие ожидаемого фильма в результатах"
                        "выдачи.")
    @allure.severity("blocker")
    def test_search_movie(self, driver) -> None:
        """
        Проверка поиска: ввод названия и проверка выдачи.
        :return: None — метод выполняет проверку и ничего не возвращает.
        """
        driver.get(Config.BASE_URL_UI)
        search = SearchPage(driver)
        search.find_movie("Зеленая миля")
        assert search.is_result_present("Зеленая миля")

    @allure.title("Проверка жанра на странице фильма")
    @allure.description("Тест открывает страницу конкретного"
                        "фильма и проверяет, что в блоке "
                        "информации указан верный жанр.")
    @allure.severity("blocker")
    def test_check_genre(self, driver) -> None:
        """
        Проверка отображения жанра на странице конкретного фильма.
        :return: None — метод выполняет проверку и ничего не возвращает.
        """
        driver.get(f"{Config.BASE_URL_UI}/film/435/")
        details = MovieDetailsPage(driver)
        assert details.is_genre_present("драма")

    @allure.title("Переход в раздел Сериалы")
    @allure.description("Тест проверяет навигацию через главное меню и переход"
                        "в соответствующий раздел по заголовку страницы.")
    @allure.severity("blocker")
    def test_navigation_to_series(self, driver) -> None:
        """
        Проверка перехода через главное меню.
        :return: None — метод выполняет проверку и ничего не возвращает.
        """
        driver.get(Config.BASE_URL_UI)
        nav = NavigationPage(driver)
        nav.go_to_section("Сериалы")
        details = MovieDetailsPage(driver)
        header = details.get_movie_title()
        assert any(t in header for t in ["Сериалы", "Списки"])

    @allure.title("Прямой переход на страницу фильма")
    @allure.description("Тест проверяет корректность загрузки страницы"
                        "фильма при переходе по прямому URL-адресу.")
    @allure.severity("blocker")
    def test_direct_movie_page(self, driver) -> None:
        """
        Проверка открытия фильма по прямой ссылке.
        :return: None — метод выполняет проверку и ничего не возвращает.
        """
        driver.get(f"{Config.BASE_URL_UI}/film/326/")
        details = MovieDetailsPage(driver)
        assert "Побег из Шоушенка" in details.get_movie_title()

    @allure.title("Проверка соцсетей в футере")
    @allure.description("Тест проверяет наличие и активность ссылки на"
                        "официальную группу ВКонтакте в нижней части сайта.")
    @allure.severity("blocker")
    def test_footer_socials(self, driver) -> None:
        """
        Проверка наличия ссылки на ВК в подвале.
        :return: None — метод выполняет проверку и ничего не возвращает.
        """
        driver.get(Config.BASE_URL_UI)
        footer = FooterPage(driver)
        assert footer.is_social_link_clickable("vk")
