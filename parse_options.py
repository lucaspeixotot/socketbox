# -*- coding:utf-8 -*-

from client_create_account import ClientCreateAccount
from client_login import ClientLogin
from client_upload import ClientUpload

class ParseOptions :
    def __init__(self, status) :
        self.status = status
        self._ClientLogin = ClientLogin(self.status)
        self._ClientCreateAccount = ClientCreateAccount()
        self._ClientUpload = ClientUpload()

        self.unlogged_actions = [(self._ClientLogin.key, self._ClientLogin), (self._ClientCreateAccount.key, self._ClientCreateAccount)]

        self.logged_actions = [(self._ClientUpload.key, self._ClientUpload)]
        self.parse_options = {}
        self.parse_options[0] = {}
        self.parse_options[1] = {}

        for x in self.unlogged_actions :
            k, v = x
            print(k,v)
            print(type(k))
            self.parse_options[0][k] = v

        for x in self.logged_actions :
            k, v = x
            self.parse_options[1][k] = v

    def run(self, opt, client_socket) :
        self.parse_options[self.status[0]][opt].run(client_socket)
        print("opaa", self.status[0])
