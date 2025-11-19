#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import sqlite3

schema_filename = './sqlite3/todo_schema.sql'

with sqlite3.connect(':memory') as conn:
    conn.row_factory = sqlite3.Row

    print('Creating schema')
    with open(schema_filename, 'rt') as f:
        schema = f.read()
    conn.executescript(schema)

    print('Inseting initial data')
    conn.execute("""
    insert into project (name, description, deadline)
    values ('pymotw', 'python module of the week', '2010-11-01')
    """)
    data = [
        ('write about select', 'done', '2010-10-03',
        'pymotw'),
        ('write about random', 'waiting', '2010-10-10',
        'pymotw'),
        ('write about sqlite3', 'active', '2010-10-17',
        'pymotw'),
    ]

    conn.executemany("""
    insert into task (details, status, deadline, project) values (?, ?, ?, ?)
    """, data)

    print('Dumping:')
    for text in conn.iterdump():
        print(text)
