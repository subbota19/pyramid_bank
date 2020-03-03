from .views import ViewOperation


class APIRouteOperation:
    @classmethod
    def router(cls, config):
        config.add_route('rest_api_operation_list', '/rest_api/list')
        config.add_route('rest_api_operation_create', '/rest_api/create')
        config.add_route('rest_api_operation_get', 'rest_api/get/{id}')
        config.add_route('rest_api_operation_delete', 'rest_api/del/{id}')
        config.add_route('rest_api_operation_put', 'rest_api/put/{id}')
        config.add_route('rest_api_operation_info', 'rest_api/info/{id}')

        config.add_view(ViewOperation, route_name='rest_api_operation_create', attr='create_operation',
                        request_method='POST')
        config.add_view(ViewOperation, route_name='rest_api_operation_list', attr='list_operations',
                        request_method='GET')
        config.add_view(ViewOperation, route_name='rest_api_operation_delete', attr='delete_operation',
                        request_method='GET')
        config.add_view(ViewOperation, route_name='rest_api_operation_get', attr='get_operation', request_method='GET')
        config.add_view(ViewOperation, route_name='rest_api_operation_put', attr='put_operation', request_method='PUT')
        config.add_view(ViewOperation, route_name='rest_api_operation_info', attr='info_operation',
                        request_method='GET')
