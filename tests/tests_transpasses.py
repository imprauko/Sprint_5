import selenium
import pytest
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestTranspasses:
    
    BUTTON_ACCOUNT_MAIN_PAGE = '//*[@id="root"]/div/header/nav/a'
    BUTTON_LOGOUT = '//*[@id="root"]/div/main/div/nav/ul/li[3]/button'
    BUTTON_CONSTRUCTOR = '//*[@id="root"]/div/header/nav/ul/li[1]/a'
    HEADER_CONSTRUCTOR = '//*[@id="root"]/div/main/section[1]/h1'
    BUTTON_STELLAR_BURGERS = '//*[@id="root"]/div/header/nav/div/a'
    BUTTON_SAUCES = '//*[@id="root"]/div/main/section[1]/div[1]/div[2]'
    BUTTON_FILLINGS = '//*[@id="root"]/div/main/section[1]/div[1]/div[3]'
    HEADER_SAUCES = '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]'
    HEADER_FILLINGS = '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]'
    BUTTON_BUNS = '//*[@id="root"]/div/main/section[1]/div[1]/div[1]'
    
    def test_to_profile_page_transpass(self, setup_logged_in):
        driver = setup_logged_in
        driver.find_element(By.XPATH, self.BUTTON_ACCOUNT_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.BUTTON_LOGOUT))
            )

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    def test_to_constructor_from_profile_transpass_by_button(self, setup_logged_in):
        driver = setup_logged_in
        driver.find_element(By.XPATH, self.BUTTON_ACCOUNT_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.BUTTON_LOGOUT))
        )
        driver.find_element(By.XPATH, self.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.HEADER_CONSTRUCTOR))
            )

        text = driver.find_element(By.XPATH, self.HEADER_CONSTRUCTOR).text
        assert "Соберите бургер" in text

    def test_to_constructor_from_profile_transpass_by_logo(self, setup_logged_in):
        driver = setup_logged_in
        driver.find_element(By.XPATH, self.BUTTON_ACCOUNT_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.BUTTON_LOGOUT))
        )

        driver.find_element(By.XPATH, self.BUTTON_STELLAR_BURGERS).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.HEADER_CONSTRUCTOR))
            )

        text = driver.find_element(By.XPATH, self.HEADER_CONSTRUCTOR).text
        assert "Соберите бургер" in text
    
    def test_to_sauces_from_buns(self, setup_logged_in):
        driver = setup_logged_in

        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.BUTTON_SAUCES))).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.BUTTON_SAUCES)))

        visible_block = driver.find_element(By.XPATH, self.HEADER_SAUCES)
        button = driver.find_element(By.XPATH, self.BUTTON_SAUCES)
        button_class = button.get_attribute("class")

        assert "2BEPc" in button_class
        assert visible_block.is_displayed()

    def test_to_fillings_from_buns(self, setup_logged_in):
        driver = setup_logged_in

        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.BUTTON_FILLINGS))
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, self.HEADER_FILLINGS))
        )

        visible_block = driver.find_element(By.XPATH, self.HEADER_FILLINGS)
        button = driver.find_element(By.XPATH, self.BUTTON_FILLINGS)
        button_class = button.get_attribute("class")

        assert "2BEPc" in button_class
        assert visible_block.is_displayed()

    def test_to_buns_from_fillings(self, setup_logged_in):
        driver = setup_logged_in

        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.BUTTON_FILLINGS))
        ).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.BUTTON_BUNS))
        ).click()

        visible_block = driver.find_element(By.XPATH, self.BUTTON_BUNS)
        button = driver.find_element(By.XPATH, self.BUTTON_BUNS)
        button_class = button.get_attribute("class")

        assert "2BEPc" in button_class
        assert visible_block.is_displayed()