# -*- coding:utf-8 -*-

import view
import network
from Message import Message

class ClientCreateAccount :
    def __init__(self) :
        self.create_account_entries = ["username", "password", "password_confirmation"]
        self.key = "1"

    def run(self, socket) :
        view.create_account_protocol()
        request = []
        body = {}
        body["content"] = {}
        for x in self.create_account_entries :
            request.append(raw_input(x + ": "))
        msg = self.prepare_message(request, socket)
        network.send(socket, msg)
        self.response(socket)
        
    def prepare_message(self, request, socket) :
        header = {}
        body = {}
        body["content"] = {}
        header["type"] = "create"
        header["hb"] = ""
        header["ack"] = ""
        body["content"]["username"] = request[0]
        body["content"]["password"] = request[1]
        body["content"]["password_confirmation"] = request[2]
        msg = Message(header, body)
        return msg

    def response(self, socket) :
        msg, rest = network.receive(socket)
        message = Message()
        message.create_message(msg)
        body = message.get_body()
        print("%s - %s" % (body["status"], body["content"]))
