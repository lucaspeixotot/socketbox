# -*- coding: utf-8 -*-
import messages
import re

class CreateAccount :
    def __init__(self, users, database) :
        self.key = '1'
        self.users = users
        self.database = database

    def run(self, connection) :
        request = []
        for _ in range(3) :
            l = connection.recv(1024)
            request = request + [l]
        username = request[0].split()[1]
        if username not in self.users :
            password = request[1].split()[1]
            passconf = request[2].split()[1]
            if password == passconf :
                messages.create_successfull(connection)
                messages.create_successfull()
                self.users[username] = password
                self.database.create_user(username, password)
            else :
                messages.create_not_successfull(connection, "As senhas digitadas não foram iguais")
        else :
            messages.create_not_successfull(connection, "Alguém já possui o username digitado!")
