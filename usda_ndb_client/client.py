import requests
import json
from .errors import ApiError
from .odict import ODict


class Client:
    '''The API client with all 4 endpoints to the USDA NDB API

    Specifically the endpoint methods are:

    * food_report
    * list
    * nutrients
    * search

    For more information on the request parameters and response
    body, read the documentation of the USDA NDB API at:

    https://ndb.nal.usda.gov/ndb/api/doc

    The endpoint methods accept the request parameters as keyword
    arguments and return an ODict object, which is a convenience
    object that allows accessing the json response content as
    object attributes instead of dict keys.

    In case of errors in the API call, the client raises an
    ApiError exception with information about the error that
    has occurred.
    '''

    BASE_URL = 'https://api.nal.usda.gov/ndb'
    FORMAT = 'json'

    def __init__(self, api_key):
        self.api_key = api_key

    def food_report(self, **kwargs):
        return self._call('V2/reports', **kwargs)

    def list(self, **kwargs):
        return self._call('list', **kwargs)

    def nutrients(self, **kwargs):
        return self._call('nutrients', **kwargs)

    def search(self, **kwargs):
        return self._call('search', **kwargs)

    def _call(self, ep, **kwargs):
        url = '{0}/{1}'.format(self.BASE_URL, ep)
        kwargs.update({'format': self.FORMAT, 'api_key': self.api_key})

        response = requests.get(url, params=kwargs)

        if response.status_code >= 400:
            raise ApiError(
                'An error occurred. Details: {0}'.format(response.json())
            )

        odict_response = json.loads(response.text, object_hook=ODict)
        return odict_response
