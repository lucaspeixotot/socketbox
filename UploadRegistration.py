# -*- coding:utf-8 -*-

import os
import network
from database import Database
from Registration import Registration

class UploadRegistration(Registration) :

    def __init__(self, key, users) :
        Registration.__init__(self, key, users)
        self.database = Database()

    def run(self, body, socket) :
        file_read = body["content"]["upload"]
        file_read = file_read.decode('base64')
        file_name = body["content"]["file_name"]
        file_type = body["content"]["file_type"]
        username = body["content"]["username"]
        password = body["content"]["password"]

        if username not in self.users or self.users[username] != password:
            status = "0000"
            content = "Problemas na identificação do usuário!"
        else :
            try :
                self.database.upload_file(username, file_name, file_read, file_type, "uploads")
                status = "1014"
                content = "Upload do arquivo " + file_name + " realizado com sucesso!"
            except :
                status = "0000"
                content = "Falha no upload!"
            
        msg = self.ack_construct(content, status, self.response_type)
        network.send(socket, msg)
        print("-----\nStatus - %s\nRequisição de upload realizada com sucesso!\n-----" % status)
