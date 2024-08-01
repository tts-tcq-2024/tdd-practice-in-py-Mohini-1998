import unittest
from StringCalculator import add
class TestStringCalculator(unittest.TestCase):
   
        def test_expectZeroForEmptyInput(self):
                self.assertEqual(add("1\n2,3"),6);


if __name__ == '__main__':
    unittest.main()
