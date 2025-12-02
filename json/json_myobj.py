#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

class MyObj:

    def __init__(self, s):
        self.s = s
    def __repr__(self):
        return '<MyObj({})>'.format(self.s)
    
