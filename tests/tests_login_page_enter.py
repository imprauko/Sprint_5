from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.all_locators import (
    MainPageLocators,
    LoginPageLocators,
    RegistrationPageLocators
)
from test_data.test_data import (
    Urls,
)

class TestToLoginPageTranspass:
    def test_enter_account_button(self, setup):
        driver = setup
        driver.get(Urls.site)
        driver.find_element(*MainPageLocators.BUTTON_ENTER_ACC_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((LoginPageLocators.HEADER_LOGIN_PAGE)))

        element = driver.find_element(*LoginPageLocators.HEADER_LOGIN_PAGE)
        assert "Вход" in element.text
        assert driver.current_url == Urls.login


    def test_enter_cabinet_button(self, setup):
        driver = setup
        driver.get(Urls.site)
        driver.find_element(*MainPageLocators.BUTTON_ACCOUNT_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((LoginPageLocators.HEADER_LOGIN_PAGE))
            )

        element = driver.find_element(*LoginPageLocators.HEADER_LOGIN_PAGE)
        assert "Вход" in element.text
        assert driver.current_url == Urls.login

    def test_enter_button_in_registration_form(self, setup):
        driver = setup
        driver.get(Urls.register)
        driver.find_element(*RegistrationPageLocators.BUTTON_ENTER_REG_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((LoginPageLocators.HEADER_LOGIN_PAGE))
            )

        element = driver.find_element(*LoginPageLocators.HEADER_LOGIN_PAGE)
        assert "Вход" in element.text
        assert driver.current_url == Urls.login

    def test_enter_button_in_recovery_form(self, setup):
        driver = setup
        driver.get(Urls.forgot_password)
        driver.find_element(*RegistrationPageLocators.BUTTON_ENTER_REG_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((LoginPageLocators.HEADER_LOGIN_PAGE))
            )

        element = driver.find_element(*LoginPageLocators.HEADER_LOGIN_PAGE)
        assert "Вход" in element.text
        assert driver.current_url == Urls.login