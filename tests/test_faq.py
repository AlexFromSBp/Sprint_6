import pytest
import allure
from pages.home_page import YandexScooterHomePage
from helper.test_data import YandexScooterHomePageFAQ
from helper.locators import YandexScooterHomePageLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestYandexScooterFAQPage:
    @pytest.mark.parametrize(
        "question,answer,expected_answer",
        [
            (0, 0, YandexScooterHomePageFAQ.answer1),
            (1, 1, YandexScooterHomePageFAQ.answer2),
            (2, 2, YandexScooterHomePageFAQ.answer3),
            (3, 3, YandexScooterHomePageFAQ.answer4),
            (4, 4, YandexScooterHomePageFAQ.answer5),
            (5, 5, YandexScooterHomePageFAQ.answer6),
            (6, 6, YandexScooterHomePageFAQ.answer7),
            (7, 7, YandexScooterHomePageFAQ.answer8),
        ]
    )

    @allure.description('Проверка: нажатие на вопрос раздела "Вопросы о важном", вызывает ответ из ТЗ')
    def test_faq_click_first_question_show_answer(self, driver, question, answer, expected_answer):
        yandex_scooter_home_page = YandexScooterHomePage(driver)
        yandex_scooter_home_page.go_to_site()
        yandex_scooter_home_page.click_faq_question(question)
        actual_answer = yandex_scooter_home_page.get_faq_answer_text(answer)

        assert actual_answer == expected_answer, \
            f'Ответ на вопрос не совпадает. Ожидали: "{expected_answer}", получили: "{actual_answer}"'
