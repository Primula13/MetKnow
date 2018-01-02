import requests
import json
from frames import models
uri = "http://metknow.dev.cleveroad.com/api/"
token = models.user1.token
token2 = models.user2.token


def test_01_create_member_success(valid_member_data):
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    payload = {"firstName": valid_member_data["firstName"], "lastName": valid_member_data["lastName"],
               "email": valid_member_data["email"], "phone": valid_member_data["phone"],
               "gender": valid_member_data["gender"], "city": valid_member_data["city"],
               "title": valid_member_data["title"], "company": valid_member_data["company"],
               "whereWeMet": valid_member_data["whereWeMet"], "myNotes": valid_member_data["myNotes"]}
    r = requests.put(url=uri + "Member/161/CreateMember", headers=header, data=json.dumps(payload))
    assert r.status_code == 200
    assert r.json() is not None


def test_02_create_member_fail(invalid_member_data):
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    payload = {"firstName": invalid_member_data["firstName"], "lastName": invalid_member_data["lastName"],
               "email": invalid_member_data["email"], "phone": invalid_member_data["phone"],
               "gender": invalid_member_data["gender"], "city": invalid_member_data["city"],
               "title": invalid_member_data["title"], "company": invalid_member_data["company"],
               "whereWeMet": invalid_member_data["whereWeMet"], "myNotes": invalid_member_data["myNotes"]}
    r = requests.put(url=uri + "Member/161/CreateMember", headers=header, data=json.dumps(payload))
    assert r.status_code == 400
    assert r.json()["errors"][0]["message"] == invalid_member_data["expected_message"]


def test_03_add_member_to_another_user_group():
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + token2}
    payload = {"firstName": "Test", "lastName": "Test"}
    r = requests.put(url=uri + "Member/161/CreateMember", headers=header, data=json.dumps(payload))
    assert r.status_code == 403
    assert r.json()["errors"][0]["message"] == "Not enough permissions"


def test_04_delete_another_user_member():
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    r = requests.delete(url=uri + "Member/DeleteMember", headers=header, params={"memberId": 14})
    assert r.status_code == 403
    assert r.json()["errors"][0]["message"] == "Not enough permissions"


def test_05_edit_member_success(valid_member_data):
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    payload = {"id": 438, "firstName": valid_member_data["firstName"], "lastName": valid_member_data["lastName"],
               "email": valid_member_data["email"], "phone": valid_member_data["phone"],
               "gender": valid_member_data["gender"], "city": valid_member_data["city"],
               "title": valid_member_data["title"], "company": valid_member_data["company"],
               "whereWeMet": valid_member_data["whereWeMet"], "myNotes": valid_member_data["myNotes"]}
    r = requests.post(url=uri + "Member/EditMember", headers=header, data=json.dumps(payload))
    assert r.status_code == 200
    assert r.json() is not None


def test_06_edit_member_fail(invalid_member_data):
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
    payload = {"id": 438, "firstName": invalid_member_data["firstName"], "lastName": invalid_member_data["lastName"],
               "email": invalid_member_data["email"], "phone": invalid_member_data["phone"],
               "gender": invalid_member_data["gender"], "city": invalid_member_data["city"],
               "title": invalid_member_data["title"], "company": invalid_member_data["company"],
               "whereWeMet": invalid_member_data["whereWeMet"], "myNotes": invalid_member_data["myNotes"]}
    r = requests.post(url=uri + "Member/EditMember", headers=header, data=json.dumps(payload))
    assert r.status_code == 400
    assert r.json()["errors"][0]["message"] == invalid_member_data["expected_message"]


def test_07_edit_member_from_another_user_group():
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + token2}
    payload = {"id": 438, "firstName": "Test", "lastName": "Test"}
    r = requests.post(url=uri + "Member/EditMember", headers=header, data=json.dumps(payload))
    assert r.status_code == 403
    assert r.json()["errors"][0]["message"] == "Not enough permissions"
