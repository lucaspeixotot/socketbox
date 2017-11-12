# -*- coding:utf-8 -*-

import network
import messages
from Registration import Registration

class LoginRegistration(Registration) :

    def __init__(self, key, users) :
        Registration.__init__(self, key, users)
        
    def run(self, body, socket) :
        messages.begin_registration(self.key, socket)
        username = body["content"]["username"]
        password = body["content"]["password"]

        if username in self.users and password == self.users[username] :
            status = "1014"
            content = "SUCCESS: User successfully logged in."
        elif username not in self.users :
            status = "0000"
            content = "ERROR: The typed user doesn't exist in the system."
        else :
            status = "0000"
            content = "ERROR: The types password was incorrect."
        msg = self.ack_construct(content, status, self.response_type)
        network.send(socket, msg)
        messages.end_registration(self.key, socket, content)
