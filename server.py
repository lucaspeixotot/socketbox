# -*- coding:utf-8 -*-

import socket
import threading
from ServerSBProtocol import ServerSBProtocol
import network
from database import Database

class ServerSocket :
    def __init__(self, host="", port=6789) :
        self.host = host
        self.port = port
        self.database = Database()
        self.database.create_folder("/database/")
        self.users = self.database.get_users()
        print(self.users)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(10)
        self.clients = 0
        print("Server is listening in %d port" % self.port)

    def listening(self) :
        while True :
            while self.clients >= 10 :
                pass
            print("to aqui pacato %d", self.clients)
            conn, addr = self.server_socket.accept()
            host, port = conn.getpeername()
            print("Connected =>", host, port)
            self.clients += 1
            threading.Thread(target = self.active_client, args = (conn, addr,)).start()

    def active_client(self, conn, addr) :
        protocol = ServerSBProtocol(conn, addr, self.users)
        protocol.run()
        host, port = conn.getpeername()
        print("Disconnected => ", host, port)
        conn.close()
        self.clients -= 1

server = ServerSocket()
server.listening()
