from bank_system.transaction.routes import APIRouteTransaction


def includeme(config):
    config.include(APIRouteTransaction.router, route_prefix='/transactions')
    config.scan()
