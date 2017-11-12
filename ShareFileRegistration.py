# -*- coding:utf-8 -*-

from Registration import Registration
from database import Database
import network
import messages

class ShareFileRegistration(Registration) :
    def __init__(self, key, users) :
        Registration.__init__(self, key, users)
        self.database = Database()

    def run(self, body, socket) :
        messages.begin_registration(self.key, socket)
        username = body["content"]["username"]
        password = body["content"]["password"]
        file_name = body["content"]["file_name"]
        file_type = body["content"]["file_type"]
        download_type = body["content"]["download_type"]
        target = body["content"]["target"]
        if username not in self.users or self.users[username] != password:
            status = "0000"
            content = "ERROR: The server had problems with the user identification, please try log in again."
        else :
            status = "1014"
            content = "SUCCESS: Your file was shared successful."
            file_read = self.database.download_file(download_type, file_name + file_type, username)
            file_read = file_read.decode("base64")
            if not file_read :
                status = "0000"
                content = "ERROR: The typed file doesn't exist in your account."
            else :
                try :
                    self.database.upload_file(target, file_name, file_read, file_type, "shared_files")
                except :
                    status = "0000"
                    content = "ERROR: Troubles was encoutered and your file doesn't shared!"
        msg = self.ack_construct(content, status, self.response_type)
        network.send(socket, msg)
        messages.end_registration(self.key, socket, content)
