#!/usr/bin/env python3
# encoding: utf-8

import heapq
from heapq_heapqdata import data
from heapq_showtree import show_tree

heapq.heapify(data)
print('start: ')
show_tree(data)

for n in [0, 13]:
    smallest = heapq.heapreplace(data, n)
    print('replace {:>2} with {:>2}:'.format(smallest, n))
    show_tree(data)
