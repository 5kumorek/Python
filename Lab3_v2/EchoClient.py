_author_="Radzio_pro_player"
import socket
import Validator
import message_pb2
from ManageProtobuf import *

#wartość zmiennej self.listening określa stan:0-wyślij wartość
#1-nasłuchuj,
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
            #client wpisuje wartość
            value = input()
            #client wysyła swoją wartość i typ, czyli definiuje
            # jakę chce wiadomość wysłać

            makeAndSendMessage(self.sock, value, typ)
            #zmieniam stan mojego servera na nasłuchiwanie
            self.listening = 1
        except InvalidValueError:
            print("Write number")

    def receiveMsg(self):
        msg = getResponse(self.sock)
        if msg:
            #client rozkodowuje wiadomość przy pomocy klas
            temp = DictionaryOfClass[msg.typeA](msg)
            #wypisuje wiadomość otrzymaną od servera
            print(temp.getMessage())
            #sprawdzam jaki stan mi nakazał server, czy kazał mi nasłuchiwać
            #czy mam wysłać wiadomość
            self.listening = msg.stateA
        return msg.typeA


if __name__ == '__main__':
    host = 'localhost'
    try:
        port=int(input('Write a number of port\n'))
        data_size  = 1024
        client = EchoClient(host, port, data_size)
        t=1
        #t = 1 to znaczy że zaczynamy program od nasłuchiwania od servera
        while int(client.listening)!=100:
            #jeżeli mam nasluchiwać to nasłuchuje, jeśli nie to wysyłam wiadomość
            if client.listening:
                t = client.receiveMsg()
            else:
                client.sendMsg(t+1)
        print("Program zakończył działanie")
    except OverflowError:
        print("Port must be 0-65535. ")
    except socket.error:
        print("Invalid port. ")
