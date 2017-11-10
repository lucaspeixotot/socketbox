# -*- coding:utf-8 -*-

from Requests import Requests
from ListFilesRequest import ListFilesRequest
import network

class ShareFileRequest(Requests) :
    def __init__(self, key, message_type, status) :
        Requests.__init__(self, key, message_type)
        self.status = status
        self.list_files = ListFilesRequest("3", "list_files", self.status)

    def run(self, socket) :
        self.content = {}
        self.content["username"] = self.status["cur_username"]
        self.content["password"] = self.status["cur_password"]
        self.list_files.run(socket)
        print("\nWARNING: You can only share your uploaded files!\n")
        self.content["download_type"] = "uploads"
        file_total_name = raw_input("File name: ")
        file_name = file_total_name[:file_total_name.rfind(".")]
        file_type = file_total_name[file_total_name.rfind("."):]
        self.content["file_name"] = file_name
        self.content["file_type"] = file_type
        print("Type the username that you want share your file.")
        self.content["target"] = raw_input("username: ")
        msg = self.prepare_message(socket)
        network.send(socket, msg)
        self.response(socket)

    def response(self, socket) :
        body = Requests.response(self, socket)
        print("Status - %s\n%s" % (body["status"], body["content"]))
