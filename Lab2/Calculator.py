from sympy import diff
import AbstractClass
import Validator
from MyExceptions import itsNotNumber, itsNotString, isLoverThanZero, isOne, isZero
import math


class Calculator(AbstractClass.AbstractClass):
    # Dodawanie
    def Addition(self, first, second):
        if not Validator.Validator.isNumber(first):
            raise itsNotNumber(first)
        if not Validator.Validator.isNumber(second):
            raise itsNotNumber(second)
        return first + second

    # Dzielenie
    def Divide(self, first, second):
        if not Validator.Validator.isNumber(first):
            raise itsNotNumber(first)
        if not Validator.Validator.isNumber(second):
            raise itsNotNumber(second)
        if Validator.Validator.isZero(second):
            raise isZero(second)
        return first / second

    # Obliczanie pochodnej
    def Derivative(self, function, step):
        return diff(function)

    # Logarytmowanie
    def Logarithm(self, first, second):
        if not Validator.Validator.isNumber(first):
            raise itsNotNumber(first)
        if Validator.Validator.isOne(first):
            raise isOne(first)
        if not Validator.Validator.isHighterThanZero(first):
            raise isLoverThanZero(first)

        if not Validator.Validator.isNumber(second):
            raise itsNotNumber(second)
        if not Validator.Validator.isHighterThanZero(second):
            raise isLoverThanZero(second)

        return math.log(first, second)
