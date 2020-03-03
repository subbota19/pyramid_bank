from pyramid.view import view_defaults
from bank_system.common_package.common_view import CommonRESTView
from .services import TransactionServices
from bank_system.model.models import Transaction


@view_defaults(route_name='rest_api_transaction', renderer='json')
class ViewTransaction:
    def __init__(self, request):
        self.obj_rest_view = CommonRESTView(request, TransactionServices, Transaction)
        self.request = request

    def list_transactions(self):
        return self.obj_rest_view.list()

    def get_transaction(self):
        return self.obj_rest_view.get()

    def create_transaction(self):
        return self.obj_rest_view.obj_common_service.create_transaction(self.request)

    def put_transaction(self):
        return self.obj_rest_view.put()

    def delete_transaction(self):
        return self.obj_rest_view.delete()

    def info_transaction(self):
        return self.obj_rest_view.obj_common_service.get_full_info_about_obj(self.request)
