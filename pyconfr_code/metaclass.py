# -*- coding: utf-8 -*-

class MetaBase(type):

    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        """
        Builds a dict that will be used to populate the class
        """
        print(metacls)
        return {}

    def __new__(metacls, name, bases, namespace, **kwargs):
        """
        Builds a new class object
        """
        cls_dict = dict(namespace)
        cls_instance = type.__new__(metacls, name, bases, cls_dict)
        return cls_instance


class Base(metaclass=MetaBase):
    pass
