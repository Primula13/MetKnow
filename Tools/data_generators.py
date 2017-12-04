import mimesis
import requests
from frames import models


def create_groups():
    authorization = "Bearer" + models.user1.token
    for _ in range(30):
        payload = {"name": mimesis.Text.words(quantity=1), "description": mimesis.Text.text(quantity=2)}
        requests.put(url="http://metknow.dev.cleveroad.com/api/Group/CreateGroup", headers=authorization, data=payload)


def create_members_in_group():
    authorization = "Bearer" + models.user1.token
    for _ in range(60):
        payload = {
            "firstName": mimesis.Personal.name,
            "lastName": mimesis.Personal.surname,
            "email": mimesis.Personal.email,
            "phone": mimesis.Personal.telephone,
            "gender": mimesis.Personal.gender,
            "city": mimesis.Address.city,
            "company": mimesis.Business.company,
            "whereWeMet": mimesis.Text.text(quantity=1),
        }
        requests.put(url="http://metknow.dev.cleveroad.com/api/Member/30/CreateMember", headers=authorization,
                     data=payload)
