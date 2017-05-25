import random
from ManageProtobuf import *
from Validator import *
from StatesFile import State

#guess a number class
class Helpfull:
    # zmienna używana w klasie GuessANumber
    firstInvoked = True
    # kolejna zmienna tam używana
    finalValue = 0

class GuessANumber(State):
    def __init__(self, connection, msg):
        self.msg = msg
        self.connection = connection

    def run(self):
        msg_rec = proto.msg()
        if Helpfull.firstInvoked:
            minValue = 0
            maxValue = 100
            Helpfull.finalValue = random.randint(minValue, maxValue)
            print(Helpfull.finalValue)
            # definiuje wiadomość
            self.msg.typeA = 3
            self.msg.stateA = 1
            self.msg.sentenceA = "HI, now you start game against computer by server"
            sendMessage(self.connection, self.msg)
            self.msg.sentenceA = "Your task: guess what number it is?(number 1-100)"
            sendMessage(self.connection, self.msg)
            Helpfull.firstInvoked = False
        self.msg.sentenceA = "Could you give me value?"
        self.msg.stateA = 0
        sendMessage(self.connection, self.msg)
        msg_rec = getResponse(self.connection)
        temp = DictionaryOfClass[msg_rec.typeA](msg_rec)
        self.value = temp.getMessage()

    def getState(self):
        try:
            NumbersValidator.GuessedValueIsValid(self.value)
            if int(self.value) == Helpfull.finalValue:
                self.msg.stateA = 1
                self.msg.sentenceA = "Congratulation you win. Wanted value = {}".format(self.value)
                sendMessage(self.connection, self.msg)
                return 0
            elif int(self.value) < Helpfull.finalValue:
                self.msg.sentenceA = "Too low. "
                self.msg.stateA = 1
                sendMessage(self.connection, self.msg)
                return 2
            else:
                self.msg.sentenceA = "Too hight. "
                self.msg.stateA = 1
                sendMessage(self.connection, self.msg)
                return 2
        except NotAInt:
            self.msg.stateA = 1
            self.msg.sentenceA = "Write integer"
            sendMessage(self.connection, self.msg)
            return 2
        except InvalidValueError:
            self.msg.stateA = 1
            self.msg.sentenceA = "Write 1-100"
            sendMessage(self.connection, self.msg)
            return 2

