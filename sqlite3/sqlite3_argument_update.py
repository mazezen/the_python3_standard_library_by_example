#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import sqlite3
import sys

db_filename = './sqlite3/todo.db'
id = int(sys.argv[1])
status = sys.argv[2]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    query = "update task set status = :status where id = :id"
    cursor.execute(query, {'status': status, 'id': id})
