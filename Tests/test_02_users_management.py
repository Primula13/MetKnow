import requests
from Tools import tools_for_tests
from frames import models
uri = "http://metknow.dev.cleveroad.com/api/"
token = models.admin.token


def test_01_view_users_lis_admin():
    assert tools_for_tests.get_users_list(token)[0] == 200
    assert tools_for_tests.get_users_list(token)[1] is not None
    assert len(tools_for_tests.get_users_list(token)[1]["data"]) == 12


def test_02_view_users_lis_user():
    assert tools_for_tests.get_users_list(models.user1.token)[0] == 403
    assert tools_for_tests.get_users_list(models.user1.token)[1]["message"] == "Forbidden"


def test_03_admin_search_user_success():
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer " + token}
    parameters = {"Length": 12, "Search.Value": "test"}
    r = requests.post(url=uri + "User/GetAll", headers=header, params=parameters)
    assert r.status_code == 200
    assert r.json()["data"] is not None
    for i in range(0, len(r.json()["data"])):
        assert "test" in r.json()["data"][i]["email"]


def test_04_admin_search_user_no_results():
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer " + token}
    parameters = {"Length": 12, "Search.Value": "frw"}
    r = requests.post(url=uri + "User/GetAll", headers=header, params=parameters)
    assert r.status_code == 200
    assert r.json()["data"] == []


def test_05_admin_search_user_too_short_query():
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer " + token}
    parameters = {"Length": 12, "Search.Value": "f"}
    r = requests.post(url=uri + "User/GetAll", headers=header, params=parameters)
    assert r.status_code == 200
    assert r.json()["data"] is not None
    assert len(r.json()["data"]) == 12


def test_06_admin_block_unblock_user():
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer " + token}
    user_id = 4
    for _ in range(2):
        if tools_for_tests.get_users_list(token)[1]["data"][2]["isActive"] is True:
            r = requests.post(url=uri + "User/Block/%d" % user_id, headers=header)
            assert r.status_code == 200
            assert tools_for_tests.get_users_list(token)[1]["data"][2]["isActive"] is False
        else:
            r = requests.post(url=uri + "User/Block/%d" % user_id, headers=header)
            assert r.status_code == 200
            assert tools_for_tests.get_users_list(token)[1]["data"][2]["isActive"] is True
