#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ChanageManager to register observer(dependent) listen to subject.
Allows register multiple observers to the same subject.

ChangeManager is using Singleton Pattern. 

#subjects    
>>> data1 = Data('Data 1')
>>> data2 = Data('Data 2')

#observers
>>> view1 = DecimalViewer()
>>> view2 = HexViewer()

#changeManager
>>> chmanSingleton.register(data1, view1)
>>> chmanSingleton.register(data1, view2)
>>> chmanSingleton.register(data2, view2)

>>> data1.data = 10
DecimalViewer: Subject Data 1 has data 10
HexViewer: Subject Data 1 has data 0xa


>>> data2.data = 15
HexViewer: Subject Data 2 has data 0xf

>>> data1.data = 3
DecimalViewer: Subject Data 1 has data 3
HexViewer: Subject Data 1 has data 0x3


>>> data2.data = 5
HexViewer: Subject Data 2 has data 0x5

>>> chmanSingleton.unregister(data1, view2)
>>> chmanSingleton.unregister(data2, view2)
>>> data1.data = 10
DecimalViewer: Subject Data 1 has data 10
>>> data2.data = 15

>>> chmanSingleton.unregister(data2, view2)
Traceback (most recent call last):
...
ValueError: Invalid subject or observer
"""


from __future__ import print_function
from collections import defaultdict
from collections import OrderedDict

class ChangeManager(object):
    _initialized = False

    def __init__(self):
        if ChangeManager._initialized:
            return

        self.sbj2obs = defaultdict(OrderedDict)
        ChangeManager._initialized = True

    def register(self, subject, observer):
        self.sbj2obs[subject][observer] = None

    def unregister(self, subject, observer):
        if subject not in self.sbj2obs or \
            observer not in self.sbj2obs[subject]:
            raise ValueError('Invalid subject or observer')

        del self.sbj2obs[subject][observer]
        if not len(self.sbj2obs[subject]):
            del self.sbj2obs[subject]

    def notify(self, subject):
        for observer in self.sbj2obs[subject]:
            observer.update(subject)

chmanSingleton = ChangeManager()

class Subject(object):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        chmanSingleton.notify(self)

# Example usage
class Data(Subject):
    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        #not recommend to notify in setting
        self.notify()

class Alarm(Subject):
    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._msg = ''

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

class HexViewer:
    def update(self, subject):
        print(u'HexViewer: Subject %s has data 0x%x' % (subject.name, subject.data))

class DecimalViewer:
    def update(self, subject):
        print(u'DecimalViewer: Subject %s has data %d' % (subject.name, subject.data))


# Example usage...
def main():
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

if __name__ == '__main__':
    main()
