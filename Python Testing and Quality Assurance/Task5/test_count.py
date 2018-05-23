import unittest
from countnum import countNum


class countNumTestCase(unittest.TestCase):
    """Tests for 'countnum.py'."""    

    def test_countNum1(self):
        count1 = countNum(1,5,8)        
        self.assertEqual(count1, 0)

    def test_countNum2(self):
        count2 = countNum(1,500,2)        
        self.assertEqual(count2, 176)

    def test_countNum3(self):
        count3 = countNum(-50,-5,6)        
        self.assertEqual(count3, 5)

    def test_countNum4(self):
        count4 = countNum(100,1000,42)        
        self.assertEqual(count4, 19)

    def test_countNum5(self):
        count5 = countNum(1,12,1)        
        self.assertEqual(count5, 4)

    def test_countNum1(self):
        count6 = countNum(5,5,5)        
        self.assertEqual(count6, 1)
        

unittest.main()
