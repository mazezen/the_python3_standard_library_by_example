#!/usr/bin/env python3
# encoding: utf-8

import queue

q = queue.Queue()
for i in range(5):
    q.put(item=i)

while not q.empty():
    print(q.get(), end=' ')
print()
