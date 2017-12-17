import requests
import json
uri = "http://metknow.dev.cleveroad.com/api/"

def authorization(email, password):
    header = {"Content-Type": "application/json"}
    payload = {"email": email, "password": password}
    r = requests.post(url=uri + "Account/Login", headers=header, data=json.dumps(payload))
    return r.status_code, r.json()


def get_users_list(token):
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer " + token}
    r = requests.post(url=uri + "User/GetAll", headers=header, params={"Length": 12})
    return r.status_code, r.json()
