class NumbersValidator:
    @staticmethod
    def variablesAreValid(x,y,size):
        if isinstance(x, int) and isinstance(y,int):
            return x<=size and x>0 and y<=size and y>0
        else:
            NotAInt()

    @staticmethod
    def isInt(x):
        try:
            x=int(x)
            return True
        except:
            return False

    @staticmethod
    def sizeOfBoardIsValid(size):
        if isinstance(size, int):
            return size<10
        else:
            NotAInt()

class NotAInt(Exception):
    pass

class OutOfBoard(Exception):
    pass