#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import sqlite3
import sys

db_filenane = './sqlite3/todo.db'

sql = 'select id, details, deadline from task'

def show_deadline(conn):
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    for col in ['id', 'details', 'deadline']:
        print(' {:<8} {!r:<26} {}'.format(
            col, row[col], type(row[col])
        ))
    return

print('Without type detection:')
with sqlite3.connect(db_filenane) as conn:
    show_deadline(conn)

print('\nWith type detection:')
with sqlite3.connect(db_filenane, 
                     detect_types=sqlite3.PARSE_DECLTYPES) as conn:
    show_deadline(conn)

