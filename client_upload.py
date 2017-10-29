# -*- coding:utf-8 -*-

import os
import view
import messages

class ClientUpload :
    def __init__(self) :
        self.key = '1'

    def run(self, client_socket) :
        view.apresentation()
        file_dir = raw_input("Digite o diretório completo do arquivo a ser upado: ")
        stats = os.stat(file_dir)
        client_socket.send(file_dir + "\n")
        client_socket.send(str(stats.st_size) + "\n")
        messages.sending_file() 
        with open(file_dir, "rb") as f :
            sended_so_far = 0
            while sended_so_far < stats.st_size :
                chunk_to_be_send = f.read(min(stats.st_size - sended_so_far, 1024))
                sended_so_far += len(chunk_to_be_send)
                client_socket.send(chunk_to_be_send)
        messages.end_sending_file() 
