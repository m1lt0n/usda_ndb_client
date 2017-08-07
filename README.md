# USDA NDB API client
[![Build Status](https://travis-ci.org/graffic/ratelimitpy.svg?branch=master)](https://travis-ci.org/m1lt0n/usda_ndb_client)

### Installation
* Clone repository
* cd usda_ndb_client
* install the package (pip install .)

If you want to run the tests, you need to install pytest and pytest-pep8. After that, you can run the tests using the pytest command.

### Usage
The client is quite lightweight but adds a couple conveniences compared to rolling your own implementation. Specifically:

1. When an error occurs as a result from an API call, the client raises an ApiError exception with a custom message that includes information and the specific errors that occurred.
2. Offers shorter access of the resulting json, by wrapping it around an object that allows access of the json keys as attributes (in order to do food.desc.name instead of food['desc']['name']).

In order to use the client, head over to https://ndb.nal.usda.gov/ndb/api/doc and signup in order to obtain an API key.

### Example
```python
from usda_ndb_client.client import Client

client = Client('YOUR_API_KEY')

# get information about a food
data = client.food_report(ndbno='01009')

# access information nested in the response
print(data.foods[0].food.desc.name)
```

There are 4 API endpoints (and methods in the client): food_report, nutrients, search, list.

### Notes
* The package supports only python 3+
* The client supports only JSON responses currently, while the USDA NDB API supports XML too.
* To see which are the required parameters for the available endpoints, check out the documentation of the original API at https://ndb.nal.usda.gov/ndb/api/doc
