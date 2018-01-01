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


@pytest.fixture(scope="function", params=[
    {
        "case": "Email already exists",
        "email": "test@gmail.com",
        "password": "qwerty",
        "confirm_password": "qwerty",
        "error_message": "Email is already taken"
    },
    {
        "case": "Invalid email",
        "email": "testgmail.com",
        "password": "qwerty",
        "confirm_password": "qwerty",
        "error_message": "Invalid Email"
    },
    {
        "case": "Password and confirm password do not match",
        "email": "user@test.com",
        "password": "qwerty",
        "confirm_password": "qwerty1",
        "error_message": "Confirm password field doesn’t match password"
    },
    {
        "case": "Password invalid - too short",
        "email": "user@test.com",
        "password": "qwert",
        "confirm_password": "qwert",
        "error_message": "Password should be at least 6 symbols"
    },
    {
        "case": "Empty password",
        "email": "user@test.com",
        "password": "",
        "confirm_password": "qwerty",
        "error_message": "Password field is required"
    }
])
def failed_registration(request):
    return request.param


@pytest.fixture(scope="session", params=[
    {
        "case": "Group without description",
        "name": "Test",
        "description": ""
    },
    {
        "case": "Group with description",
        "name": "Test",
        "description": "Test description"
    },
    {
        "case": "Short group's name and description",
        "name": "1",
        "description": "1"
    },
    {
        "case": "Long group's name and description",
        "name": "vSjzekSExwJvLPK6QjobeHERFjxxqu",
        "description": "uoO5JqzJMq CN6k2nTGk1DqdVD Q88cg6 4R0nvowXX2KZzj9S"
    }
])
def valid_groups_data(request):
    return request.param


@pytest.fixture(scope="session", params=[
    {
        "case": "Group's name is empty",
        "name": "",
        "description": "test",
        "error_message": "Group name is required"
    },
    {
        "case": "Group's name is too long",
        "name": "CiCRFRw1gbeaLo2OY2GXe48jTrI6leJ",
        "description": "test",
        "error_message": "Group name length can`t be greater than 30 characters"
    },
    {
        "case": "Group's name contains only spaces",
        "name": "   ",
        "description": "test",
        "error_message": "Group name cannot contain only spaces"
    },
{
        "case": "Group's description is too long",
        "name": "New Group",
        "description": "wFVggpiI2pfYmcyYmmNy1AzmYxw8lwkotyg9dVZvIVPXdf64ILA",
        "error_message": "Description length can`t be greater than 50 characters"
    }
])
def invalid_groups_data(request):
    return request.param