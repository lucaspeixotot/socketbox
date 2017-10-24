# -*- coding:utf-8 -*-

import view

class ClientLogin :
    def __init__(self) :
        self.fields = ["USERNAME", "PASSWORD"]

    def run(self, client_socket) :
        view.client_login()
        for x in self.fields :
            l = raw_input(x)
            client_socket.send(l)
        response = client_socket.recv(1024)
        return response
