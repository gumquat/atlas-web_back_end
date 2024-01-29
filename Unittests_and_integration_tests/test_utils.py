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


class TestGetJson(unittest.TestCase):
    """CLASS - test the `get_json` function 'utils.py'
    """
    # below are inputs to be tested in 'test_get_json'
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """tests that `utils.get_json` returns correctly
        """
        mock_response = Mock()
        mock_response.json.return_value = payload
        with patch('requests.get', return_value=mock_response) as mock_get:
            response = get_json(url)
            mock_get.assert_called_once_with(url)
            self.assertEqual(response, payload)


class TestMemoize(unittest.TestCase):
    """CLASS - test the `memoize` function from 'utils.py'
    """

    def test_memoize(self):
        """test `memoize` with a TestClass class
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mock_method.assert_called_once()
