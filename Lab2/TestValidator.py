import unittest
from Validator import Validator

class TestValidator(unittest.TestCase):

    #Test isString function
    def test_check_compare_string_return_true(self):
        string="string"
        self.assertEqual(True, Validator.isString(string))

    def test_check_compare_string_with_something_else_return_false(self):
        something=Validator()
        self.assertEqual(False, Validator.isString(something))

    #Test isNumber function
    def test_check_compare_numbers_return_true(self):
        string='cos'
        self.assertEqual(True, Validator.isString(string))

    def test_check_compare_number_return_something_else_return_false(self):
        something=Validator()
        self.assertEqual(False, Validator.isNumber(something))

    #Test isZero function
    def test_check_if_i_give_zero_return_true(self):
        number=0
        self.assertEqual(True, Validator.isZero(number))

    def test_check_if_i_give_something_another_than_zero_return_false(self):
        something=Validator()
        self.assertEqual(False, Validator.isZero(something))

    #Test isOne function
    def test_check_if_i_give_one_return_true(self):
        number=1
        self.assertEqual(True, Validator.isOne(number))

    def test_check_if_i_give_something_another_than_one_return_false(self):
        something=Validator()
        self.assertEqual(False, Validator.isOne(something))

    #Test isHighterThanZero function
    def test_check_if_number_is_highter_than_zero_this_return_true(self):
        number=3
        self.assertEqual(True, Validator.isHighterThanZero(number))

    def test_check_if_number_is_lover_or_equal_than_zero_this_return_false(self):
        something = Validator()
        self.assertEqual(False, Validator.isHighterThanZero(something))

if __name__=='__main__':
    unittest.main(exit=False)