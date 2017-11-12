# -*- coding:utf-8 -*-

import view
import network
from Message import Message
from Requests import Requests

class CreateRequest(Requests) :
    def __init__(self, key, message_type, fields) :
        Requests.__init__(self, key, message_type)
        self.fields = fields

    def response(self, socket) :
        body = Requests.response(self, socket)
        print(body["content"])
