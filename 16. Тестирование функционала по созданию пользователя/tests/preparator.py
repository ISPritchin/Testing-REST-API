from faker import Faker


def prepare_register_data(email: str = None):
    if email is None:
        fake = Faker(locale="en")
        email = fake.email()

    return {
        'password': '123',
        'username': 'learnqa',
        'firstName': 'learnqa',
        'lastName': 'learnqa',
        'email': email,
    }
