from abc import ABCMeta, abstractmethod
from ManageProtobuf import *
import logging
from Validator import *

class State(metaclass=ABCMeta):
    #for server
    @abstractmethod
    def run(self):
        """pass"""

    @abstractmethod
    def getState(self):
        """pass"""

#klasy for client
class ServerListeningGame(State):
    def __init__(self, connection, msg):
        self.msg = msg
        self.connection = connection
        self.value=0

    def run(self):
        logging.info('Current state %s', 'ServerListeningGame')
        self.msg.typeA = 1
        self.msg.stateA = 0
        self.msg.sentenceA = "Select a game. 1-TicTacToe, 2-GuessANumber, 3-End"
        sendMessage(self.connection, self.msg)
        self.msg = getResponse(self.connection)
        self.value = DictionaryOfClass[self.msg.typeA]().getMessage(self.msg)

    def getState(self):
        try:
            NumbersValidator.GameNumberIsValid(self.value)
            if self.value == 3:
                return 100
            logging.info('State %s is finished', 'ServerListeningGame')
            return self.value
        except NotAInt:
            self.msg.typeA = 1
            self.msg.stateA = 0
            self.msg.sentenceA = "Write integer"
            sendMessage(self.connection, self.msg)
            return 0
        except InvalidValueError:
            self.msg.typeA = 1
            self.msg.stateA = 0
            self.msg.sentenceA = "Write 1, 2 or 3"
            sendMessage(self.connection, self.msg)
            return 0


