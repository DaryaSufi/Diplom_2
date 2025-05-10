import allure
import requests
from constants import burgers_url
from api_metods import User
from api_metods import Order
from data import Data
class TestGetingUsersOrders:
    @allure.title("Проверка получения заказов авторизованного пользователя")
    def test_receiving_orders_authorized_user(self, create_and_delete_user_for_login):
        responce, payload, user_info = create_and_delete_user_for_login
        login_data = {
            "email": user_info['user']['email'],
            "password": payload['password']
        }
        ingredients = {
            "ingredients": [Data.ingr_1, Data.ingr_2]
        }
        autorization = requests.post(f"{burgers_url}{User.auth}", json=login_data)
        create_order = requests.post(f"{burgers_url}{Order.cr_order}", json=ingredients)
        receiving_orders=requests.get(f"{burgers_url}{Order.cr_order}")
        assert receiving_orders.status_code==200
        assert receiving_orders.json()['success'] is True
        assert receiving_orders.json().get("orders")

    @allure.title("Проверка получения заказов неавторизованного пользователя")
    def test_receiving_orders_unauthorized_user(self, create_and_delete_user_for_login):
        responce, payload, user_info = create_and_delete_user_for_login
        ingredients = {
            "ingredients": [Data.ingr_1, Data.ingr_2]
        }
        create_order = requests.post(f"{burgers_url}{Order.cr_order}", json=ingredients)
        receiving_orders = requests.get(f"{burgers_url}{Order.cr_order}")
        assert receiving_orders.status_code == 401
        assert receiving_orders.json().get("message") == Data.unauth_user_message



