#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import multiprocessing
import multiprocessing_import_woker

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(
            target=multiprocessing_import_woker.worker,
        )
        jobs.append(p)
        p.start()


