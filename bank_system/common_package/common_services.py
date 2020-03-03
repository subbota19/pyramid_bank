from bank_system.model import meta
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
from abc import ABC, abstractmethod


class CommonServices(ABC):
    def __init__(self, model):
        self.connection = sessionmaker(bind=meta.Base.engine)()
        self.model = model

    @abstractmethod
    def get_full_info_about_obj(self, request):
        pass

    def create_obj(self, request, with_commit=True):
        try:
            self.connection.add(self.model(**request.POST))
            if with_commit:
                self.connection.commit()
            response = dict(request.POST)
        except exc.IntegrityError:
            response = {'integrity_error': 'this object is already exist'}
            if self.model.__tablename__ == 'transactions':
                response = {"integrity_error": "this object doesn't exist "}
        except KeyError:
            response = {'key_error': 'incorrect keys'}
        except TypeError:
            response = {'type_error': 'incorrect types'}
        return response

    def delete_obj(self, request):
        self.connection.query(self.model).filter(self.model.id == request.matchdict['id']).delete()
        self.connection.commit()
        return {'response': 'object with id={} was deleted'.format(request.matchdict['id'])}

    def list_obj(self):
        return self._treatment_request(self.connection.query(self.model))

    def get_obj(self, request):
        return self._treatment_request(
            self.connection.query(self.model).filter(self.model.id == request.matchdict['id']))

    def put_obj(self, request):
        response = {'response': 'object with id={} was updated'.format(request.matchdict['id'])}
        try:
            self.connection.query(self.model).filter(self.model.id == request.matchdict['id']).update(**request.POST)
            self.connection.commit()
        except exc.IntegrityError:
            response = {'integrity_error': 'this user is already exist'}
        except KeyError:
            response = {'key_error': 'incorrect keys'}
        return response

    @staticmethod
    def _treatment_request(db_request):
        response = {}
        try:
            for item in db_request:
                del item.__dict__['_sa_instance_state']
                if 'budget' in item.__dict__:
                    item.__dict__['budget'] = str(item.__dict__['budget'])
                if 'creation_date' in item.__dict__:
                    item.__dict__['creation_date'] = str(item.__dict__['creation_date'])
                if 'negative_percent' in item.__dict__:
                    item.__dict__['negative_percent'] = str(item.__dict__['negative_percent'])
                if 'cost' in item.__dict__:
                    item.__dict__['cost'] = str(item.__dict__['cost'])
                response[item.__dict__['id']] = item.__dict__
        except exc.DataError:
            return {'response': 'incorrect data'}
        return response if response else {'found_error': 'data was not found'}
