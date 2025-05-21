import pytest
import selenium
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators.all_locators import (
    LoginPageLocators,
    ProfilePageLocators
)
from test_data.test_data import (
    UserData,
    Urls
)

login_page_locators = LoginPageLocators()
profile_page_locators = ProfilePageLocators()

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def setup_logged_in():
    driver = webdriver.Chrome()
    driver.get(Urls.login)

    driver.find_element(*LoginPageLocators.INPUT_LOGIN).send_keys(UserData.email)
    driver.find_element(*LoginPageLocators.INPUT_LOGIN_PASSWORD).send_keys(UserData.password)
    driver.find_element(*LoginPageLocators.BUTTON_LOGIN).click()

    yield driver

    try:
        driver.get(Urls.profile)
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((
            ProfilePageLocators.BUTTON_LOGOUT))).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((LoginPageLocators.HEADER_LOGIN_PAGE))
        )
        driver.quit()
    except TimeoutException:
        driver.quit()
    driver.quit()