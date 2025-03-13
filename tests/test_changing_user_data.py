import allure
import requests
from constants import burgers_url
class TestChangingUserData: 
    @allure.title("Проверка возможности изменить имя пользователя с авторизацией")
    def test_changing_user_name_with_authorization(self, create_and_delete_user):
        _,user_info = create_and_delete_user
        update_data={
            'name':'Lidiya'
        }
        access_token = user_info["accessToken"]
        headers = {
            "Authorization": access_token
        }
        response = requests.patch(f"{burgers_url}/auth/user", headers=headers, json=update_data)
        assert response.status_code==200
        assert response.json().get("user").get("name") == "Lidiya"

    @allure.title("Проверка возможности изменить почту пользователя с авторизацией")
    def test_changing_user_email_with_authorization(self, create_and_delete_user):
        _, user_info = create_and_delete_user
        update_data = {
            'email': 'lidiya@yandex.ru'
        }
        access_token = user_info["accessToken"]
        headers = {
            "Authorization": access_token
        }
        response = requests.patch(f"{burgers_url}/auth/user", headers=headers, json=update_data)
        assert response.status_code == 200
        assert response.json().get("user").get("email") == "lidiya@yandex.ru"

    @allure.title("Проверка невозможности изменить имя пользователя без авторизации")
    def test_changing_user_name_without_authorization(self, create_and_delete_user):
        _, user_info = create_and_delete_user
        update_data = {
            'name': 'Lidiya'
        }
        response = requests.patch(f"{burgers_url}/auth/user", json=update_data)
        assert response.status_code == 401
        assert response.json()['success'] is False
        assert response.json().get("message") == "You should be authorised"

    @allure.title("Проверка невозможности изменить почту пользователя без авторизации")
    def test_changing_user_email_without_authorization(self, create_and_delete_user):
        _, user_info = create_and_delete_user
        update_data = {
            'email': 'lidiya@yandex.ru'
        }
        response = requests.patch(f"{burgers_url}/auth/user", json=update_data)
        assert response.status_code == 401
        assert response.json()['success'] is False
        assert response.json().get("message") == "You should be authorised"





