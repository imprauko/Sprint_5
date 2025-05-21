from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    INPUT_NAME = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')  # Поле "Имя"
    INPUT_EMAIL = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')  # Поле "Email"
    INPUT_PASSWORD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')  # Поле "Пароль"
    BUTTON_REGISTER = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')  # Кнопка "Зарегистрироваться"
    BUTTON_ENTER_REG_PAGE = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a') # Кнопка "Войти" (из формы регистрации)

class LoginPageLocators:
    INPUT_LOGIN = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')  # Поле логина
    INPUT_LOGIN_PASSWORD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')  # Поле пароля
    BUTTON_LOGIN = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')  # Кнопка "Войти"
    HEADER_LOGIN_PAGE = (By.XPATH, '//*[@id="root"]/div/main/div/h2')  # Заголовок "Вход"
    ERROR_HEADER = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')  # Ошибка "Некорректный пароль"
    BUTTON_ENTER_RECOVERY_PAGE = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')  # Кнопка "Войти" на странице восстановления

class MainPageLocators:
    BUTTON_ENTER_ACC_MAIN_PAGE = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')  # "Войти в аккаунт"
    BUTTON_ACCOUNT_MAIN_PAGE = (By.XPATH, '//*[@id="root"]/div/header/nav/a')  # "Личный кабинет"
    BUTTON_CONSTRUCTOR = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a')  # Кнопка "Конструктор"
    BUTTON_STELLAR_BURGERS = (By.XPATH, '//*[@id="root"]/div/header/nav/div/a')  # Кнопка "Stellar Burgers"

class ProfilePageLocators:
    BUTTON_LOGOUT = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')  # Кнопка "Выйти"


class ConstructorPageLocators:
    HEADER_CONSTRUCTOR = (By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')  # Заголовок "Соберите бургер"

    BUTTON_BUNS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]')  # Кнопка "Булки"
    HEADER_BUNS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]')  # Заголовок "Булки"

    BUTTON_SAUCES = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]')  # Кнопка "Соусы"
    HEADER_SAUCES = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]')  # Заголовок "Соусы"

    BUTTON_FILLINGS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]')  # Кнопка "Начинки"
    HEADER_FILLINGS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]')  # Заголовок "Начинки"