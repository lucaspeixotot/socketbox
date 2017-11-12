# -*- coding:utf-8 -*-

from Registration import Registration
from database import Database
import network
import messages

class DownloadRegistration(Registration) :
    def __init__(self, key, users) :
        Registration.__init__(self, key, users)
        self.database = Database()

    def run(self, body, socket) :
        messages.begin_registration(self.key, socket)
        file_name = body["content"]["file_name"]
        download_type = body["content"]["download_type"]
        username = body["content"]["username"]
        password = body["content"]["password"]
        if username not in self.users or self.users[username] != password:
            status = "0000"
            content = "ERROR: The server had problems with the user identification, please try log in again."
        else :
            status = "1014"
            file_download = self.database.download_file(download_type, file_name, username)
            content = "SUCCESS: The file was downloaded successfully."
            if not file_download :
                status = "0000"
                content = "ERROR: The typed file doesn't exist in your account."
        msg = self.ack_construct(file_download, status, self.response_type)
        network.send(socket, msg)
        messages.end_registration(self.key, socket, content)
        
