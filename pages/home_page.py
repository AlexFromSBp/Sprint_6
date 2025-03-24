import allure
from pages.base_page import BasePage
from helper.locators import BasePageLocator
from selenium.webdriver.support.wait import WebDriverWait
from helper.locators import YandexScooterHomePageLocator as Locators
from selenium.webdriver.support import expected_conditions as EC


class YandexScooterHomePage(BasePage):

    @allure.step('Нажать на кнопку заказа вверху страницы')
    def click_top_order_button(self):
        return self.find_element(Locators.top_order_button_locator).click()

    @allure.step('Нажать на кнопку заказа внизу страницы')
    def click_bottom_order_button(self):
        return self.find_element(Locators.bottom_order_button_locator).click()

    @allure.step('Нажать на вопрос в FAQ')
    def click_faq_question(self, question_number: int):
        question = self.find_elements(Locators.faq_question_buttons_locator, 10)
        return question[question_number].click()

    @allure.step('Переключиться на вкладку браузера')
    def switch_window(self, window_number: int = 1):
        return self.driver.switch_to.window(self.driver.window_handles[window_number])

    def wait_url_until_not_about_blank(self, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))

    @allure.step('Перейти на страницу яндекса')
    def click_yandex_button(self):
        return self.find_element(BasePageLocator.yandex_logo_link_locator).click()

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        return self.find_element(BasePageLocator.accept_cookies_button_locator).click()
