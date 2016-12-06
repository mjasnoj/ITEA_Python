# coding: utf-8

import unittest
from example import Number

class TestNumber(unittest.TestCase):
    def test_add(self):
        n = Number(4)
        n.add(4)
        self.assertEqual(n.n, 9)
