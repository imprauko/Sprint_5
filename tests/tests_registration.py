import selenium
import pytest
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def generate_email():
    domains = ["ya.ru", "mail.ru", "gmail.com", "yandex.ru"]
    login = str(random.randint(100000, 999999))
    domain = random.choice(domains)
    return f"{login}@{domain}"

def generate_password(length=6):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))

class TestRegistration:
    INPUT_NAME = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
    INPUT_EMAIL = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'
    INPUT_PASSWORD = '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input'
    BUTTON_REGISTER = '//*[@id="root"]/div/main/div/form/button'
    BUTTON_LOGOUT = '//*[@id="root"]/div/main/div/nav/ul/li[3]/button'
    HEADER_LOGIN_PAGE = '//*[@id="root"]/div/main/div/h2'
    ERROR_HEADER = "//*[@id='root']/div/main/div/form/fieldset[3]/div/p"
    BUTTON_ACCOUNT_MAIN_PAGE = '//*[@id="root"]/div/header/nav/a' #проба
    INPUT_LOGIN = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
    INPUT_LOGIN_PASSWORD = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'
    BUTTON_LOGIN = '//*[@id="root"]/div/main/div/form/button'

    def test_valid_registration(self, setup_registration):
        email = generate_email()
        password = generate_password(length=6)

        driver = setup_registration
        driver.find_element(By.XPATH, self.INPUT_NAME).send_keys("testuser")
        driver.find_element(By.XPATH, self.INPUT_EMAIL).send_keys(email)
        driver.find_element(By.XPATH, self.INPUT_PASSWORD).send_keys(password)
        driver.find_element(By.XPATH, self.BUTTON_REGISTER).click()
        time.sleep(0.2)
        login_input = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.INPUT_LOGIN))
        )

        login_input.send_keys(email)

        driver.find_element(By.XPATH, self.INPUT_LOGIN_PASSWORD).send_keys(password)
        driver.find_element(By.XPATH, self.BUTTON_LOGIN).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.BUTTON_ACCOUNT_MAIN_PAGE))).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.BUTTON_LOGOUT)))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    def test_registration_password_error(self, setup_registration):
        email = generate_email()

        driver = setup_registration
        driver.find_element(By.XPATH, self.INPUT_NAME).send_keys(
            "testuser")
        driver.find_element(By.XPATH, self.INPUT_EMAIL).send_keys(email)
        driver.find_element(By.XPATH, self.INPUT_PASSWORD).send_keys("abc")
        driver.find_element(By.XPATH, self.BUTTON_REGISTER).click()
        WebDriverWait(driver, 3)
        error_message = driver.find_element(By.XPATH, self.ERROR_HEADER).text
        assert "Некорректный пароль" in error_message

    def test_logout(self, setup_logged_in):
        driver = setup_logged_in
        driver.find_element(By.XPATH, self.BUTTON_ACCOUNT_MAIN_PAGE).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.BUTTON_LOGOUT))).click()
        login_header = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.HEADER_LOGIN_PAGE)))
        assert "Вход" in login_header.text
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"