# -*- coding: utf-8 -*-


class DescriptorBase:
    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Spam:
    name = DescriptorBase()


s = Spam()

s.name = 'Guido'
print(s.name)
