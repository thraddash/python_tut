#!/usr/bin/env python

## test msmath and msstring 
## import unittest module
## create class MsPackMsMathTestCase and inherite test case class (unittest.TestCase)
## create list of test functions use test_ before each of the methods

import unittest
from mspack import msmath
from mspack import msstring

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

class MsPackMsStringTestCase(unittest.TestCase):
    def test_full_name(self):
        name = msstring.MsName("Life", "Good").full_name()
        self.assertEqual("Life Good", name)

### setUp function is called before the  test full name function
class MsPackMsString1TestCase(unittest.TestCase):
    def setUp(self): # setUp U is in uppercase
        self.str_obj = msstring.MsName("Life", "Good")

    def test_full_name(self):
        name = self.str_obj.full_name()
        self.assertEqual("Life Good", name)

    def test_full_name_length(self):
        length = len(self.str_obj.full_name())
        self.assertTrue(length == 9)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
