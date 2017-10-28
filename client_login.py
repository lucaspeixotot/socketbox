# -*- coding:utf-8 -*-

import view
import messages

class ClientLogin :
    def __init__(self, status) :
        self.fields = ["USERNAME: ", "PASSWORD: "]
        self.key = 2
        self.status = status

    def run(self, client_socket) :
        view.client_login()
        for x in self.fields :
            l = raw_input(x)
            client_socket.send(l)
        response = int(client_socket.recv(1024))
        if response == 0 or response == 2 :
            messages.login_not_successfull(response)
        else :
            self.status[0] = response
            messages.login_successfull()

