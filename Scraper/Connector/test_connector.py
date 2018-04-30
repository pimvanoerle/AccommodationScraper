from unittest import TestCase
from Scraper.Connector.Connector import Connector
from Scraper.Connector.ConnectorType import ConnectorTypes
from Scraper.Config import Config


class TestConnector(TestCase):

    @staticmethod
    def create_config_instance():
        return Config("http://www.google.com", ConnectorTypes.Airbnb)

    def test_config_set_config(self):
        # tests if the connector can be set up with a config
        config = self.create_config_instance()
        connector = Connector(config)
        self.assertEqual(connector.config, config)

    def test_config_fail_invalid_config(self):
        # tests if the connector fails when set up with an invalid or no config
        for config in [None, "string"]:
            with self.assertRaises(Exception) as cm:
                Connector(config)
            err = cm.exception
            self.assertEqual(str(err), 'config is not a config object')

    def test_fail_wrong_url(self):
        # tests if the connector fails when set up with a wrong url
        config = self.create_config_instance()
        config.url = "http://doesnotexist"
        connector = Connector(config)
        with self.assertRaises(Exception) as cm:
            connector.retrieve_data()
        err = cm.exception
        self.assertEqual(str(err), '<urlopen error [Errno 8] nodename nor servname provided, or not known>')

    def test_set_rate_limiter(self):
        # tests if the connector accepts a change in the rate limiter
        self.fail()

    def test_set_timeout(self):
        # tests if the connector accepts a change in the timeout
        self.fail()

    def test_call_retrieve_data(self):
        # tests if the connector can run when be set up with a test config
        config = self.create_config_instance()
        connector = Connector(config)
        data = connector.retrieve_data()
        self.assertIsNotNone(data)
        self.assertEquals(data.status, 200)

    def test_rate_limit(self):
        # tests if the connector rate limits
        self.fail()

    def test_parser_returns_empty(self):
        # this base type has no parser, so should return an empty Accommodation object
        self.fail()

