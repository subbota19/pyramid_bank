from pyramid.view import view_defaults
from bank_system.common_package.common_view import CommonRESTView
from .services import ClientServices
from bank_system.model.models import Client


@view_defaults(route_name='rest_api_client', renderer='json')
class ViewClient:
    def __init__(self, request):
        self.obj_rest_view = CommonRESTView(request, ClientServices, Client)
        self.request = request

    def list_clients(self):
        return self.obj_rest_view.list()

    def get_client(self):
        return self.obj_rest_view.get()

    def create_client(self):
        return self.obj_rest_view.create()

    def put_client(self):
        return self.obj_rest_view.put()

    def delete_client(self):
        return self.obj_rest_view.delete()

    def info_client(self):
        return self.obj_rest_view.obj_common_service.get_full_info_about_obj(self.request)
