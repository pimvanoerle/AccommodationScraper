from Scraper.Server.views import connect


def setup_routes(app):
    #todo: consider making this a proper restful endpoint - just a hacky POST api call for now, expecting some JSON
    app.router.add_post('/accommodation', connect)