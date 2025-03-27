import allure
from selenium.common import WebDriverException, TimeoutException

from helper.urls import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    @allure.step('Переход по указанному URL')
    def go_to_site(self, url=None):
        if url is None:
            url = Urls.main_page
        try:
            self.driver.get(url)
        except WebDriverException as e:
            raise RuntimeError(f"Ошибка WebDriver: не удалось открыть {url}: {str(e)}")
        except TimeoutException as e:
            raise RuntimeError(f"Ошибка времени ожидания: сайт {url} не загрузился: {str(e)}")

    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Переход на вкладку браузера')
    def switch_window(self, window_number: int):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step("Ожидание, что URL изменится с 'about:blank'")
    def wait_url_until_not_about_blank(self, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))

    def switch_to_window(self, window_number: int = 1): #Переключиться на вкладку браузера.
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > window_number)
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    def wait_until_url_changes(self, expected_url='about:blank', timeout=10): #Ждать, пока URL изменится с указанного (по умолчанию 'about:blank').
        WebDriverWait(self.driver, timeout).until_not(EC.url_to_be(expected_url))
