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


@pytest.fixture(scope="session", params=[
    {
        "case": "Only mandatory fields filled",
        "firstName": "A",
        "lastName": "B",
        "email": "",
        "phone": "",
        "gender": "",
        "city": "",
        "title": "",
        "company": "",
        "whereWeMet": "",
        "myNotes": ""
    },
    {
        "case": "All fields are filled, minimal value",
        "firstName": "A",
        "lastName": "B",
        "email": "memeber@gmail.com",
        "phone": "5555555",
        "gender": "male",
        "city": "D",
        "title": "1",
        "company": "2",
        "whereWeMet": "Q",
        "myNotes": "U"
    },
    {
        "case": "All fields are filled, maximal value",
        "firstName": "6eeEr8hzuK*HyD)+3LJ9qz&+cjN)wr",
        "lastName": "z^s)$HPi75nj3(H@IffNhopSf86xHe",
        "email": "new_member@gmail.com",
        "phone": "5554444",
        "gender": "female",
        "city": "872jXgeo9@W GzyCTrnC#6+d#4_iapEC$wKPS A2evwls5tpuP",
        "title": "fO2Qs$m1eI)Nujk^v1X3!H US1 KPakJ16qpFfsgfx7Sa7pgJY",
        "company": "lpJOpTX&uWRPqkWYJR3ruMfniKr80o81BrwynZ!0i iIBq)$iU",
        "whereWeMet": "PwMWdmOZv!x6z%5+g4q8S I!wx#WLZHdJnmCMvUN3cjK!BXnfZ",
        "myNotes": "8nH6Pu%2uKS%e!RBiFVDBIZ7*9Hm JL&7cS)OAGBdcW=w5B_T7X%$Ed!31vG&5#4Kw5tJ_ qj(5ud4*L%xT%W%&M" +
                   "m4pU7L5T3V6Ohau2C4juCDMY=g#1BbShWegIu73p^dPvK3p^bhlgcVGB33J4SkBuisO(xChrQQ1WkPsd5qBX6JJSXQR" +
                   "FE0z6GkYnYY!#%RXQ@Fc"
    }
])
def valid_member_data(request):
    return request.param


@pytest.fixture(scope="session", params=[
    {
        "case": "First name is missing",
        "firstName": "",
        "lastName": "Test",
        "email": "valid@gmail.com",
        "phone": "3333333",
        "gender": "male",
        "city": "Ottawa",
        "title": "",
        "company": "",
        "whereWeMet": "",
        "myNotes": "",
        "expected_message": "First name is required"
    },
    {
        "case": "Last name is missing",
        "firstName": "Test",
        "lastName": "",
        "email": "memeber@gmail.com",
        "phone": "5555555",
        "gender": "male",
        "city": "D",
        "title": "1",
        "company": "2",
        "whereWeMet": "Q",
        "myNotes": "U",
        "expected_message": "Last name is required"
    },
    {
        "case": "First name is too long",
        "firstName": "l(R)013_NolcY(55j$ BxOhw(tueV+%",
        "lastName": "Test",
        "email": "memeber@gmail.com",
        "phone": "5555555",
        "gender": "male",
        "city": "D",
        "title": "1",
        "company": "2",
        "whereWeMet": "Q",
        "myNotes": "U",
        "expected_message": "First name length can`t be greater than 30 characters"
    },
    {
        "case": "Last name is too long",
        "firstName": "Test",
        "lastName": "l(R)013_NolcY(55j$ BxOhw(tueV+%",
        "email": "memeber@gmail.com",
        "phone": "5555555",
        "gender": "male",
        "city": "D",
        "title": "1",
        "company": "2",
        "whereWeMet": "Q",
        "myNotes": "U",
        "expected_message": "First name length can`t be greater than 30 characters"
    },
    {
        "case": "Invalid email",
        "firstName": "Test",
        "lastName": "Test",
        "email": "memebergmail.com",
        "phone": "5555555",
        "gender": "male",
        "city": "D",
        "title": "1",
        "company": "2",
        "whereWeMet": "Q",
        "myNotes": "U",
        "expected_message": "Invalid Email"
    },
    {
        "case": "Invalid phone number",
        "firstName": "Test",
        "lastName": "Test",
        "email": "memeber@gmail.com",
        "phone": "222e5",
        "gender": "male",
        "city": "D",
        "title": "1",
        "company": "2",
        "whereWeMet": "Q",
        "myNotes": "U",
        "expected_message": "Invalid Phone"
    },
    {
        "case": "City name is too long",
        "firstName": "Test",
        "lastName": "Test",
        "email": "memeber@gmail.com",
        "phone": "5555555",
        "gender": "male",
        "city": "63VRLaPkqX(() EeDiM&4Be@+=VDSZHYxysDPSWVtBVtI&$g&u8",
        "title": "1",
        "company": "2",
        "whereWeMet": "Q",
        "myNotes": "U",
        "expected_message": "City length can`t be greater than 50 characters"
    },
    {
        "case": "Title is too long",
        "firstName": "Test",
        "lastName": "Test",
        "email": "memeber@gmail.com",
        "phone": "5555555",
        "gender": "male",
        "city": "Ottawa",
        "title": "tme9hOY*Jy_#d7bx&&sQ5zLS1+)fq_WM$U(4Ung+Q4i2wVYGWg$",
        "company": "2",
        "whereWeMet": "Q",
        "myNotes": "U",
        "expected_message": "Title length can`t be greater than 50 characters"
    },
    {
        "case": "Company name is too long",
        "firstName": "Test",
        "lastName": "Test",
        "email": "memeber@gmail.com",
        "phone": "5555555",
        "gender": "male",
        "city": "Ottawa",
        "title": "Manager",
        "company": "*=FcunMx!W)(z10J+@y9xPhDg8g!(SI1D8AgLl9621cJgSmEcFH",
        "whereWeMet": "Q",
        "myNotes": "U",
        "expected_message": "Company name length can`t be greater than 50 characters"
    },
    {
        "case": "WhereWeMet field is too long",
        "firstName": "Test",
        "lastName": "Test",
        "email": "memeber@gmail.com",
        "phone": "5555555",
        "gender": "male",
        "city": "Ottawa",
        "title": "Manager",
        "company": "String",
        "whereWeMet": "*%r@XGd(iNa#9YDTS=kBb5rxEVrTGJMs*uuBuzRfS^V2j7pNxWw",
        "myNotes": "U",
        "expected_message": "Where we met length can`t be greater than 50 characters"
    },
    {
        "case": "MyNotes field is too long",
        "firstName": "Test",
        "lastName": "Test",
        "email": "memeber@gmail.com",
        "phone": "5555555",
        "gender": "male",
        "city": "Ottawa",
        "title": "Manager",
        "company": "String",
        "myNotes": "8nH6Pu%2uKS%e!RBiFVDBIZ7*9Hm JL&7cS)OAGBdcW=w5B_T7X%$Ed!31vG&5#4Kw5tJ_ qj(5ud4*L%xT%W%&M" +
                   "m4pU7L5T3V6Ohau2C4juCDMY=g#1BbShWegIu73p^dPvK3p^bhlgcVGB33J4SkBuisO(xChrQQ1WkPsd5qBX6JJSXQR" +
                   "FE0z6GkYnYY!#%RXQ@Fc1",
        "expected_message": "My notes length can`t be greater than 200 characters"
    }
])
def invalid_member_data(request):
    return request.param
