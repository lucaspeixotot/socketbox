# -*- coding:utf-8 -*-

from Registration import Registration
from database import Database
import network

class DownloadRegistration(Registration) :
    def __init__(self, key, users) :
        Registration.__init__(self, key, users)
        self.database = Database()

    def run(self, body, socket) :
        file_name = body["content"]["file_name"]
        download_type = body["content"]["download_type"]
        username = body["content"]["username"]
        password = body["content"]["password"]
        if username not in self.users or self.users[username] != password:
            status = "0000"
            content = "Problemas na identificação do usuário!"
        else :
            status = "1014"
            content = self.database.download_file(download_type, file_name, username)
            if not content :
                status = "0000"
                content = "The typed file doesn't exist."
        msg = self.ack_construct(content, status, self.response_type)
        network.send(socket, msg)
        print("-----\nStatus - %s\nRequisição de download realizada com sucesso!\n-----" % status)
        
