class Validator:
    @staticmethod
    def assertZero(firstValue, secondValue):
        return abs(firstValue-secondValue)<0.00001
    @staticmethod
    def isString(string):
        return isinstance(string, str)
    @staticmethod
    def isNumber(value):
        return isinstance(value, int) or isinstance(value, float)
    @staticmethod
    def isZero(value):
        return CalcValidator.assertZero(value, 0)
    @staticmethod
    def isHighterThanZero(value):
        return value>0
    @staticmethod
    def isOne(value):
        return CalcValidator.assertZero(value,1)