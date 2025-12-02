#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

# python3 -m unittest unittest_outcomes.py 

import unittest

class OutcomesTest(unittest.TestCase):

    def testPass(self):
        return
    def testFail(self):
        self.assertFalse(True)

    def testError(self):
        raise RuntimeError('Test error!')
