import socket
import message_pb2 as proto
import logging
from GuessANumber import GuessANumber
from TicTacToeGame import *
from ManageProtobuf import *
from Validator import *
from StatesFile import *

class EchoServer:
    def __init__(self, address, port, data_size):
        #inicjalizacja logów
        logging.basicConfig(filename='example.log', level=logging.DEBUG)
        #możliwe stany gry
        self.DictionaryOfStates = {0:ServerListeningGame, 1: Size, 2: GuessANumber, 3:Char, 4:SelectXandY}
        #ten try to takie zabezpieczenie czegoś co powinno być zawsze poprawne
        # bo jest na sztywno wpisane do programu
        try:
            NumbersValidator.IsInt(port)
            if port<0 or port>65535:
                raise InvalidPortError
        except NotAInt:
            logging.warning('Obtained value is invalid %s is wrong', port)
            raise NotAInt
        except InvalidPortError:
            logging.info('Obtained value is to high or to low %s is wrong', port)
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
        #nasłuchujemy
        self.serverSocket.listen(1)
        connection, client_address = self.serverSocket.accept()
        msg = proto.msg()
        # stan zero jest to stan wybóru gry więc od niego zaczynamy
        state = 0
        # stany są od 0 do 4, gdy state =100 to znaczy że client chce zakończyć gre
        while state != 100:
            #tworze instancje odpowiedniego stanu, uruchamia się funkcja init
            currentState = self.DictionaryOfStates[state](connection, msg)
            #wykonuje funckje dla mojego stanu
            currentState.run()
            #sprawdzam jaki stan mam po wykonaniu odpowiedniej funckji
            state = currentState.getState()
        #wysyłam wiadomość że to już koniec
        msg.typeA = 1
        msg.stateA = 100
        msg.sentenceA = "Disconnect"
        sendMessage(connection, msg)
        connection.close()


if __name__ =='__main__':
    host = 'localhost'
    port = 1111
    data_size = 1024
    #dałem maksymalnie trzy gry
    NumberOfGame=3
    print('Server będzie obsługiwał {} gier\n'.format(NumberOfGame))
    for i in range(NumberOfGame):
        server = EchoServer(host, port, data_size)
        server.handle_connect()
        print('Client is gone. Waiting for new player')
