from abc import ABC, abstractmethod

class AbstractBoard(ABC):
    @abstractmethod
    def printBoard(self):
        pass

    @abstractmethod
    def movePlayer(self, x, y):
        pass

    @abstractmethod
    def moveCPU(self):
        pass

    @abstractmethod
    def checkCoordinates(self, x, y):
        pass

    @abstractmethod
    def checkPlayersWin(self):
        pass

    @abstractmethod
    def checkCPUsWin(self):
        pass

    @abstractmethod
    def checkVerticalOrHorizontal(self, array, how):
        pass

    @abstractmethod
    def checkDiagonal(self, array, how):
        pass