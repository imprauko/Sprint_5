from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.all_locators import (
    MainPageLocators,
    ProfilePageLocators,
    ConstructorPageLocators
)
from test_data.test_data import (
    Urls,
)
class TestTranspasses:

    def test_to_profile_page_transpass(self, setup_logged_in):
        driver = setup_logged_in
        driver.find_element(*MainPageLocators.BUTTON_ACCOUNT_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((ProfilePageLocators.BUTTON_LOGOUT))
            )

        assert driver.current_url == Urls.profile

    def test_to_constructor_from_profile_transpass_by_button(self, setup_logged_in):
        driver = setup_logged_in
        driver.find_element(*MainPageLocators.BUTTON_ACCOUNT_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (ProfilePageLocators.BUTTON_LOGOUT))
        )
        driver.find_element(*MainPageLocators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((ConstructorPageLocators.HEADER_CONSTRUCTOR))
            )

        text = driver.find_element(*ConstructorPageLocators.HEADER_CONSTRUCTOR).text
        assert "Соберите бургер" in text

    def test_to_constructor_from_profile_transpass_by_logo(self, setup_logged_in):
        driver = setup_logged_in
        driver.find_element(*MainPageLocators.BUTTON_ACCOUNT_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (ProfilePageLocators.BUTTON_LOGOUT))
        )

        driver.find_element(*MainPageLocators.BUTTON_STELLAR_BURGERS).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((ConstructorPageLocators.HEADER_CONSTRUCTOR))
            )

        text = driver.find_element(*ConstructorPageLocators.HEADER_CONSTRUCTOR).text
        assert "Соберите бургер" in text
    
    def test_to_sauces_from_buns(self, setup_logged_in):
        driver = setup_logged_in
# кликаем на кнопку соусы
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (ConstructorPageLocators.BUTTON_SAUCES))).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(
                (ConstructorPageLocators.HEADER_SAUCES)))
# ловим заголовок блока соусов в скролле
        sauces_block = driver.find_element(*ConstructorPageLocators.HEADER_SAUCES)
# ловим кнопку соусов
        button = driver.find_element(*ConstructorPageLocators.BUTTON_SAUCES)
# определяем класс кнопки соусов
        button_class = button.get_attribute("class")
# проверяем, что кнопка стала активной и что скролл прокрутился на соусы
        assert "tab_tab_type_current" in button_class
        assert sauces_block.is_displayed()

    def test_to_fillings_from_buns(self, setup_logged_in):
        driver = setup_logged_in
        # кликаем на начинки
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (ConstructorPageLocators.BUTTON_FILLINGS))
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (ConstructorPageLocators.HEADER_FILLINGS))
        )
        # ловим заголовок блока начинок в скролле
        fillings_block = driver.find_element(*ConstructorPageLocators.HEADER_FILLINGS)
        # ловим кнопку начинок
        button = driver.find_element(*ConstructorPageLocators.BUTTON_FILLINGS)
        # определяем класс кнопки соусов
        button_class = button.get_attribute("class")
        # проверяем, что кнопка стала активной и что скролл прокрутился на начинки
        assert "tab_tab_type_current" in button_class
        assert fillings_block.is_displayed()

    def test_to_buns_from_fillings(self, setup_logged_in):
        driver = setup_logged_in
        # кликаем на начинки
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (ConstructorPageLocators.BUTTON_FILLINGS))
        ).click()
        # кликаем обратно на булки
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(
                (ConstructorPageLocators.BUTTON_BUNS))
        ).click()
        # ловим заголовок блока булок в скролле
        buns_block = driver.find_element(*ConstructorPageLocators.HEADER_BUNS)
        # ловим кнопку булок
        button = driver.find_element(*ConstructorPageLocators.BUTTON_BUNS)
        # определяем класс булок
        button_class = button.get_attribute("class")
        # проверяем, что кнопка стала активной и что скролл прокрутился на булки
        assert "tab_tab_type_current" in button_class
        assert buns_block.is_displayed()