import allure
import requests
from pages_api.base_api import BaseAPI


class SearchMovie(BaseAPI):
    """
    Класс для реализации метода поиска фильмов по названию.
    """
    @allure.step("API: Поиск фильма по ключевому слову'{query}'")
    def execute(self, query: str) -> requests.Response:
        """
        Выполняет GET запрос к эндпоинту поиска фильма.
        :param query: Название фильма для поиска (строка).
        :return: Объект ответа requests.Response.
        """
        params = {"query": query}
        return requests.get(f"{self.base_url}/v1.4/movie/search",
                            headers=self.headers, params=params)
