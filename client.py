import socket
import view # implementar view
from client_create_account import ClientCreateAccount

class Client :
    def __init__(self, host="localhost", port=6789) :
        self.host = host
        self.port = port
        self.running = 1
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self) :
        self.client_socket.connect((self.host, self.port))

    def run(self) :
        while self.running :
            view.apresentation()
            view.menu_options()
            opt = raw_input("Digite a sua opcao: ")
            if opt == '1' :
                self.client_socket.send(opt)
                cca = ClientCreateAccount()
                cca.run(self.client_socket)
                response = self.client_socket.recv(1024)
                print(response)
            elif opt == '2' :
                pass
            elif opt == '3' :
                pass
            else :
                self.running = 0
        self.client_socket.close()
client = Client()
client.connect()
client.run()
