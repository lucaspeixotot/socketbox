-*- coding:utf-8 -*-

import json

BUFFER_SIZE = 1024
FLAG_END_MESSAGE = "\nend-message\n"

def receive(socket, msg_initial='') :
    msg = msg_initial

    while msg.find(FLAG_END_MESSAGE) == -1 :
        msg = msg + socket.recv(BUFFER_SIZE)

    begin_message_index = msg.find(FLAG_END_MESSAGE) - 1
    end_message_index = begin_message_index + len(FLAG_END_MESSAGE) 
    rest = msg[end_message_index:]
    msg = [:begin_message_index]

    return [msg, rest]

def send(socket, msg) :
    msg = msg.prepare_to_send()
    sended = 0
    MSG_LEN = len(msg)
    while sended < MSG_LEN :
        sended = socket.send(msg[sended:])
    
