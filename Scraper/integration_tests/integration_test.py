from unittest import TestCase
from Scraper.Connector.ConnectorType import ConnectorTypes
from Scraper.Config import Config
from Scraper.Scraper import Scraper
from Scraper.Accommodation import Accommodation


class TestScraper(TestCase):

    def test_airbnb_3_cases_can_be_parsed(self):
        scraper = Scraper()
        config = Config("https://www.airbnb.co.uk/rooms/14531512?s=51", ConnectorTypes.Airbnb)
        accommodation_data = scraper.scrape(config)
        self.assertEqual(accommodation_data.bathroom_count, 1)
        self.assertEqual(accommodation_data.bedroom_count, 0)
        self.assertTrue("Garden Rooms" in accommodation_data.property_name)
        self.assertEqual(accommodation_data.property_type, Accommodation.Types.Apartment)
        self.assertTrue(Accommodation.Amenities.CableTV in accommodation_data.amenities)
        self.assertFalse(Accommodation.Amenities.Unknown in accommodation_data.amenities)
        self.assertFalse(Accommodation.Amenities.Breakfast in accommodation_data.amenities)

        config = Config("https://www.airbnb.co.uk/rooms/19278160?s=51", ConnectorTypes.Airbnb)
        accommodation_data = scraper.scrape(config)
        self.assertEqual(accommodation_data.bathroom_count, 1)
        self.assertEqual(accommodation_data.bedroom_count, 1)
        self.assertTrue("York Place" in accommodation_data.property_name)
        self.assertEqual(accommodation_data.property_type, Accommodation.Types.Apartment)
        self.assertTrue(Accommodation.Amenities.TV in accommodation_data.amenities)
        self.assertTrue(Accommodation.Amenities.WiFi in accommodation_data.amenities)
        self.assertFalse(Accommodation.Amenities.Unknown in accommodation_data.amenities)
        self.assertFalse(Accommodation.Amenities.Essentials in accommodation_data.amenities)

        config = Config("https://www.airbnb.co.uk/rooms/19292873?s=51", ConnectorTypes.Airbnb)
        accommodation_data = scraper.scrape(config)
        self.assertEqual(accommodation_data.bathroom_count, 1)
        self.assertEqual(accommodation_data.bedroom_count, 1)
        self.assertTrue("Turreted" in accommodation_data.property_name)
        self.assertEqual(accommodation_data.property_type, Accommodation.Types.Apartment)
        self.assertTrue(Accommodation.Amenities.LaptopWorkspace in accommodation_data.amenities)
        self.assertFalse(Accommodation.Amenities.TV in accommodation_data.amenities)
