from .routes import APIRouteBank


def includeme(config):
    config.include(APIRouteBank.router, route_prefix='/banks')
    config.scan()
