from enum import Enum

class Accommodation:
    """Class that represents a generic Accommodation"""

    # some default constraints
    name_max_char = 1024
    max_bedrooms = 128
    max_bathrooms = 128

    # types of accommodation
    # todo: only focused on airbnb-relevant types, needs extending to a generic list
    class Types(Enum):
        Apartment = "type_apartment",
        Room_private = "type_room_private",
        Room_shared = "type_room_shared"

    # types of amenities
    # todo: only focused on airbnb-relevant types, needs extending to a generic list
    class Amenities(Enum):
        Kitchen = "kitchen",
        WiFi = "am_wifi",
        CableTV = "am_cable_tv",
        TV = "am_tv",
        HairDryer ="am_hair_dryer",
        LaptopWorkspace = "am_laptop_workspace",
        Iron = "am_iron",
        Breakfast = "am_breakfast",
        Essentials = "am_essentials",
        Unknown = "am_unknown"

    def __init__(self, property_name, property_type, bedroom_count, bathroom_count, amenities):
        self.property_name = property_name
        self.property_type = property_type
        self.bedroom_count = bedroom_count
        self.bathroom_count = bathroom_count
        self.amenities = amenities

    def serialize(self):
        """helper function to serialize to a dict for easy json output"""

        return {
            "property_name": self.property_name,
            "property_type": self.property_type.value,
            "bedroom_count": self.bedroom_count,
            "bathroom_count": self.bathroom_count,
            "amenities": [item.value for item in self.amenities]
        }

    @property
    def property_name(self):
        return self.__property_name

    @property_name.setter
    def property_name(self, val):
        # name must be a string, cannot be empty (or just whitespace), nor too long
        if not val.strip() or len(val) > self.name_max_char:
            raise Exception("property_name empty or too long")
        self.__property_name = val

    @property
    def property_type(self):
        return self.__property_type

    @property_type.setter
    def property_type(self, val):
        # type must be one of Types
        if val not in self.Types:
            raise Exception("property_type not one of Types enum")
        self.__property_type = val

    @property
    def bedroom_count(self):
        return self.__bedroom_count

    @bedroom_count.setter
    def bedroom_count(self, val):
        # bedroom_count can be zero but must be less or equal to a sensible max
        if val < 0 or val > self.max_bedrooms:
            raise Exception("bedroom_count smaller than zero or larger than max_bedrooms")
        self.__bedroom_count = val

    @property
    def bathroom_count(self):
        return self.__bathroom_count

    @bathroom_count.setter
    def bathroom_count(self, val):
        # bathroom_count must be one or larger and less or equal to a sensible max
        # todo: check assumption that there is always one bedroom at least (and check max)
        if val <= 0 or val > self.max_bathrooms:
            raise Exception("bathroom_count smaller than one or larger than max_bathrooms")
        self.__bathroom_count = val

    @property
    def amenities(self):
        return self.__amenities

    @amenities.setter
    def amenities(self, val):
        # type must be one of Amenities
        for amenity in val:
            if amenity not in self.Amenities:
                raise Exception("one or more amenities not of Amenities enum")
        self.__amenities = val
