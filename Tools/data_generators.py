import requests
from Main.frames import models
from mimesis import Generic
generic = Generic('en')


def create_groups():
    auth = {"Authorization": "Bearer " + models.user1.token}
    payload = {"name": generic.text.word(), "description": generic.text.text(quantity=1)}
    requests.put(url="http://metknow.dev.cleveroad.com/api/Group/CreateGroup", headers=auth, data=payload)


def create_members_in_group():
    auth = {"Authorization": "Bearer " + models.user1.token}
    for _ in range(60):
        payload = {
            "firstName": generic.personal.name(),
            "lastName": generic.personal.surname(),
            "email": generic.personal.email(),
            "phone": generic.personal.telephone(),
            "gender": generic.personal.gender(),
            "city": generic.address.city(),
            "company": generic.business.company(),
            "whereWeMet": generic.text.text(quantity=1),
        }
        requests.put(url="http://metknow.dev.cleveroad.com/api/Member/30/CreateMember", headers=auth,
                     data=payload)

