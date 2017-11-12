# -*- coding:utf-8 -*-

import os
import network
import messages
from database import Database
from Registration import Registration

class UploadRegistration(Registration) :

    def __init__(self, key, users) :
        Registration.__init__(self, key, users)
        self.database = Database()

    def run(self, body, socket) :
        messages.begin_registration(self.key, socket)
        file_read = body["content"]["upload"]
        file_read = file_read.decode('base64')
        file_name = body["content"]["file_name"]
        file_type = body["content"]["file_type"]
        username = body["content"]["username"]
        password = body["content"]["password"]

        if username not in self.users or self.users[username] != password:
            status = "0000"
            content = "ERROR: The server had problems with the user identification, please try log in again."
        else :
            try :
                self.database.upload_file(username, file_name, file_read, file_type, "uploads")
                status = "1014"
                content = "SUCCESS: Updated " + file_name + " was successfully completed."
            except :
                status = "0000"
                content = "ERROR: The server had some problems and your file wasn't able to be uploaded."
            
        msg = self.ack_construct(content, status, self.response_type)
        network.send(socket, msg)
        messages.end_registration(self.key, socket, content)
