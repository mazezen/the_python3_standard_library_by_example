#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

# python3 -m unittest unittest_simple.py

import unittest

class SimplisticTest(unittest.TestCase):

    def test(self):
        a = 'a'
        b = 'a'
        self.assertEqual(a, b)
