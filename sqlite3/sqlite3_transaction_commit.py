#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import sqlite3

db_filename = './sqlite3/todo.db'

def show_projects(conn):
    cursor = conn.cursor()
    cursor.execute('select name, description from project')
    for name, desc in cursor.fetchall():
        print(' ', name)

with sqlite3.connect(db_filename) as conn1:
    print('Before changes: ')
    show_projects(conn1)

    # Insert in one cursor.
    cursor1 = conn1.cursor()
    cursor1.execute("""
    insert into project (name, description, deadline)
    values (''virtualenvwrapper', 'Virtualenv Extensions',
    2011-01-01')
    """)

    print('\nAfter changes in conn1: ')
    # select from another connection, without committing first.
    print('\nBefore commit: ')
    with sqlite3.connect(db_filename) as conn2:
        show_projects(conn2)
    
    # Commit, the select from another connection.
    conn1.commit()
    print('\nAfter commit: ')
    with sqlite3.connect(db_filename) as conn3:
        show_projects(conn3)


