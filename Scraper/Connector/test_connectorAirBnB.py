from unittest import TestCase
from Scraper.Connector.ConnectorType import ConnectorTypes
from Scraper.Config import Config
from Scraper.Connector.ConnectorAirBnB import ConnectorAirBnB


class TestScraper(TestCase):

    @staticmethod
    def create_config_instance():
        return Config("https://www.airbnb.co.uk/rooms/14531512?s=51", ConnectorTypes.Airbnb)

    def test_parser_returns_accommodation(self):
        # parse a pre-set chunk of data and see if the parser returns as expected
        self.fail()


    ## this is really an integration test, should move it there
    def test_airbnb_can_be_parsed(self):
        config = self.create_config_instance()
        connector = ConnectorAirBnB(config)
        accommodation_data = connector.connect()
        self.assertEqual(1, accommodation_data.bathroom_count)
