_author_="Radzio_pro_player"
import socket
import Validator
import message_pb2
from ManageProtobuf import *

#wartość zmiennej self.listening określa stan:0-wyślij wartość
#1-nasłuchuj, 2- zakończ program
class EchoClient:
    def __init__(self, address, port, data_size):
        self.listening = 1
        self.msg = message_pb2.msg()
        self.data_size = data_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #ten try jest niepotrzebny
        try:
            self.sock.connect((address, port))
        except socket.error:
            raise socket.error
        except OverflowError:
            raise OverflowError
        print('connected to {0} port {1}'.format(address, port))


    def sendMsg(self,typ):
        try:
            value = input()
            self.msg.typeA = typ
            if typ==2:
                self.msg.gameS = int(value)
            elif typ==4:
                self.msg.numberG = int(value)
            elif typ==6:
                self.msg.sizeT = int(value)
            elif typ==8:
                self.msg.crossT = value
            else:
                self.msg.xT = int(value)
            # ciekawe czy tak może być self.msg[typ+2] = value
            sendMessage(self.sock, self.msg)
            self.listening = 1
        except TypeError:
            print("Write number")
        except ValueError:
            print("Write number")

    def receiveMsg(self):
        msg = getResponse(self.sock)
        if msg:
            temp = DictionaryOfClass[msg.typeA](msg)
            print(temp.getMessage())
            self.listening = msg.stateA
        return msg.typeA


if __name__ == '__main__':
    host = 'localhost'
    try:
        port=int(input('Write a number of port\n'))
        data_size  = 1024
        client = EchoClient(host, port, data_size)
        t=1
        while int(client.listening)!=22:
            if client.listening:
                t = client.receiveMsg()
            else:
                client.sendMsg(t+1)
        print("Program zakończył działanie")
    except OverflowError:
        print("Port must be 0-65535. ")
    except socket.error:
        print("Invalid port. ")
