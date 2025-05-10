import allure
import requests
from constants import burgers_url
from faker import Faker
from api_metods import User
from data import Data
class TestLoginUser:
    @allure.title("Проверка успешного логина под существующим пользователем")
    def test_login_under_an_existing_user(self, create_and_delete_user_for_login):
        responce, payload, user_info = create_and_delete_user_for_login
        login_data = {
            "email": user_info['user']['email'],
            "password": payload['password']
        }
        user_response = requests.post(f"{burgers_url}{User.auth}", json=login_data)
        user_response_json=user_response.json()
        assert user_response.status_code==200
        assert user_response_json['success'] is True

    @allure.title("Проверка невозможности логина с неверным login и password")
    def test_impossible_login_with_incorrect_login_and_password(self, create_and_delete_user_for_login):
        responce, payload, user_info = create_and_delete_user_for_login
        fake=Faker()
        login_data = {
            "email": fake.email(),
            "password": fake.password()
        }
        user_response = requests.post(f"{burgers_url}{User.auth}", json=login_data)
        user_response_json = user_response.json()
        assert user_response.status_code == 401
        assert user_response_json.get("message") == Data.incorrect_log_and_pass_message


