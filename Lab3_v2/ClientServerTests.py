import unittest
import Validator
from EchoServer import EchoServer
from EchoClient import EchoClient
#tests for client

class BoardTests(unittest.TestCase):
    def test_check_if_number_of_port_for_server_is_str(self):
        self.assertRaises(Validator.NotAInt, EchoServer, 'localhost', 'adf', 1024)

    def test_check_if_number_of_port_for_server_is_toHight(self):
        self.assertRaises(Validator.InvalidPortError, EchoServer, 'localhost', 999999 , 1024)

    def test_check_if_number_of_port_for_client_is_str(self):
        self.assertRaises(TypeError, EchoClient, 'localhost', 'adf', 1024)

    def test_check_if_number_of_port_for_client_is_toHight(self):
        self.assertRaises(OverflowError, EchoClient, 'localhost', 999999 , 1024)


if __name__=='__main__':
    unittest.main(exit=False)