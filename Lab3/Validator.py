class NumbersValidator:

    @staticmethod
    def IsInt(value):
        try:
            int(value)
        except ValueError:
            raise NotAInt()

    @staticmethod
    def sizeOfBoardIsValid(size):
        try:
            NumbersValidator.IsInt(size)
            if int(size)<2 or int(size)>9:
                raise WrongSizeboardError
        except NotAInt:
            raise WrongSizeboardError

    def GuessedValueIsValid(value):
        try:
            NumbersValidator.IsInt(value)
            if int(value)<1 or int(value)>101:
                raise InvalidValueError
        except NotAInt:
            raise NotAInt

class NotAInt(Exception):
    pass

class WrongSizeboardError(Exception):
    pass

class InvalidValueError(Exception):
    pass

class InvalidPortError(Exception):
    pass

class EndOfGameError(Exception):
    pass

class FieldIsOccupiedError(Exception):
    pass

class OutOfArrayError(Exception):
    pass