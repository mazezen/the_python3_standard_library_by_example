#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import sqlite3

db_filename = './sqlite3/todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select * from task where project = 'pymotw'
    """)

    print('Task table has these columns:')
    for colinfo in cursor.description:
        print(colinfo)
