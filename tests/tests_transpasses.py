import selenium
import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestToProfilePageTranspass:
    def test_to_profile_page_transpass(self, setup_logged_in):
        driver = setup_logged_in
        driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button"))
            )

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    def test_to_constructor_from_profile_transpass_by_button(self, setup_logged_in):
        driver = setup_logged_in
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")

        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button"))
        )
        driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='root']/div/main/section[1]/h1"))
            )

        text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/h1").text
        assert "Соберите бургер" in text

    def test_to_constructor_from_profile_transpass_by_logo(self, setup_logged_in):
        driver = setup_logged_in
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")

        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button"))
        )
        driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/div/a/svg").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='root']/div/main/section[1]/h1"))
            )

        text = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/h1").text
        assert "Соберите бургер" in text

    def test_logout(self, setup_logged_in):
        driver = setup_logged_in
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")

        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button"))
        ).click()

        element = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/h2")
        assert "Вход" in element.text
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_to_sauces_from_buns(self, setup_logged_in):
        driver = setup_logged_in
        driver.get("https://stellarburgers.nomoreparties.site")

        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]/span"))).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]/span")))

        visible_block = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/h2[2]")
        button = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]/span")
        button_class = button.get_attribute("class")

        assert "2BEPc" in button_class
        assert visible_block.is_displayed()

    def test_to_fillings_from_buns(self, setup_logged_in):
        driver = setup_logged_in
        driver.get("https://stellarburgers.nomoreparties.site")

        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]/span"))
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/h2[3]"))
        )

        visible_block = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/h2[3]")
        button = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]/span")
        button_class = button.get_attribute("class")

        assert "2BEPc" in button_class
        assert visible_block.is_displayed()

    def test_to_buns_from_fillings(self, setup_logged_in):
        driver = setup_logged_in
        driver.get("https://stellarburgers.nomoreparties.site")

        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]/span"))
        ).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]/span"))
        ).click()

        visible_block = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/h2[1]")
        button = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]/span")
        button_class = button.get_attribute("class")

        assert "2BEPc" in button_class
        assert visible_block.is_displayed()