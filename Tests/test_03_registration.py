import requests
from Tools import tools_for_tests
from frames import models


def test_01_successful_registration():
    assert tools_for_tests.register_user("test@test.com", "qwerty", "qwerty")[0] == 200
    assert tools_for_tests.register_user("test@test.com", "qwerty", "qwerty")[1]["data"][0]["email"] == "test@test.com"
    assert tools_for_tests.register_user("test@test.com", "qwerty", "qwerty")[1]["data"][0]["emailSent"] is True


def test_02_failed_registration(failed_registration):
    assert tools_for_tests.register_user(failed_registration["email"], failed_registration["password"],
                                         failed_registration["confirm_password"])[0] == 400
    assert tools_for_tests.register_user(failed_registration["email"], failed_registration["password"],
                                         failed_registration["confirm_password"])[1]["errors"][0]["message"] == \
        failed_registration["error_message"]
