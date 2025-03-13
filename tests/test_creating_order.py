import allure
import requests
from constants import burgers_url
class TestCreatingOrder:
    @allure.title("Проверка создания заказа авторизованного пользователя с ингридиентами")
    def test_creating_authorized_users_order_with_ingredients(self, create_and_delete_user_for_login):
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
        assert create_order.status_code==200
        assert create_order.json()['success'] is True

    @allure.title("Проверка создания заказа авторизованного пользователя без ингридиентов")
    def test_creating_authorized_users_order_without_ingredients(self, create_and_delete_user_for_login):
        responce, payload, user_info = create_and_delete_user_for_login
        login_data = {
            "email": user_info['user']['email'],
            "password": payload['password']
        }
        autorization = requests.post(f"{burgers_url}/auth/login", json=login_data)
        create_order = requests.post(f"{burgers_url}/orders")
        assert create_order.status_code == 400
        assert create_order.json().get("message") == "Ingredient ids must be provided"

    @allure.title("Проверка создания заказа неавторизованного пользователя с ингридиентами")
    def test_creating_unauthorized_users_order_with_ingredients(self, create_and_delete_user_for_login):
        responce, payload, user_info = create_and_delete_user_for_login
        ingredients = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6e", "61c0c5a71d1f82001bdaaa72"]
        }
        create_order = requests.post(f"{burgers_url}/orders", json=ingredients)
        assert create_order.status_code == 400
        assert create_order.json()['success'] is False

    @allure.title("Проверка создания заказа неавторизованного пользователя без ингридиентов")
    def test_creating_unauthorized_users_order_without_ingredients(self, create_and_delete_user_for_login):
        responce, payload, user_info = create_and_delete_user_for_login
        create_order = requests.post(f"{burgers_url}/orders")
        assert create_order.status_code == 400
        assert create_order.json()['success'] is False

    @allure.title("Проверка создания заказа авторизованного пользователя с невалидным хешем ингредиента")
    def test_creating_authorized_users_order_with_invalid_hash_of_the_ingredient(self, create_and_delete_user_for_login):
        responce, payload, user_info = create_and_delete_user_for_login
        login_data = {
            "email": user_info['user']['email'],
            "password": payload['password']
        }
        ingredients = {
            "ingredients": ["61c0c5a71d1f834562001bdaaa6e", "61c0c5a71d1f8678902001bdaaa72"]
        }
        autorization = requests.post(f"{burgers_url}/auth/login", json=login_data)
        create_order = requests.post(f"{burgers_url}/orders", json=ingredients)
        assert create_order.status_code == 500

    @allure.title("Проверка создания заказа неавторизованного пользователя с невалидным хешем ингредиента")
    def test_creating_unauthorized_users_order_with_invalid_hash_of_the_ingredient(self,create_and_delete_user_for_login):
        responce, payload, user_info = create_and_delete_user_for_login
        ingredients = {
            "ingredients": ["61c0c5a71d1f834562001bdaaa6e", "61c0c5a71d1f8678902001bdaaa72"]
        }
        create_order = requests.post(f"{burgers_url}/orders", json=ingredients)
        assert create_order.status_code == 500







    