import requests
import allure

from urls import *

class OrderPage:

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload):
        response = requests.post(ORDERS_URL, data=payload, timeout=20)
        return response

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_all_orders():
        response = requests.get(ORDERS_URL, timeout=60)
        return response