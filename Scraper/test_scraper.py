from unittest import TestCase
from Scraper.Scraper import Scraper
from Scraper.Config import Config
from Scraper.Connector import ConnectorType


class TestScraper(TestCase):

    @staticmethod
    def create_config_values():
        return Config(
            url="https://www.airbnb.co.uk/rooms/14531512?s=51",
            connector_type=ConnectorType.ConnectorTypes.Airbnb
        )

    def test_scraper_runs(self):
        # tests if the scraper can set up and run a scrape. This is against live data
        # so will fail once updated. Smelly but will do for now.
        # todo: hitting live target here, should mock the Connector so that we test just the scraper in isolation!!
        scraper = Scraper()
        accommodation_data = scraper.scrape(self.create_config_values())
        self.assertEqual(accommodation_data.bedroom_count, 0)
        self.assertEqual(accommodation_data.bathroom_count, 1)
        self.assertTrue("Garden Rooms" in accommodation_data.property_name)

