# -*- coding:utf-8 -*-

import view
import messages
from Requests import Requests

class LoginRequest(Requests) :
    def __init__(self, key, message_type, fields, status) :
        Requests.__init__(self, key, message_type, fields)
        self.status = status

    def response(self, socket) :
        body = Requests.response(self, socket)
        if body["status"] == "0025" or body["status"] == "0017" :
            messages.login_not_successfull(body["status"])
        else :
            self.status["logged"], self.status["cur_username"], self.status["cur_password"] = 1, self.content["username"], self.content["password"]
            messages.login_successfull()
