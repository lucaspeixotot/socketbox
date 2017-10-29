from login import Login
from upload import Upload
from create_account import CreateAccount
from server_socket import ServerSocket
from database import Database

class SocketBox :
    def __init__(self) :
        self.database = Database()
        self.database.create_folder("/database/")
        self.users = self.database.get_users()
        print(self.users)
        self.create_account = CreateAccount(self.users, self.database)
        self.login = Login(self.users)
        self.upload = Upload()


        self.unlogged_actions = [(self.login.key, self.login), (self.create_account.key, self.create_account)]
        self.logged_actions = [(self.upload.key, self.upload)]


        self.my_server = ServerSocket()
        self.my_server.actions_initialize(self.logged_actions, self.unlogged_actions)
        self.login.socketuser = self.my_server.socketuser
        self.upload.socketuser = self.my_server.socketuser
        self.my_server.run()

socketbox = SocketBox()
