# -*- coding:utf-8 -*-

import network
from Registration import Registration
from database import Database

class CreateRegistration(Registration) :

    def __init__(self, key, users) :
        Registration.__init__(self, key, users)
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
