# -*- coding: utf-8 -*-

class BaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        cls_instance = type.__new__(cls, clsname, bases, clsdict)
        return cls_instance

    def __add__(self, value):
        # Merge dicts
        result_dict = {}
        result_dict.update(self.__dict__)
        result_dict.update(value.__dict__)

        cls_name = f'{self.__name__}{value.__name__}'
        return BaseMeta.__new__(
            self.__class__,
            cls_name,
            self.__bases__,
            result_dict,
        )

class Base(metaclass=BaseMeta):
    pass


class A(Base):
    def func_a(self):
        pass


class B(Base):
    def func_b(self):
        pass


C = A + B

print(C)
