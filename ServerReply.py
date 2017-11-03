# -*- coding:utf-8 -*-

from CreateRegistration import CreateRegistration
from LoginRegistration import LoginRegistration
from UploadRegistration import UploadRegistration
# import UploadRequest
# import DownloadRequest


class ServerReply :
    def __init__(self, users) :
        self.users = users
        create_registration = CreateRegistration("create", self.users)
        login_registration = LoginRegistration("login", self.users)
        upload_registration = UploadRegistration("upload", self.users)
        # download_request = DownloadRequest(self.users)
        # self.ack_request = AckRequest()
        # self.hb_request = HbRequest()
        all_type_registration = [create_registration, login_registration, upload_registration]
        # all_type_requests = [create_request, login_request, upload_request, download_request]
        self.type_registration = {}

        for x in all_type_registration :
            self.type_registration[x.key] = x

