#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import logging
import sqlite3
import sys
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-10s) %(message)s',
)

db_filename = './sqlite3/todo.db'
isolation_level = sys.argv[1]

def writer():
    with sqlite3.connect(
        db_filename,
        isolation_level=isolation_level
    ) as conn:
        cursor = conn.cursor()
        cursor.execute('update task set priority = priority + 1')
        logging.debug('waiting to synchronize')
        ready.wait()
        time.sleep(1)
        logging.debug('CHANGES COMMITTED')

def reader():
    with sqlite3.connect(
        db_filename,
        isolation_level=isolation_level
    ) as conn:
        cursor = conn.cursor()
        logging.debug('waiting to synchronize')
        ready.wait()
        logging.debug('wait over')
        cursor.execute('select * from task')
        logging.debug('SELECT EXECUTED')
        cursor.fetchall()
        logging.debug('results fetched')

if __name__ == '__main__':
    ready = threading.Event()

    threads = [
        threading.Thread(name='Reader 1', target=reader),
        threading.Thread(name='Reader 2', target=reader),
        threading.Thread(name='Writer 1', target=writer),
        threading.Thread(name='Writer 2', target=writer),
    ]

    [t.start() for t in threads]

    time.sleep(1)

    logging.debug('seting ready')
    ready.set()

    [t.join() for t in threads]
