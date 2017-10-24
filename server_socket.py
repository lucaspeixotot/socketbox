from __future__ import print_function
import socket
import messages
import select

class ServerSocket :
    def __init__(self, host="localhost", port=6789) :
        self.host = host
        self.port = port
        self.buffer_size = 1024
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.status = {}
        self.server_socket.listen(10)
        messages.show("SocketBox server is running")
        self.active_clients = [self.server_socket]
        self.running = 1

    def actions_initialize(self, logged_actions, unlogged_actions) :
        self.communication_protocol = {}
        self.communication_protocol[0] = {}
        for x in unlogged_actions :
            k,v = x
            self.communication_protocol[0][k] = v

    def new_socket_connected(self) :
        connection, addr = self.server_socket.accept()
        host, port = addr
        self.status[host] = 0
        self.active_clients.append((connection))
        messages.show_new_client(host, port)

    def run(self) :

        while self.running :
            update_sockets, write, error = select.select(self.active_clients, [], [])

            for conn in update_sockets :
                if conn == self.server_socket :
                    self.new_socket_connected()
                else :
                    host, port = conn.getpeername()
                    message = conn.recv(self.buffer_size)
                    if message not in self.communication_protocol[self.status[host]] :
                        messages.action_not_found()
                    else :
                        self.communication_protocol[self.status[host]][message].run(conn)
