# -*- coding: utf-8 -*-
def apresentation() :
    print("--------------------- BEM VINDO AO SOCKET BOX ---------------------")

def menu_options(status) :
    if status == 0 :
        print("*** Opcoes:")
        print("1 : Criar conta")
        print("2 : Logar")
        print("3 : Sair\n")
    elif status == 1 :
        print("*** Opcoes:")
        print("1 : Upload")
        print("2 : Download")
        print("3 : My files")

def create_account_protocol() :
    print("Para fazer uma requisição de criação de conta siga o padrão abaixo:")
    print("---------- BEGIN CREATE ACCOUNT PROTOCOL ----------")
    print("USERNAME: YOUR_NAME")
    print("PASSWORD: YOUR_PASSWORD")
    print("PASSWORD_CONFIRMATION: YOUR_PASSWORD")
    print("---------- END CREATE ACCOUNT PROTOCOL ----------\n\n")

def client_login() :
    print("Identifique-se")
