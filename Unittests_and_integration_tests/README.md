# Pre-Work Questions and Answers
## What is a mock() object, and what is Mock-Testing?
A Mock() object is a simulated object that simulates the behavior of another, real object, like an API or a database.
Its good for doing things like letting you test API requests without sending real requests to a real API. 
## What is unittest.TestCase?
unittest.TestCase serves as the base class for test cases. When you create a test case class, you typically inherit
from 'unittest.TestCase', and your test methods are defined within the class.
## But what are Test Methods?
Test methods are individual functions within the test case class that perform specific tests on your code.
### Example #1, testing with a real API:
```
import unittest
import requests

class APITestCase(unittest.TestCase):
    def test_api_get_request(self):
        # Assume a hypothetical API endpoint for fetching user data
        api_url = 'https://jsonplaceholder.typicode.com/users/1'
        
        # Make a GET request to the API endpoint
        response = requests.get(api_url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Parse the JSON response
        user_data = response.json()

        # Check if the 'name' key is present in the response
        self.assertIn('name', user_data)

        # Check if the 'username' is equal to a specific value
        self.assertEqual(user_data['username'], 'Bret')

    def test_api_post_request(self):
        # Assume a hypothetical API endpoint for creating a new user
        api_url = 'https://jsonplaceholder.typicode.com/users'
        
        # Sample user data for the POST request
        new_user_data = {
            'name': 'John Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com'
        }

        # Make a POST request to the API endpoint
        response = requests.post(api_url, json=new_user_data)

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Parse the JSON response
        created_user_data = response.json()

        # Check if the 'id' key is present in the response
        self.assertIn('id', created_user_data)

        # Optionally, you may add further assertions based on the API's behavior

if __name__ == '__main__':
    unittest.main()
```
*  'test_api_get_request' and 'test_api_post_request' are two test methods that make GET and POST requests, respectively, to a hypothetical API using the requests library. The assertions in each test method check various aspects of the API response to ensure it meets the expected criteria. Adjust the API endpoints and assertions based on the specifics of the API you are testing.

### Example #2, Mock testing an API:
```
import unittest
from unittest.mock import patch, Mock
import requests

class APITestCase(unittest.TestCase):
    @patch('requests.get')
    def test_api_get_request(self, mock_get):
        # Mocking the requests.get function
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'id': 1,
            'name': 'John Doe',
            'username': 'johndoe'
        }
        mock_get.return_value = mock_response

        # Assume a hypothetical API endpoint for fetching user data
        api_url = 'https://jsonplaceholder.typicode.com/users/1'

        # Make a GET request to the API endpoint
        response = requests.get(api_url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Parse the JSON response
        user_data = response.json()

        # Check if the 'name' key is present in the response
        self.assertIn('name', user_data)

        # Check if the 'username' is equal to a specific value
        self.assertEqual(user_data['username'], 'johndoe')

    @patch('requests.post')
    def test_api_post_request(self, mock_post):
        # Mocking the requests.post function
        mock_response = Mock()
        mock_response.status_code = 201
        mock_response.json.return_value = {
            'id': 101,
            'name': 'John Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com'
        }
        mock_post.return_value = mock_response

        # Assume a hypothetical API endpoint for creating a new user
        api_url = 'https://jsonplaceholder.typicode.com/users'

        # Sample user data for the POST request
        new_user_data = {
            'name': 'John Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com'
        }

        # Make a POST request to the API endpoint
        response = requests.post(api_url, json=new_user_data)

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Parse the JSON response
        created_user_data = response.json()

        # Check if the 'id' key is present in the response
        self.assertIn('id', created_user_data)

if __name__ == '__main__':
    unittest.main()

```
* The @patch decorator is used to replace the 'requests.get' and 'requests.post' functions with mock versions. The mock responses are then configured to simulate the behavior of the actual API responses. This allows you to isolate the tests from the actual external API calls and control the responses for testing various scenarios.

### What is Patch()?
The patch() function is part of the unittest.mock module in Python. It is a powerful tool for temporarily replacing an object or a function with a mock object during the execution of a specific code block. This is commonly used in unit testing to isolate the code being tested from external dependencies or to control the behavior of certain functions.
The patch() function can be used both as a decorator or a context manager. When applied as a decorator, it patches the specified target for the duration of the decorated function or method. When used as a context manager, it patches the target for the duration of the block inside the with statement.

