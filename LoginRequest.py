# -*- coding:utf-8 -*-

import view
import messages
from Requests import Requests

class LoginRequest(Requests) :
    def __init__(self, key, message_type, fields, status) :
        Requests.__init__(self, key, message_type)
        self.status = status
        self.fields = fields

    def response(self, socket) :
        body = Requests.response(self, socket)
        if body["status"] == "1014" :
            self.status["logged"], self.status["cur_username"], self.status["cur_password"] = 1, self.content["username"], self.content["password"]
        print(body["content"])
