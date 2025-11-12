#!/usr/bin/env python3
# encoding: utf-8

import functools

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B):
    pass

class E(C, D):
    pass

@functools.singledispatch
def myFunc(arg):
    print('default myfunc({})'.format(arg.__class__.__name__))

@myFunc.register(A)
def myfunc_A(arg):
    print('myfunc_A({})'.format(arg.__class__.__name__))

@myFunc.register(B)
def myfunc_B(arg):
    print('myfunc_B({})'.format(arg.__class__.__name__))

@myFunc.register(C)
def myfunc_C(arg):
    print('myfunc_C({})'.format(arg.__class__.__name__))

myFunc(A())
myFunc(B())
myFunc(C())
myFunc(D())
myFunc(E())
