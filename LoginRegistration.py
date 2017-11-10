# -*- coding:utf-8 -*-

import network
from Registration import Registration

class LoginRegistration(Registration) :

    def __init__(self, key, users) :
        Registration.__init__(self, key, users)
        
    def run(self, body, socket) :
        username = body["content"]["username"]
        password = body["content"]["password"]

        if username in self.users and password == self.users[username] :
            status = "1025"
            content = "Usuário logado com sucesso!"
        elif username not in self.users :
            status = "0025"
            content = "O usuário digitado não existe no sistema!"
        else :
            status = "0017"
            content = "A senha digitada está incorreta!"
        msg = self.ack_construct(content, status, self.response_type)
        network.send(socket, msg)
        print("-----\nStatus - %s\nRequisição realizada com sucesso!\n-----" % status)
