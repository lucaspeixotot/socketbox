# -*- coding:utf-8 -*-

import os
import view
import messages
import network
from Requests import Requests

class UploadRequest(Requests) :
    def __init__(self, key, message_type, fields, status) :
        Requests.__init__(self, key, message_type, fields)
        self.status = status

    def run(self, socket) :
        self.content = {}
        try :
            filedir = raw_input("Digite o diretório COMPLETO do arquivo que deseja enviar: ")
            with open(filedir, "rb") as f :
                read_file = f.read()
        except :
            print("O diretório do arquivo digitado não existe!\n")
            return
        read_file = read_file.encode("base64")
        self.content["username"] = self.status["cur_username"]
        self.content["password"] = self.status["cur_password"]
        self.content["upload"] = read_file
        self.content["file_name"] = filedir[filedir.rfind("/") + 1 :]
        msg = self.prepare_message(socket, self.message_type)
        network.send(socket, msg)
        self.response(socket)

    def response(self, socket) :
        body = Requests.response(self, socket)
        print("Status " + body["status"] + " -> " + body["content"])
