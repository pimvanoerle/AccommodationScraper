from Scraper.Connector.ConnectorType import ConnectorTypes

class Config:
    """class that represents a Configuration, consisting of a URL
    and a Connector Type (so that we know what to scrape)
    """

    def __init__(self, url, connector_type):
        self.url = url
        self.connector_type = connector_type

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, val):
        # url must be a string and cannot be empty (or just whitespace). We could test for a
        # minimal URL, but we'll fail anyway at connection at that point, so lets cut that
        # particular bit of complexity.
        if not val.strip():
            raise Exception("url empty or whitespace")
        self.__url = val

    @property
    def connector_type(self):
        return self.__connector_type

    @connector_type.setter
    def connector_type(self, val):
        # type must be one of ConnectorTypes
        if val not in ConnectorTypes:
            raise Exception("connector_type not one of ConnectorTypes enum")
        self.__connector_type = val