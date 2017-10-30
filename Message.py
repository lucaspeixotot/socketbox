# -*- coding:utf-8 -*-

import json

class Message :
    def __init__(self, header={}, body={}) :
        self.msg = {}
        self.msg["header"] = header
        self.msg["body"] = body

    def get_header(self):
        return self.msg["header"]

    def get_body(self) :
        return self.msg["body"]

    def set_body(self, body) :
        self.msg["body"] = body

    def set_header(self, header) :
        self.msg["header"] = header

    def prepare_to_send(self) :
        msg_str = json.dumps(self.msg, indent=2)
        msg_str += "\nend-message\n"
        return msg_str

    def create_message(self, msg) :
        message = json.loads(msg)
        self.msg = message
