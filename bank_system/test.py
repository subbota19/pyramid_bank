from abc import ABC, abstractmethod


class Abstract(ABC):
    @abstractmethod
    def func(self):
        print('abstract')

    def without(self):
        print('without')


class A(Abstract):
    def func(self):
        pass

    def hello(self):
        print('hello')


a = A()
a.hello()
