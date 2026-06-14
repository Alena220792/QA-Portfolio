import allure
import requests
from pages_api.base_api import BaseAPI


class FilterByRating(BaseAPI):
    """
    Класс для реализации метода фильтрации фильмов по рейтингу.
    """
    @allure.step("API: Фильтрация списка фильмов по рейтингу {rating}")
    def execute(self, rating: str, limit: int = 5) -> requests.Response:
        """
        Выполняет запрос на фильтрацию фильмов по заданному диапазону рейтинга.
        :param rating: Диапазон рейтинга (например, '9-10').
        :param limit: Лимит количества возвращаемых фильмов.
        :return: Объект ответа requests.Response.
        """
        params = {"rating.kp": rating, "limit": limit}
        return requests.get(f"{self.base_url}/v1.4/movie",
                            headers=self.headers, params=params)
