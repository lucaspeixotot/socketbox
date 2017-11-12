# -*- coding: utf-8 -*-
from __future__ import print_function

def show(msg) :
    print(msg)

def create_account(connection) :
    apresentation = "Digite"

def show_new_client(host, port) :
    print("Novo cliente conectado")
    print(">>> IP:", host)
    print(">>> PORT:", port)

def action_not_found() :
    print("A acao escolhida nao existe")

def create_successfull(connection=None) :
    msg = "A conta foi criada com sucesso!\n"
    if connection :
        connection.send(msg)
    else :
        print(msg)

def create_not_successfull(connection, err) :
    msg = "A conta não foi criada devido ao erro abaixo\n"
    err = ">>> " + err + "\n"
    msg = msg + err
    connection.send(msg)

def sending_file() :
    print("Enviando arquivo...")

def end_sending_file() :
    print("Arquivo enviado com sucesso!")

def receiving_file() :
    print("Recebendo arquivo...")

def end_receiving_file() :
    print("Arquivo recebido com sucesso!")

def invalid_opt() :
    print("\nWARNING: Your option was invalid, please choose a possible option.\n")

def begin_registration(key, socket) :
    host, port = socket.getpeername()
    print("---------------NEW REGISTRATION---------------")
    print("FROM: %s:%s" % (host, port))
    print("The server will start the registration: %s request" % (key))
    print("---------------NEW REGISTRATION---------------\n\n")

def end_registration(key, socket, content) :
    host, port = socket.getpeername()
    print("--------------END REGISTRATION----------------")
    print("FROM: %s:%s" % (host, port))
    print("REGISTRATION TYPE: %s" % key)
    print("RESULT: \"%s\"" % content)
    print("--------------END REGISTRATION----------------\n\n")
