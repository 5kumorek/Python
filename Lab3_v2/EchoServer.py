import socket
import message_pb2 as proto
from GuessANumber import GuessANumber
from TicTacToeGame import *
from ManageProtobuf import *
from Validator import *
from StatesFile import *

class EchoServer:
    def __init__(self, address, port, data_size):
        self.DictionaryOfStates = {0:ServerListeningGame, 1: Size, 2: GuessANumber, 3:Char, 4:SelectXandY}
        #ten try to takie zabezpieczenie czegoś co powinno być zawsze poprawne
        # bo jest na sztywno wpisane do programu
        try:
            NumbersValidator.IsInt(port)
            if port<0 or port>65535:
                raise InvalidPortError
        except NotAInt:
            raise NotAInt
        except InvalidPortError:
            raise InvalidPortError

        #a tu właściwa częśc inita
        self.data_size = data_size
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for i in range(10):
            try:
                self.serverSocket.bind((address, port))
                break
            except socket.error:
                port+=1
                continue
        print('bind to {0} port {1}'.format(address, port))


    def handle_connect(self):
        self.serverSocket.listen(1)
        connection, client_address = self.serverSocket.accept()
        msg = proto.msg()
        state = 0
        while state != 100:
            currentState = self.DictionaryOfStates[state](connection, msg)
            currentState.run()
            state = currentState.getState()
            print(state)
        #wysyłam wiadomość że to już koniec
        msg.typeA = 1
        msg.stateA = 22
        msg.sentenceA = "Disconnect"
        sendMessage(connection, msg)
        connection.close()


if __name__ =='__main__':
    host = 'localhost'
    port = 1111
    data_size = 1024
    NumberOfGame=3
    print('Server będzie obsługiwał {} gier\n'.format(NumberOfGame))
    for i in range(NumberOfGame):
        server = EchoServer(host, port, data_size)
        server.handle_connect()
        print('Client is gone. Waiting for new player')
