# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 9
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_2_2
from isi_sdk_8_2_2.api.storagepool_api import StoragepoolApi  # noqa: E501
from isi_sdk_8_2_2.rest import ApiException


class TestStoragepoolApi(unittest.TestCase):
    """StoragepoolApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_2_2.api.storagepool_api.StoragepoolApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_storagepool_nodepool(self):
        """Test case for create_storagepool_nodepool

        """
        pass

    def test_create_storagepool_tier(self):
        """Test case for create_storagepool_tier

        """
        pass

    def test_delete_storagepool_nodepool(self):
        """Test case for delete_storagepool_nodepool

        """
        pass

    def test_delete_storagepool_nodepools(self):
        """Test case for delete_storagepool_nodepools

        """
        pass

    def test_delete_storagepool_tier(self):
        """Test case for delete_storagepool_tier

        """
        pass

    def test_delete_storagepool_tiers(self):
        """Test case for delete_storagepool_tiers

        """
        pass

    def test_get_storagepool_nodepool(self):
        """Test case for get_storagepool_nodepool

        """
        pass

    def test_get_storagepool_nodetype(self):
        """Test case for get_storagepool_nodetype

        """
        pass

    def test_get_storagepool_nodetypes(self):
        """Test case for get_storagepool_nodetypes

        """
        pass

    def test_get_storagepool_settings(self):
        """Test case for get_storagepool_settings

        """
        pass

    def test_get_storagepool_status(self):
        """Test case for get_storagepool_status

        """
        pass

    def test_get_storagepool_storagepools(self):
        """Test case for get_storagepool_storagepools

        """
        pass

    def test_get_storagepool_suggested_protection_nid(self):
        """Test case for get_storagepool_suggested_protection_nid

        """
        pass

    def test_get_storagepool_tier(self):
        """Test case for get_storagepool_tier

        """
        pass

    def test_get_storagepool_unprovisioned(self):
        """Test case for get_storagepool_unprovisioned

        """
        pass

    def test_list_storagepool_nodepools(self):
        """Test case for list_storagepool_nodepools

        """
        pass

    def test_list_storagepool_tiers(self):
        """Test case for list_storagepool_tiers

        """
        pass

    def test_update_storagepool_nodepool(self):
        """Test case for update_storagepool_nodepool

        """
        pass

    def test_update_storagepool_settings(self):
        """Test case for update_storagepool_settings

        """
        pass

    def test_update_storagepool_tier(self):
        """Test case for update_storagepool_tier

        """
        pass


if __name__ == '__main__':
    unittest.main()