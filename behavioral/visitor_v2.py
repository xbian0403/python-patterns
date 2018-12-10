#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://peter-hoffmann.com/2010/extrinsic-visitor-pattern-python-inheritance.html

*TL;DR80
Separates an algorithm from an object structure on which it operates.
"""


class Node(object):
    def accept(self, visitor):
        visitor.visit(self)

class A(Node):
    pass

class B(Node):
    pass


class C(A, B):
    def accept(self, visitor):
        visitor.visit_C(self)

class Visitor(object):
    def visit(self, node, *args, **kwargs):
        meth = None
        for cls in node.__class__.__mro__:
            meth_name = 'visit_'+cls.__name__
            meth = getattr(self, meth_name, None)
            if meth:
                break
        else:
            return self.generic_visit(node, *args, **kwargs)
        return meth(node, *args, **kwargs)

    def generic_visit(self, node, *args, **kwargs):
        print('generic_visit ' + node.__class__.__name__)

class ConcreteVisitor1(Visitor):
    def visit_B(self, node, *args, **kwargs):
        print('ConcreteVisitor1 visit_B ' + node.__class__.__name__)
        
    def visit_C(self, node, *args, **kwargs):
        print('ConcreteVisitor1 visit_C ' + node.__class__.__name__)

class ConcreteVisitor2(Visitor):
    def visit_A(self, node, *args, **kwargs):
        print('ConcreteVisitor2 visit_A ' + node.__class__.__name__)
        
    def visit_C(self, node, *args, **kwargs):
        print('ConcreteVisitor2 visit_C ' + node.__class__.__name__)

a = A()
b = B()
c = C()
visitor1 = ConcreteVisitor1()
a.accept(visitor1)
b.accept(visitor1)
c.accept(visitor1)

visitor2 = ConcreteVisitor2()
a.accept(visitor2)
b.accept(visitor2)
c.accept(visitor2)

### OUTPUT ###
# generic_visit A
# ConcreteVisitor1 visit_B B
# ConcreteVisitor1 visit_C C
# ConcreteVisitor2 visit_A A
# generic_visit B
# ConcreteVisitor2 visit_C C
