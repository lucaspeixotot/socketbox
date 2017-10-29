# -*- coding:utf-8 -*-
import view

class ClientCreateAccount :
    def __init__(self) :
        self.create_account_entries = ["USERNAME: ", "PASSWORD: ", "PASSWORD_CONFIRMATION: "]
        self.key = "1"

    def run(self, client_socket) :
        view.create_account_protocol()
        request = []
        for x in self.create_account_entries :
            l = raw_input(x)
            l = x + l
            client_socket.send(l)
        response = client_socket.recv(1024)
        print(response)
