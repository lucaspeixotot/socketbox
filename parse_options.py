# -*- coding:utf-8 -*-

from CreateRequest import CreateRequest
from LoginRequest import LoginRequest
from UploadRequest import UploadRequest

class ParseOptions :
    def __init__(self, status) :
        self.status = status
        self._LoginRequest = LoginRequest("2", "login", ["username", "password"], self.status)
        self._CreateRequest = CreateRequest("1", "create", ["username", "password", "password_confirmation"])
        self._UploadRequest = UploadRequest()

        self.unlogged_actions = [(self._LoginRequest.key, self._LoginRequest), (self._CreateRequest.key, self._CreateRequest)]

        self.logged_actions = [(self._UploadRequest.key, self._UploadRequest)]
        self.parse_options = {}
        self.parse_options[0] = {}
        self.parse_options[1] = {}

        for x in self.unlogged_actions :
            k, v = x
            self.parse_options[0][k] = v

        for x in self.logged_actions :
            k, v = x
            self.parse_options[1][k] = v

    def run(self, opt, client_socket) :
        self.parse_options[self.status[0]][opt].run(client_socket)
