import pytest
import allure
from pages.home_page import YandexScooterHomePage
from helper.test_data import YandexScooterHomePageFAQ
from helper.locators import YandexScooterHomePageLocator


@allure.epic('Эпик_Upgrade Main page / ui usability')
@allure.parent_suite('Parent_suite_Домашняя страница')
@allure.suite('Suite_FAQ')
class TestYandexScooterFAQPage:
    @allure.feature('Фича_Аккордион с вопрос/ответ на Домашней страницы')
    @allure.story('Стори_При нажатии на вопрос в разделе "Вопросы о важном" раскрывается ответ.')
    @allure.title('При нажатии на вопрос раскрывается ответ ')
    @allure.description('Проверка что при нажатии на поле вопроса в блоке "Вопросы о важном", '
                        'данный вопрос раскрывается и текст в нем соответствует ТЗ')
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
    def test_faq_click_first_question_show_answer(self, driver, question, answer, expected_answer):
        yandex_scooter_home_page = YandexScooterHomePage(driver)
        yandex_scooter_home_page.go_to_site()
        yandex_scooter_home_page.click_cookie_accept()
        yandex_scooter_home_page.click_faq_question(question_number=question)
        answer = ya_scooter_home_page.find_element(YandexScooterHomePageLocator.faq_answer_paragraphs_locator(answer_number=answer))

        assert answer.is_displayed() and answer.text == expected_answer, 'Ответ на вопрос не совпадает с ожидаемым значением '