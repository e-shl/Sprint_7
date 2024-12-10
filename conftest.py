import random
import string

import pytest

from pages.courier_api import CourierPage


@pytest.fixture
# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def valid_courier_payload():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    len_random = 100
    login = generate_random_string(len_random)
    password = generate_random_string(len_random)
    first_name = generate_random_string(len_random)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # тела запроса для регистрации
    return payload

@pytest.fixture
def valid_log_in_payload(valid_courier_payload):
    CourierPage.create_courier(valid_courier_payload)
    login_payload = {
        "login": valid_courier_payload["login"],
        "password": valid_courier_payload["password"],
    }
    return login_payload