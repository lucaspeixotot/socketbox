# -*- coding:utf-8 -*-

import os
import shutil

class Database :
    def __init__(self) :
        self.dot = os.getcwd()

    def create_folder(self,folderPath) :
        if not os.path.exists(self.dot + folderPath) :
            try :
                os.makedirs(self.dot + folderPath)
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
        if os.path.exists(self.dot + "/database/") :
            getting = os.listdir(self.dot + "/database/")
            for username in getting :
                with open("%s/database/%s/password" % (self.dot, username), "r") as f :
                    password = f.readline()
                users[username] = password
        return users

    def get_files(self, username, file_name) :
        upload_path = self.dot + "/database/" + username + "/uploads"
        if os.path.exists(self.dot + "/database/" + username + "/uploads") :
            upload_files = set(os.listdir(upload_files))
            if file_name in upload_path :
                return True
            else :
                return False

    def get_list_files(self, username) :
        uploads_path = self.dot + "/database/" + username + "/uploads"
        shared_path = self.dot + "/database/" + username + "/shared_files"
        content = {}
        shared_list = ""
        upload_list = ""
        shared_files = os.listdir(shared_path)
        upload_files = os.listdir(uploads_path)
        for x in shared_files :
            if os.path.isfile(shared_path + "/" + x) :
                shared_list += x + "----------" + str(os.stat(shared_path + "/" + x).st_size) + "----------\n" 
            else :
                dir_files = os.listdir(shared_path + "/" + x)
                for y in dir_files :
                    shared_list += y + "----------"  + str(os.stat(shared_path + "/" + x + "/" + y).st_size) + "----------\n"
        for x in upload_files :
            if os.path.isfile(uploads_path + "/" + x) :
                upload_list += x + "----------" + str(os.stat(uploads_path + "/" + x).st_size) + "----------\n"
            else :
                print(upload_files)
                dir_files = os.listdir(uploads_path + "/" + x)
                for y in dir_files :
                    upload_list += y + "----------" + str(os.stat(uploads_path + "/" + x + "/" + y).st_size) + "----------\n"
        content["uploads"] = upload_list
        content["shared"] = shared_list
        return content

    def upload_file(self, username, file_name, file_read, file_type, upload_type) :
        file_path = self.dot + "/database/" + username + "/" + upload_type
        if os.path.exists(file_path) :
            all_files = set(os.listdir(file_path))
            if file_name in all_files :
              get_versions = os.listdir(file_path + '/' + file_name)
              get_versions.sort()
              last_file = get_versions[-1]
              version = int(last_file[:last_file.find(":")])
              version += 1
              new_file_name = str(version) + last_file[last_file.find(":"):]
              with open(file_path + "/" + file_name + "/" + new_file_name, "wb") as f :
                f.write(file_read)
            elif (file_name + file_type) in all_files :
              new_file_name = "1:" + file_name + file_type
              shutil.move(file_path + "/" + file_name + file_type, file_path + "/" + new_file_name)
              os.makedirs(file_path + "/" + file_name)
              shutil.copy(file_path + "/" + new_file_name, file_path + "/" + file_name)
              os.unlink(file_path + '/' + new_file_name)
              with open(file_path + "/" + file_name + "/" + "2:" + file_name + file_type, "wb") as f:
                f.write(file_read)
            else :
                with open(file_path + "/" + file_name + file_type, "wb") as f :
                    f.write(file_read)

    def download_file(self, download_type, file_name, username) :
        print("EPA VAMOS ANALISAR")
        print(download_type)
        print(file_name)
        print(username)
        print("E AGORA JEREMIAS?")
        downloaded = ""
        file_path = self.dot + "/database/" + username + "/" + download_type
        folder_path = file_path + "/" + file_name[file_name.find(":") + 1:file_name.rfind(".")]
        all_files = set(os.listdir(file_path))
        if file_name in all_files :
            with open( file_path + "/" + file_name, "rb") as f :
                downloaded = f.read()
        elif file_name[file_name.find(":") + 1:file_name.rfind(".")] in all_files :
            folder_files = set(os.listdir(folder_path))
            if file_name in folder_files :
                with open(folder_path + "/" + file_name, "rb") as f :
                    downloaded = f.read()
        return downloaded.encode("base64")
            

