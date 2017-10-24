# -*- coding:utf-8 -*-

import socket
import view # implementar view
from client_create_account import ClientCreateAccount
from client_login import ClientLogin

class Client :
    def __init__(self, host="localhost", port=6789) :
        self.host = host
        self.port = port
        self.running = 1
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self) :
        self.client_socket.connect((self.host, self.port))

    def run(self) :
        status = 0
        while self.running :
            view.apresentation()
            view.menu_options(status)
            opt = raw_input("Digite a sua opcao: ")
            self.client_socket.send(opt)
            if opt == '1' :
                cca = ClientCreateAccount()
                cca.run(self.client_socket)
                response = self.client_socket.recv(1024)
                print(response)
            elif opt == '2' :
                cl = ClientLogin()
                response = cl.run(self.client_socket)
                if response == 0 or response == 2 :
                    messages.login_not_successfull(response)
                else :
                    status = response
                    messages.login_successfull()
            elif opt == '3' :
                pass
            else :
                self.running = 0
        self.client_socket.close()
client = Client()
client.connect()
client.run()
