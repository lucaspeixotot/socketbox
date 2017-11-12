# -*- coding: utf-8 -*-
def apresentation() :
    print("--------------------- WELCOME TO SOCKETBOX ---------------------")

def menu_options(status) :
    if status == 0 :
        print("*** Actions:")
        print("0 : Exit")
        print("1 : Sign up")
        print("2 : Sign in\n")
    elif status == 1 :
        print("*** Actions:")
        print("0 : Exit")
        print("1 : Upload")
        print("2 : Download")
        print("3 : List files")
        print("4 : Share files\n")

def client_login() :
    print("Who are you?")
