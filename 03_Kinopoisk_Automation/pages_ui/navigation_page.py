import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages_ui.base_page import BasePage


class NavigationPage(BasePage):
    """
    Класс для навигации по разделам сайта.
    """
    @allure.step("UI: Переход в раздел '{link_text}' через JS-клик")
    def go_to_section(self, link_text: str) -> None:
        """
        Выполняет клик по ссылке в главном меню.
        """
        link = self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, link_text)))
        self.driver.execute_script("arguments[0].click();", link)
