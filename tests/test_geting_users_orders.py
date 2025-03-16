import allure
import requests
from constants import burgers_url
class TestGetingUsersOrders:
    @allure.title("Проверка получения заказов авторизованного пользователя")
    def test_receiving_orders_authorized_user(self, create_and_delete_user_for_login):
        responce, payload, user_info = create_and_delete_user_for_login
        login_data = {
            "email": user_info['user']['email'],
            "password": payload['password']
        }
        ingredients = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6e", "61c0c5a71d1f82001bdaaa72"]
        }
        autorization = requests.post(f"{burgers_url}/auth/login", json=login_data)
        create_order = requests.post(f"{burgers_url}/orders", json=ingredients)
        receiving_orders=requests.get(f"{burgers_url}/orders")
        assert receiving_orders.status_code==200
        assert receiving_orders.json()['success'] is True
        assert receiving_orders.json().get("orders")

    @allure.title("Проверка получения заказов неавторизованного пользователя")
    def test_receiving_orders_unauthorized_user(self, create_and_delete_user_for_login):
        responce, payload, user_info = create_and_delete_user_for_login
        ingredients = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6e", "61c0c5a71d1f82001bdaaa72"]
        }
        create_order = requests.post(f"{burgers_url}/orders", json=ingredients)
        receiving_orders = requests.get(f"{burgers_url}/orders")
        assert receiving_orders.status_code == 401
        assert receiving_orders.json().get("message")=="You should be authorised"



