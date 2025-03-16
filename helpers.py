from faker import Faker
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

