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
        self.server_socket.listen(10)
        self.messages = Messages.Messages()
        self.messages.show("SocketBox server is running")
        self.active_clients = [(self.server_socket, 2)]
        self.manager_actions = ManagerActions.ManagerActions()
        self.actions_initialize(self.manager_actions.all_actions)
        self.running = 1

    def actions_initialize(self, logged_actions, unlogged_actions) :
        self.communication_protocol = {} # implementar a lógica dessa função
        for i in range(0,2) :
            self.communication_protocol[i] = {}
            for k, v in [logged_actions, unlogged_action] : #implementar isso aqui no __init__
                self.communication_protocol[i][k] = v

    def new_socket_connected(self) :
        connection, addr = self.socket_server.accept()
        host, port = addr
        self.active_clients.append((connection, 0))
        self.messages.show_new_client(host, port) # fazer função disso no messages
        self.messages.welcome_to_server(connection) # fazer função disso no messages

    def run(self) :

        while self.running :
            update_sockets, write, error = select.select(self.active_clients, [], [])

            for conn, status in update_sockets :
                if conn == self.server_socket :
                    self.new_socket_connected()
                else :
                    message = conn.recv(self.buffer_size)
                    if message not in self.communication_protocol[status] :
                        self.messages.action_not_found()
                    else :
                        self.communication_protocol[status][message].run()
