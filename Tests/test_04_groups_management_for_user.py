import requests
import json
from frames import models
uri = "http://metknow.dev.cleveroad.com/api/"
token1 = models.user1.token
token2 = models.user2.token


def test_01_get_list_of_groups_user():
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + token1}
    parameters = {"limit": 25, "offset": 0}
    r = requests.get(url=uri + "Group/GetGroups", headers=header, params=parameters)
    assert r.status_code == 200
    assert r.json() is not None
    assert len(r.json()["data"]) == 25


def test_02_get_group_details_user():
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + token1}
    parameters = {"groupId": 159, "limit": 25, "offset": 0}
    r = requests.get(url=uri + "Member/GetGroupMembers", headers=header, params=parameters)
    assert r.status_code == 200
    assert len(r.json()["data"]) == 25


def test_03_get_another_user_group_details():
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + token2}
    parameters = {"groupId": 159, "limit": 25, "offset": 0}
    r = requests.get(url=uri + "Member/GetGroupMembers", headers=header, params=parameters)
    assert r.status_code == 403
    assert r.json()["errors"][0]["message"] == "Not enough permissions"


def test_04_create_group_success(valid_groups_data):
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + token1}
    payload = {"name": valid_groups_data["name"], "description": valid_groups_data["description"]}
    r = requests.put(url=uri + "Group/CreateGroup", headers=header, data=json.dumps(payload))
    assert r.status_code == 200
    assert r.json()["data"]["name"] == valid_groups_data["name"] and r.json()["data"]["description"] == \
        valid_groups_data["description"]


def test_05_create_group_fail(invalid_groups_data):
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + token1}
    payload = {"name": invalid_groups_data["name"], "description": invalid_groups_data["description"]}
    r = requests.put(url=uri + "Group/CreateGroup", headers=header, data=json.dumps(payload))
    assert r.status_code == 400
    assert r.json()["errors"][0]["message"] == invalid_groups_data["error_message"]


def test_06_edit_group_success(valid_groups_data):
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + token1}
    payload = {"id": 160, "name": valid_groups_data["name"], "description": valid_groups_data["description"]}
    r = requests.post(url=uri + "Group/EditGroup", headers=header, data=json.dumps(payload))
    assert r.status_code == 200
    assert r.json()["data"]["name"] == valid_groups_data["name"] and r.json()["data"]["description"] == \
        valid_groups_data["description"]


def test_07_edit_group_fail(invalid_groups_data):
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + token1}
    payload = {"id": 160, "name": invalid_groups_data["name"], "description": invalid_groups_data["description"]}
    r = requests.post(url=uri + "Group/EditGroup", headers=header, data=json.dumps(payload))
    assert r.status_code == 400
    assert r.json()["errors"][0]["message"] == invalid_groups_data["error_message"]


def test_08_edit_other_user_group():
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + token2}
    payload = {"id": 160, "name": "test", "description": "some description"}
    r = requests.post(url=uri + "Group/EditGroup", headers=header, data=json.dumps(payload))
    assert r.status_code == 403
    assert r.json()["errors"][0]["message"] == "Not enough permissions"


def test_09_blocked_user_create_group():
    admin_header = {"Content-Type": "application/json", "Authorization": "Bearer " + models.admin.token}
    r1 = requests.post(url=uri + "User/Block/17", headers=admin_header)
    assert r1.status_code == 200
    user_header = {"Content-Type": "application/json", "Authorization": "Bearer " + token1}
    payload = {"name": "test", "description": "some description"}
    r2 = requests.put(url=uri + "Group/CreateGroup", headers=user_header, data=json.dumps(payload))
    assert r2.status_code == 403
    assert r2.json()["errors"][0]["message"] == "You are blocked by admin and not able to create a group."
    requests.post(url=uri + "User/Block/17", headers=admin_header)


def test_10_delete_another_user_group():
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + token2}
    r = requests.delete(url=uri + "Group/DeleteGroup", headers=header, params={"id": 160})
    assert r.status_code == 403
    assert r.json()["errors"][0]["message"] == "Not enough permissions"
