from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    INPUT_NAME = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')  # Поле "Имя"
    INPUT_EMAIL = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')  # Поле "Email"
    INPUT_PASSWORD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')  # Поле "Пароль"
    BUTTON_REGISTER = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')  # Кнопка "Зарегистрироваться"
    BUTTON_ENTER_REG_PAGE = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a') # Кнопка "Войти" (из формы регистрации)

class LoginPageLocators:
    INPUT_LOGIN = (By.XPATH, '//div/input[@name="name"]')  # Поле логина
    INPUT_LOGIN_PASSWORD = (By.XPATH, '//div/input[@name="Пароль"]')  # Поле пароля
    BUTTON_LOGIN = (By.XPATH, '//button[text()="Войти"]')  # Кнопка "Войти"
    HEADER_LOGIN_PAGE = (By.XPATH, '//h2[text()="Вход"]')  # Заголовок "Вход"
    ERROR_HEADER = (By.XPATH, '//p[text()="Некорректный пароль"]')  # Ошибка "Некорректный пароль"
    BUTTON_ENTER_RECOVERY_PAGE = (By.XPATH, '//a[@href="/login"]')  # Кнопка "Войти" на странице восстановления

class MainPageLocators:
    BUTTON_ENTER_ACC_MAIN_PAGE = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # "Войти в аккаунт"
    BUTTON_ACCOUNT_MAIN_PAGE = (By.XPATH, '//a[@href="/account"]')  # "Личный кабинет"
    BUTTON_CONSTRUCTOR = (By.XPATH, '//a[.//p[text()="Конструктор"]]')  # Кнопка "Конструктор"
    BUTTON_STELLAR_BURGERS = (By.XPATH, '//div/a[@href="/"]')  # Кнопка "Stellar Burgers"

class ProfilePageLocators:
    BUTTON_LOGOUT = (By.XPATH, '//button[text()="Выход"]')  # Кнопка "Выход"


class ConstructorPageLocators:
    HEADER_CONSTRUCTOR = (By.XPATH, '//h1[text()="Соберите бургер"]')  # Заголовок "Соберите бургер"

    BUTTON_BUNS = (By.XPATH, '//div[1][contains(@class, "tab_tab__1SPyG")]')  # Кнопка "Булки"
    HEADER_BUNS = (By.XPATH, '//h2[text()="Булки"]')  # Заголовок "Булки" в скролле

    BUTTON_SAUCES = (By.XPATH, '//div[2][contains(@class, "tab_tab__1SPyG")]')  # Кнопка "Соусы"
    HEADER_SAUCES = (By.XPATH, '//h2[text()="Соусы"]')  # Заголовок "Соусы" в скролле

    BUTTON_FILLINGS = (By.XPATH, '//div[3][contains(@class, "tab_tab__1SPyG")]')  # Кнопка "Начинки"
    HEADER_FILLINGS = (By.XPATH, '//h2[text()="Начинки"]')  # Заголовок "Начинки" в скролле