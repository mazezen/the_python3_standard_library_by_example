#!/usr/bin/env python3
# encoding: utf-8
# @Author mazezen

import unittest

class TruthTest(unittest.TestCase):

    def testAssertTrue(self):
        self.assertTrue(True)

    def testAssertFalse(self):
        self.assertFalse(False)
