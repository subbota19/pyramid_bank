from pyramid.view import view_defaults
from bank_system.common_package.common_view import CommonRESTView
from .services import BankServices
from bank_system.model.models import Bank


@view_defaults(route_name='rest_api_bank', renderer='json')
class ViewBank:
    def __init__(self, request):
        self.obj_rest_view = CommonRESTView(request, BankServices, Bank)
        self.request = request

    def list_banks(self):
        return self.obj_rest_view.list()

    def get_bank(self):
        return self.obj_rest_view.get()

    def create_bank(self):
        return self.obj_rest_view.create()

    def put_bank(self):
        return self.obj_rest_view.put()

    def delete_bank(self):
        return self.obj_rest_view.delete()

    def info_bank(self):
        return self.obj_rest_view.obj_common_service.get_full_info_about_obj(self.request)
