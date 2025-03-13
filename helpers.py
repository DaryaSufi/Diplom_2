from faker import Faker
import requests
from constants import burgers_url
def create_user():
    fake = Faker()
    email = fake.email()
    password = fake.password()
    name = fake.name()
    payload = {
            "email": email,
            "password": password,
            "name": name
        }
    return payload

