# -*- coding:utf-8 -*-

import socket
import threading
from ServerSBProtocol import ServerSBProtocol
import network
from database import Database

class ServerSocket :
    def __init__(self, host="localhost", port=6789) :
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

    def run(self) :
        print("Server iniciado na porta %d" % self.port)
        while True :
            conn, addr = self.server_socket.accept()
            host, port = conn.getpeername()
            print("Connected =>", host, port)
            threading.Thread(target = self.active_client, args = (conn, addr,)).start()

    def active_client(self, conn, addr) :
        protocol = ServerSBProtocol(conn, addr, self.users)
        protocol.run()
        conn.close()

server = ServerSocket()
server.run()
