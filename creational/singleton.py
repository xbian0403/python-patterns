#!/usr/bin/env python


#metaclass method
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        print('metaclass method calling Singleton')
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    def __init__(self, *args, **kwargs):
        print('init singleton')

#Python3
class MyClass(object, metaclass=Singleton):
    def __new__(cls, *args, **kwargs):
        print('new_', cls.__name__)
        print('super', super.__name__)
        return super(MyClass, cls).__new__(cls, *args, **kwargs)
    x = 1
    #will be called only once
    def __init__(self):
        MyClass.x+=1
        print('init', MyClass.x)
c = MyClass()
c = MyClass()
c = MyClass()

#__new__ method
class Singleton(object):
    _instances = {}
    def __new__(class_, *args, **kwargs):
        #name is subclass name
        print('__new__ method')
        print('new_', class_.__name__)
        print('super', super.__name__)
        if class_ not in class_._instances:
            class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
        return class_._instances[class_]

class MyClass(Singleton):
    x = 1
    #will be called for each instance creation
    def __init__(self):
        MyClass.x+=1
        print('init', MyClass.x)

c = MyClass()
c = MyClass()
c = MyClass()