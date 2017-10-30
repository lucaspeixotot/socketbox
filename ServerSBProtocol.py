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
        self.active = True
        self.hb_thread = threading.Thread(target = self.check_hb, args = ())
        self.rest_messages = Queue()
        self.rest_messages.put('')
        self.server_reply = ServerReply(self.users)

    def run(self) :
        self.hb_thread.start()
        while self.active :
            self.receive_message()

    def check_hb(self) :
        pass

    def send_message(self) :
        pass

    def receive_message(self) :
        getting_messages = network.receive(self.socket, self.rest_messages.get())
        self.rest_messages.put(getting_messages[1])
        self.verify_and_reply(getting_messages[0])

    def verify_and_reply(self, msg) :
        message = Message()
        message.create_message(msg)
        header = message.get_header()
        body = message.get_body()

        if header["type"] != "" :
            print("(%s , %s) fez uma requisição %s" % (str(self.host), str(self.port), str(header["type"])))
            self.server_reply.type_registration[header["type"]].run(body, self.socket)
        # elif message.msg["header"]["ack"] != "" :
        #     self.server_reply.ack_registration.run(message.msg["body"], self.socket)
        # elif message.msg["header"]["hb"] != "" :
        #     self.server_reply.hb_registration.run(message.msg["body"], self.socket)
