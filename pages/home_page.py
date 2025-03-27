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
        questions = self.find_elements(Locators.faq_question_buttons_locator, 10)
        self.scroll_to_element(questions[question_number])
        self.wait_for_element_to_be_clickable(questions[question_number]).click()

    @allure.step('Получить текст ответа в FAQ')
    def get_faq_answer_text(self, answer_number: int):
        answers = self.find_elements(Locators.faq_answer_paragraphs_locator)
        self.wait_for_element_to_be_visible(answers[answer_number])
        return answers[answer_number].text.strip()

    @allure.step('Переключиться на вкладку браузера')
    def switch_window(self, window_number: int = 1):
        return self.switch_to_window(window_number)

    @allure.step('Ожидать смены URL') #        """Используем метод из BasePage."""
    def wait_url_until_not_about_blank(self, time=10):
        return self.wait_until_url_changes(timeout=time)

    @allure.step('Перейти на страницу яндекса')
    def click_yandex_button(self):
        return self.find_element(BasePageLocator.yandex_logo_link_locator).click()

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        return self.find_element(BasePageLocator.accept_cookies_button_locator).click()
