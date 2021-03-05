#!/usr/bin/env python

import unittest
import hello
# capture system stdout stderr

class myTest(unittest.TestCase):

    def test_main(self):
        greet = hello.main(['Bob'])
        self.assertEqual('Hello Bob', greet)

if __name__ == '__main__':
    unittest.main()
