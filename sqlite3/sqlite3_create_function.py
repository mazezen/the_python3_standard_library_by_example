#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import codecs
import sqlite3

db_filename = './sqlite3/todo.db'

def encrypt(s):
    print('Encrypting {!r}'.format(s))
    return codecs.encode(s, 'rot-13')

def decrypt(s):
    print('Decrypting {!r}'.format(s))
    return codecs.encode(s, 'rot-13')
