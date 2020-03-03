from bank_system.common_package.common_services import CommonServices


class OperationServices(CommonServices):
    """This class can contain additional rest_method with different functionality  """

    def get_full_info_about_obj(self, request):
        request_obj = self.connection.query(self.model).filter(self.model.id == request.matchdict['id'])
        response = self._treatment_request(request_obj)
        if request_obj.first():
            response[request_obj.first().id].update({'transactions': "this operation doesn't have transactions"})
            if request_obj.first().card:
                response[request_obj.first().id].update(
                    {'transactions': self._treatment_request(request_obj.first().card)})
        return response
