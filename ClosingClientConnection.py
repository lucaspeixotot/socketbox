# -*- coding:utf-8 -*-

class ClosingClientConnection() :
    def __init__(self, key, running) :
        self.key = key
        self.running = running

    def run(self, sock) :
        sock.close()
        self.running[0] = 0
        print("Volte sempre ao SocketBox!")
