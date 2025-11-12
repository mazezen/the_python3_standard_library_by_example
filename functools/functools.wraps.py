#!/usr/bin/env python3
# encoding: utf-8

import functools

def show_details(name, f):
    "Show details of a callable object."
    print('{}:'.format(name))
    print(' object:', f)
    print(' __name__:', end=' ')

    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print(' __doc__', repr(f.__doc__))

def simaple_decorator(f):
    @functools.wraps(f)
    def decorated(a='decorated defaults', b=1):
        print(' decorated:', (a, b))
        print(' ', end=' ')
        return f(a, b=b)
    
def myFunc(a, b=2):
    "myFunc() is not complicated"
    print(' myFunc:', (a, b))
    return

# The raw function
show_details('myFunc', myFunc)
myFunc('unwrapped, default b')
myFunc('unwrapped, passing b', 3)
print()

# Wrap explicitly.
wrapped_myFunc = simaple_decorator(myFunc)
show_details('wrapped_myFunc', wrapped_myFunc)
wrapped_myFunc()
wrapped_myFunc('args to wrapped', 4)
print()

# wrap with decorator syntax.
@simaple_decorator
def decorated_myFunc(a, b):
    myFunc(a, b)
    return

show_details('decorated_myFunc', decorated_myFunc)
decorated_myFunc()
decorated_myFunc('args to decorated', 4)