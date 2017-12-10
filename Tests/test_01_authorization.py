import requests
from Tools import auth_tools
from frames import models
uri = "http://metknow.dev.cleveroad.com/api/"


def test_01_successful_authorization():
    assert auth_tools.authorization("test@gmail.com", "qwerty")[0] == 200
    assert auth_tools.authorization("test@gmail.com", "qwerty")[1] is not None


def test_02_failed_authorization(invalid_credentials):
    assert auth_tools.authorization(invalid_credentials["email"], invalid_credentials["password"])[0] == 400
    assert auth_tools.authorization(invalid_credentials["email"],
                                    invalid_credentials["password"])[1]["errors"][0]["message"] == \
        "Incorrect email or password"


def test_03_success_logout():
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer " + models.user1.token}
    r = requests.delete(url=uri + "Account/Logout", headers=header)
    assert r.status_code == 200
    r1 = requests.get(url=uri + "Group/GetGroups", headers=header, params={"limit": 25, "offset": 0})
    assert r1.status_code == 401
