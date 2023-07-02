import time
from enum import Enum

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ProjectQuestionnairePage:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.browser.get("https://only.digital/projects#brief")
        self.browser.set_page_load_timeout(10)

    def scroll_and_input_name(self, name):
        el = self.browser.find_element(Selectors.NAME_FIELD.value)
        self.scroll_to_element(el)
        el.send_keys(name)

    def scroll_and_input_email(self, email):
        el = self.browser.find_element(Selectors.EMAIL_FIELD.value)
        self.scroll_to_element(el)
        el.send_keys(email)

    def scroll_and_input_phone_number(self, phone_number):
        el = self.browser.find_element(Selectors.PHONE_FIELD.value)
        self.scroll_to_element(el)
        el.send_keys(phone_number)

    def scroll_and_click_complex_of_works(self):
        el = self.browser.find_element(Selectors.COMPLEX_OF_WORKS.value)
        self.scroll_to_element(el)
        el.click()

    def scroll_and_click_budget_less_two_millions(self):
        el = self.browser.find_element(Selectors.BUDGET_LESS_TWO_MILLIONS.value)
        self.scroll_to_element(el)
        el.click()

    def scroll_and_click_captcha(self):
        el = self.browser.find_element(Selectors.CAPTCHA.value)
        self.scroll_to_element(el)
        el.click()

    def scroll_and_click_ratings_button(self):
        el = self.browser.find_element(Selectors.RATINGS_BUTTON.value)
        self.scroll_to_element(el)
        el.click()

    def scroll_and_click_send_button(self):
        el = self.browser.find_element(Selectors.SEND_BUTTON.value)
        self.scroll_to_element(el)
        el.click()

    def get_text_success_message(self):
        el = self.browser.find_element(Selectors.SUCCESS_MESSAGE.value)
        return el.text

    def scroll_to_element(self, element):
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()

    def is_page_title_displayed(self):
        el = self.browser.find_element(Selectors.PAGE_TITLE.value)
        if not el.is_displayed():
            time.sleep(5)
            self.browser.refresh()

    def get_name_error_message(self):
        return self.browser.find_element(Selectors.NAME_ERROR_MESSAGE.value).text

    def get_email_error_message(self):
        return self.browser.find_element(Selectors.EMAIL_ERROR_MESSAGE.value).text

    def get_phone_error_message(self):
        return self.browser.find_element(Selectors.PHONE_ERROR_MESSAGE.value).text

    def get_budget_error_message(self):
        return self.browser.find_element(Selectors.BUDGET_MANDATORY_ERROR_MESSAGE.value).text

    def get_information_source_error_message(self):
        return self.browser.find_element(Selectors.INFORMATION_SOURCE_MANDATORY_ERROR_MESSAGE.value).text


class Selectors(Enum):
    NAME_FIELD = (By.CSS_SELECTOR, "input[name=\"name\"]")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name=\"email\"]")
    PHONE_FIELD = (By.CSS_SELECTOR, "input[name=\"phone\"]")
    COMPLEX_OF_WORKS = (By.CSS_SELECTOR,
                        "div#__next div:nth-child(2) > div.eNvGYA > label:nth-child(1) > span")
    BUDGET_LESS_TWO_MILLIONS = (By.CSS_SELECTOR,
                                "div#__next div:nth-child(3) > div > label:nth-child(1) > span")
    CAPTCHA = (By.CSS_SELECTOR,
               "div#__next div:nth-child(3) > div > label:nth-child(1) > span")
    RATINGS_BUTTON = (By.CSS_SELECTOR,
                      "div#__next div:nth-child(4) > div > label:nth-child(1) > span")
    SEND_BUTTON = (By.CSS_SELECTOR, "div#__next div.lgfktX > button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,
                       "div#__next div:nth-child(4) > div > label:nth-child(1) > span")
    PAGE_TITLE = (By.CSS_SELECTOR, "div#__next h1")
    NAME_ERROR_MESSAGE = (By.CSS_SELECTOR, "div#__next form > div:nth-child(1) > div > div:nth-child(1) > p")
    EMAIL_ERROR_MESSAGE = (By.CSS_SELECTOR, "div#__next div:nth-child(1) > div > div:nth-child(2) > p")
    PHONE_ERROR_MESSAGE = (By.CSS_SELECTOR, "div#__next div > div:nth-child(3) > p")
    BUDGET_MANDATORY_ERROR_MESSAGE = (By.CSS_SELECTOR, "div#__next form > div:nth-child(3) > p.sc-cebffa9c-3.cCKpas")
    INFORMATION_SOURCE_MANDATORY_ERROR_MESSAGE = (By.CSS_SELECTOR,
                                                  "div#__next div:nth-child(4) > p.sc-cebffa9c-3.cCKpas")
