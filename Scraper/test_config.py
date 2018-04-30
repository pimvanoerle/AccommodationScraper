from unittest import TestCase
from Scraper.Config import Config
from Scraper.Connector.ConnectorType import ConnectorTypes


class TestConfig(TestCase):

    @staticmethod
    def initialize_config_instance(vals):
        return Config(vals["url"], vals["type"])

    @staticmethod
    def create_config_values():
        return {
            "url": "http://testurl.net/thing",
            "type": ConnectorTypes.Airbnb
        }

    def test_url_fails_if_empty(self):
        # tests the url setter checks for empty and whitespace
        vals = self.create_config_values()

        for url in ["", "    "]:
            vals["url"] = url
            with self.assertRaises(Exception) as cm:
                self.initialize_config_instance(vals)
            err = cm.exception
            self.assertEqual(str(err), 'url empty or whitespace')

    def test_connector_type_fails_if_not_in_enum(self):
        # tests the connector type setter checks for non-membership of the enum
        vals = self.create_config_values()

        for proptype in [None, "string"]:
            vals["type"] = proptype
            with self.assertRaises(Exception) as cm:
                self.initialize_config_instance(vals)
            err = cm.exception
            self.assertEqual(str(err), 'connector_type not one of ConnectorTypes enum')

    def test_property_sets(self):
        # tests the property setters work when all is well
        vals = self.create_config_values()

        instance = self.initialize_config_instance(vals)

        self.assertEqual(vals["url"], instance.url)
        self.assertEqual(vals["type"], instance.connector_type)
