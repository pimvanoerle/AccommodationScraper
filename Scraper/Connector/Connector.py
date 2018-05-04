import urllib.request
from Scraper.Config import Config
from Scraper.Accommodation import Accommodation

class Connector:
    """ base Connector class that fetches and parses an accomodation target.
    This base class does nothing much special, and should be extended
    for specific scrape target typess that need it.
    Connector and parser are combined into one to keep things simple, can be
    separated if needed (which then does mean implementing a new type in two places)

    Key notion is that of rate limiting
    """

    @staticmethod
    def parse(retrieved_data):
        """parses the retrieved data.
        Returns an object of type Accommodation, or throws an exception if parsing fails.
        (which we accomplish in this case by building an empty Accommodation object, which will fail)
        """
        return Accommodation()

    def __init__(self, config):
        self.config = config
        self.timeout_seconds = 5
        pass

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, val):
        # there needs to be a config object
        if not isinstance(val, Config):
            raise Exception("config is not a config object")
        self.__config = val

    def retrieve_data(self):
        """Connects to a target url, as given in the instance's config object.
        will time out if taking too long and throw an Exception.
        Will rate limit if another connector instance of the same type is active
        """
        request = urllib.request.Request(
            url=self.config.url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        data = urllib.request.urlopen(
            request,
            timeout=self.timeout_seconds
        )
        if data.status is not 200:
            raise Exception("connection status was not 200")
        return data

    def connect(self):
        return self.parse(self.retrieve_data())

