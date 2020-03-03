from .views import ViewClient


class APIRouteClient:
    @classmethod
    def router(cls, config):
        config.add_route('rest_api_client_list', '/rest_api/list')
        config.add_route('rest_api_client_create', '/rest_api/create')
        config.add_route('rest_api_client_get', 'rest_api/get/{id}')
        config.add_route('rest_api_client_delete', 'rest_api/del/{id}')
        config.add_route('rest_api_client_put', 'rest_api/put/{id}')
        config.add_route('rest_api_client_info', 'rest_api/info/{id}')

        config.add_view(ViewClient, route_name='rest_api_client_create', attr='create_client',
                        request_method='POST')
        config.add_view(ViewClient, route_name='rest_api_client_list', attr='list_clients', request_method='GET')
        config.add_view(ViewClient, route_name='rest_api_client_delete', attr='delete_client',
                        request_method='GET')
        config.add_view(ViewClient, route_name='rest_api_client_get', attr='get_client', request_method='GET')
        config.add_view(ViewClient, route_name='rest_api_client_put', attr='put_client', request_method='PUT')
        config.add_view(ViewClient, route_name='rest_api_client_info', attr='info_client', request_method='GET')
