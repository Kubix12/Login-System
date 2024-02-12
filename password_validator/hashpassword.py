import bcrypt
from database import Database

class Login():
    def __init__(self, password, login):
        self.password = password
        self.login = login
    @staticmethod
    def validate_password(self, hash_value):
        hash_value = b'$2b$12$uZv8YagUvbYkNlj.RWquDOeprxnBGFkxKydlL7.jw3xrF5p89IBKC'
        password = bytes(self.password, encoding='utf-8')
        if bcrypt.checkpw(self.password, hash_value):
            print('Login successful')

        else:
            print('Invalid password')

    @staticmethod
    def validate_login(self):
        if bcrypt.checkpw(self.login, self.):
            print('Login successful')
        else:
            print('Invalid password')
