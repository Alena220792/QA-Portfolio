import pytest
import allure
import requests
from config import Config
from pages_api.search_movie import SearchMovie
from pages_api.get_by_id import GetMovieById
from pages_api.get_genres import GetGenres
from pages_api.filter_rating import FilterByRating


@pytest.mark.api
@allure.feature("API тесты Кинопоиска")
@allure.story("Пользовательские сценарии")
class TestKinopoiskAPI:
    """
    Класс с набором API-тестов:
    1. Поиск фильма по названию
    2. Получение фильма по ID
    3. Проверка списка доступных жанров
    4. Фильтрация по высокому рейтингу (проверка всех в цикле)
    5. Негативный тест (неверный токен)
    """
    @allure.title("Поиск фильма по названию")
    @allure.description("Проверка, что поиск"
                        "возвращает корректный статус и искомый фильм.")
    @allure.severity("blocker")
    def test_search_movie(self) -> None:
        """
        Тест проверяет поиск фильма 'Зеленая миля'.
        :return: None — метод выполняет проверку и ничего не возвращает.
        """
        movie_name = "Зеленая миля"
        response = SearchMovie().execute(movie_name)
        assert response.status_code == 200
        assert any(
            movie['name'] == movie_name for movie in response.json()['docs'])

    @allure.title("Получение фильма по ID")
    @allure.description("Тест проверяет получение данных"
                        "конкретного фильма по его уникальному идентификатору.")
    @allure.severity("blocker")
    def test_get_movie_by_id(self) -> None:
        """
        Проверка получения фильма по ID.
        :return: None — метод выполняет проверку и ничего не возвращает.
        """
        movie_id = 435
        response = GetMovieById().execute(movie_id)
        with allure.step("Проверка статус-кода и ID в ответе"):
            assert response.status_code == 200
            assert response.json()['id'] == movie_id

    @allure.title("Проверка списка доступных жанров")
    @allure.description("Тест запрашивает справочник жанров"
                        "и проверяет наличие в нем 'комедии'.")
    @allure.severity("blocker")
    def test_get_genres(self) -> None:
        """
        Проверка наличия жанра в справочнике.
        :return: None — метод выполняет проверку и ничего не возвращает.
        """
        response = GetGenres().execute()
        with allure.step("Проверка статус-кода и наличия жанра 'комедия'"):
            assert response.status_code == 200
            genres = [item['name'] for item in response.json()]
            assert "комедия" in genres

    @allure.title("Фильтрация по высокому рейтингу (проверка всех в цикле)")
    @allure.description("Запрос топ-фильмов и валидация рейтинга для"
                        "каждого элемента в списке.")
    @allure.severity("blocker")
    def test_filter_by_rating(self) -> None:
        """
        Проверка фильтрации рейтинга с валидацией каждого фильма.
        :return: None — метод выполняет проверку и ничего не возвращает.
        """
        limit_val: int = 5
        rating_range: str = "9-10"
        response = FilterByRating().execute(rating_range, limit_val)

        assert response.status_code == 200
        docs = response.json()['docs']

        with allure.step(f"Проверка, что в списке {len(docs)} фильмов"):
            assert len(docs) == limit_val

        with allure.step("Валидация рейтинга для каждого фильма в цикле"):
            for movie in docs:
                movie_name = movie.get('name', 'Без названия')
                kp_rating = movie['rating']['kp']
                assert kp_rating >= 9, f"Рейтинг фильма '{movie_name}' ниже 9 (фактически: {kp_rating})"

    @allure.title("Негативный тест (неверный токен)")
    @allure.description("Проверка системы безопасности: запрос"
                        "с некорректным API-ключом должен возвращать 401.")
    @allure.severity("blocker")
    def test_invalid_token(self) -> None:
        """
        Проверка обработки неавторизованного запроса.
        :return: None — метод выполняет проверку и ничего не возвращает.
        """
        with allure.step("Выполнение запроса с неверным токеном"):
            response = requests.get(f"{Config.BASE_URL_API}/v1.4/movie/435",
            headers={"X-API-KEY": "BAD_TOKEN_123"}
            )

        with allure.step("Проверка получения ошибки 401 (Unauthorized)"):
            assert response.status_code == 401
