#!/usr/bin/env python

## test msmath and msstring 
## import unittest module
## create class MsPackMsMathTestCase and inherite test case class (unittest.TestCase)
## create list of test functions use test_ before each of the methods

import unittest
from mspack import msmath

class MsPackMSMathTestCase(unittest.TestCase):
    def test_sum(self):
        sum = msmath.sum(8, 12)
        self.assertEqual(sum, 20)

    def test_subtract(self):
        result = msmath.subtract(109, 9)
        self.assertTrue(result == 100)

    def test_multiplication(self):
        result = msmath.multiplication(9, 3)
        self.assertEqual(result, 27)

    def test_division(self):
        result = msmath.division(50, 25)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
