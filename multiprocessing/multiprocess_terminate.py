#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import multiprocessing
import time

def show_worker():
    print('Starting worker')
    time.sleep(0.1)
    print('Finished worker')

if __name__ == '__main__':
    p = multiprocessing.Process(target=show_worker)
    print('BEFORE:', p, p.is_alive())
    p.start()
    print('DURING:', p, p.is_alive())
