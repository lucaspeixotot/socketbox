# -*- coding:utf-8 -*-

from ListFilesRequest import ListFilesRequest
from Requests import Requests
import network

class DownloadRequest(Requests) :
    def __init__(self, key, message_type, status) :
        Requests.__init__(self, key, message_type)
        self.status = status
        self.list_files = ListFilesRequest("3", "list_files", self.status)

    def run(self, socket) :
        self.content = {}
        self.content["username"] = self.status["cur_username"]
        self.content["password"] = self.status["cur_password"]
        self.list_files.run(socket)
        print("Type what download type you want to do(uploads or shared), or type cancel to abort.")
        l = ""
        while l != "uploads" and l != "shared" and l != "cancel" :
            l = raw_input("Download type: ")
            if l == "shared" : l = "shared_files"
            self.content["download_type"] = l
        file_name = raw_input("File name: ")
        print("Have you a path of your preference to the file to be stored? If not, the file will be downloaded in application path, in this case type enter.")
        file_path = raw_input("Type the path here: ")
        file_path = file_path + "/" if file_path[-1] != "/" else file_path
        self.content["file_name"] = file_name
        msg = self.prepare_message(socket)
        network.send(socket, msg)
        self.response(socket, file_path, file_name)

    def response(self, socket, file_path, file_name) :
        body = Requests.response(self, socket)
        if body["status"] == "1014" :
            with open(file_path + file_name, "wb") as f:
                file_to_be_save = body["content"].decode("base64")
                f.write(file_to_be_save)
            print("Status - %s\nThe file was downloaded successful!" % body["status"])
        else :
            print("Status - %s\nMessage: %s" % (body["status"], body["content"]))
