from .views import ViewCard


class APIRouteCard:
    @classmethod
    def router(cls, config):
        config.add_route('rest_api_card_list', '/rest_api/list')
        config.add_route('rest_api_card_create', '/rest_api/create')
        config.add_route('rest_api_card_get', 'rest_api/get/{id}')
        config.add_route('rest_api_card_delete', 'rest_api/del/{id}')
        config.add_route('rest_api_card_put', 'rest_api/put/{id}')
        config.add_route('rest_api_card_info', 'rest_api/info/{id}')

        config.add_view(ViewCard, route_name='rest_api_card_create', attr='create_card',
                        request_method='POST')
        config.add_view(ViewCard, route_name='rest_api_card_list', attr='list_cards', request_method='GET')
        config.add_view(ViewCard, route_name='rest_api_card_delete', attr='delete_card',
                        request_method='GET')
        config.add_view(ViewCard, route_name='rest_api_card_get', attr='get_card', request_method='GET')
        config.add_view(ViewCard, route_name='rest_api_card_put', attr='put_card', request_method='PUT')
        config.add_view(ViewCard, route_name='rest_api_card_info', attr='info_card', request_method='GET')
