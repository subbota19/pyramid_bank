from .routes import APIRouteClient


def includeme(config):
    config.include(APIRouteClient.router, route_prefix='/clients')
    config.scan()
