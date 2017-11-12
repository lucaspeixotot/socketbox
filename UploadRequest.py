# -*- coding:utf-8 -*-

import os
import view
import messages
import network
from Requests import Requests

class UploadRequest(Requests) :
    def __init__(self, key, message_type, fields, status) :
        Requests.__init__(self, key, message_type)
        self.status = status
        self.fields = fields

    def run(self, socket) :
        self.content = {}
        try :
            filedir = raw_input("Type the complete file directory that you want upload: ")
            print("Reading file...")
            with open(filedir, "rb") as f :
                read_file = f.read()
        except :
            print("ERROR: The typed directory doesn't match with a possible file to be uploaded, pay attention in the next try.")
            return
        read_file = read_file.encode("base64")
        self.content["username"] = self.status["cur_username"]
        self.content["password"] = self.status["cur_password"]
        self.content["upload"] = read_file
        file_total_name = filedir[filedir.rfind("/") + 1 :]
        file_name = file_total_name[:file_total_name.find(".")]
        file_type = file_total_name[file_total_name.find("."):]
        self.content["file_name"] = file_name
        self.content["file_type"] = file_type
        msg = self.prepare_message(socket)
        print("Sending file...")
        network.send(socket, msg)
        self.response(socket)

    def response(self, socket) :
        body = Requests.response(self, socket)
        print(body["content"])
