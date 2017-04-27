import socket
import Board
from Validator import NotAInt
from Validator import OutOfBoard
from Validator import NumbersValidator

class EchoServer:
    def __init__(self, address, port, data_size):
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
        cos =connection.recv(self.data_size)
        connection.send(str.encode("HI, now you start game aginst computer by server\n"))
        while (True):
            connection.send(str.encode("Could you give me board's size?"))
            sizeBoard = connection.recv(self.data_size).decode()
            try:
                NumbersValidator.sizeOfBoardIsValid(sizeBoard)
            except NotAInt:
                print('Zły rozmiar planysz\n')
                break
            connection.send(str.encode("'o' or 'x'?"))
            char = connection.recv(self.data_size)
            MyGame = Board.Board(int(sizeBoard), char.decode())
            while (True):
                while (True):
                    connection.send(str.encode("Select x coordinate"))
                    x=connection.recv(self.data_size).decode()
                    connection.send(str.encode("Select y coordinate"))
                    y = connection.recv(self.data_size).decode()
                    try:
                        if NumbersValidator.isInt(x) and NumbersValidator.isInt(y) and MyGame.checkCoordinates(int(x),int(y)):
                            #if MyGame.checkCoordinates(int(x),int(y)):
                            break
                            #else:
                             #   connection.send(str.encode("Wrong coordinates\n"))
                        else:
                            connection.send(str.encode("Wrong coordinates\n"))
                    except:
                        print("Indeks out of board or x not are int")

                x,y=int(x)-1, int(y)-1
                MyGame.movePlayer(x, y)
                if MyGame.checkPlayersWin():
                    connection.send(str.encode(MyGame.printBoard()))
                    connection.send(str.encode('You win!!\n'))
                    break

                MyGame.moveCPU()
                connection.send(str.encode(MyGame.printBoard()))
                if MyGame.checkCPUsWin():
                    connection.send(str.encode('Unfortunately you lose'))
                    break
            end = '0'

            while end != '1' and end != '2':
                connection.send(str.encode("Type 1 to end and 2 to next game\n"))
                end =connection.recv(self.data_size).decode()

            if end is '2':
                continue
            elif end is '1':
                break
        connection.send(str.encode('bye'))
        connection.close()


if __name__ =='__main__':
    host = 'localhost'
    port = 1111
    data_size = 1024
    print('Server będzie obsługiwał 10 gier\n')
    for i in range(10):
        server = EchoServer(host, port, data_size)
        if server.serverSocket:
            server.handle_connect()