class ConnectorAirBnB():
    """ base Connector class that fetches and parses an accomodation target.
    This base class does nothing much special, and should be extended
    for specific scrape target typess that need it.
    Connector and parser are combined into one to keep things simple, can be
    separated if needed (which then does mean implementing a new type in two places)
    """
    type = None

    def __init__(self):
        pass
