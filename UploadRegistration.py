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
        username = body["content"]["username"]
        password = body["content"]["password"]

        if username not in self.users or self.users[username] != password:
            status = "0000"
            content = "Problemas na identificação do usuário!"
        else :
            self.database.upload_file(username, file_name, file_read)
            status = "1025"
            content = "Upload do arquivo " + file_name + " realizado com sucesso!"
        msg = self.ack_construct(content, status, self.response_type)
        network.send(socket, msg)
        print("-----\nStatus - %s\nRequisição de upload realizada com sucesso!\n-----" % status)

        # RESOLVE PROBLEMA DO ENVIO DE UMA IMAGEM E  RESOLVER O PROBLEMA DE ADICIONAR UM ARQUIVO VERSAO 3
