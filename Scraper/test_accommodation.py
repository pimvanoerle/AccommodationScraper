from unittest import TestCase
from Scraper.Accommodation import Accommodation


class TestAccommodation(TestCase):

    @staticmethod
    def initialize_accommodation_instance(vals):
        return Accommodation(vals["name"], vals["type"], vals["bedrooms"], vals["bathrooms"], vals["amenities"])

    @staticmethod
    def create_property_values():
        return {
            "name": "name",
            "type": Accommodation.Types.Apartment,
            "bedrooms": 1,
            "bathrooms": 1,
            "amenities": [Accommodation.Amenities["LaptopWorkspace"], Accommodation.Amenities["WiFi"]]
        }

    def test_empty_accommodation_fails(self):
        # tests if the accommodation objects refuses to init empty
        self.assertRaises(Exception, self.initialize_accommodation_instance)

    def test_property_name_fails_if_empty_or_too_long(self):
        # tests the property name setter checks for empty, whitespace and too-large strings
        vals = self.create_property_values()

        for name in ["", "    ", "g"*(Accommodation.name_max_char+1)]:
            vals["name"] = name
            with self.assertRaises(Exception) as cm:
                self.initialize_accommodation_instance(vals)
            err = cm.exception
            self.assertEqual(str(err), 'property_name empty or too long')

    def test_max_name_char_can_be_changed(self):
        # tests the max name char setter
        vals = self.create_property_values()
        original_max = Accommodation.name_max_char
        vals["name"] = "g"*original_max
        instance = self.initialize_accommodation_instance(vals)
        self.assertEqual(vals["name"], instance.property_name)

        Accommodation.name_max_char = original_max - 1
        with self.assertRaises(Exception) as cm:
            self.initialize_accommodation_instance(vals)
        err = cm.exception
        self.assertEqual(str(err), 'property_name empty or too long')

    def test_property_type_fails_if_not_in_enum(self):
        # tests the property type setter checks for non-membership of the enum
        vals = self.create_property_values()

        for proptype in [None, "string"]:
            vals["type"] = proptype
            with self.assertRaises(Exception) as cm:
                self.initialize_accommodation_instance(vals)
            err = cm.exception
            self.assertEqual(str(err), 'property_type not one of Types enum')

    def test_bedroom_count_fails_if_wrong(self):
        # tests the bedroom setter tests for values zero or smaller, or lager than max.
        vals = self.create_property_values()

        for bedrooms in [-1, Accommodation.max_bedrooms + 1]:
            vals["bedrooms"] = bedrooms
            with self.assertRaises(Exception) as cm:
                self.initialize_accommodation_instance(vals)
            err = cm.exception
            self.assertEqual(str(err), 'bedroom_count smaller than zero or larger than max_bedrooms')

    def test_max_bedroom_count_can_be_changed(self):
        # tests the max bedroom setter
        vals = self.create_property_values()
        original_max = Accommodation.max_bedrooms
        vals["bedrooms"] = original_max
        instance = self.initialize_accommodation_instance(vals)
        self.assertEqual(vals["bedrooms"], instance.bedroom_count)

        Accommodation.max_bedrooms = original_max - 1
        with self.assertRaises(Exception) as cm:
            self.initialize_accommodation_instance(vals)
        err = cm.exception
        self.assertEqual(str(err), 'bedroom_count smaller than zero or larger than max_bedrooms')

    def test_bathroom_count_fails_if_wrong(self):
        # tests the bathroom setter tests for values zero or smaller, or lager than max.
        vals = self.create_property_values()

        for bathrooms in [0, -1, Accommodation.max_bathrooms + 1]:
            vals["bathrooms"] = bathrooms
            with self.assertRaises(Exception) as cm:
                self.initialize_accommodation_instance(vals)
            err = cm.exception
            self.assertEqual(str(err), 'bathroom_count smaller than one or larger than max_bathrooms')

    def test_max_bathroom_count_can_be_changed(self):
        # tests the max bathroom setter
        vals = self.create_property_values()
        original_max = Accommodation.max_bathrooms
        vals["bathrooms"] = original_max
        instance = self.initialize_accommodation_instance(vals)
        self.assertEqual(vals["bathrooms"], instance.bathroom_count)

        Accommodation.max_bathrooms = original_max - 1
        with self.assertRaises(Exception) as cm:
            self.initialize_accommodation_instance(vals)
        err = cm.exception
        self.assertEqual(str(err), 'bathroom_count smaller than one or larger than max_bathrooms')

    def test_amenity_type_fails_if_not_in_enum(self):
        # tests the property amenity setter checks for non-membership of the enum
        vals = self.create_property_values()

        for amenity in [
            [Accommodation.Amenities["LaptopWorkspace"], None],
            ["string", Accommodation.Amenities["LaptopWorkspace"]],
        ]:
            vals["amenities"] = amenity
            with self.assertRaises(Exception) as cm:
                self.initialize_accommodation_instance(vals)
            err = cm.exception
            self.assertEqual(str(err), 'one or more amenities not of Amenities enum')

    def test_property_sets(self):
        # tests the property setters work when all is well
        vals = self.create_property_values()

        instance = self.initialize_accommodation_instance(vals)

        self.assertEqual(vals["name"], instance.property_name)
        self.assertEqual(vals["type"], instance.property_type)
        self.assertEqual(vals["bedrooms"], instance.bedroom_count)
        self.assertEqual(vals["bathrooms"], instance.bathroom_count)
        self.assertEqual(vals["amenities"], instance.amenities)

    def test_property_sets_with_no_amenities(self):
        # tests the property setters work with empty amenities
        vals = self.create_property_values()
        vals["amenities"] = []

        instance = self.initialize_accommodation_instance(vals)

        self.assertEqual(vals["name"], instance.property_name)
        self.assertEqual(vals["type"], instance.property_type)
        self.assertEqual(vals["bedrooms"], instance.bedroom_count)
        self.assertEqual(vals["bathrooms"], instance.bathroom_count)
        self.assertEqual(vals["amenities"], instance.amenities)
