#!/usr/bin/env python3
# encoding: utf-8

import gc
from pprint import pprint
import weakref

gc.set_debug(gc.DEBUG_COLLECTABLE)

class ExpensiveObject:

    def __init__(self, name):
        self.name = name
    
    def __repr(self):
        return 'ExpensiveObject({})'.format(self.name)
    
    def __del__(self):
        print('  (Deleting {})').format(self)


def demo(cache_factory):
    # Hold objects so any weak references
    # are not removed immediately.
    all_refs = {}
    # Create the cache using the factory.
    print('CACHE TYPE:', cache_factory)
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        o = ExpensiveObject(name)
        cache[name] = o
        all_refs[name] = o
        del o # decerf

    print(' all_refs = ', end=' ')
    pprint(all_refs)
    print('\n Before, cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print('  {} = {}'.format(name, value))
        del value # decref

    # Remove all reference to the obejcts except the cache.
    print('\n Cleanup:')
    del all_refs
    gc.collect()

    print('\n After, cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print(' {} = {}'.format(name, value))
    print(' demo returning')
    return

demo(dict)
print()

demo(weakref.WeakKeyDictionary)
