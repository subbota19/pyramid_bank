from .routes import APIRouteOperation


def includeme(config):
    config.include(APIRouteOperation.router, route_prefix='/operations')
    config.scan()
