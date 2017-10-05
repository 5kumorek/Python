import socket
import Board
import random
from Validator import *

class EchoServer:
    def __init__(self, address, port, data_size):
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
        while True:
            end = '0'
            while "1" not in end and "2" not in end and "3" not in end:
                connection.send(str.encode("Select a game. 1-TicTacToe, 2-GuessANumber, 3-End"))
                connection.send(str.encode("(Print value)"))
                end = connection.recv(self.data_size).decode()
            if "1" in end:
                self.TicTacToeGame(connection)
            elif "2" in end:
                self.GuessANumber(connection)
            else:
                connection.send(str.encode("end"))
                break
        connection.close()


    def TicTacToeGame(self, connection):
        connection.send(str.encode("HI, now you start game aginst computer by server\n"))
        while True:
            connection.send(str.encode("Could you give me board's size lower than 10 and highter than 1?"))
            connection.send(str.encode("(Print value)"))
            sizeBoard = connection.recv(self.data_size).decode()
            try:
                NumbersValidator.sizeOfBoardIsValid(sizeBoard)
                break
            except WrongSizeboardError:
                continue
        connection.send(str.encode("'o' or 'x'?- x is default value"))
        connection.send(str.encode("(Print value)"))
        char = connection.recv(self.data_size)
        MyGame = Board.Board(int(sizeBoard), char.decode())
        while True:
            while True:
                connection.send(str.encode("Select x coordinate"))
                connection.send(str.encode("(Print value)"))
                x=connection.recv(self.data_size).decode()
                connection.send(str.encode("Select y coordinate"))
                connection.send(str.encode("(Print value)"))
                y = connection.recv(self.data_size).decode()
                try:
                    NumbersValidator.IsInt(x)
                    NumbersValidator.IsInt(y)
                    x, y = int(x) - 1, int(y) - 1
                    MyGame.checkCoordinates(x,y)
                    break
                except NotAInt:
                    connection.send(str.encode("x or y not a integer. "))
                except OutOfArrayError:
                    connection.send(str.encode("x or y is highter than sizeboard. "))
                except FieldIsOccupiedError:
                    connection.send(str.encode("Field is occupied. "))

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

    def GuessANumber(self, connection):
        minValue = 0
        maxValue = 100
        finalValue = random.randint(minValue,maxValue)
        connection.send(str.encode("HI, now you start game aginst computer by server\n"))
        connection.send(str.encode("Your task: guess what number it is?(number 1-100)\n"))
        while True:
            while True:
                connection.send(str.encode("Could you give me value?"))
                connection.send(str.encode("(Print value)"))
                value = connection.recv(self.data_size).decode()
                try:
                    NumbersValidator.GuessedValueIsValid(value)
                    break
                except NotAInt:
                    connection.send(str.encode("You must write integer. "))
                except InvalidValueError:
                    connection.send(str.encode("Value must be highter than 0 and lower than 101. "))

            if int(value)==finalValue:
                connection.send(str.encode("Congratulation you win. Wantend value = ", value, ". "))
                break
            elif int(value)<finalValue:
                connection.send(str.encode("Too low. "))
            else:
                connection.send(str.encode("Too hight. "))

if __name__ =='__main__':
    host = 'localhost'
    port = 1111
    data_size = 1024
    print('Server będzie obsługiwał 10 gier\n')
    for i in range(10):
        server = EchoServer(host, port, data_size)
        while server.serverSocket:
            try:
                server.handle_connect()
            except BrokenPipeError:
                print('Client is gone. Waiting for new player')
                continue
        server.serverSocket.close()
