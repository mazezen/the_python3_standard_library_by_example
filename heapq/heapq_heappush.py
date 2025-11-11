#!/usr/bin/env python3
# encoding: utf-8

import heapq
from heapq_showtree import show_tree
from heapq_heapqdata import data

heap = []
print('random :', data)
print()

for n in data:
    print('add {:>3}'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)
