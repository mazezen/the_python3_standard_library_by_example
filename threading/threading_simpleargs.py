#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import threading

def worker(num):
    """thread worker function"""
    print('Worker: %s' % num)

threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
