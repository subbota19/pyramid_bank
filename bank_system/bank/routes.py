from .views import ViewBank


class APIRouteBank:
    @classmethod
    def router(cls, config):
        config.add_route('rest_api_bank_list', '/rest_api/list')
        config.add_route('rest_api_bank_create', '/rest_api/create')
        config.add_route('rest_api_bank_get', 'rest_api/get/{id}')
        config.add_route('rest_api_bank_delete', 'rest_api/del/{id}')
        config.add_route('rest_api_bank_put', 'rest_api/put/{id}')
        config.add_route('rest_api_bank_info', 'rest_api/info/{id}')

        config.add_view(ViewBank, route_name='rest_api_bank_create', attr='create_bank',
                        request_method='POST')
        config.add_view(ViewBank, route_name='rest_api_bank_list', attr='list_banks', request_method='GET')
        config.add_view(ViewBank, route_name='rest_api_bank_delete', attr='delete_bank',
                        request_method='GET')
        config.add_view(ViewBank, route_name='rest_api_bank_get', attr='get_bank', request_method='GET')
        config.add_view(ViewBank, route_name='rest_api_bank_put', attr='put_bank', request_method='PUT')
        config.add_view(ViewBank, route_name='rest_api_bank_info', attr='info_bank', request_method='GET')
