import unittest
from mock import patch
from Calculator import Calculator
from MyExceptions import *

class TestCalculator(unittest.TestCase):
    #Testing Addition Function
    def this_test_check_addition_two_float_give_me_their_sum(self):
        calculator = Calculator()
        value1 = 2.13
        value2 = -4.12
        sum = -1.99
        self.assertAlmostEqual(calculator.Addition(value1,value2), sum)

    def this_test_check_addtion_string_and_int_raises_exception(self):
        calculator = Calculator()
        value1="string"
        value2=2
        self.assertRaises(itsNotNumber, calculator.Addition, value1, value2)

    def this_test_check_addtion_string_and_string_raises_exception(self):
        calculator = Calculator()
        value1="string"
        value2="second_string"
        self.assertRaises(itsNotNumber, calculator.Addition, value1, value2)


    #Testing Divide Function
    def this_test_check_division_two_float_give_me_their_quotient(self):
        calculator = Calculator()
        value1 = 4.2
        value2 = -2.1
        sum = -2
        self.assertAlmostEqual(calculator.Divide(value1,value2), sum)

    def this_test_check_division_string_and_int_raises_exception(self):
        calculator = Calculator()
        value1="string"
        value2=2
        self.assertRaises(itsNotNumber, calculator.Divide, value1, value2)

    def this_test_check_division_string_and_string_raises_exception(self):
        calculator = Calculator()
        value1="string"
        value2="second_string"
        self.assertRaises(itsNotNumber, calculator.Divide, value1, value2)

    def this_test_check_division_per_zero_raises_exception(self):
        calculator = Calculator()
        value1=4
        value2=0
        self.assertRaises(isZero, calculator.Divide, value1, value2)

    #Testing Logarithm Function
    def this_test_check_logarithm_two_float_give_me_result(self):
        calculator = Calculator()
        value1 = 2
        value2 = 2
        sum = 1
        self.assertAlmostEqual(calculator.Logarithm(value1,value2), sum)

    def this_test_check_if_value1_lover_than_zero_raises_exception(self):
        calculator = Calculator()
        value1=-1
        value2=2
        self.assertRaises(isLoverThanZero, calculator.Logarithm, value1, value2)

    def this_test_check_if_value2_lover_than_zero_raises_exception(self):
        calculator = Calculator()
        value1=3
        value2=-3
        self.assertRaises(isLoverThanZero, calculator.Logarithm, value1, value2)

    def this_test_check_value1_is_one_raises_exception(self):
        calculator = Calculator()
        value1=1
        value2=1
        self.assertRaises(isOne, calculator.Logarithm, value1, value2)

    #Testing Derivative Function using mock
    def this_test_check_derivative_return_good_result(self):
        calculator = Calculator()
        value1 = 'x**2'
        value2 = 'x'
        self.assertEqual('2*x', str(calculator.Derivative(value1, value2)))

    @patch("sympy.diff", return_value='2*x')
    def this_test_check_derivative_return_good_result(self, my_mock):
        calculator = Calculator()
        value1 = 'x**2'
        value2 = 'x'
        self.assertEqual(calculator.Derivative(value1, value2), my_mock(value1, value2))
