import Login
import CreateAccount
import Messages

class ManagerActions :
    def __init__(self) :
        self.login = Login.Login()
        self.create_account = CreateAccount.CreateAccount()
        self.messages = Messages.Messages()

        self.all_actions = [(self.login.key, self.login), (self.create_account.key, self.create_account)]
