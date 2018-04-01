# coding: utf-8

"""
    Internal APIs

    The internal apis of LBRY Inc.

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """ UserApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.user_api.UserApi()

    def tearDown(self):
        pass

    def test_user_new_get(self):
        """
        Test case for user_new_get

        Creates new user and returns an authtoken for interaction with the API
        """
        pass


if __name__ == '__main__':
    unittest.main()