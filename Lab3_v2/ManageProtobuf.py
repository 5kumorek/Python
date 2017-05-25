import message_pb2 as proto
import struct

#funkcje doodczytywania widomości z protobudda
#wiadmości mogą być:sentence czyli indeks 1 i 3 albo int czyli 2 i 4
def getResponse(sock):
    msg = proto.msg()
    len_buf = socket_read_n(sock, 4)
    msg_len = struct.unpack('>L', len_buf)[0]
    msg_buf = socket_read_n(sock, msg_len)
    msg.ParseFromString(msg_buf)
    return msg

def sendMessage(sock, msg):
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
    def __init__(self, msg):
        self.msg = msg
    def getMessage(self):
        #określa którą gre wybrałem
        return self.msg.gameS

class Number_Request:
    def __init__(self, msg):
        self.msg = msg
    def getMessage(self):
        return self.msg.sentenceA
    def getState(self):
        return self.msg.stateA

class Number_Response:
    def __init__(self, msg):
        self.msg = msg
    def getMessage(self):
        #numberG określa jaką liczbe wybrał gracz
        return self.msg.numberG

class Size_Request:
    def __init__(self, msg):
        self.msg = msg

    def getMessage(self):
        # numberG określa jaką liczbe wybrał gracz
        return self.msg.sentenceA

class Size_Response:
    def __init__(self, msg):
        self.msg = msg

    def getMessage(self):
        # numberG określa jaką liczbe wybrał gracz
        return self.msg.sizeT

class Char_Request:
    def __init__(self, msg):
        self.msg = msg

    def getMessage(self):
        # numberG określa jaką liczbe wybrał gracz
        return self.msg.sentenceA

class Char_Response:
    def __init__(self, msg):
        self.msg = msg

    def getMessage(self):
        # numberG określa jaką liczbe wybrał gracz
        return self.msg.crossT

class X_Request:
    def __init__(self, msg):
        self.msg = msg

    def getMessage(self):
        # numberG określa jaką liczbe wybrał gracz
        return self.msg.sentenceA

class X_Response:
    def __init__(self, msg):
        self.msg = msg

    def getMessage(self):
        # numberG określa jaką liczbe wybrał gracz
        return self.msg.xT

class Y_Request:
    def __init__(self, msg):
        self.msg = msg

    def getMessage(self):
        # numberG określa jaką liczbe wybrał gracz
        return self.msg.sentenceA

class Y_Response:
    def __init__(self, msg):
        self.msg = msg

    def getMessage(self):
        # numberG określa jaką liczbe wybrał gracz
        return self.msg.yT

#słownik potrzebny do indekskowania klas
DictionaryOfClass={1:Game_Request, 2:Game_Response, 3:Number_Request, 4:Number_Response, 5:Size_Request, 6:Size_Response, 7:Char_Request, 8:Char_Response, 9:X_Request, 10:X_Response, 11:Y_Request, 12:Y_Response}
