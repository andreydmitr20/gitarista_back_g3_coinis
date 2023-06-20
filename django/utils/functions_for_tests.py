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


class Endpoints:
    """ base test endpoint class """

    pytestmark = pytest.mark.django_db

    logger = logging.getLogger(__name__)

    @staticmethod
    def log(a):
        """ log """
        Endpoints.logger.info(a)

    @staticmethod
    def is_equal(obj1, obj2):
        """ compare two python objects """
        return json.dumps(obj1) == json.dumps(obj2)

    @staticmethod
    def api_client():
        """ api_client """
        return APIClient

    def fill_model(self, model):
        """ fill model with test_data"""
        if self.test_data is None:
            self.test_data = model.test_data
        # TODO
        # obj.objects.bulk_create([obj(row) for row in test_data])
        # obj.save()
        for data_dict in self.test_data:
            new_row = model.objects.create(**data_dict)
            new_row.save()

    def get(self,
            client,
            api_endpoint,
            status_code=200,
            negative_status_code_test=False):

        self.log(f'GET {api_endpoint}')
        response = client.get(api_endpoint)
        self.log(f'\n{response.data}\n')

        result = response.status_code == status_code

        if negative_status_code_test:
            result = not result
        assert result
        return response

    def post(self,
             client,
             api_endpoint,
             data,
             status_code=201,
             negative_status_code_test=False):

        self.log(f'POST {api_endpoint}')
        self.log(f'{data}')

        response = client.post(api_endpoint,
                               content_type='application/json',
                               data=data)
        self.log(f'\n{response.data}\n')

        result = response.status_code == status_code
        if negative_status_code_test:
            result = not result
        assert result
        return response

    def put(self,
            client,
            api_endpoint,
            data,
            status_code=200,
            negative_status_code_test=False):

        self.log(f'PUT {api_endpoint}')
        self.log(f'{data}')

        response = client.put(api_endpoint,
                              content_type='application/json',
                              data=data)
        self.log(f'\n{response.data}\n')

        result = response.status_code == status_code
        if negative_status_code_test:
            result = not result
        assert result
        return response

    def delete(self,
               client,
               api_endpoint,
               status_code=204,
               negative_status_code_test=False):

        self.log(f'DELETE {api_endpoint}\n')

        response = client.delete(api_endpoint)

        result = response.status_code == status_code
        if negative_status_code_test:
            result = not result
        assert result
        return response

    def get_assert(self,
                   client,
                   api_endpoint,
                   expected_data=None,
                   negative_expected_data_test=False,
                   negative_status_code_test=False):

        response = self.get(client,
                            api_endpoint,
                            negative_status_code_test=negative_status_code_test)

        if expected_data is None:
            expected_data = []
        else:
            expected_data = [expected_data]

        result = self.is_equal(
            response.data,
            expected_data
        )
        if negative_expected_data_test:
            result = not result
        assert result
        return response


class ListEndpoints(Endpoints):
    """ tests for table with pk_id """

    endpoint = None
    model = None
    model_pk_field_name = None
    model_search_field_name = None
    temp_data = None

    # --------------------

    def test_get_count_bad(self, client):

        self.fill_model(self.model)

        self.get_assert(
            client,

            self.endpoint +
            '0/',

            expected_data={'count': len(self.test_data)},
            negative_expected_data_test=True)

    # ++++++++++++++++++++

    def test_get_count0(self, client):

        self.get_assert(
            client,
            self.endpoint +
            '0/?page=0',

            expected_data={'count': 0})

    def test_get_count(self, client):

        self.fill_model(self.model)

        self.get_assert(
            client,

            self.endpoint +
            '0/?page=0',

            expected_data={'count': len(self.test_data)})

    def test_get_search(self, client):

        self.fill_model(self.model)

        self.get_assert(
            client,

            self.endpoint +
            '0/?page_size=1000&search=' +
            self.test_data[0][self.model_search_field_name],

            expected_data={
                self.model_pk_field_name: 1,
                **self.test_data[0]
            }
        )

    def test_get_short(self, client):

        self.fill_model(self.model)

        pk_id = 2

        self.get_assert(
            client,

            self.endpoint +
            str(pk_id) +
            '/?page_size=1000&short=1',

            expected_data={
                self.model_pk_field_name: pk_id,
                self.model_search_field_name:
                self.test_data[pk_id -
                               1][self.model_search_field_name]
            }
        )

    def test_post(self, client):

        self.fill_model(self.model)

        expected_data = {
            self.model_pk_field_name: len(self.test_data)+1,
            **self.temp_data
        }

        response = self.post(
            client,
            self.endpoint +
            '0/',
            self.temp_data
        )

        assert self.is_equal(response.data, expected_data)

        self.get_assert(
            client,

            self.endpoint +
            str(expected_data[self.model_pk_field_name])+'/',

            expected_data
        )

    def test_put(self, client):

        self.fill_model(self.model)

        pk_id = 2
        api_endpoint = self.endpoint + str(pk_id)+'/'
        expected_data = {
            self.model_pk_field_name: pk_id,
            ** self.test_data[pk_id-1]
        }

        self.get_assert(client, api_endpoint, expected_data)

        response = self.put(client, api_endpoint, self.temp_data)

        expected_data = {
            **expected_data,
            **self.temp_data
        }

        assert self.is_equal(
            response.data,
            expected_data
        )

        self.get_assert(client, api_endpoint, expected_data)

    def test_delete(self, client):

        self.fill_model(self.model)

        pk_id = 2
        api_endpoint = self.endpoint + str(pk_id)+'/'
        expected_data = {
            self.model_pk_field_name: pk_id,
            ** self.test_data[pk_id-1]
        }

        self.get_assert(client, api_endpoint, expected_data)
        self.delete(client, api_endpoint)
        self.get_assert(client, api_endpoint, None)
