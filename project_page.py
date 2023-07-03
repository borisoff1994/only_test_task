from enum import Enum

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProjectQuestionnairePage:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.browser.get("https://only.digital/projects#brief")

    def scroll_and_input_name(self, name):
        """
        Скроллим к полю "Имя" и вписываем значение
        """
        el = self.browser.find_element(*Selectors.NAME_FIELD.value)
        self.scroll_to_element(el)
        el.send_keys(name)

    def scroll_and_input_email(self, email):
        """
        Скроллим к полю "E-mail" и вписываем значение
        """
        el = self.browser.find_element(*Selectors.EMAIL_FIELD.value)
        self.scroll_to_element(el)
        el.send_keys(email)

    def scroll_and_input_phone_number(self, phone_number):
        """
        Скроллим к полю "Телефон" и вписываем значение
        """
        el = self.browser.find_element(*Selectors.PHONE_FIELD.value)
        self.scroll_to_element(el)
        el.send_keys(phone_number)

    def scroll_and_click_complex_of_works(self):
        """
        Скроллим к полю "О проекте"
        Кликаем "Комплекс работ"
        """
        el = self.browser.find_element(*Selectors.COMPLEX_OF_WORKS.value)
        self.scroll_to_element(el)
        el.click()

    def scroll_and_click_budget_less_two_millions(self):
        """
        Скроллим к полю "Бюджет"
        Кликаем "Меньше 2-ух миллионов"
        """
        el = self.browser.find_element(*Selectors.BUDGET_LESS_TWO_MILLIONS.value)
        self.scroll_to_element(el)
        el.click()

    def scroll_and_click_captcha(self):
        """
        Скроллим к чекбоксу "reCaptcha"
        Ждем, пока он станет кликабельным
        Кликаем чекбокс "reCaptcha"
        """
        el = self.browser.find_element(*Selectors.CAPTCHA.value)
        self.scroll_to_element(el)
        self.wait_until_clickable(*Selectors.CAPTCHA.value)
        el.click()

    def scroll_and_click_ratings_button(self):
        """
        Скроллим к полю "Откуда вы узнали о нас?"
        Кликаем "Рейтинги"
        """
        el = self.browser.find_element(*Selectors.RATINGS_BUTTON.value)
        self.scroll_to_element(el)
        el.click()

    def scroll_and_click_send_button(self):
        """
        Скроллим и кликаем кнопку "Отправить"
        """
        el = self.browser.find_element(*Selectors.SEND_BUTTON.value)
        self.scroll_to_element(el)
        el.click()

    def get_text_success_message(self):
        """
        Получаем текст формы успешной отправки
        """
        el = self.browser.find_element(*Selectors.SUCCESS_MESSAGE.value)
        return el.text

    def scroll_to_element(self, element):
        """
        Скроллим к веб-элементу
        """
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()

    def is_page_title_displayed(self):
        """
        Проверяем отображение заголовка анкеты
        """
        el = self.browser.find_element(*Selectors.PAGE_TITLE.value)
        el.is_displayed()

    def get_name_error_message(self):
        """
        Получаем текст ошибки поля "Имя"
        """
        return self.browser.find_element(*Selectors.NAME_ERROR_MESSAGE.value).text

    def get_email_error_message(self):
        """
        Получаем текст ошибки поля "E-mail"
        """
        return self.browser.find_element(*Selectors.EMAIL_ERROR_MESSAGE.value).text

    def get_phone_error_message(self):
        """
        Получаем текст ошибки поля "Телефон"
        """
        return self.browser.find_element(*Selectors.PHONE_ERROR_MESSAGE.value).text

    def get_budget_error_message(self):
        """
        Получаем текст ошибки поля "Бюджет"
        """
        return self.browser.find_element(*Selectors.BUDGET_MANDATORY_ERROR_MESSAGE.value).text

    def get_information_source_error_message(self):
        """
        Получаем текст ошибки поля "Откуда вы узнали о нас?"
        """
        return self.browser.find_element(*Selectors.INFORMATION_SOURCE_MANDATORY_ERROR_MESSAGE.value).text

    def wait_until_clickable(self, timeout=20, *locator):
        """
        Ожидаем, пока элемент по локатору станет кликабельным
        """
        WebDriverWait(self.browser, timeout=timeout).until(EC.element_to_be_clickable(*locator))


class Selectors(Enum):
    BUDGET_LESS_TWO_MILLIONS = (By.CSS_SELECTOR,
                                "div#__next div:nth-child(3) > div > label:nth-child(1) > span")
    BUDGET_MANDATORY_ERROR_MESSAGE = (By.CSS_SELECTOR, "div#__next form > div:nth-child(3) > p.sc-cebffa9c-3.cCKpas")
    CAPTCHA = (By.CSS_SELECTOR,
               "div#__next div:nth-child(3) > div > label:nth-child(1) > span")
    COMPLEX_OF_WORKS = (By.CSS_SELECTOR,
                        "div#__next div:nth-child(2) > div.eNvGYA > label:nth-child(1) > span")
    EMAIL_ERROR_MESSAGE = (By.CSS_SELECTOR, "div#__next div:nth-child(1) > div > div:nth-child(2) > p")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name=\"email\"]")
    INFORMATION_SOURCE_MANDATORY_ERROR_MESSAGE = (By.CSS_SELECTOR,
                                                  "div#__next div:nth-child(4) > p.sc-cebffa9c-3.cCKpas")
    NAME_ERROR_MESSAGE = (By.CSS_SELECTOR, "div#__next form > div:nth-child(1) > div > div:nth-child(1) > p")
    NAME_FIELD = (By.CSS_SELECTOR, "input[name=\"name\"]")
    PAGE_TITLE = (By.CSS_SELECTOR, "div#__next h1")
    PHONE_ERROR_MESSAGE = (By.CSS_SELECTOR, "div#__next div > div:nth-child(3) > p")
    PHONE_FIELD = (By.CSS_SELECTOR, "input[name=\"phone\"]")
    RATINGS_BUTTON = (By.CSS_SELECTOR,
                      "div#__next div:nth-child(4) > div > label:nth-child(1) > span")
    SEND_BUTTON = (By.CSS_SELECTOR, "div#__next div.lgfktX > button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,
                       "div#__next div:nth-child(4) > div > label:nth-child(1) > span")
