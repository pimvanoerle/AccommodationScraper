from Scraper.Connector import connector_helpers


class Scraper:
    """ central scraper class that exists mainly for testing, proper use is through HTTP server"""

    def scrape(self, config_object):
        """Scrape the target indicate in config_object async.
        Returns an Accommodation object with details
        Throws Exceptions when encountering errors
        """
        return connector_helpers.get_connector(config_object).connect()

