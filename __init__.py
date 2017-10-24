import login
import create_account
import server_socket

class SocketBox :
    def __init__(self) :
        self.users = {}
        # self.login = login.Login(self.users)
        self.create_account = create_account.CreateAccount(self.users)
        self.login = login.Login(self.users)


        self.unlogged_actions = [(self.login.key, self.login), (self.create_account.key, self.create_account)]
        self.logged_actions = []


        self.my_server = server_socket.ServerSocket()
        self.my_server.actions_initialize(self.logged_actions, self.unlogged_actions)
        self.my_server.run()

socketbox = SocketBox()
