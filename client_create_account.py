import view

class ClientCreateAccount :
    def __init__(self) :
        self.create_account_entries = ["USERNAME: ", "PASSWORD: ", "PASSWORD_CONFIRMATION: "]

    def run(self, client_socket) :
        view.create_account_protocol()
        request = []
        for x in self.create_account_entries :
            l = raw_input(x)
            l = x + l
            client_socket.send(l)
