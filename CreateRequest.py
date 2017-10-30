# -*- coding:utf-8 -*-

import network
from Request import Request
from database import Database

class CreateRequest(Request) :

    def __init__(self, key, users) :
        Request.__init__(self, key)
        self.users = users
        self.response_type = "create_response"
        self.database = Database()
        
    def run(self, body, socket) :
        username = body["content"]["username"]
        password = body["content"]["password"]
        password_confirmation = body["content"]["password_confirmation"]

        if username in self.users:
            content = "The typed username already exist in the system!"
            status = "0025"
        elif password != password_confirmation :
            content = "The typed passwords are differente!"
            status = "0017"
        else :
            content = "Account created with successful!"
            status = "1025"
            self.users[username] = password
            self.database.create_user(username, password)

        msg = self.ack_construct(content, status, self.response_type)
        network.send(socket, msg)
        print("%s - Requisição realizada com sucesso!" % status)
