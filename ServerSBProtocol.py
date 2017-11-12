# -*- coding:utf-8 -*-

import json
from Queue import Queue
from ServerReply import ServerReply
import threading
import network
from Message import Message


class ServerSBProtocol :
    def __init__(self, socket, addr, users) :
        self.host, self.port = socket.getpeername()
        self.socket = socket
        self.addr = addr
        self.users = users
        self.broken = False
        self.rest_messages = Queue()
        self.rest_messages.put('')
        self.server_reply = ServerReply(self.users)

    def run(self) :
        while not self.broken :
            self.receive_message()

    def send_message(self) :
        pass

    def receive_message(self) :
        getting_messages = network.receive(self.socket, self.rest_messages.get())
        if not getting_messages[0] :
            self.broken = True
            return
        self.rest_messages.put(getting_messages[1])
        self.verify_and_reply(getting_messages[0])

    def verify_and_reply(self, msg) :
        message = Message()
        message.create_message(msg)
        header = message.get_header()
        body = message.get_body()

        if header["type"] != "" :
            self.server_reply.type_registration[header["type"]].run(body, self.socket)
        # elif message.msg["header"]["ack"] != "" :
        #     self.server_reply.ack_registration.run(message.msg["body"], self.socket)
        # elif message.msg["header"]["hb"] != "" :
        #     self.server_reply.hb_registration.run(message.msg["body"], self.socket)
