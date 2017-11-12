# -*- coding:utf-8 -*-

from Requests import Requests
import network

class ListFilesRequest(Requests) :
  def __init__(self, key, message_type, status) :
    Requests.__init__(self, key, message_type)
    self.status = status

  def run(self, socket) :
    self.content = {}
    self.content["username"] = self.status["cur_username"]
    self.content["password"] = self.status["cur_password"]
    msg = self.prepare_message(socket)
    network.send(socket, msg)
    self.response(socket)

  def response(self, socket) :
    body = Requests.response(self, socket)
    if body["status"] == "1025" :
      print("Your uploaded files:")
      print("FILE NAME ---------- SIZE")
      print(body["content"]["uploads"])
      print("\nYour shared files:")
      print("FILE NAME ---------- SIZE")
      print(body["content"]["shared"])
    else :
      print(body["status"] + " - Request failed")
      print(body)
        
