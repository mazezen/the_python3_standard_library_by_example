#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import threading

def worker():
    """thread worker function"""
    print("worker")

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
