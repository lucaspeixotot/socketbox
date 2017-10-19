from __future__ import print_function
import socket
import Messages
import select

class Socketbox :
    def __init__(self, host, port) :
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(10)
        self.messages = Messages.Messages()
        self.messages.show("SocketBox server is running")
        self.active_clients = [self.server_socket]
        self.running = 1


    def new_socket_connected(self) :
        connection, addr = self.socket_server.accept()
        host, port = addr
        self.active_clients.append(connection)
        self.messages.show_new_client(host, port) # fazer função disso no messages
        self.messages.welcome_to_server(connection) # fazer função disso no messages

    def run(self) :

        while self.running :
            update_sockets, write, error = select.select(self.active_clients, [], [])

            for s in update_sockets :
                if s == self.server_socket :
                    self.new_socket_connected()
                else :

