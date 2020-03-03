from bank_system.common_package.common_services import CommonServices


class CardServices(CommonServices):
    """This class can contain additional rest_method with different functionality  """

    def get_full_info_about_obj(self, request, check_number=0):
        request_obj = self.connection.query(self.model).filter(self.model.id == request.matchdict['id'])
        response = self._treatment_request(request_obj)
        if request_obj.first():
            response[request_obj.first().id].update({'bank': "this card doesn't have bank"})
            response[request_obj.first().id].update({'client': "this card doesn't have client"})

            response = self.convert_to_json_format(response)
            if request_obj.first().card_bank:
                response[request_obj.first().id].update(
                    {'bank': self._treatment_request([request_obj.first().card_bank])})
            if request_obj.first().card_client:
                response[request_obj.first().id].update(
                    {'client': self._treatment_request([request_obj.first().card_client])})

        return response

    def list_obj(self, check_number=0):
        request = self.connection.query(self.model)
        response = self._treatment_request(request)
        if request.first():
            response = self.convert_to_json_format(response)
        return response

    def get_obj(self, request, check_number=0):
        request = self.connection.query(self.model).filter(self.model.id == request.matchdict['id'])
        response = self._treatment_request(request)
        if request.first():
            response = self.convert_to_json_format(response)
        return response

    @staticmethod
    def convert_to_json_format(response):
        for index in response:
            response[index]['creation_date'] = str(response[index]['creation_date'])
            response[index]['budget'] = str(response[index]['budget'])
        return response
