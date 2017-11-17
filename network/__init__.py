# -*- coding:utf-8 -*-

import json

BUFFER_SIZE = 1024
FLAG_END_MESSAGE = "\nend-message\n"

def receive(socket, msg_initial='') :
    msg = msg_initial

    while msg.find(FLAG_END_MESSAGE) == -1 :
        receiving = socket.recv(BUFFER_SIZE)
        if not receiving :
            return ['', '']
        msg = msg + receiving

    begin_message_index = msg.find(FLAG_END_MESSAGE)
    end_message_index = begin_message_index + len(FLAG_END_MESSAGE)
    rest = msg[end_message_index:]
    msg = msg[:begin_message_index]
    return [msg, rest]

def send(socket, msg) :
    msg = msg.prepare_to_send()
    sended = 0
    MSG_LEN = len(msg)
    while sended < MSG_LEN :
        sended = socket.send(msg[sended:])
    return sended == MSG_LEN
    
