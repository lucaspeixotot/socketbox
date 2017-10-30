# -*- coding:utf-8 -*-

import view
import network
from Message import Message
from Requests import Requests

class CreateRequest(Requests) :
    def __init__(self, key, message_type, fields) :
        Requests.__init__(self, key, message_type, fields)

    def response(self, socket) :
        body = Requests.response(self, socket)
        print("%s - %s" % (body["status"], body["content"]))
