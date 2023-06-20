""" functions for unit testing """

import json
import logging

import pytest
from rest_framework.test import APIClient

# from utils.functions_for_tests import TestEndpoints
"""
    pytest.ini:
    [pytest]
    DJANGO_SETTINGS_MODULE = gitarista.settings
    python_files = tests.py test_*.py *_tests.py
    log_cli = 1
    log_cli_level = INFO
    log_cli_format = %(message)s
    ; log_cli_format = %(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)
    ; log_cli_date_format=%Y-%m-%d %H:%M:%S
"""


@pytest.fixture
def client():
    return APIClient()


class TestEndpoints:
    """ base test endpoint class """

    pytestmark = pytest.mark.django_db

    logger = logging.getLogger(__name__)

    @staticmethod
    def log(a):
        """ log """
        TestEndpoints.logger.info(a)

    @staticmethod
    def is_equal(obj1, obj2):
        """ compare two python objects """
        return json.dumps(obj1) == json.dumps(obj2)

    @staticmethod
    def api_client():
        """ api_client """
        return APIClient

    @staticmethod
    def fill_test_data(model, test_data: list = None):
        """ fill model with test_data"""
        if test_data is None:
            test_data = model.test_data
        # TODO
        # obj.objects.bulk_create([obj(row) for row in test_data])
        # obj.save()
        for data_dict in test_data:
            new_row = model.objects.create(**data_dict)
            new_row.save()

    def get(self,
            client,
            api_endpoint,
            status_code=200):

        self.log(f'{api_endpoint}')
        response = client.get(api_endpoint)
        self.log(f'\n{response.data}')

        assert response.status_code == status_code
        return response
