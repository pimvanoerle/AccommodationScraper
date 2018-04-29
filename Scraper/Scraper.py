from enum import Enum
from Scraper import Accommodation

class Scraper:
    """ key scraper class that:
    1) reads a config from config object
    2) finds the right type of connector (there's only one but hey) for each entry
    3) kicks off a scrape asynchronously and sets up a parse on return into generic Accommodation format
    4) dumps the results into a csv file (generically from the Accommodation thing)
    """

    class Types(Enum):
        Airbnb = 1

    def read_config(self, config_object):
        raise Exception("did not find valid scraper type")

