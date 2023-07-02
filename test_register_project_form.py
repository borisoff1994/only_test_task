import time

import pytest

from project_page import ProjectQuestionnairePage


@pytest.mark.usefixtures("browser")
def test_fill_out_form__positive(browser):
    # Data
    name = "Test"
    email = "test_autotest@exmple.com"
    phone_number = "1234567890"
    expected_success_message = "Заявка успешно отправлена"

    # Arrange
    page = ProjectQuestionnairePage(browser)
    page.is_page_title_displayed()

    # Act
    page.scroll_and_input_name(name)
    page.scroll_and_input_email(email)
    page.scroll_and_input_phone_number(phone_number)
    page.scroll_and_click_complex_of_works()
    page.scroll_and_click_budget_less_two_millions()
    page.scroll_and_click_ratings_button()
    page.scroll_and_click_captcha()
    page.scroll_and_click_send_button()

    time.sleep(2)

    actual_success_message = page.get_text_success_message()

    # Assert
    assert actual_success_message.text == expected_success_message


@pytest.mark.usefixtures("browser")
def test_fill_out_form__negative(browser):
    # Data
    mandatory_error_message = "Обязательное поле"

    # Arrange
    page = ProjectQuestionnairePage(browser)
    page.is_page_title_displayed()

    # Act
    page.scroll_and_click_captcha()
    page.scroll_and_click_send_button()

    mandatory_name_error_message = page.get_name_error_message()
    mandatory_email_error_message = page.get_email_error_message()
    mandatory_phone_error_message = page.get_phone_error_message()
    mandatory_budget_error_message = page.get_budget_error_message()
    mandatory_information_source_error_message = page.get_information_source_error_message()

    # Assert
    assert mandatory_name_error_message == mandatory_error_message
    assert mandatory_email_error_message == mandatory_error_message
    assert mandatory_phone_error_message == mandatory_error_message
    assert mandatory_budget_error_message == mandatory_error_message
    assert mandatory_information_source_error_message == mandatory_error_message


@pytest.mark.usefixtures("browser")
@pytest.mark.parametrize("name_value", "email_value", "phone_value",
                         [
                             (1, "a1&", 123456789),
                             ("&", 123456, 1)
                         ])
def test_check_validation_message__field_name(browser, name_value, email_value, phone_value):
    # Data
    expected_validation_error_message = "Неверный формат"

    # Arrange
    page = ProjectQuestionnairePage(browser)
    page.is_page_title_displayed()

    # Act
    page.scroll_and_input_name(name_value)
    page.scroll_and_input_email(email_value)
    page.scroll_and_input_phone_number(phone_value)

    actual_validation_name_error_message = page.get_name_error_message()
    actual_validation_email_error_message = page.get_email_error_message()
    actual_validation_phone_error_message = page.get_phone_error_message()

    # Assert
    assert expected_validation_error_message == actual_validation_name_error_message
    assert actual_validation_email_error_message == actual_validation_name_error_message
    assert actual_validation_phone_error_message == actual_validation_name_error_message


