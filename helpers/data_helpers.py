import random
import string

class DataHelper:
    @staticmethod
    def generate_email():
        domains = ["ya.ru", "mail.ru", "gmail.com", "yandex.ru"]
        login = str(random.randint(100000, 999999))
        domain = random.choice(domains)
        return f"{login}@{domain}"

    @staticmethod
    def generate_password(length=6):
        characters = string.ascii_letters + string.digits
        return "".join(random.choice(characters) for _ in range(length))
