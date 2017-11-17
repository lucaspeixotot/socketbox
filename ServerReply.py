# -*- coding:utf-8 -*-

from CreateRegistration import CreateRegistration
from LoginRegistration import LoginRegistration
from UploadRegistration import UploadRegistration
from ListFilesRegistration import ListFilesRegistration
from DownloadRegistration import DownloadRegistration
from ShareFileRegistration import ShareFileRegistration


class ServerReply :
    def __init__(self, users) :
        self.users = users
        create_registration = CreateRegistration("create", self.users)
        login_registration = LoginRegistration("login", self.users)
        upload_registration = UploadRegistration("upload", self.users)
        list_files_registration = ListFilesRegistration("list_files", self.users)
        download_registration = DownloadRegistration("download", self.users)
        share_file_registration = ShareFileRegistration("share_file", self.users)

        all_type_registration = [create_registration, login_registration, upload_registration, list_files_registration, download_registration, share_file_registration]

        self.type_registration = {}

        for x in all_type_registration :
            self.type_registration[x.key] = x

