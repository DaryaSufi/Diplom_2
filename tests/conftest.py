import pytest
import allure
import requests
from constants import burgers_url
from helpers import create_user
from api_metods import User
@allure.step("Создаём пользователя")
@pytest.fixture()
def create_and_delete_user():
    payload = create_user()
    responce = requests.post(f"{burgers_url}{User.registr}", json=payload)
    user_info = responce.json()
    yield responce, user_info
    access_token = user_info["accessToken"]
    headers = {
        "Authorization": access_token
    }
    requests.delete(f"{burgers_url}{User.user_info}", headers=headers)


@allure.step("Создаём пользователя без email")
@pytest.fixture()
def create_user_without_email():
    payload = create_user()
    payload["email"] = ""
    responce = requests.post(f"{burgers_url}{User.registr}", json=payload)
    user_info = responce.json()
    yield responce, user_info
    access_token = user_info["accessToken"]
    headers = {
        "Authorization": access_token
    }
    requests.delete(f"{burgers_url}{User.user_info}", headers=headers)
@allure.step("Создаём пользователя без name")
@pytest.fixture()
def create_user_without_name():
    payload = create_user()
    payload["name"] = ""
    responce = requests.post(f"{burgers_url}{User.registr}", json=payload)
    user_info = responce.json()
    yield responce, user_info
    access_token = user_info["accessToken"]
    headers = {
        "Authorization": access_token
    }
    requests.delete(f"{burgers_url}{User.user_info}", headers=headers)
@allure.step("Создаём пользователя без password")
@pytest.fixture()
def create_user_without_password():
    payload = create_user()
    payload["password"] = ""
    responce = requests.post(f"{burgers_url}{User.registr}", json=payload)
    user_info = responce.json()
    yield responce, user_info
    access_token = user_info["accessToken"]
    headers = {
        "Authorization": access_token
    }
    requests.delete(f"{burgers_url}{User.user_info}", headers=headers)
@allure.step("Создаём пользователя для логина")
@pytest.fixture()
def create_and_delete_user_for_login():
    payload = create_user()
    responce = requests.post(f"{burgers_url}{User.registr}", json=payload)
    user_info = responce.json()
    yield responce, payload, user_info
    access_token = user_info["accessToken"]
    headers = {
        "Authorization": access_token
    }
    requests.delete(f"{burgers_url}{User.user_info}", headers=headers)

