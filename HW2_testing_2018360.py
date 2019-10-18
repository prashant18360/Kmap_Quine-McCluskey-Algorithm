# CSE 101 - IP HW2 TESTCASES
# Name : PRASHANT
# Roll Number : 2018360
# Section : B
# Group : 1
# Date : October 12, 2018

import unittest
from HW2_2018360 import minFunc

class testpoint(unittest.TestCase):
    def test_minFunc(self):
        self.assertEqual(minFunc(4,'(0,1,3,4,9,11,15)d(2,14,6)'),"A'D'+B'D")
        self.assertEqual(minFunc(4,'(2,6,14,10,7,4,9,11)d-'),"A'BC+A'BD'+AB'D+CD'")
        self.assertEqual(minFunc(4,'(0,1,4,5,8,13,2)d(12,9,6)'),"A'D'+C'")
        self.assertEqual(minFunc(4,'(2,1,9,11)d(6)'),"A'CD'+AB'D+B'C'D")
        self.assertEqual(minFunc(4,'(10,7,2)d-'),"A'BCD+B'CD'")
        self.assertEqual(minFunc(4,'(0,1,4,5,12,13,8,9,2,6,14)d-'),"A'D'+BD'+C'")
        self.assertEqual(minFunc(4,'(8,9,6,7)d(10,11,12,13,14,15)'),"A+BC")
        self.assertEqual(minFunc(3,'(4,1)d(7)'),"A'B'C+AB'C'")
        self.assertEqual(minFunc(3,'(0,2,5,6)d(7)'),"A'C'+AC")
        self.assertEqual(minFunc(3,'(0,1,6)d(4,7)'),"A'B'")
        self.assertEqual(minFunc(3,'(0,4,5,7,6)d-'),"A+B'C'")
        self.assertEqual(minFunc(2,'(0,2)d(1)'),"A'+B'")
        self.assertEqual(minFunc(2,'(0,3)d(1)'),"A'+B")
        self.assertEqual(minFunc(2,'(2)d(1)'),"AB'")


if __name__=='__main__':
    unittest.main()
