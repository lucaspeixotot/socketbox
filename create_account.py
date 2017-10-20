from . import messages
import re

class CreateAccount :
    def __init__(self, users, conn) :
        self.key = "SIGNUP"
        self.conn = conn
        self.parse_options = {}


    def run(self) :
        messages.options_create_account()
        username_pattern = re.compile("USERNAME : [a-zA-Z0-9_.-]+")
        password_pattern = re.compile("PASSWORD : [a-zA-Z0-9_.-]+")
        password_confirmation_pattern = re.compile("PASSWORD_CONFIRMATION : [a-zA-Z0-9_.-]+")
        for y in [username_pattern, password_pattern, password_confirmation_patter] :
            match = None
            while not match :


            opt = self.conn.recv(1024)
            match = y.match(opt)

