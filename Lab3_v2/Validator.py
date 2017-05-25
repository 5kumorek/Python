class NumbersValidator:
    @staticmethod
    def IsInt(value):
        try:
            int(value)
        except ValueError:
            raise NotAInt()

    @staticmethod
    def SizeOfBoardIsValid(size):
        try:
            NumbersValidator.IsInt(size)
            if int(size)<2 or int(size)>9:
                raise WrongSizeboardError
        except NotAInt:
            raise WrongSizeboardError

    @staticmethod
    def IsXorY(size):
        try:
            size = str(size)
            if size is 'x' or size is 'y':
                raise NotXorY
        except NotAInt:
            raise NotXorY

    @staticmethod
    def IsXandY(x,y,size):
        try:
            NumbersValidator.IsInt(x)
            NumbersValidator.IsInt(y)
            if int(x)<1 or int(x)>size:
                raise NotXandY
            if int(y)<1 or int(y)>size:
                raise NotXandY
        except NotAInt:
            raise NotXandY
        except NotXandY:
            raise NotXandY

    @staticmethod
    def GuessedValueIsValid(value):
        try:
            NumbersValidator.IsInt(value)
            if int(value)<1 or int(value)>101:
                raise InvalidValueError
        except NotAInt:
            raise NotAInt

    @staticmethod
    def GameNumberIsValid(value):
        try:
            NumbersValidator.IsInt(value)
            if int(value) < 1 or int(value) > 3:
                raise InvalidValueError
        except NotAInt:
            raise NotAInt

class NotAInt(Exception):
    pass

class NotXorY(Exception):
    pass

class NotXandY(Exception):
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