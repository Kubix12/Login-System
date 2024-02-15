import bcrypt
from database.database import Database


class Login:

    @staticmethod
    def validate_data(login: str, user_password):
        if len(login) == 0 or len(user_password) == 0:
            pass
        else:
            password_check = Login.validate_password(user_password)
            # Database setting
            name = 'demo'
            user = 'postgres'
            password = '123'
            host = 'localhost'
            port = '5432'
            db = Database(database_name=name, database_user=user,
                          database_password=password, database_host=host,
                          database_port=port)
            db.search_data(login, password_check)

    @staticmethod
    def validate_password(password: str) -> str:
        bytes_password = password.encode('utf-8')
        salt_password = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(bytes_password, salt_password)
        return hash_password.decode('utf-8')