# 0. Parameterize a unit test [test_utils.py]
Write the first unit test for utils.access_nested_map
Create a `TestAccessNestedMap` class which inherits from `unittest.TestCase`.
Implements `TestAccessNestedMap.test_access_nested_map` method to test that that the method returns what it is supposed to.
Decorate the method with @parameterized.expand to test the function for following inputs:
```
    nested_map={"a": 1}, path=("a",)
    nested_map={"a": {"b": 2}}, path=("a",)
    nested_map={"a": {"b": 2}}, path=("a", "b")
```
Tests these inputs with `assertEqual` that the function returns the expected result.

# 1. Parameterize a unit test [test_utils.py]

Implement a `TestAccessNestedMap.test_access_nested_map_exception`.  Uses the `assertRaises` context manager to test that a `KeyError` is raised for the following inputs, using `@parameterized.expand`):
```
    nested_map={}, path=("a",)
    nested_map={"a": 1}, path=("a", "b")
```

# 2. Mock HTTP calls [test_utils.py]

Define the `TestGetJson(unittest.TestCase)` class and implements the `TestGetJson.test_get_json` method to test that `utils.get_json` returns the expected result.
Use `unittest.mock.patch` to patch `requests.get`.  Return a `Mock` object with a `json` method that returns `test_payload` which is parameterized alongside the `test_url` that you will pass to `get_json` with the following inputs:
```
    test_url="http://example.com", test_payload={"payload": True}
    test_url="http://holberton.io", test_payload={"payload": False}
```

# 3. Parameterize and patch [test_utils.py]

Implement the `TestMemoize(unittest.TestCase)` class with a `test_memoize` method.
Inside `test_memoize`, defines the following class:
```
    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()
```

# 4. Parameterize and patch as decorators [test_client.py]

Declare the `TesthithubOrgClient(unittest.TestCase)` class and implement the `test_org` method to test that `GithubOrgClient.org` returns the correct value.
Use `@patch` as a decorator to make sure `get_json` is called once with the expected argument but ensures it is not executed.
Use `@parameterized.expand` as a decorator to parameterize the test with a couple of `org` examples to pass to `GithubOrgClient`, in this order:

* google
* abc

# 5. Mocking a property [test_client.py]

`memoize` turns methods into properties.
Implement the `test_public_repos_url` method to unit-test `GithubOrgClient._public_repos_url`.
Use `patch` as a context manager to patch `GithubOrgClient.org` and make it return a known payload.
Test that the result of `_public_repos_url` is the expected one based on the mocked payload.

# 6. More patching [test_client.py]

Implement `TestGithubOrgClient.test_public_repos` to unittest `GithubOrgClient.public_repos`.
Use `@patch` as a decorator to mock `get_json` and make it return a payload.
Use `patch` as a context manager to mock `GithubOrgClient._public_repos_url` and return a value.
Test that the list of repos is what you expect from the chosen payload.
Test that the mocked property and the mocked `get_json` was called once.

# 7. Parameterize [test_client.py]

Implement `TestGithubOrgClient.test_has_license` to unit-test `GithubOrgClient.has_license`.
Parameterize the test with the following inputs:
```
    repo={"license": {"key": "my_license"}}, license_key="my_license"
    repo={"license": {"key": "other_license"}}, license_key="my_license"
```
Also parameterizes the expected returned value.

# 8. Integration test: fixtures [test_client.py]

Create the `TestIntegrationGithubOrgClient(unittest.TestCase)` class and implement the `setUpClass` and `tearDownClass` which are part of the `unittest.TestCase` API.
Use `@parameterized_class` to decorate the class and parameterize it with fixtures found in `fixtures.py`.
The file contains the fixtures `org_payload`, `repos_payload`, `expected_repos`, `apache2_repos`.

The `setupClass` mocks `requests.get` to return example payloads found in the fixtures.
Use `patch` to start a patcher named `get_patcher`, and use `side_effect` to make sure the mock of `requests.get(url).json()` return the correct fixtures for the various values of `url` that you anticipate to receive.

Implements the `tearDownClass` class method to stop the patcher.