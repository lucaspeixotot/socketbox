# -*- coding:utf-8 -*-

import os
import shutil

class Database :
    def __init__(self) :
        self.dot = os.getcwd()

    def create_folder(self,folderPath) :
        if not os.path.exists(os.path.dirname(self.dot + folderPath)) :
            try :
                os.makedirs(os.path.dirname(self.dot + folderPath))
            except OSError as error :
                if error.errno != errno.EEXIST :
                    raise

    def create_user(self, username, password) :
        user_path = "/database/%s/" % (username)
        for x in ["uploads/", "shared_files/"] :
            direc = "%s%s" % (user_path, x)
            self.create_folder(direc)
        with open("%s%spassword" % (self.dot, user_path), "w") as f :
            f.write(password)

    def get_users(self) :
        users = {}
        if os.path.exists(os.path.dirname(self.dot + "/database/")) :
            getting = os.listdir(self.dot + "/database/")
            for username in getting :
                with open("%s/database/%s/password" % (self.dot, username), "r") as f :
                    password = f.readline()
                users[username] = password
        return users
