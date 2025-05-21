import pytest
import selenium
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

INPUT_LOGIN = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
INPUT_LOGIN_PASSWORD = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'
BUTTON_LOGIN = '//*[@id="root"]/div/main/div/form/button'
BUTTON_LOGOUT = '//*[@id="root"]/div/main/div/nav/ul/li[3]/button'
HEADER_LOGIN_PAGE = '//*[@id="root"]/div/main/div/h2'

@pytest.fixture(scope="function")
def setup_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def setup_main_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def setup_logged_in():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(By.XPATH, INPUT_LOGIN).send_keys(
        'konstantin_novitskii_22_222@mail.ru')
    driver.find_element(By.XPATH, INPUT_LOGIN_PASSWORD).send_keys(
        'qwerty')
    driver.find_element(By.XPATH, BUTTON_LOGIN).click()

    yield driver

    try:
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((
            By.XPATH, BUTTON_LOGOUT))).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, HEADER_LOGIN_PAGE))
        )
        driver.quit()
    except TimeoutException:
        driver.quit()
    driver.quit()