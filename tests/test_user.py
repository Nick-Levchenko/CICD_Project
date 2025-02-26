from services.auth.helpers.user_helper import UserHelper


class TestUser:

    def test_get_me(self, auth_api_utils_admin):
        user_helper = UserHelper(auth_api_utils_admin)
        response = user_helper.get_me()
        print(response.json())
