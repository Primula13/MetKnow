import pytest


@pytest.fixture(scope="session", params=[
    {
     "case": "Wrong email",
     "email": " test3@gmail.com",
     "password": "qwerty"
    },
    {
     "case": "Wrong password",
     "email": "test3@gmail.com",
     "password": "qwerty "
    },
    {
     "case": "Empty email",
     "email": "",
     "password": "qwerty"
    },
    {
     "case": "Empty password",
     "email": "test3@gmail.com",
     "password": ""
    },
    {
     "case": "Unconfirmed email",
     "email": "test4@gmail.com",
     "password": "qwerty"
    }
])
def invalid_credentials(request):
    return request.param
