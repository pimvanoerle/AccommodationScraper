from unittest import TestCase
from Scraper import Scraper


class TestConnector(TestCase):

    def test_config_set_config(self):
        # tests if the connector can be set up with a config
        self.fail()

    def test_config_fail_invalid_config(self):
        # tests if the connector fails when set up with an invalid config
        self.fail()

    def test_config_fail_no_config(self):
        # tests if the connector fails when set up with no config
        self.fail()

    def test_config_fail_no_type(self):
        # tests if the connector fails when set up with no clear type
        self.fail()

    def test_fail_wrong_url(self):
        # tests if the connector fails when set up with no clear type
        self.fail()

    def test_set_rate_limiter(self):
        # tests if the connector accepts a change in the rate limiter
        self.fail()

    def test_set_rate_limiter(self):
        # tests if the connector accepts a change in the timeout
        self.fail()

    def test_call_runner(self):
        # tests if the connector will dry run with a fake target URL
        self.fail()

    def test_rate_limit(self):
        # tests if the connector rate limits
        self.fail()

    def test_parser_returns_empty(self):
        # this base type has no parser, so should return an empty Accommodation object
        self.fail()

