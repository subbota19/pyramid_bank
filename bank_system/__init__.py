from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)

    config.include('bank_system.card')
    config.include('bank_system.operation')
    config.include('bank_system.client')
    config.include('bank_system.bank')
    config.include('bank_system.transaction')
    return config.make_wsgi_app()
