import math
import unittest
def area(r):
    ''' Принимает число r, возращает число pi, умноженное на квадрат числа числа r'''
    return math.pi * r * r


def perimeter(r):
    ''' Принимает число r, возращает 2, умноженное на число pi, умноженное на квадрат числа числа r'''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    
        def test_area_1_integer(self):
            res = area(3)
            self.assertAlmostEqual(res, 28.27433, places=4)
        
        def test_area_2_integer(self):
            res = area(82858948)
            self.assertAlmostEqual(res, 21568935058782732, places=4)
        
        def test_area_1_zero(self):
            res = area(0)
            self.assertEqual(res, 0)
        
        def test_area_1_non_integer(self):
            res = area(9.3) 
            self.assertAlmostEqual(res, 271.71634, places=4)
        
        def test_area_2_non_integer(self):
            res = area(58859.9405)
            self.assertAlmostEqual(res, 10884024486.95281, places=4)
        

        def test_perimeter_1_integer(self):
            res = perimeter(3)
            self.assertAlmostEqual(res, 18.84955, places=4)
        
        def test_perimeter_2_integer(self):
            res = perimeter(82858948)
            self.assertAlmostEqual(res, 520618124.64195, places=4)
        
        def test_perimeter_1_zero(self):
            res = perimeter(0)
            self.assertEqual(res, 0)
        
        def test_perimeter_1_non_integer(self):
            res = perimeter(9.3)
            self.assertAlmostEqual(res, 58.43362, places=4)
       
        def test_perimeter_2_non_integer(self):
            res = perimeter(58859.9405)
            self.assertAlmostEqual(res, 369827.91333, places=4)
