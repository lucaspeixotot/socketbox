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

    def get_files(self, username, file_name) :
        upload_path = self.dot + "/database/" + username + "/uploads"
        if os.path.exists(os.path.dirname(self.dot + "/database/" + username + "/uploads")) :
            upload_files = set(os.listdir(upload_files))
            if file_name in upload_path :
                return True
            else :
                return False

    def upload_file(self, username, file_name, file_read) :
        file_name_dir =file_name[:file_name.find(".") if file_name.find(".") != -1 else len(file_name)] 
        file_path = self.dot + "/database/" + username + "/uploads"
        if os.path.exists(os.path.dirname(file_path)) :
            all_files = set(os.listdir(file_path))
            if file_name not in all_files :
                with open(file_path + "/" + file_name, "wb") as f :
                    f.write(file_read)
            else :
                for x in all_files :
                    if x == file_name :
                        if not os.path.isdir(os.path.join(file_path, x)) :
                            new_file_name = "1.0:" + file_name
                            shutil.move(file_path + "/" + file_name, file_path + "/" + new_file_name)
                            os.makedirs(file_path + "/" + file_name_dir)
                            shutil.copy(file_path + "/" + new_file_name, file_path + "/" + file_name_dir )
                            os.unlink(file_path + '/' + new_file_name)
                            with open(file_path + "/" + file_name_dir + "/" + "2.0:" + file_name, "wb") as f:
                                f.write(file_read)
                        else :
                            get_versions = os.listdir(os.path.dirname(file_path + '/' + file_name_dir))
                            get_versions.sort()
                            last_file = get_versions[-1]
                            version = float(last_file[:last_file.find(":")])
                            version += 1
                            new_file_name = str(version) + last_file[last_file.find(":"):]
                            with open(file_path + "/" + file_name_dir + "/" + new_file_name, "wb") as f :
                                f.write(file_read)
                        break
