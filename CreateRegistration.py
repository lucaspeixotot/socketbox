# -*- coding:utf-8 -*-

import network
from Registration import Registration
from database import Database
import messages

class CreateRegistration(Registration) :

    def __init__(self, key, users) :
        Registration.__init__(self, key, users)
        self.database = Database()
        
    def run(self, body, socket) :
        messages.begin_registration(self.key, socket)
        username = body["content"]["username"]
        password = body["content"]["password"]
        password_confirmation = body["content"]["password_confirmation"]

        if username in self.users:
            content = "ERROR: The typed username already exist in the system!"
            status = "0000"
        elif password != password_confirmation :
            content = "ERROR: The typed passwords are different!"
            status = "0000"
        else :
            content = "SUCCESS: Account was created successful!"
            status = "1014"
            self.users[username] = password
            self.database.create_user(username, password)

        msg = self.ack_construct(content, status, self.response_type)
        network.send(socket, msg)
        messages.end_registration(self.key, socket, content)
