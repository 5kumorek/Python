import message_pb2 as proto
import struct
from Validator import *

#funkcja do odczytywania widomości z protobuffa, socket_read_n
def getResponse(sock):
    msg = proto.msg()
    len_buf = socket_read_n(sock, 4)
    msg_len = struct.unpack('>L', len_buf)[0]
    msg_buf = socket_read_n(sock, msg_len)
    msg.ParseFromString(msg_buf)
    return msg
#funckja która otrzymuje wiadomość, serializuje i wysyła
def sendMessage(sock, msg):
    s = msg.SerializeToString()
    length = struct.pack('>L', len(s))
    message = length + s
    sock.send(message)
#funkcja stworzona dla clienta, troche inaczej działa bo nie zakładamy
# że client jest nieomylny więc sprawdzamy wartości
def makeAndSendMessage(sock, value, type):
    try:
        msg = DictionaryOfClass[type]().makeMessage(value, type)
    except NotAInt:
        raise InvalidValueError
    s = msg.SerializeToString()
    length = struct.pack('>L', len(s))
    message = length + s
    sock.send(message)

def socket_read_n(sock, n):
    buf = bytes()
    while n > 0:
        data = sock.recv(n)
        if data == '':
            raise RuntimeError('unexpected connection close')
        buf += data
        n -= len(data)
    return buf

#klasy definiujące typ wiadomości
class Game_Request:
    def __init__(self, msg):
        self.msg = msg
    def getMessage(self):
        return self.msg.sentenceA
    def getState(self):
        return self.msg.stateA

class Game_Response:
    def __init__(self):
        self.msg = proto.msg()
    # tworzy mi wiadomość
    def makeMessage(self, value, type):
        try:
            NumbersValidator.IsInt(value)
        except NotAInt:
            raise InvalidValueError
        self.msg.gameS = int(value)
        self.msg.typeA = int(type)
        return self.msg
    #odczytuje wartosć z wiadomości
    def getMessage(self, msg):
        return msg.gameS

class Number_Request:
    def __init__(self, msg):
        self.msg = msg
    def getMessage(self):
        return self.msg.sentenceA
    def getState(self):
        return self.msg.stateA

class Number_Response:
    def __init__(self):
        self.msg = proto.msg()
    # tworzy mi wiadomość
    def makeMessage(self, value, type):
        try:
            NumbersValidator.IsInt(value)
        except NotAInt:
            raise InvalidValueError
        self.msg.numberG = int(value)
        self.msg.typeA = int(type)
        return self.msg
    #odczytuje wartosć z wiadomości
    def getMessage(self, msg):
        return msg.numberG

class Size_Request:
    def __init__(self, msg):
        self.msg = msg

    def getMessage(self):
        # numberG określa jaką liczbe wybrał gracz
        return self.msg.sentenceA

class Size_Response:
    def __init__(self):
        self.msg = proto.msg()
    # tworzy mi wiadomość
    def makeMessage(self, value, type):
        try:
            NumbersValidator.IsInt(value)
        except NotAInt:
            raise InvalidValueError
        self.msg.sizeT = int(value)
        self.msg.typeA = int(type)
        return self.msg
    #odczytuje wartosć z wiadomości
    def getMessage(self, msg):
        return msg.sizeT

class Char_Request:
    def __init__(self, msg):
        self.msg = msg

    def getMessage(self):
        # numberG określa jaką liczbe wybrał gracz
        return self.msg.sentenceA

class Char_Response:
    def __init__(self):
        self.msg = proto.msg()
    def makeMessage(self, value, type):
        self.msg.crossT = value
        self.msg.typeA = int(type)
        return self.msg
    def getMessage(self, msg):
        #określa którą gre wybrałem
        return msg.crossT

class X_Request:
    def __init__(self, msg):
        self.msg = msg

    def getMessage(self):
        # numberG określa jaką liczbe wybrał gracz
        return self.msg.sentenceA

class X_Response:
    def __init__(self):
        self.msg = proto.msg()
    # tworzy mi wiadomość
    def makeMessage(self, value, type):
        try:
            NumbersValidator.IsInt(value)
        except NotAInt:
            raise InvalidValueError
        self.msg.xT = int(value)
        self.msg.typeA = int(type)
        return self.msg
    #odczytuje wartosć z wiadomości
    def getMessage(self, msg):
        return msg.xT

class Y_Request:
    def __init__(self, msg):
        self.msg = msg

    def getMessage(self):
        # numberG określa jaką liczbe wybrał gracz
        return self.msg.sentenceA

class Y_Response:
    def __init__(self):
        self.msg = proto.msg()
    # tworzy mi wiadomość
    def makeMessage(self, value, type):
        try:
            NumbersValidator.IsInt(value)
        except NotAInt:
            raise InvalidValueError
        self.msg.yT = int(value)
        self.msg.typeA = int(type)
        return self.msg
    #odczytuje wartosć z wiadomości
    def getMessage(self, msg):
        return msg.yT

#słownik potrzebny do indekskowania klas
DictionaryOfClass={1:Game_Request, 2:Game_Response, 3:Number_Request, 4:Number_Response, 5:Size_Request, 6:Size_Response, 7:Char_Request, 8:Char_Response, 9:X_Request, 10:X_Response, 11:Y_Request, 12:Y_Response}
