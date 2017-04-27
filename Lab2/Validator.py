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
        if Validator.isNumber(value):
            return Validator.assertZero(value, 0)
        else:
            return False
    @staticmethod
    def isHighterThanZero(value):
        if Validator.isNumber(value):
            return value>0
        else:
            return False
    @staticmethod
    def isOne(value):
        if Validator.isNumber(value):
            return Validator.assertZero(value,1)
        else:
            return False