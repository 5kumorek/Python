import Board
import logging
from ManageProtobuf import *
from Validator import *
from StatesFile import State

class TicTacToeGame:
    # zmienna używana w klasie GuessANumber
    firstInvoked = True
    #rozmiar mojej tablicy
    finalSize = 0
    # znak jaki wybrał gracz (domyślnie x)
    finalChar = 'x'
    game = None


class Size(State):
    def __init__(self, connection, msg):
        self.msg = msg
        self.connection = connection

    def run(self):
        logging.info('Current state %s', 'WaitingOnSize')
        self.msg.typeA = 5
        if TicTacToeGame.firstInvoked:
            self.msg.stateA = 1
            self.msg.sentenceA = "HI, now you start game against computer by server"
            sendMessage(self.connection, self.msg)
            TicTacToeGame.firstInvoked = False
        self.msg.sentenceA = "Could you give me board's size lower than 10 and higher than 1?"
        self.msg.stateA = 0
        sendMessage(self.connection, self.msg)
        msg_rec = getResponse(self.connection)
        self.value = DictionaryOfClass[msg_rec.typeA]().getMessage(msg_rec)

    def getState(self):
        try:
            NumbersValidator.SizeOfBoardIsValid(self.value)
            TicTacToeGame.finalSize=int(self.value)
            logging.info('State %s is finished', 'WaitingOnSize')
            return 3
        except NotAInt:
            self.msg.stateA = 1
            self.msg.sentenceA = "Write integer"
            sendMessage(self.connection, self.msg)
            return 1
        except WrongSizeboardError:
            self.msg.stateA = 1
            self.msg.sentenceA = "Write 1-9"
            sendMessage(self.connection, self.msg)
            return 1

class Char(State):
    def __init__(self, connection, msg):
        self.msg = msg
        self.connection = connection

    def run(self):
        logging.info('Current state %s', 'WaitingOnChar')
        self.msg.typeA = 7
        self.msg.stateA = 0
        self.msg.sentenceA = "'o' or 'x'?- x is default value"
        sendMessage(self.connection, self.msg)
        msg_rec = getResponse(self.connection)
        self.value = DictionaryOfClass[msg_rec.typeA]().getMessage(msg_rec)

    def getState(self):
        try:
            NumbersValidator.IsXorY(self.value)
            TicTacToeGame.finalChar=self.value
        finally:
            TicTacToeGame.game = Board.Board(TicTacToeGame.finalSize, TicTacToeGame.finalChar)
            logging.info('State %s is finished', 'WaitingOnChar')
            return 4

class SelectXandY(State):
    def __init__(self, connection, msg):
        self.msg = msg
        self.connection = connection

    def run(self):
        logging.info('Current state %s', 'SeletctXandY')
        self.msg.typeA = 9
        self.msg.stateA = 0
        self.msg.sentenceA = "Select x coordinate"
        sendMessage(self.connection, self.msg)
        msg_rec = getResponse(self.connection)
        self.x = DictionaryOfClass[msg_rec.typeA]().getMessage(msg_rec)
        #teraz wybieramy y
        self.msg.typeA = 11
        self.msg.stateA = 0
        self.msg.sentenceA = "Select y coordinate"
        sendMessage(self.connection, self.msg)
        msg_rec = getResponse(self.connection)
        self.y = DictionaryOfClass[msg_rec.typeA]().getMessage(msg_rec)

    def getState(self):
        try:
            NumbersValidator.IsInt(self.x)
            NumbersValidator.IsInt(self.y)
            x, y = int(self.x) - 1, int(self.y)-1
            TicTacToeGame.game.checkCoordinates(x, y)
        except NotAInt:
            self.msg.typeA = 9
            self.msg.stateA = 1
            self.msg.sentenceA = "x or y not a integer. "
            sendMessage(self.connection, self.msg)
            return 4
        except OutOfArrayError:
            self.msg.typeA = 9
            self.msg.stateA = 1
            self.msg.sentenceA = "x or y is highter or lower than sizeboard. "
            sendMessage(self.connection, self.msg)
            return 4
        except FieldIsOccupiedError:
            self.msg.typeA = 9
            self.msg.stateA = 1
            self.msg.sentenceA = "Field is occupied. "
            sendMessage(self.connection, self.msg)
            return 4
        TicTacToeGame.game.movePlayer(x, y)
        if TicTacToeGame.game.checkPlayersWin():
            self.msg.typeA = 9
            self.msg.stateA = 1
            self.msg.sentenceA = TicTacToeGame.game.printBoard()
            sendMessage(self.connection, self.msg)
            self.msg.typeA = 9
            self.msg.stateA = 1
            self.msg.sentenceA = "You win!!"
            sendMessage(self.connection, self.msg)
            logging.info('State %s is finished', 'SeletctXandY')
            return 0
        TicTacToeGame.game.moveCPU()
        self.msg.typeA = 9
        self.msg.stateA = 1
        self.msg.sentenceA = TicTacToeGame.game.printBoard()
        sendMessage(self.connection, self.msg)
        if TicTacToeGame.game.checkCPUsWin():
            self.msg.typeA = 9
            self.msg.stateA = 1
            self.msg.sentenceA = 'Unfortunately you lose'
            sendMessage(self.connection, self.msg)
            logging.info('State %s is finished', 'SeletctXandY')
            return 0
        return 4