import pytest
import allure
from pages.home_page import YandexScooterHomePage
from helper.test_data import YandexScooterHomePageFAQ
from helper.locators import YandexScooterHomePageLocator

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
    @allure.title('Проверка ответов блока "Вопросы о важном".')
    @allure.description('Тап "Вопросы о важном" раскрывает ответ')

    def test_faq_click_question_show_answer(self, driver, question, answer, expected_answer):
        yandex_scooter_home_page = YandexScooterHomePage(driver)
        yandex_scooter_home_page.go_to_site()
        yandex_scooter_home_page.click_faq_question(question_number=question)
        answer = yandex_scooter_home_page.find_element(YandexScooterHomePageLocator.faq_answer_paragraphs_locator(answer_number=answer))

        assert answer.is_displayed() and answer.text == expected_answer, 'Ответ не совпадает с ожидаемым'
