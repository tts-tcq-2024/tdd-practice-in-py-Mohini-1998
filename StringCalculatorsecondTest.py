import unittest
from StringCalculator import add
class TestStringCalculator(unittest.TestCase):
                
        def test_expectZeroForEmptyInput(self):
                self.assertEqual(add("1,2"), 3)
     
        def test_expectZeroForEmptyInput(self):
               self.assertEqual(add("//;\n1;2"), 3)
          
        def test_expectZeroForEmptyInput(self):
               self.assertEqual(add("1+2+0"), 3) 
                
if __name__ == '__main__':
    unittest.main()
