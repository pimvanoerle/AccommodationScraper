import logging
import sys
from aiohttp import web
from Scraper.Connector import connector_helpers
from Scraper.Connector.ConnectorType import ConnectorTypes
from Scraper.Config import Config


async def connect(request):
    config_object = None
    body = await request.json()
    try:
        if "airbnb" in body["url"]:
            config_object = Config(url=body["url"], connector_type=ConnectorTypes.Airbnb)
        else:
            return web.Response(status=400, text='could not handle url type')
    except:
        return web.Response(status=400, text='could not parse json object coming in, should be of shape { url="http://url, type=airbnb"  }')

    try:
        data_object = connector_helpers.get_connector(config_object).connect()
        serialized = data_object.serialize()
        return web.json_response(data_object.serialize())
    except:
        return web.Response(status=500, text='An exception occured (this should be a tad more helpful really)')