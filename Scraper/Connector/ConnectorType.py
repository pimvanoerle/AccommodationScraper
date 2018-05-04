from enum import Enum

class ConnectorTypes(Enum):
    """enum representing possible connector types. this is suboptimal as types need to be added
    to this list when a new connector is made, better to use reflection or the like. It will do
    for this specific case though, and keeping it simple saves on not-yet-needed complexity"""
    Airbnb = 1
