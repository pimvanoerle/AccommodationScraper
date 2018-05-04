from aiohttp import web
from Scraper.Server.routes import setup_routes

# start an async web app
app = web.Application()
setup_routes(app)

# kick off the web server
web.run_app(app, host='127.0.0.1', port=8081)