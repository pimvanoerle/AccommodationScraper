class Connector:
    """ base Connector class that fetches and parses an accomodation target.
    This base class does nothing much special, and should be extended
    for specific scrape target typess that need it.
    Connector and parser are combined into one to keep things simple, can be
    separated if needed (which then does mean implementing a new type in two places)

    Key notion is that of rate limiting
    """

    def __init__(self):
        self.timeout_seconds = 10
        pass

    def do_connect(self):
        """Connects to a target url, as given in the instance's config object.
        will time out if taking too long and throw an Exception.
        Will rate limit if another connector instance of the same type is active
        """
        return None

    def do_parse(self, retrieved_data):
        """parses the retrieved data.
        Returns an object of type Accommodation, or throws and exception if not there.
        """
