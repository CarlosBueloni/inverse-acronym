import pytest
from inverse_acronym.data import Data
import json

class TestData:
    def test_get_initials(self):
        x = "this is a test"
        new_data = Data()
        assert new_data._get_initials(x) == "tiat"
        assert new_data._get_initials("") == ""

    def test_get_restults(self):
        x = "hw"
        new_data = Data()
        new_data._dict = {'':{}}
        new_data._dict['']['hw'] = ['hello world']
        assert new_data.get_results(x) == ["hello world"]
        assert new_data.get_results("dfsfd") == "I'm sorry please try another acronym" 

    def test_get_requests(self):
        new_data = Data()
        new_data.get_requests("Portuguese_idioms")
        assert len(new_data._dict) > 0

    def test_write_to_file(self):
        new_data = Data()
        new_data._dict = {'category':{'a':['after']}}
        new_data._file_name = 'test_data.json'
        new_data.write_to_file()
        with open(new_data._file_name) as f:
            assert json.load(f) == {'category':{'a':['after']}}


