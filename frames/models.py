import requests


def get_token(role):
    payload = {"email": role.email, "password": role.password}
    r = requests.post(url="http://metknow.dev.cleveroad.com/api/Account/Login", params=payload)
    return r.json()["data"]["token"]["accessToken"]


class User(object):

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.token = get_token(self)


user1 = User("test@gmail.com", "qwerty")
