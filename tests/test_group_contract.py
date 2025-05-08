import requests
from faker import Faker

from services.university.helpers.group_helper import GroupHelper

faker = Faker()


class TestGroupContract:

    def test_create_group_anonym(self, university_api_utils_admin):
        group_helper = GroupHelper(university_api_utils_admin)
        response = group_helper.post_group({"name": faker.name()})
        assert response.status_code == requests.status_codes.codes.created, \
            (f"Wrong status code: {response.status_code},"
             f" expected {requests.status_codes.codes.unauthorized}")

    def test_get_group_by_id(self, university_api_utils_admin):
        group_helper = GroupHelper(university_api_utils_admin)
        response = group_helper.get_group_by_id()
        assert response.status_code == requests.status_codes.codes.ok, f"Wrong status code: {response.status_code}, expected {requests.status_codes.codes.ok}"
