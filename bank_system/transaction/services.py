from bank_system.common_package.common_services import CommonServices
from bank_system.model.models import Transaction
from sqlalchemy import desc


class TransactionServices(CommonServices):
    """This class can contain additional rest_method with different functionality  """

    def get_full_info_about_obj(self, request):
        request_obj = self.connection.query(self.model).filter(self.model.id == request.matchdict['id'])
        response = self._treatment_request(request_obj)
        if request_obj.first():
            response[request_obj.first().id].update({'cards': "this transaction doesn't have card"})
            response[request_obj.first().id].update({'operations': "this transaction doesn't have operation"})
            if request_obj.first().card_r or request_obj.first().card_s:
                response[request_obj.first().id].update(
                    {'cards': {'recipient': self._treatment_request([request_obj.first().card_r]),
                               'sender': self._treatment_request([request_obj.first().card_s])}})
            if request_obj.first().operation:
                response[request_obj.first().id].update(
                    {'operations': self._treatment_request([request_obj.first().operation])})
        return response

    def create_transaction(self, request):
        response = self.create_obj(request)
        if 'operation_id' in response:
            transaction_obj = self.connection.query(self.model).order_by(desc(self.model.creation_date)).first()
            if transaction_obj.card_s.budget >= transaction_obj.operation.cost:
                transaction_obj.card_s.budget -= transaction_obj.operation.cost
            if transaction_obj.card_s.card_bank.name == transaction_obj.card_r.card_bank.name:
                transaction_obj.card_r.budget += transaction_obj.operation.cost
            else:
                transaction_obj.card_r.budget += transaction_obj.operation.cost * (
                        1 - transaction_obj.card_s.card_bank.negative_percent)

                transaction_obj.card_s.card_bank.budget += \
                    transaction_obj.operation.cost * transaction_obj.card_s.card_bank.negative_percent

            transaction_obj.status = True
            self.connection.commit()
        return response
