from .routes import APIRouteCard


def includeme(config):
    config.include(APIRouteCard.router, route_prefix='/cards')
    config.scan()
