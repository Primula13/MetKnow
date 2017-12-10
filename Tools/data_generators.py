import requests
import json
from frames import models
from mimesis import Generic
generic = Generic('en')


def create_groups():
    auth = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + models.user1.token
        }
    for _ in range(30):
        payload = {"name": generic.text.word(), "description": generic.text.word()}
        requests.put(url="http://metknow.dev.cleveroad.com/api/Group/CreateGroup", headers=auth,
                         data=json.dumps(payload))


def create_members_in_group():
    auth = {
        "Content-Type": "application/json",
        "Authorization": models.user1.token
        }
    for _ in range(60):
        payload = {
            "firstName": generic.personal.name(),
            "lastName": generic.personal.surname(),
            "email": generic.personal.email(),
            "phone": "54755757858",
            "gender": generic.personal.gender(),
            "city": generic.address.city(),
            "company": generic.business.company()
        }
        r = requests.put(url="http://metknow.dev.cleveroad.com/api/Member/76/CreateMember", headers=auth,
                         data=json.dumps(payload))
        return r.status_code, r.json()
