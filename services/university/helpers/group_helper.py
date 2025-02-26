import requests

from services.general.helpers.base_helper import BaseHelper


class GroupHelper(BaseHelper):
    ENDPOINT_PREFIX = '/groups'

    ROOT_ENDPOINT = f'{ENDPOINT_PREFIX}/'
    GROUP_BY_ID = f'{ENDPOINT_PREFIX}/2/'

    def post_group(self, json: dict) -> requests.Response:
        response = self.api_utils.post(endpoint_url=self.ROOT_ENDPOINT, json=json)
        return response

    def get_group_by_id(self) -> requests.Response:
        response = self.api_utils.get(endpoint_url=self.GROUP_BY_ID)
        return response
