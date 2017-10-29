# -*- coding:utf-8 -*-

import os
import messages

class Upload :
    def __init__(self) :
        self.key = '1'
        self.socketuser = ""
        self.dot = os.getcwd()

    def run(self, connection) :
        host, port = connection.getpeername()
        filename = connection.recv(1024)
        print(filename)
        filename = filename.split("/")[-1]
        print(filename)
        filesize = int(connection.recv(1024))
        save_path = self.dot + "/database/%s/" % (self.socketuser[port]["account"]) + "uploads/" + filename
        messages.receiving_file() 
        with open(save_path, "w") as f :
            print("A-")
            size_so_far = 0
            file_so_far = ""
            print("B-")
            while size_so_far < filesize :
                file_so_far = file_so_far + connection.recv(min(filesize - size_so_far, 1024))
                size_so_far = len(file_so_far)
                print(file_so_far)
            f.write(file_so_far)
        messages.end_receiving_file() 

