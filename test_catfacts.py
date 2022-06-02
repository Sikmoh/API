from unittest import TestCase
from catfacts import Facts


class TestFacts(TestCase):
    def test_catfacts(self):
        fact = Facts()
        fact.request_data_sync('/facts/random', 'cat', 1)
        assert fact.facts_data['type'] == 'cat'

    def test_request_async(self):
        facts = Facts()
        facts.request_data_async('/facts/random', 'cat', 2)
        assert facts.facts_data[0][1]['type'] == 'cat'

    def test_request_async_len(self):
        facts = Facts()
        facts.request_data_async('/facts/random', 'cat', 2)
        assert len(facts.facts_data) == 1
