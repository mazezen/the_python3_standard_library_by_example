#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

# python3 -m unittest unittest_failwithmessage.py

import unittest

class FailureMessageTest(unittest.TestCase):

    def testFail(self):
        self.assertFalse(True, 'failure message goes there')
