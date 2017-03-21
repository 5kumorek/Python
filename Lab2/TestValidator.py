import unittest
from Validator import Validator

class TestValidator(unittest.TestCase):

    #Test isString function
    def this_test_check_compare_string_return_true(self):
        string="string"
        self.assertEqual(True, Validator.isString(string))

    def this_test_check_compare_string_with_something_else_return_false(self):
        string=Validator()
        self.assertEqual(False, Validator.isString(string))

    #Test isNumber function
    def this_test_check_compare_numbers_return_true(self):
        string=3
        self.assertEqual(True, Validator.isString(string))

    def this_test_check_compare_number_return_something_else_return_false(self):
        string=Validator()
        self.assertEqual(False, Validator.isNumber(string))

    #Test isZero function
    def this_test_check_if_i_give_zero_return_true(self):
        string=3
        self.assertEqual(True, Validator.isZero(string))

    def this_test_check_if_i_give_something_another_than_zero_return_false(self):
        string=Validator()
        self.assertEqual(False, Validator.isZero(string))

    #Test isOne function
    def this_test_check_if_i_give_one_return_true(self):
        string=3
        self.assertEqual(True, Validator.isOne(string))

    def this_test_check_if_i_give_something_another_than_one_return_false(self):
        string=Validator()
        self.assertEqual(False, Validator.isOne(string))

    #Test isHighterThanZero function
    def this_test_check_if_number_is_highter_than_zero_this_return_true(self):
        string=3
        self.assertEqual(True, Validator.isHighterThanZero(string))

    def this_test_check_if_number_is_lover_or_equal_than_zero_this_return_false(self):
        string = Validator()
        self.assertEqual(False, Validator.isHighterThanZero(string))

if __name__=='__main__':
    unittest.main(exit=False)