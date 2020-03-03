from pyramid.view import view_defaults
from bank_system.common_package.common_view import CommonRESTView
from .services import OperationServices
from bank_system.model.models import Operation


@view_defaults(route_name='rest_api_operation', renderer='json')
class ViewOperation:
    def __init__(self, request):
        self.obj_rest_view = CommonRESTView(request, OperationServices, Operation)
        self.request = request

    def list_operations(self):
        return self.obj_rest_view.list()

    def get_operation(self):
        return self.obj_rest_view.get()

    def create_operation(self):
        return self.obj_rest_view.create()

    def put_operation(self):
        return self.obj_rest_view.put()

    def delete_operation(self):
        return self.obj_rest_view.delete()

    def info_operation(self):
        return self.obj_rest_view.obj_common_service.get_full_info_about_obj(self.request)
