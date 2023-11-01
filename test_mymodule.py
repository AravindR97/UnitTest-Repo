import unittest
    #python standard library for unit testing
from mymodule import square,double
    #imported the units that needs to be tested

class TestSquare(unittest.TestCase):
    #inherited 'TestCase' class from unittest library
    def test1(self):
        #defining the test function
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3), 9)
        self.assertEqual(square(-3), 9)
        self.assertNotEqual(square(-2), -4)
        
    def test2(self):
        self.assertEqual(double(2), 4)
        self.assertEqual(double(3), 6)
        self.assertEqual(double(-3), -6)
        self.assertNotEqual(double(-2), 4)
        

unittest.main()

#assertEqual() & assertNotEqual() are methods of the class 'TestCase' in unittest library
#Theses methods checks if the two values given as args are equal or not.
#to test another Fn(unit), create another class or another test fn inside the same class.
