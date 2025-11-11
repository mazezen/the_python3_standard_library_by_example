#!/usr/bin/env python3
# encoding: utf-8

import heapq
from heapq_showtree import show_tree
from heapq_heapqdata import data

print('random :', data)
heapq.heapify(data)
print('heapified :')
show_tree(data)
