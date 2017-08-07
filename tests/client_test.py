import pytest
import requests
import json
from usda_ndb_client.client import Client
from mock import patch, Mock
from usda_ndb_client.errors import ApiError


class TestClient:
    BASE_URL = 'https://api.nal.usda.gov/ndb'

    @pytest.fixture(scope="module")
    def client(self):
        return Client('DEMO_KEY')

    @pytest.fixture(scope="module")
    def error_response(self):
        text = '{"error": {"message": "whoops!"}}'

        return Mock(
          text=text,
          status_code=400,
          json=lambda: json.loads(text)
        )

    @pytest.fixture(scope="module")
    def sample_response(self):
        text = '{"key1": "value1", "key2": "value2"}'

        return Mock(
          text=text,
          status_code=200,
          json=lambda: json.loads(text)
        )

    def test_food_report(self, client, sample_response):
        with patch('requests.get', return_value=sample_response) as api_call:
            res = client.food_report(ndbno='01009')

            api_call.assert_called_once_with(
                '{0}/{1}'.format(self.BASE_URL, 'V2/reports'),
                params={
                    'format': 'json', 'ndbno': '01009', 'api_key': 'DEMO_KEY'
                }
            )

            assert len(res.__dict__) == 2
            assert res.key1 == 'value1'
            assert res.key2 == 'value2'

    def test_list(self, client, sample_response):
        with patch('requests.get', return_value=sample_response) as api_call:
            res = client.list(offset=50)

            api_call.assert_called_once_with(
                '{0}/{1}'.format(self.BASE_URL, 'list'),
                params={
                    'format': 'json', 'offset': 50, 'api_key': 'DEMO_KEY'
                }
            )

            assert len(res.__dict__) == 2
            assert res.key1 == 'value1'
            assert res.key2 == 'value2'

    def test_nutrients(self, client, sample_response):
        with patch('requests.get', return_value=sample_response) as api_call:
            res = client.nutrients(nutrients='010000')

            api_call.assert_called_once_with(
                '{0}/{1}'.format(self.BASE_URL, 'nutrients'),
                params={
                    'format': 'json', 'nutrients': '010000',
                    'api_key': 'DEMO_KEY'
                }
            )

            assert len(res.__dict__) == 2
            assert res.key1 == 'value1'
            assert res.key2 == 'value2'

    def test_search(self, client, sample_response):
        with patch('requests.get', return_value=sample_response) as api_call:
            res = client.search(q='butter')

            api_call.assert_called_once_with(
                '{0}/{1}'.format(self.BASE_URL, 'search'),
                params={
                    'format': 'json', 'q': 'butter',
                    'api_key': 'DEMO_KEY'
                }
            )

            assert len(res.__dict__) == 2
            assert res.key1 == 'value1'
            assert res.key2 == 'value2'

    def test_api_error(self, client, error_response):
        with patch('requests.get', return_value=error_response) as api_call:
            with pytest.raises(ApiError):
                client.search(q='butter')
