"""
11、简述面向对象中__new__和__init__区别
__init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值。
__new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该
实例，是个静态方法。
也就是，__new__在__init__之前被调用，__new__的返回值（实例）将传递给
__init__方法的第一个参数，然后__init__给这个实例设置一些参数。
__new__方法用于创建对象并返回对象，当返回对象时会自动调用__init__方法进行初始化
"""
class Person(object):

    def __new__(cls, *args, **kwargs):
        print("in __new__")
        instance = object.__new__(cls)
        return instance

    def __init__(self, name, age):
        print("in __init__")
        self._name = name
        self._age = age


p = Person("Wang", 33)
