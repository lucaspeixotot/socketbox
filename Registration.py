# -*- coding:utf-8 -*-

from Message import Message

class Registration :
    def __init__(self, key, users):
        self.key = key
        self.users = users
        self.response_type = self.key + "_response"

    def ack_construct(self, content, status, response_type) :
        header = {}
        body = {}
        header["type"] = ""
        header["ack"] = response_type
        body["content"] = content
        body["status"] = status
        msg = Message(header, body)
        return msg
