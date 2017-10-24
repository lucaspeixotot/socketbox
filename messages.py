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

def successfull(connection=None) :
    msg = "A operação foi realizada com sucesso!\n"
    if connection :
        connection.send(msg)
    else :
        print(msg)

def not_successfull(connection, err) :
    msg = "A operação não foi realizada devido ao erro abaixo\n"
    err = ">>> " + err + "\n"
    msg = msg + err
    connection.send(msg)

def login_successfull() :
    print("Login efetuado com sucesso!")

def login_not_successfull(response) :
    if response == 0 :
        print("O username digitado não existe!")
    elif response == 2 :
        print("Senha incorreta!")

