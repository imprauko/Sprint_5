from dataclasses import dataclass


@dataclass
class UserData:
    email: str = "konstantin_novitskii_22_222@mail.ru"
    password: str = 'qwerty'

@dataclass
class Urls:
    register: str = "https://stellarburgers.nomoreparties.site/register"
    site: str = "https://stellarburgers.nomoreparties.site/"
    login: str = "https://stellarburgers.nomoreparties.site/login"
    profile: str = "https://stellarburgers.nomoreparties.site/account/profile"
    forgot_password: str = "https://stellarburgers.nomoreparties.site/forgot-password"
