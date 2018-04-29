from Scraper import Accommodation

class Scraper:
    """ central scraper class that:
    1) reads a config from config object
    2) finds the right type of connector (there's only one but hey) for each entry
    3) kicks off a scrape asynchronously and sets up a parse on return into generic Accommodation format
    4) dumps the results into a csv file (generically from the Accommodation thing)
    This class should use AsyncIO to parallelize the tasks it is running (up to a maximum)
    """
    def __init__(self):
        self.max_parallel = 4
        pass

    def scrape(self, config_object):
        """Scrape the target indicate in config_object async.
        Returns an Accommodation object with details
        Throws Exceptions when encountering errors
        """
        raise Exception("Did not find valid scraper type")
