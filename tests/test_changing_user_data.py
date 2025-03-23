import allure
import requests
from constants import burgers_url
from api_metods import User
from data import Data
class TestChangingUserData: 
    @allure.title("Проверка возможности изменить имя пользователя с авторизацией")
    def test_changing_user_name_with_authorization(self, create_and_delete_user):
        _,user_info = create_and_delete_user
        update_data={
            'name': Data.name
        }
        access_token = user_info["accessToken"]
        headers = {
            "Authorization": access_token
        }
        response = requests.patch(f"{burgers_url}{User.auth}", headers=headers, json=update_data)
        assert response.status_code==200
        assert response.json().get("user").get("name") == Data.name

    @allure.title("Проверка возможности изменить почту пользователя с авторизацией")
    def test_changing_user_email_with_authorization(self, create_and_delete_user):
        _, user_info = create_and_delete_user
        update_data = {
            'email': Data.email
        }
        access_token = user_info["accessToken"]
        headers = {
            "Authorization": access_token
        }
        response = requests.patch(f"{burgers_url}{User.user_info}", headers=headers, json=update_data)
        assert response.status_code == 200
        assert response.json().get("user").get("email") == Data.email

    @allure.title("Проверка невозможности изменить имя пользователя без авторизации")
    def test_changing_user_name_without_authorization(self, create_and_delete_user):
        _, user_info = create_and_delete_user
        update_data = {
            'name': Data.name
        }
        response = requests.patch(f"{burgers_url}{User.user_info}", json=update_data)
        assert response.status_code == 401
        assert response.json()['success'] is False
        assert response.json().get("message") == Data.unauthorization_user_message

    @allure.title("Проверка невозможности изменить почту пользователя без авторизации")
    def test_changing_user_email_without_authorization(self, create_and_delete_user):
        _, user_info = create_and_delete_user
        update_data = {
            'email': Data.email
        }
        response = requests.patch(f"{burgers_url}{User.user_info}", json=update_data)
        assert response.status_code == 401
        assert response.json()['success'] is False
        assert response.json().get("message") == Data.unauthorization_user_message





