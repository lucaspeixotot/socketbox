# -*- coding:utf-8 -*-

from database import Database
from Registration import Registration
import network
import messages

class ListFilesRegistration(Registration) :
    def __init__(self, key, users) :
        Registration.__init__(self, key, users)
        self.database = Database()

    def run(self, body, socket) :
        messages.begin_registration(self.key, socket)
        username = body["content"]["username"]
        password = body["content"]["password"]

        if username not in self.users or self.users[username] != password:
            status = "0000"
            content = "ERROR: The server had problems with the user identification, please try log in again."
            messages.end_registration(self.key, socket, content)
        else :
            content = self.database.get_list_files(username)
            status = "1025"
            messages.end_registration(self.key, socket, "SUCCESS: The user list files was sended successfully.")
        msg = self.ack_construct(content, status, self.response_type)
        network.send(socket, msg)



        
