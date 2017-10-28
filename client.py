# -*- coding:utf-8 -*-

import socket
import view # implementar view
import messages
from parse_options import ParseOptions

class Client :
    def __init__(self, host="localhost", port=6789) :
        self.host = host
        self.port = port
        self.running = 1
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.status = [0]
        self._parse_options = ParseOptions(self.status)

    def connect(self) :
        self.client_socket.connect((self.host, self.port))

    def run(self) :
        while self.running :
            view.apresentation()
            view.menu_options(self.status[0])
            opt = raw_input("Digite a sua opcao: ")
            self.client_socket.send(opt)
            self._parse_options.run(int(opt), self.client_socket)
            print("status client", self.status[0])
        self.client_socket.close()

client = Client()
client.connect()
client.run()
