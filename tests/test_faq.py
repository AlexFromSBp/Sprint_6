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
        wait = WebDriverWait(driver, 10)
        faq_questions = wait.until(EC.presence_of_all_elements_located(YandexScooterHomePageLocator.faq_question_buttons_locator))
        # Кликаем по нужному вопросу
        driver.execute_script("arguments[0].scrollIntoView(true);", faq_questions[question])

        wait.until(EC.element_to_be_clickable(faq_questions[question])).click()
        faq_answers = wait.until(EC.presence_of_all_elements_located(YandexScooterHomePageLocator.faq_answer_paragraphs_locator))

        wait.until(EC.visibility_of(faq_answers[answer]))

        # Убираем лишние пробелы, переносы строк
        actual_answer = faq_answers[answer].text.strip()

        assert actual_answer == expected_answer, \
            f'Ответ на вопрос не совпадает. Ожидали: "{expected_answer}", получили: "{actual_answer}"'
