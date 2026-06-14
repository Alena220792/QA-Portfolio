import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages_ui.base_page import BasePage


class FooterPage(BasePage):
    """
    Класс для работы с футером (подвалом) сайта.
    """

    @allure.step("UI: Проверка доступности ссылки на соцсеть '{platform}'")
    def is_social_link_clickable(self, platform: str) -> bool:
        """
        Проверяет наличие и активность ссылки на социальную сеть в футере.
        :param platform: Название платформы (например, 'vk').
        :return: True, если ссылка активна.
        """
        selector = f"a[href*='{platform}.com/kinopoisk']"

        link = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector)),
            message=f"Ссылка на соцсеть {platform} не найдена в футере"
        )
        return link.is_enabled()
