import allure
import requests
from faker import Faker
from constants import burgers_url
from api_metods import User
from data import Data
class TestCreatingUser:
    @allure.title("Проверка успешного создания уникального пользователя")
    def test_create_unic_user(self, create_and_delete_user):
        responce,user_data = create_and_delete_user
        assert responce.status_code == 200
        assert user_data['success'] is True
    @allure.title("Проверка невозможности создания пользователя с уже существующими данными")
    def test_creating_an_existing_user(self, create_and_delete_user):
        _, user_data = create_and_delete_user
        fake=Faker()
        payload= {
            "email": user_data['user']['email'],
            "password": fake.password(),
            "name": user_data['user']['name']
        }
        responce = requests.post(f"{burgers_url}{User.auth}", json=payload)
        responce_json=responce.json()
        assert responce.status_code == 403
        assert responce_json.get("message") == Data.an_existing_user_message
    @allure.title("Проверка невозможности создания пользователя без заполения всех обязательных полей")
    def test_creating_a_user_without_required_fields(self):
        payload = {
            "email":'',
            "password":'',
            "name": ''
        }
        responce = requests.post(f"{burgers_url}{User.registr}", json=payload)
        responce_json = responce.json()
        assert responce.status_code == 403
        assert responce_json.get("message") == Data.user_without_required_fields_message

    @allure.title("Проверка невозможности создания пользователя без заполнения поля email")
    def test_creating_a_user_without_email(self, create_user_without_email):
        responce,user_data = create_user_without_email
        responce_json = responce.json()
        assert responce.status_code == 403
        assert responce_json.get("message") == Data.user_without_required_fields_message

    @allure.title("Проверка невозможности создания пользователя без заполнения поля name")
    def test_creating_a_user_without_name(self, create_user_without_name):
        responce, user_data = create_user_without_name
        responce_json = responce.json()
        assert responce.status_code == 403
        assert responce_json.get("message") == Data.user_without_required_fields_message

    @allure.title("Проверка невозможности создания пользователя без заполнения поля password")
    def test_creating_a_user_without_password(self, create_user_without_password):
        responce, user_data = create_user_without_password
        responce_json = responce.json()
        assert responce.status_code == 403
        assert responce_json.get("message") == Data.user_without_required_fields_message





