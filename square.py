import unittest

def area(a):
    ''' Принимает числа a, возращает квадрат числа a'''
    return a * a


def perimeter(a):
    ''' Принимает числа a, возращает произведение числа a и 4'''
    return 4 * a

class SquareTestCase(unittest.TestCase):
    
    def test_area_1_integer(self):
        res = area(3)
        self.assertEqual(res, 9)
    
    def test_area_2_integer(self):
        res = area(82858948)
        self.assertEqual(res, 6865605263666704)
    
    def test_area_1_zero(self):
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_area_1_non_integer(self):
        res = area(9.3) 
        self.assertEqual(res, 86.49)
    
    def test_area_2_non_integer(self):
        res = area(58859.9405)
        self.assertEqual(res, 3464492595.66354025)
        
    
    def test_perimeter_1_integer(self):
        res = perimeter(3)
        self.assertEqual(res, 12)
    
    def test_perimeter_2_integer(self):
        res = perimeter(82858948)
        self.assertEqual(res, 331435792)
    
    def test_perimeter_1_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimeter_1_non_integer(self):
        res = perimeter(9.3)
        self.assertEqual(res, 37.2)
    
    def test_perimeter_2_non_integer(self):
        res = perimeter(58859.9405)
        self.assertEqual(res, 235439.762)
