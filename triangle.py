import unittest

def area(a, h):
    ''' Принимает 2 числа a и h, возращает произведение чисел a и h, деленное на 2'''
    return a * h / 2 

def perimeter(a, b, c): 
    ''' Принимает 3 числа a, b и c, возращает сумму чисел a, b и c'''
    return a + b + c 

class TriangleTestCase(unittest.TestCase):
    
        def test_area_1_integers(self):
            res = area(3, 4)
            self.assertEqual(res, 6)
        
        def test_area_2_integers(self):
            res = area(82858948, 40490356)
            self.assertEqual(res, 1677494151152744)
        
        def test_area_1_zero(self):
            res = area(0, 52)
            self.assertEqual(res, 0)
        
        def test_area_2_zero(self):
            res = area(67, 0)
            self.assertEqual(res, 0)
        
        def test_area_3_zero(self):
            res = area(0, 0)
            self.assertEqual(res, 0)
        
        def test_area_1_non_integer_and_integer(self):
            res = area(15.8, 3)
            self.assertEqual(res, 23.7)
        
        def test_area_2_non_integer_and_integer(self):
            res = area(6521, 398402.43521745)
            self.assertEqual(res, 1298991140.026495725)
        
        def test_area_1_non_integers(self):
            res = area(9.3, 4.1) 
            self.assertEqual(res, 19.065)
        
        def test_area_2_non_integers(self):
            res = area(58859.9405, 3545.90909345)
            self.assertEqual(res, 104355999.12943795)
        
        
        def test_perimeter_1_integers(self):
            res = perimeter(3, 4, 5)
            self.assertEqual(res, 12)
        
        def test_perimeter_2_integers(self):
            res = perimeter(8285894895, 4049035664, 848084014)
            self.assertEqual(res, 13183014573)
        
        def test_perimeter_1_zero(self):
            res = perimeter(67, 0, 0)
            self.assertEqual(res, 67)
        
        def test_perimeter_2_zero(self):
            res = perimeter(0, 0, 0)
            self.assertEqual(res, 0)
        
        def test_perimeter_1_non_integer_and_integer(self):
            res = perimeter(15.8, 3, 73)
            self.assertEqual(res, 91.8)
        
        def test_perimeter_2_non_integer_and_integer(self):
            res = perimeter(6521, 398402.43521745, 4546.7965)
            self.assertEqual(res, 409470.23171745)
        
        def test_perimeter_1_non_integers(self):
            res = perimeter(9.3, 4.1, 2.324354658)
            self.assertEqual(res, 15.724354658)
        
        def test_perimeter_2_non_integers(self):
            res = perimeter(58859.9405, 3545.90909345, 23243542.19898658)
            self.assertEqual(res, 23305948.04858003)

