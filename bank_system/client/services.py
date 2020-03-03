from bank_system.common_package.common_services import CommonServices


class ClientServices(CommonServices):
    """This class can contain additional rest_method with different functionality  """

    def get_full_info_about_obj(self, request):
        request_obj = self.connection.query(self.model).filter(self.model.id == request.matchdict['id'])
        response = self._treatment_request(request_obj)
        if request_obj:
            response[request_obj.first().id].update({'cards': "this card doesn't have card"})
            if request_obj.first().client_card:
                response[request_obj.first().id].update({'cards': self._treatment_request(request_obj.first().client_card)})
        return response
