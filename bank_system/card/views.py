from pyramid.view import view_defaults
from bank_system.common_package.common_view import CommonRESTView
from .services import CardServices
from bank_system.model.models import Card


@view_defaults(route_name='rest_api_card', renderer='json')
class ViewCard:
    def __init__(self, request):
        self.obj_rest_view = CommonRESTView(request, CardServices, Card)
        self.request = request

    def list_cards(self):
        return self.obj_rest_view.list()

    def get_card(self):
        return self.obj_rest_view.get()

    def create_card(self):
        return self.obj_rest_view.create()

    def put_card(self):
        return self.obj_rest_view.put()

    def delete_card(self):
        return self.obj_rest_view.delete()

    def info_card(self):
        return self.obj_rest_view.obj_common_service.get_full_info_about_obj(self.request)
