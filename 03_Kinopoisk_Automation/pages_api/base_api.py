from config import Config


class BaseAPI:
    """
    Базовый класс для всех API-запросов к Кинопоиску.
    """
    def __init__(self) -> None:
        """
        Инициализация базового URL и заголовков с токеном.
        :return: None — метод выполняет проверку и ничего не возвращает.
        """
        self.base_url = Config.BASE_URL_API
        self.headers = {"X-API-KEY": Config.TOKEN}
