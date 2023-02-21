import requests
import json


class TestSyntheticCrud:
    def test_get_request(self):
        response = requests.get('some_url')
        assert response.status_code == 200

    def test_post_request(self):
        url = 'some_url'
        headers = {'key': 'value', 'key1': 'value1'}
        data = {'key': 'value', 'key1': 'value1', 'key2': 'value2'}
        response = requests.post(url, headers=headers, json=data)
        assert response.status_code == 201

    def test_put_request(self):
        url = 'some_url'
        headers = {'key': 'value', 'key1': 'value1'}
        data = {'key': 'value', 'key1': 'value1', 'key2': 'value2'}
        response = requests.put(url, headers=headers, json=data)
        assert json.loads(response.text).get('key')

    def test_delete_request(self):
        url = 'some url'
        data = {'id': 'value'}
        response = requests.delete(url, json=data)
        assert response.status_code == 204
