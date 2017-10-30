# -*- coding:utf-8 -*-

from CreateRequest import CreateRequest
# import LoginRequest
# import UploadRequest
# import DownloadRequest


class ServerReply :
    def __init__(self, users) :
        self.users = users
        create_request = CreateRequest("create", self.users)
        # login_request = LoginRequest(self.users)
        # upload_request = UploadRequest(self.users)
        # download_request = DownloadRequest(self.users)
        # self.ack_request = AckRequest()
        # self.hb_request = HbRequest()
        all_type_requests = [create_request]
        # all_type_requests = [create_request, login_request, upload_request, download_request]
        self.type_requests = {}

        for x in all_type_requests :
            self.type_requests[x.key] = x

