_author_="Radzio_pro_player"
import socket
import sys

class EchoClient:
    def __init__(self, address, port, data_size):
        self.data_size = data_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((address, port))
        except socket.error:
            print('Nie udało sie\n')
        print('connected to {0} port {1}'.format(address, port))


    def sendMessage(self, msg):
        try:
            self.sock.send(str.encode(msg))
            response = self.sock.recv(self.data_size).decode()
        except:
            print('no i lipa')
            sys.exit()
        #nie wiem dlaczego tak musi być, siedziałem nad tym godzine i dalej nie wiem
        while response is "Something":
            print(response)
            response = self.sock.recv(self.data_size).decode()
        print(response)

    def _createTcpIpSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _connectToServer(self, address, port):
        server_address = (address, port)
        print('connecting to %s port %s' %server_address)
        self.sock.connect(server_address)

if __name__ == '__main__':
    host = 'localhost'
    port=int(input('Write a number of port\n'))
    #port = 1235
    data_size  = 1024
    client = EchoClient(host, port, data_size)
    if client.sock:
        data = 'Hi'
        while True:
            client.sendMessage(data)
            data = input()

