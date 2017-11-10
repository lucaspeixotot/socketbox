# -*- coding:utf-8 -*-

from CreateRegistration import CreateRegistration
from LoginRegistration import LoginRegistration
from UploadRegistration import UploadRegistration
from ListFilesRegistration import ListFilesRegistration
from DownloadRegistration import DownloadRegistration


class ServerReply :
    def __init__(self, users) :
        self.users = users
        create_registration = CreateRegistration("create", self.users)
        login_registration = LoginRegistration("login", self.users)
        upload_registration = UploadRegistration("upload", self.users)
        list_files_registration = ListFilesRegistration("list_files", self.users)
        download_registration = DownloadRegistration("download", self.users)
        # download_request = DownloadRequest(self.users)
        # self.ack_request = AckRequest()
        # self.hb_request = HbRequest()
        all_type_registration = [create_registration, login_registration, upload_registration, list_files_registration, download_registration]
        # all_type_requests = [create_request, login_request, upload_request, download_request]
        self.type_registration = {}

        for x in all_type_registration :
            self.type_registration[x.key] = x

