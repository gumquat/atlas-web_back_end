#!/usr/bin/env python3
"""testing testing 123"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """CLASS - test the `access_nested_map`function from 'utils.py'
    """
    # below are inputs to be tested in 'access_nested_map'
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """tests 'access_nested_map'
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_output)
    # below are inputs to be tested in 'test_access_nested_map_exception'
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """checks that a `KeyError` gets raised correctly
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(cm.exception.args[0], path[-1])
