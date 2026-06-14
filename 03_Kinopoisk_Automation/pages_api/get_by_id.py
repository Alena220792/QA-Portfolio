import allure
import requests
from pages_api.base_api import BaseAPI


class GetMovieById(BaseAPI):
    """
    Класс для реализации метода получения фильма по его уникальному ID.
    """
    @allure.step("API: Запрос фильма по ID {movie_id}")
    def execute(self, movie_id: int) -> requests.Response:
        """
        Получает детальную информацию о фильме.
        :param movie_id: Уникальный идентификатор фильма (число).
        :return: Объект ответа requests.Response.
        """
        return requests.get(f"{self.base_url}/v1.4/movie/{movie_id}",
                            headers=self.headers)
