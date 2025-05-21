import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers.data_helpers import DataHelper
from locators.all_locators import (
    MainPageLocators,
    LoginPageLocators,
    RegistrationPageLocators,
    ProfilePageLocators
)
from test_data.test_data import (
    Urls,
)

class TestRegistration:
    def test_valid_registration(self, setup):
        email = DataHelper.generate_email()
        password = DataHelper.generate_password(length=6)

        driver = setup
        driver.get(Urls.register)
        driver.find_element(*RegistrationPageLocators.INPUT_NAME).send_keys("testuser")
        driver.find_element(*RegistrationPageLocators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*RegistrationPageLocators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*RegistrationPageLocators.BUTTON_REGISTER).click()
        time.sleep(0.2)
        login_input = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((LoginPageLocators.INPUT_LOGIN))
        )

        login_input.send_keys(email)

        driver.find_element(*LoginPageLocators.INPUT_LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*LoginPageLocators.BUTTON_LOGIN).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((MainPageLocators.BUTTON_ACCOUNT_MAIN_PAGE))).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((ProfilePageLocators.BUTTON_LOGOUT)))

        assert driver.current_url == Urls.profile

    def test_registration_password_error(self, setup):
        email = DataHelper.generate_email()

        driver = setup
        driver.get(Urls.register)
        driver.find_element(*RegistrationPageLocators.INPUT_NAME).send_keys(
            "testuser")
        driver.find_element(*RegistrationPageLocators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*RegistrationPageLocators.INPUT_PASSWORD).send_keys("abc")
        driver.find_element(*RegistrationPageLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 3)
        error_message = driver.find_element(*LoginPageLocators.ERROR_HEADER).text
        assert "Некорректный пароль" in error_message

    def test_logout(self, setup_logged_in):
        driver = setup_logged_in
        driver.find_element(*MainPageLocators.BUTTON_ACCOUNT_MAIN_PAGE).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((ProfilePageLocators.BUTTON_LOGOUT))).click()
        login_header = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((LoginPageLocators.HEADER_LOGIN_PAGE)))
        assert "Вход" in login_header.text
        assert driver.current_url == Urls.login