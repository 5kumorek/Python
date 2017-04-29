_author_="Radzio_pro_player"
import socket
import Validator

class EchoClient:
    def __init__(self, address, port, data_size):
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


    def sendMessage(self, msg):
            self.sock.send(str.encode(msg))

    def receiveMessage(self):
        while True:
            response = self.sock.recv(self.data_size).decode()
            print(response)
            if "(Print value)" in response:
                break
            elif "end" in response:
                self.sock.close()
                raise Validator.EndOfGameError
            elif response=="":
                self.sock.close()
                raise Validator.EndOfGameError

if __name__ == '__main__':
    host = 'localhost'
    try:
        port=int(input('Write a number of port\n'))
        data_size  = 1024
        client = EchoClient(host, port, data_size)
        while client:
            try:
                client.receiveMessage()
            except Validator.EndOfGameError:
                break
            data = input()
            client.sendMessage(data)
    except OverflowError:
        print("Port must be 0-65535. ")
    except socket.error:
        print("Invalid port. ")
