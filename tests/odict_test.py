from usda_ndb_client.odict import ODict


class TestODict:
    def test_init(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        sut = ODict(data)

        assert sut.key1 == data['key1']
        assert sut.key2 == data['key2']
