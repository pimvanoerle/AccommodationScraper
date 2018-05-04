from unittest import TestCase
import json
import urllib.request
from Scraper.Connector.ConnectorType import ConnectorTypes
from Scraper.Config import Config
from Scraper.Scraper import Scraper
from Scraper.Accommodation import Accommodation


class TestScraper(TestCase):

    def test_setup_client_and_test_server(self):
        # this needs a running server!! at localhost:8081!
        request = urllib.request.Request(
            data=json.dumps({"url": "https://www.airbnb.co.uk/rooms/14531512?s=51"}).encode('utf8'),
            url="http://127.0.0.1:8081/accommodation"
        )
        request.add_header('Content-Type', 'application/json')

        requested_data = urllib.request.urlopen(
            request
        )
        data = requested_data.read()
        print(data)
        encoding = requested_data.info().get_content_charset('utf-8')
        accommodation = json.loads(data.decode(encoding))
        self.assertEqual(accommodation["bathroom_count"], 1)
        self.assertTrue("Garden Rooms" in accommodation["property_name"])
        self.assertTrue("apartment" in accommodation["property_type"][0])



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
