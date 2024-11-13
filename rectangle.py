import unittest

def area(a, b):
    ''' Принимает 2 числа a и b, возращает произведение чисел a и b'''
    return a * b

def perimeter(a, b):
    ''' Принимает 2 числа a и b, возращает сумму чисел a и b, умноженная на 2'''
    return (a+b)*2

class RectangleTestCase(unittest.TestCase):
    
        def test_area_1_integers(self):
            res = area(3, 4)
            self.assertEqual(res, 12)
        
        def test_area_2_integers(self):
            res = area(82858948, 40490356)
            self.assertEqual(res, 3354988302305488)
        
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
            self.assertEqual(res, 47.4)
        
        def test_area_2_non_integer_and_integer(self):
            res = area(6521, 398402.43521745)
            self.assertEqual(res, 2597982280.0529914)
        
        def test_area_1_non_integers(self):
            res = area(9.3, 4.1) 
            self.assertEqual(res, 38.13)
        
        def test_area_2_non_integers(self):
            res = area(58859.9405, 3545.90909345)
            self.assertEqual(res, 208711998.25887594)
        

        
        def test_perimeter_1_integers(self):
            res = perimeter(3, 4)
            self.assertEqual(res, 14)
        
        def test_perimeter_2_integers(self):
            res = perimeter(82858948, 40490356)
            self.assertEqual(res, 246698608)
        
        def test_perimeter_1_zero(self):
            res = perimeter(0, 52)
            self.assertEqual(res, 104)
        
        def test_perimeter_2_zero(self):
            res = perimeter(67, 0)
            self.assertEqual(res, 134)
        
        def test_perimeter_3_zero(self):
            res = perimeter(0, 0)
            self.assertEqual(res, 0)
        
        def test_perimeter_1_non_integer_and_integer(self):
            res = perimeter(15.8, 3)
            self.assertEqual(res, 37.6)
        
        def test_perimeter_2_non_integer_and_integer(self):
            res = perimeter(6521, 398402.43521745)
            self.assertEqual(res, 809846.8704349)
        
        def test_perimeter_1_non_integers(self):
            res = perimeter(9.3, 4.1)
            self.assertEqual(res, 26.8)
        
        def test_perimeter_2_non_integers(self):
            res = perimeter(58859.9405, 3545.90909345)
            self.assertEqual(res, 124811.69918689999)
