# -*- coding:utf-8 -*-

from database import Database
from Registration import Registration
import network

class ListFilesRegistration(Registration) :
    def __init__(self, key, users) :
        Registration.__init__(self, key, users)
        self.database = Database()

    def run(self, body, socket) :
        username = body["content"]["username"]
        password = body["content"]["password"]

        if username not in self.users or self.users[username] != password:
            status = "0000"
            content = "Problemas na identificação do usuário!"
        else :
            content = self.database.get_list_files(username)
            status = "1025"
            # status = "0102"
            # content = "Falha em pegar a lista de arquivos upados!"
        msg = self.ack_construct(content, status, self.response_type)
        network.send(socket, msg)
        print("-----\nStatus - %s\nRequisição de listar aquivos realizada com sucesso!\n-----" % status)



        
