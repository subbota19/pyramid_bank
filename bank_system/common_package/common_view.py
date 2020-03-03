from bank_system.common_package.common_services import CommonServices


class CommonRESTView:
    def __init__(self, request, services, model):
        self.request = request
        self.obj_common_service = services(model)

    def list(self):
        return self.obj_common_service.list_obj()

    def get(self):
        return self.obj_common_service.get_obj(self.request)

    def create(self):
        return self.obj_common_service.create_obj(self.request)

    def put(self):
        return self.obj_common_service.put_obj(self.request)

    def delete(self):
        return self.obj_common_service.delete_obj(self.request)
