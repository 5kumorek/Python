class Validator:
    @staticmethod
    def variablesAreValid(x,y,size):
        if isinstance(x, int) and isinstance(y,int):
            return x<size and y<size
        else:
            MyException.NotAInt()

class MyException(Exception):
    @staticmethod
    def NotAInt(self):
        pass

    @staticmethod
    def OutOfBoard(self):
        pass