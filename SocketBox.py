import Messages

class SocketBox :
    def __init__(self) :
        self.my_socket("", 6789)
        self.my_socket.run()

