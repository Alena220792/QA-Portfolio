import allure
import requests
from pages_api.base_api import BaseAPI


class GetGenres(BaseAPI):
    @allure.step("API: Запрос списка жанров")
    def execute(self) -> requests.Response:
        return requests.get(
            f"{self.base_url}/v1/movie/possible-values-by-field?field=genres.name", headers=self.headers)
