import bcrypt

class Password():
    @staticmethod
    def validate(password):
        hash_value = b'$2b$12$uZv8YagUvbYkNlj.RWquDOeprxnBGFkxKydlL7.jw3xrF5p89IBKC'
        password = bytes(password, encoding='utf-8')
        if bcrypt.checkpw(password, hash_value):
            print('Login successful')
        else:
            print('Invalid password')


"""password = b"thisismypassword"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

entered_password = input('Enter password to login')
entered_password = bytes(entered_password, encoding = 'utf-8')

if bcrypt.checkpw(entered_password, hashed):
    print('Login successful')
else:
    print('Invalid password')"""