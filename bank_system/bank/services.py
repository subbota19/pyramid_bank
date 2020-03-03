from bank_system.common_package.common_services import CommonServices


class BankServices(CommonServices):
    """This class can contain additional rest_method with different functionality  """

    def get_full_info_about_obj(self, request):
        request_obj = self.connection.query(self.model).filter(self.model.id == request.matchdict['id'])
        response = self._treatment_request(request_obj)
        if request_obj:
            response[request_obj.first().id].update({'card': "this bank doesn't have card"})
            response = self.convert_to_json_format(response)
            if request_obj.first().bank_card:
                response[request_obj.first().id].update(
                    {'card': self._treatment_request(request_obj.first().bank_card)})
        return response

    def list_obj(self):
        request = self.connection.query(self.model)
        response = self._treatment_request(request)
        if request:
            response = self.convert_to_json_format(response)
        return response

    def get_obj(self, request):
        request = self.connection.query(self.model).filter(self.model.id == request.matchdict['id'])
        response = self._treatment_request(request)
        if request:
            response = self.convert_to_json_format(response)
        return response

    @staticmethod
    def convert_to_json_format(response):
        for index in response:
            response[index]['negative_percent'] = str(response[index]['negative_percent'])
            response[index]['budget'] = str(response[index]['budget'])
        return response
