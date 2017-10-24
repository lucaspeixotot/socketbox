# -*- coding: utf-8 -*-
import messages
import re

class CreateAccount :
    def __init__(self, users) :
        self.key = '1'
        self.users = users
        self.parse_options = {}


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
                messages.successfull(connection)
                self.users[username] = password
            else :
                messages.not_successfull(connection, "As senhas digitadas não foram iguais")
        else :
            messages.not_successfull(connection, "Alguém já possui o username digitado!")

# username_pattern = re.compile("USERNAME : [a-zA-Z0-9_.-]+")
# password_pattern = re.compile("PASSWORD : [a-zA-Z0-9_.-]+")
# password_confirmation_pattern = re.compile("PASSWORD_CONFIRMATION : [a-zA-Z0-9_.-]+")
