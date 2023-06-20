""" functions for unit testing """

from rest_framework.test import APIClient
import json
import logging
import pytest
# pytestmark = pytest.mark.django_db


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
