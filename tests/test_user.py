import requests

from services.auth.helpers.user_helper import UserHelper


class TestUser:

    def test_get_me(self, auth_api_utils_admin):
        user_helper = UserHelper(auth_api_utils_admin)
        response = user_helper.get_me()
        assert response.status_code == requests.status_codes.codes.ok, f"Wrong status code: {response.status_code} expected {requests.status_codes.codes.ok}"
