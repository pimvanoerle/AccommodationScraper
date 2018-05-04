from Scraper.Connector.ConnectorType import ConnectorTypes
from Scraper.Connector.ConnectorAirBnB import ConnectorAirBnB


def get_connector(config):
    """helper function that gets the right connector for the type requested"""
    if config.connector_type is ConnectorTypes.Airbnb:
        return ConnectorAirBnB(config)
    else:
        raise(Exception("Unknown Connector Type - the class for it has not been added to get_connector"))
