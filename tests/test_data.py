import pytest
from inverse_acronym.data import Data

class TestData:
    def test_get_initials(self):
        x = "this is a test"
        new_data = Data("")
        assert new_data._get_initials(x) == "tiat"
        assert new_data._get_initials("") == ""

    def test_get_restults(self):
        x = "hw"
        new_data = Data("")
        new_data._dict['hw'] = 'hello world'
        assert new_data.get_results(x) == "hello world"
        assert new_data.get_results("dfsfd") == "I'm sorry please try another acronym" 

    def test_get_requests(self):
        new_data = Data("Portuguese_idioms")
        new_data.get_requests()
        assert len(new_data._dict) > 0
