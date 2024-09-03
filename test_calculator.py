import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number(self):
        self.assertEqual(self.calculator.add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(self.calculator.add("1,5"), 6)

    def test_new_line_between_numbers(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)

    def test_multiple_custom_delimiters(self):
        self.assertEqual(self.calculator.add("//[;][*]\n1;2*3"), 6)

    def test_negative_number(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2")
        self.assertEqual(str(context.exception), "negative numbers not allowed -2")

    def test_multiple_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,-3")
        self.assertEqual(str(context.exception), "negative numbers not allowed -2,-3")

if __name__ == "__main__":
    unittest.main()
