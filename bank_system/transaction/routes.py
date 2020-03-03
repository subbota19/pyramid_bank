from .views import ViewTransaction


class APIRouteTransaction:
    @classmethod
    def router(cls, config):
        config.add_route('rest_api_transaction_list', '/rest_api/list')
        config.add_route('rest_api_transaction_create', '/rest_api/create')
        config.add_route('rest_api_transaction_get', 'rest_api/get/{id}')
        config.add_route('rest_api_transaction_delete', 'rest_api/del/{id}')
        config.add_route('rest_api_transaction_put', 'rest_api/put/{id}')
        config.add_route('rest_api_transaction_info', 'rest_api/info/{id}')

        config.add_view(ViewTransaction, route_name='rest_api_transaction_create', attr='create_transaction',
                        request_method='POST')
        config.add_view(ViewTransaction, route_name='rest_api_transaction_list', attr='list_transactions',
                        request_method='GET')
        config.add_view(ViewTransaction, route_name='rest_api_transaction_delete', attr='delete_transaction',
                        request_method='GET')
        config.add_view(ViewTransaction, route_name='rest_api_transaction_get', attr='get_transaction',
                        request_method='GET')
        config.add_view(ViewTransaction, route_name='rest_api_transaction_put', attr='put_transaction',
                        request_method='PUT')
        config.add_view(ViewTransaction, route_name='rest_api_transaction_info', attr='info_transaction',
                        request_method='GET')
