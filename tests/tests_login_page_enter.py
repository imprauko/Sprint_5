import selenium
import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestToLoginPageTranspass:

    BUTTON_ENTER_ACC_MAIN_PAGE = '//*[@id="root"]/div/main/section[2]/div/button'
    HEADER_LOGIN_PAGE = '//*[@id="root"]/div/main/div/h2'
    BUTTON_ACCOUNT_MAIN_PAGE = '//*[@id="root"]/div/header/nav/a'
    BUTTON_ENTER_REG_PAGE = '//*[@id="root"]/div/main/div/div/p/a'

    def test_enter_account_button(self, setup_main_page):
        driver = setup_main_page
        driver.find_element(By.XPATH, self.BUTTON_ENTER_ACC_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.HEADER_LOGIN_PAGE)))

        element = driver.find_element(By.XPATH, self.HEADER_LOGIN_PAGE)
        assert "Вход" in element.text
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


    def test_enter_cabinet_button(self, setup_main_page):
        driver = setup_main_page
        driver.find_element(By.XPATH, self.BUTTON_ACCOUNT_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.HEADER_LOGIN_PAGE))
            )

        element = driver.find_element(By.XPATH, self.HEADER_LOGIN_PAGE)
        assert "Вход" in element.text
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_enter_button_in_registration_form(self, setup_registration):
        driver = setup_registration
        driver.find_element(By.XPATH, self.BUTTON_ENTER_REG_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.HEADER_LOGIN_PAGE))
            )

        element = driver.find_element(By.XPATH, self.HEADER_LOGIN_PAGE)
        assert "Вход" in element.text
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_enter_button_in_recovery_form(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(By.XPATH, self.BUTTON_ENTER_REG_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.HEADER_LOGIN_PAGE))
            )

        element = driver.find_element(By.XPATH, self.HEADER_LOGIN_PAGE)
        assert "Вход" in element.text
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.quit()