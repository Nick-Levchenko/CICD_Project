import requests

from services.general.helpers.base_helper import BaseHelper


class StudentHelper(BaseHelper):
    ENDPOINT_PREFIX = '/students'
    ROOT_ENDPOINT = f'{ENDPOINT_PREFIX}/'
    GET_STUDENT_ENDPOINT = f'{ENDPOINT_PREFIX}/1/'

    def post_student(self, json: dict) -> requests.Response:
        response = self.api_utils.post(endpoint_url=self.ROOT_ENDPOINT, json=json)
        return response

    def get_student_by_id(self) -> requests.Response:
        response = self.api_utils.get(endpoint_url=self.GET_STUDENT_ENDPOINT)
        return response
