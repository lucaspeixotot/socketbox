# -*- coding:utf-8 -*-

from CreateRequest import CreateRequest
from LoginRequest import LoginRequest
from UploadRequest import UploadRequest
from ListFilesRequest import ListFilesRequest
from DownloadRequest import DownloadRequest
from ShareFileRequest import ShareFileRequest

class ParseOptions :
    def __init__(self, status) :
        self.status = status
        self._LoginRequest = LoginRequest("2", "login", ["username", "password"], self.status)
        self._CreateRequest = CreateRequest("1", "create", ["username", "password", "password_confirmation"])
        self._UploadRequest = UploadRequest("1", "upload", ["file_to_be_uploaded"], self.status)
        self._ListFilesRequest = ListFilesRequest("3", "list_files", self.status)
        self._DownloadRequest = DownloadRequest("2", "download", self.status)
        self._ShareFileRequest = ShareFileRequest("4", "share_file", self.status)

        self.unlogged_actions = [(self._LoginRequest.key, self._LoginRequest), (self._CreateRequest.key, self._CreateRequest)]

        self.logged_actions = [(self._UploadRequest.key, self._UploadRequest), (self._ListFilesRequest.key, self._ListFilesRequest), (self._DownloadRequest.key, self._DownloadRequest), (self._ShareFileRequest.key, self._ShareFileRequest)]
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
        self.parse_options[self.status["logged"]][opt].run(client_socket)
