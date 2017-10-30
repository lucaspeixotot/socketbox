# -*- coding:utf-8 -*-

BUFFER_SIZE = 1024

class SBProtocol :
    def __init__(self, socket) :
        self.socket = socket
        self.active = True

    def receive_message(self, ) :
        pass

    def send_message(self) :
        pass
