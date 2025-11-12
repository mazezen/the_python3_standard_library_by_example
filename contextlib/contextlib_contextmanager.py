#!/usr/bin/env python3
# encoding: utf-8

import contextlib

@contextlib.contextmanager
def make_context():
    print(' entering')
    try:
        yield {}
    except RuntimeError as err:
        print(" Error:", err)
    finally:
        print(' exting')

print("Normal:")
with make_context() as value:
    print(' inside with statement:', value)

print('\nHandled error:')
with make_context() as value:
    raise ValueError('this exception is not handled')
