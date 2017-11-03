# -*- coding:utf-8 -*-

from Message import Message
import network

class Requests :
    def __init__(self, key, message_type, fields) :
        self.key = key
        self.fields = fields
        self.message_type = message_type

    def run(self, socket) :
        self.content = {}
        for x in self.fields :
            l = raw_input(x + ": ")
            self.content[x] = l
        msg = self.prepare_message(socket, self.message_type)
        network.send(socket, msg)
        self.response(socket)

    def prepare_message(self, socket, type_message) :
        header ={}
        body = {}
        body["content"] = {}
        header["type"] = type_message
        header["hb"] = ""
        header["ack"] = ""
        body["content"] = self.content
        msg = Message(header, body)
        return msg

    def response(self, socket) :
        msg, rest = network.receive(socket)
        message = Message()
        message.create_message(msg)
        body = message.get_body()
        return body
        
