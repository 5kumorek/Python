import random
from AbstractBoard import AbstractBoard
from Validator import Validator
from Validator import MyException

class Board(AbstractBoard):
    sizeBoard=0
    arrayChars = [' ','x','o']
    charPlayer='x'
    charCPU='o'
    arrayPlayer=None
    arrayCPU=None
    arrayGame=None
    def __init__(self, size, char):
        self.sizeBoard=size
        self.char=char
        self.arrayGame= [[0 for x in range(size)] for y in range(size)]
        self.arrayPlayer = [[0 for x in range(size)] for y in range(size)]
        self.arrayCPU = [[0 for x in range(size)] for y in range(size)]
        if(char=='o'):
            self.arrayChars = [' ', 'o', 'x']

    #metoda do wypisywania mojej planszy
    def printBoard(self):
        for i in range(2*self.sizeBoard-1):
            if i%2==0:
                for j in range(2*self.sizeBoard-1):
                    if j%2==0:
                        print(self.arrayChars[self.arrayGame[i//2][j//2]], end='', flush=True)
                    else:
                        print('|', end='', flush=True)
            else:
                for j in range(2 * self.sizeBoard - 1):
                    print('-', end='', flush=True)
            print('')

    #metoda która sprawi że wybory gracza zostaną zapamiętane
    def movePlayer(self, x, y):
        self.arrayPlayer[x][y]=1
        self.arrayGame[x][y]=1

    #metoda która sprawi że wybory komputera zostaną zapamiętane w tablicy
    def moveCPU(self):
        while True:
            x=random.randint(0,self.sizeBoard-1)
            y=random.randint(0,self.sizeBoard-1)
            if self.checkCoordinates(x,y):
                break
        self.arrayCPU[x][y]=1
        self.arrayGame[x][y]=2

    #metoda która sprawdzi czy podany ruch jest możliwy
    def checkCoordinates(self, x, y):
        if Validator.variablesAreValid(x,y,self.sizeBoard):
            return self.arrayGame[x][y]==0
        else:
            return MyException.OutOfBoard()

    #metoda sprawdza czy nie wygrał gracz
    def checkPlayersWin(self):
        inLine = self.checkVerticalOrHorizontal(self.arrayPlayer, True) or self.checkVerticalOrHorizontal(self.arrayPlayer, False)
        diagonal = self.checkDiagonal(self.arrayPlayer, True) or self.checkDiagonal(self.arrayPlayer, False)
        return inLine or diagonal

    #metoda sprawdza czy komputer wygrał
    def checkCPUsWin(self):
        inLine = self.checkVerticalOrHorizontal(self.arrayCPU, True) or self.checkVerticalOrHorizontal(self.arrayCPU, False)
        diagonal = self.checkDiagonal(self.arrayCPU, True) or self.checkDiagonal(self.arrayCPU, False)
        return inLine or diagonal

    #metoda która zwraca prawde jeśli wszystkie elementy w rzędach są takie same
    # , jeśli how jest true to sprawsza Pionowo jeśli false to sprawdza poziom
    def checkVerticalOrHorizontal(self, array, how):
        win = False
        for i in range(self.sizeBoard):
            win = False
            for j in range(self.sizeBoard):
                win = True
                if how:
                    if array[i][j] == 0:
                        win = False
                        break
                else:
                    if array[j][i] == 0:
                        win = False
                        break
            if win:
                break
        return win

    #metoda która zwraca True jeśli na którejść z dwóch diagonali są takei same znaki
    def checkDiagonal(self,array,how):
        win = False
        for i in range(self.sizeBoard):
            win = True
            if how:
                if array[i][i] == 0:
                    win = False
                    break
            else:
                if array[self.sizeBoard-i-1][i] == 0:
                    win = False
                    break
        return win