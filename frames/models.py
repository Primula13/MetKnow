import requests
import json


def get_token(role):
    header = {"Content-Type": "application/json"}
    payload = {"email": role.email, "password": role.password}
    r = requests.post(url="http://metknow.dev.cleveroad.com/api/Account/Login", headers=header,
                      data=json.dumps(payload))
    return r.json()["data"]["token"]["accessToken"]


class User(object):

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.token = get_token(self)


user1 = User("test3@gmail.com", "qwerty")
admin = User("will@metknow.com", "metknow1901")
user2 = User("test1@gmail.com", "qwerty")