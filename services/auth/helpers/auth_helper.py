from services.general.helpers.base_helper import BaseHelper


class AuthHelper(BaseHelper):
    AUTH_URL = "http://localhost:8000"
    REGISTER_ENDPOINT = "/auth/register/"
    LOGIN_ENDPOINT = "/auth/login/"
    GET_USER_ENDPOINT = "/users/me/"

    def post_register(self, data: dict):
        response = self.api_utils.post(self.REGISTER_ENDPOINT, data=data)
        return response

    def post_login(self, data: dict):
        response = self.api_utils.post(self.LOGIN_ENDPOINT, data=data)
        return response

    def get_me(self):
        response = self.api_utils.get(self.GET_USER_ENDPOINT)
        return response
