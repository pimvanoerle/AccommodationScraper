import re
from bs4 import BeautifulSoup
from Scraper.Connector.Connector import Connector
from Scraper.Connector.ConnectorType import ConnectorTypes
from Scraper.Accommodation import Accommodation


class ConnectorAirBnB(Connector):
    """ base Connector class that fetches and parses an accomodation target.
    This base class does nothing much special, and should be extended
    for specific scrape target typess that need it.
    Connector and parser are combined into one to keep things simple, can be
    separated if needed (which then does mean implementing a new type in two places)
    """
    type = ConnectorTypes.Airbnb

    ameneties_map = {
        'Kitchen': Accommodation.Amenities.Kitchen,
        'Breakfast': Accommodation.Amenities.Breakfast,
        'Hair dryer': Accommodation.Amenities.HairDryer,
        'Laptop friendly workspace': Accommodation.Amenities.LaptopWorkspace,
        'Iron': Accommodation.Amenities.Iron,
        'Essentials': Accommodation.Amenities.Essentials,
        'Wireless Internet': Accommodation.Amenities.WiFi,
        'TV': Accommodation.Amenities.TV,
        'Cable TV': Accommodation.Amenities.CableTV
    }

    property_type_map = {
        'Entire guesthouse': Accommodation.Types.Apartment,
        'Entire flat': Accommodation.Types.Apartment,
        'Private room in guesthouse': Accommodation.Types.Room_private,
        'Shared room in guesthouse': Accommodation.Types.Room_shared
    }

    @staticmethod
    def parse(retrieved_data):
        """parses the retrieved data for AirBnB using BeautifulSoup.
        Returns an object of type Accommodation, or throws an exception if parsing fails.
        There is an interesting option in that AirBNB pages contain a json object called bootstrapData,
        and we could pull that in for ease of parsing. As it feels fragile to use an hidden object rather
        than what is rendered, for now we'll choose to grab the data from the rendered html objects"""

        bedroomRegExp = "([0-9])+\sbedrooms?|Studio"  #todo: this should come from config
        bathroomRegExp = "([0-9])+\sbath?"  # todo: this should come from config

        # Create a beautifulsoup object and find the data object
        # todo: this is simple to implement but need to look at mem requirements and speed!
        soup = BeautifulSoup(retrieved_data, "html.parser")

        # fish out Property Name (this is a unique class so can just use it straight up)
        property_name = soup.select('h1._1xu9tpch')[0].text.strip()

        # fish out Property Type (this is a unique class so can just use it straight up)
        # this assumes a known property type, it will throw rather than just guess if not.
        property_type = ConnectorAirBnB.property_type_map[soup.select('span._bt56vz6')[0].text.strip()]

        # fish out number of bedrooms (there are multiple elements that share class, so we identify
        # by looking at the text of the element to find the right one. This is really fragile, but as
        # there are no further markers that indicate what element is what, it will have to do.
        # we are looking for 'Bedroom' or 'Studio' as the indicator for number of bedrooms, where we
        # treat Studio as 0 for all intents as purposes (i.e. no seperate bedrooms)
        # todo: we should run regular tests against know scrape targets to make sure we catch change.
        # we'll use regexp to find the elements we're looking for. As Beautifulsoup can only regexp for filtering,
        # this means that we have to be clunky and run another pass of the regexp to find the actual numerical element
        regex = re.compile(bedroomRegExp)
        bedroom_elements = soup.findAll('span', attrs={"class": "_y8ard79"}, text=regex)
        if len(bedroom_elements) == 0:
            raise(Exception("did not find Bedroom elements!"))
        rooms = regex.search(bedroom_elements[0].text).group(1)
        number_bedrooms = 0 if not rooms else rooms

        # fish out number of bathrooms - similar to bedrooms above, but airbnb just uses the '# bath' convention.
        regex = re.compile(bathroomRegExp)
        bathroom_elements = soup.findAll('span', attrs={"class": "_y8ard79"}, text=regex)
        if len(bathroom_elements) == 0:
            raise(Exception("did not find Bathroom elements!"))
        number_bathrooms = regex.search(bathroom_elements[0].text).group(1)

        # find the amenities and map them - we do this by finding the amenities header,
        # and then looking at the next div's contents. This is fragile, so should be tested so that
        # we capture any change.
        # This also only gets the 6 key shortlisted amenities, as the rest is not available until expanded
        # note: could be a really long one liner, split for readability
        amenities_raw = soup.findAll('span', text="Amenities")[0].parent.parent.parent.find_next_sibling('div').select('div._m7iebup')
        amenities_list = [ConnectorAirBnB.ameneties_map.get(item.text, Accommodation.Amenities.Unknown) for item in amenities_raw ]
        return Accommodation(
            property_name=property_name,
            property_type=property_type,
            bedroom_count=int(number_bedrooms),
            bathroom_count=int(number_bathrooms),
            amenities=amenities_list
        )
