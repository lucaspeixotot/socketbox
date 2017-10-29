import messages

class Login :
    def __init__(self, users) :
        self.key = "2"
        self.users = users
        self.socketuser = []

    def run(self, connection) :
        host, port = connection.getpeername()
        request = []
        for _ in range(2) :
            l = connection.recv(1024)
            request = request + [l]
        if request[0] not in self.users :
            messages.login_not_successfull(0)
            connection.send("0")
        elif request[1] != self.users[request[0]]:
            messages.login_not_successfull(2)
            connection.send("2")
        else :
            messages.login_successfull(request[0])
            self.socketuser[port]["account"] = request[0]
            self.socketuser[port]["status"] = 1
            connection.send("1")



