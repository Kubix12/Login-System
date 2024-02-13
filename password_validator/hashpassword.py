import bcrypt
from database.database import Database


class Login:

    @staticmethod
    def validate_data(login, password):
        if len(login) == 0 or len(password) == 0:
            pass
        else:
            login_check = Login.validate_login(login)
            password_check = Login.validate_password(password)
            # Database setting
            name = 'demo'
            user = 'postgres'
            password = '123'
            host = 'localhost'
            port = '5432'
            db = Database(database_name=name, database_user=user,
                          database_password=password, database_host=host,
                          database_port=port)
            db.search_data(login_check, password_check)

    @staticmethod
    def validate_password(password: str) -> str:
        bytes_password = password.encode('utf-8')
        salt_password = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(bytes_password, salt_password)
        return hash_password.decode('utf-8')

    @staticmethod
    def validate_login(login: str) -> str:
        bytes_login = login.encode('utf-8')
        salt_login = bcrypt.gensalt()
        hash_login = bcrypt.hashpw(bytes_login, salt_login)
        return hash_login.decode('utf-8')
