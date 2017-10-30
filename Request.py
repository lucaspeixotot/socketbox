# -*- coding:utf-8 -*-

from Message import Message

class Request :
    def __init__(self, key):
        self.key = key

    def ack_construct(self, content, status, response_type) :
        header = {}
        body = {}
        header["type"] = ""
        header["ack"] = response_type
        header["hb"] = ""
        body["content"] = content
        body["status"] = status
        msg = Message(header, body)
        return msg
